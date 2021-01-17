---
layout: post
title:  "Developing an Azure Function in Go: Part 1"
date: 2021-01-17 12:00:00 +0200
categories: serverless golang api
---

![Golang Serverless](/images/posts/golang-serverless.jpg)

In a [previous post](https://www.hildeberto.com/2020/12/go-business-language.html) I have presented a case for Go as a business language. Among several arguments, the most prominent one was putting an end to the massive waste of resources consumed by other technologies used in business. This time, I'm going to explore the use of Go in a serverless cloud environment as a way to push resource efficiency to the extreme with the minimal cost possible.

<!-- more -->

Serverless computing is a type of PAAS ([Platform As A Service](https://en.wikipedia.org/wiki/Platform_as_a_service)) that, in addition to a runtime environment, also offers on-demand provisioning, automatic scalability, and zero downtime deployability. In other words, a serverless app doesn't consume runtime resources like memory, networking and disk operations until it is triggered by an event like a HTTP request or a message broker. In case the demand increases, it automatically scales from 1 to N instances in a totally transparent way. It may have longer response times while deploying or auto-scaling, but it remains available all the time. Despite the name, serverless does use servers. The only difference is that you don't worry about them.

But not every application can be serverless. Everything is ephemeral. Saving files on disk, even log files, is pointless. Keeping things in memory or any other kind of internal state is hopeless. We have to rely on other cloud services for storage, computing, monitoring, etc. These limitations are actually good for the sake of scalability. If the application works in a serverless environment it probably works well in [Kubernetes](https://kubernetes.io/) and other auto-provisioning technologies.

The main cloud service providers ([AWS](https://aws.amazon.com/lambda/?nc2=h_ql_prod_cp_lbd), [Google Cloud](https://cloud.google.com/appengine), and [Azure](https://azure.microsoft.com/en-us/services/functions/)) offer serveless support, but I'm going to focus on Azure, which is the one I have more experience with. To keep things short, I'm going to divide this tutorial in three parts:

- **Part 1** is about what is inside of a Go serverless application
- In **Part 2** we deploy and run the app as an Azure Function
- Finally, in **Part 3** we explore the Function App on Azure Portal

Let's start with the business scenario we are going to implement as a Go serverless app:

> Imagine you have enough savings to pay 20% upfront for a new house. This way your mortgage will be affordable enough to keep your monthly costs low. You found a nice house listed at $600,000, for which you could pay $120,000 up front from your savings. You make an offer and realize that you are not the only one. There is an auction going on that will actually deteriorate your financial plans. You liked the house so you want to make a better offer by lowering your down payment to 15% or 10% and use the rest to increase your offer. Our Go serverless app will help you to calculate your affordable offer.

To calculate the offer we use the following formula:

    maxBid = listingPrice + (savings - (listingPrice x downPayment) - closingCosts)

where:

- `listingPrice` is the initial price of the house, as announced by the seller. It can also be an appraisal, which is more realistic.
- `maxBid` is the maximum bid you can make. Any amount between the listing price and the maximum bid can be an affordable offer.
- `savings` is the total amount you have saved over the years.
- `downPayment` is the percentage of the appraisal approved by your financial institution to give directly to the seller as down payment. It is a value ranging from 5 to 20 (percent).
- `closingCosts` is the cost of the transaction that includes legal services, taxes, fees, etc.

**WARNING**: The goal here is to teach Go, not real estate, so use this calculation in real life at your own risk.

First, let's wrap this formula in Go functions ([/offer/business.go](https://github.com/htmfilho/buyersmarket/blob/main/offer/business.go)):

    package offer

    // CalcMaxBid returns the maximum bid
    func CalcMaxBid(savings, listingPrice, downPayment, closingCosts float32) float32 {
        return listingPrice + CalcMargin(savings, listingPrice, downPayment, closingCosts)
    }

    // CalcMargin returns the remaining savings after taking the downpayment and closing costs out.=
    func CalcMargin(savings, listingPrice, downPayment, closingCosts float32) float32 {
        return savings - (listingPrice * (downPayment / 100.0)) - closingCosts
    }

Now, let's call the functions `CalcMaxBid` and `CalcMargin` from a HTTP handler that reacts to requests with GET parameters and responds with JSON ([/offer/controller.go](https://github.com/htmfilho/buyersmarket/blob/main/offer/controller.go)):

    package offer

    import (
        "encoding/json"
        "net/http"
        "strconv"
    )

    // GetOffer GET: /offer?savings=&listingPrice=&downPayment=&closingCosts=
    func GetOffer(res http.ResponseWriter, req *http.Request) {
        type Offer struct {
            Savings      float32 `json:"savings"`
            ListingPrice float32 `json:"listingPrice"`
            DownPayment  float32 `json:"downPayment"`
            ClosingCosts float32 `json:"closingCosts"`
            MaximumBid   float32 `json:"maximumBid"`
            Margin       float32 `json:"margin"`
        }

        savings := getURLParam(req, "savings")
        listingPrice := getURLParam(req, "listingPrice")
        downPayment := getURLParam(req, "downPayment")
        closingCosts := getURLParam(req, "closingCosts")

        maxBid := CalcMaxBid(savings, listingPrice, downPayment, closingCosts)
        margin := CalcMargin(savings, listingPrice, downPayment, closingCosts)

        offer := &Offer{
            Savings:      savings,
            ListingPrice: listingPrice,
            DownPayment:  downPayment,
            ClosingCosts: closingCosts,
            MaximumBid:   maxBid,
            Margin:       margin,
        }

        res.Header().Set("Content-Type", "application/json; charset=UTF-8")
        err := json.NewEncoder(res).Encode(offer)
        if err != nil {
            http.Error(res, err.Error(), http.StatusInternalServerError)
        }
    }

    func getURLParam(req *http.Request, param string) float32 {
        value, err := strconv.ParseFloat(req.URL.Query()[param][0], 32)
        if err != nil {
            return 0.0
        }
        return float32(value)
    }


This handler receives a simple get request such as:

    /offer?savings=100000&listingPrice=600000&downPayment=10&closingCosts=20000

and returns a json response such as:

    {
        "savings": 100000,
        "listingPrice": 600000,
        "downPayment": 10,
        "closingCosts": 20000,
        "maximumBid": 620000,
        "margin": 20000
    }

In addition to the request parameters, the response includes:

 - `margin`: your savings after removing the downpayment and the closing costs
 - `maximumBid`: the margin added to the listing price

To serve the handler, we call it from the entry point ([/buyersmarket.go](https://github.com/htmfilho/buyersmarket/blob/main/buyersmarket.go)):

    package main

    import (
        "buyersmarket/offer"
        "fmt"
        "net/http"
        "os"
        "strconv"
    )

    // Entry point
    func main() {
        httpPort := getHTTPPort()
        runHTTPServer(httpPort)
    }

    // We could fix the port number, but cloud environments normally require
    // some flexibility on defining the server port. This is how it would work
    // in Azure.
    func getHTTPPort() int {
        httpPort := 8080
        if val, ok := os.LookupEnv("FUNCTIONS_CUSTOMHANDLER_PORT"); ok {
            httpPort, err := strconv.Atoi(val)
            if err == nil {
                return httpPort
            }
        }
        return httpPort
    }

    // Calls the handlers and starts the HTTP server
    func runHTTPServer(httpPort int) {
        http.HandleFunc("/offer", offer.GetOffer)
        http.ListenAndServe(fmt.Sprintf(":%d", httpPort), nil)
    }

Notice that Go is very explicit about everything that is going on. There is no annotation making magical things and no frameworks making design decisions on your behalf. When we write explicit code we communicate it better to other developers. When we read explicit code we understand and maintain it better. Yet, explicit Go code is probably shorted than the equivalent in many languages used in business.

The code is available on [GitHub](https://github.com/htmfilho/buyersmarket). The project structure is very simple:

    /offer/business.go
    /offer/controller.go
    /buyersmarket.go
    /go.mod

The Go files are in the sequence presented in this article. We also have `go.mod` to define the module, the Go version, and the dependencies. To build the repo, simply run:

    $ go build buyersmarket.go

Then, run the resulting artifact:

    $ ./buyersmarket

To test it, call the URL using `curl`:

    $ curl 'http://localhost:8080/offer?savings=100000&listingPrice=600000&downPayment=10&closingCosts=20000'

In part 2, we are going to explain how to deploy it as an Azure Function. Stay tunned!