---
layout: post
title:  "Applying the Strategy Pattern to Get Prices from Different Sources in Go"
date: 2021-02-04 12:00:00 +0200
categories: golang pattern finance
---

![Stock Prices](/images/posts/golang-strategy-pattern.png)

I keep searching for concrete examples in my quest to convince you that Go is a great language for business. I found in finance a great source of ideas to prove my point. I already explored this subject twice ([1](https://www.hildeberto.com/2020/04/dealing-with-money.html) and [2](https://www.hildeberto.com/2021/01/azure-function-golang.html)) and today I'm going to explore it again.

<!-- more -->

The strategy pattern is one of the simplest yet underutilized design patterns out there. It is useful when we have one goal and several ways to achieve that. In this case, our goal is to get stock prices from different stock exchanges. Each stock exchange requires a dedicated strategy to fetch the prices since they have different APIs and abstractions. The advantage of this implementation is that if we want to support a new stock exchange all we need to do is to add a new strategy. The code that calls the strategies don't change, which also prevents breaking exising tests and introducing unexpected bugs.

Formally speaking:
> "The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it."

## Calling the Strategy Pattern Implementation

We start the implementation with constants that represent the stock exchanges:

{% highlight go %}
package main

import "fmt"

// Supported exchanges
const (
  NASDAQ = "NASDAQ"
  NYSE   = "NYSE"
  TSX    = "TSX"
)
{% endhighlight %}

These constants can even be replaced by configuration entries to make the strategies work as plugins. That's something we can explore in a future post. For the moment, let's continue representing a stock as a struct:

{% highlight go %}
type Stock struct {
  Exchange string
  Ticker   string
  Name     string
  Price    int32
}
{% endhighlight %}

Concerning the attributes, the `Exchange` is one of those constants declared above. The `Ticker` is an acronym that represents the stock. The `Name` helps to decode the ticker. The `Price` is what we are looking for, so it will be filled later. The following `main()` function has a list of pointers to instances of Stock. Yes, we are working with the same instances from the begining to the end. You may not like the multability aspect of it, but it will help to keep the order of the original list unchanged. I honestly think this is a responsible and constructive case of multability usage, since it reduces accidental complexity.

{% highlight go %}
func main() {
  stocks := []*Stock{
    {
      Exchange: NASDAQ,
      Ticker:   "GOOGL",
      Name:     "Alphabet Inc.",
    }, {
      Exchange: NYSE,
      Ticker:   "GE",
      Name:     "General Electric CO",
    }, {
      Exchange: TSX,
      Ticker:   "SHOP",
      Name:     "Shopify Inc.", 
    }, {
      Exchange: NASDAQ,
      Ticker:   "AAPL",
      Name:     "Apple Inc.",
    }, {
      Exchange: TSX,
      Ticker:   "BMO",
      Name:     "Bank of Montreal",
    }, {
      Exchange: TSX,
      Ticker:   "CP",
      Name:     "Canadian Pacific Raiway Ltd.",
    },
  }

  stocks = getPrices(stocks)

  for _, stock := range stocks {
    fmt.Printf("%s: %d\n", stock.Ticker, stock.Price)
  }
}
{% endhighlight %}

The `main()` function works like a controller or a caller of the service façade. It calls the function `getPrices()`, which is a service function, passing the list of stocks. The function is expected to return the same list with the prices defined. In the sequence, the list is printed as an output of the program. 

The `getPrices()` function counts with the help of two other functions to be consistent with the single responsibility principle. Let's take a look at them:

{% highlight go %}
func getPrices(stocks []*Stock) []*Stock {
  exchangeCoordinator := prepareExchangeStrategies(stocks)
  return searchStocks(exchangeCoordinator, stocks)
}

func prepareExchangeStrategies(stocks []*Stock) *ExchangeCoordinator {
  exchangeCoordinator := &ExchangeCoordinator{}
  for _, stock := range stocks {
    pricing := exchangeCoordinator.GetExchangePricing(stock)
    pricing.addStock(stock)
  }
  return exchangeCoordinator
}

func searchStocks(exchangeCoordinator *ExchangeCoordinator, stocks []*Stock) []*Stock {
  for _, exchange := range exchangeCoordinator.exchanges {
    err := exchange.search()
    if err != nil {
      fmt.Printf("Couldn't fetch prices from %s.\n", exchange.getName())
    }
  }
  return stocks
}
{% endhighlight %}

The `prepareExchangeStrategies()` function does something special. It groups stocks by exchange to optimize, if possible, the calls to the exchange pricing services. Notice it is using the strategies to hold the grouping (`pricing.addStock(stock)`). It helps to illustrate that a strategy can keep some temporary state to use when it's convinient.

Now, look at the `searchStocks()` function and notice how clean it is. Those three lines of code are calling distinct algorithms that do different things to achieve the same goal: retrieve the prices of the stocks they hold. The `ExchangeCoordinator` struct and the `search()` function are shaped according to the strategy pattern, making things cleaner and elegant.    

## Implemeting the Strategy Pattern

The `Pricing` interface is the core of the strategy pattern. It makes the caller think that all strategies look the same, but they actually have unique souls.

{% highlight go %}
// Pricing shapes the strategy pattern to be applied to specialized structs.
type Pricing interface {
  addStock(stock *Stock)
  search() error
  getName() string
}
{% endhighlight %}

We have met Pricing behaviors in the functions `prepareExchangeStrategies()` and `searchStocks()` above. These behaviors have an implementation per stock exchange.

The `ExchangeCoordinator` struct and its method `GetExchangePricing()` figure out which strategy the caller needs based on the stock exchange. It does it using a Map with the exchange's acronym as key.

{% highlight go %}
// ExchangeCoordinator holds the pricing strategies for the duration of the execution.
type ExchangeCoordinator struct {
  exchanges map[string]Pricing
}

// GetExchangePricing returns the Pricing based on the stock exchange.
func (ec *ExchangeCoordinator) GetExchangePricing(stock *Stock) Pricing {
  if ec.exchanges == nil {
    ec.exchanges = make(map[string]Pricing)
    ec.exchanges[NASDAQ] = new(NasdaqPricing)
    ec.exchanges[NYSE] = new(NYSEPricing)
    ec.exchanges[TSX] = new(TsxPricing)
  }
  return ec.exchanges[stock.Exchange]
}
{% endhighlight %}

Instances of the strategies are kept in memory for the length of the call. They can't be kept longer because they cache the stocks they work with, as we can see in the following three implementations.

### NASDAQ Strategy Pattern Implementation

Our goal is to explain the strategy pattern, not fetching prices from stock exchanges. Maybe we can do it in another time, but let's keep this one short. The `NasdaqPricing` struct caches Nasdaq's stocks using a list and the `addStock()` method. The cached stocks are then processed in the `search()` method.

{% highlight go %}
// NasdaqPricing is the strategy implementation to get prices from Nasdaq.
type NasdaqPricing struct {
  stocks []*Stock
}

func (np *NasdaqPricing) addStock(stock *Stock) {
  np.stocks = append(np.stocks, stock)
}

func (np *NasdaqPricing) search() error {
  if len(np.stocks) > 0 {
    // Call Nasdaq web api here and set  the prices.
  }

  return nil
}

func (np *NasdaqPricing) getName() string {
  return "Nasdaq"
}
{% endhighlight %}

The method `getName()` is used just for friendly error handling messages.

### NYSE Strategy Pattern Implementation

{% highlight go %}
// NYSEPricing is the strategy implementation to get prices from NYSE.
type NYSEPricing struct {
  stocks []*Stock
}

func (nyp *NYSEPricing) addStock(stock *Stock) {
  nyp.stocks = append(nyp.stocks, stock)
}

func (nyp *NYSEPricing) search() error {
  if len(nyp.stocks) > 0 {
    // Call NY Stock Exchange web api here and set  the prices.
  }

  return nil
}

func (nyp *NYSEPricing) getName() string {
  return "New York Stock Exchange"
}
{% endhighlight %}

### TSX Strategy Pattern Implementation

{% highlight go %}
// TsxPricing is the strategy implementation to get prices from Tsx.
type TsxPricing struct {
  stocks []*Stock
}

func (tp *TsxPricing) addStock(stock *Stock) {
  tp.stocks = append(tp.stocks, stock)
}

func (tp *TsxPricing) search() error {
  if len(tp.stocks) > 0 {
    // Call Toronto Stock Exchange web api here and set  the prices.
  }

  return nil
}

func (tp *TsxPricing) getName() string {
  return "Toronto Stock Exchange"
}
{% endhighlight %}

Here, Go shows a glance of its elegance. It doesn't require you to explicitly indicate the interfaces your structs implement, like in Java:

{% highlight java %}
public class Foo implements Bar {...}
{% endhighlight %}

It is enough to have the same method signatures. Simplicity matters and it makes me love this language more than any other.