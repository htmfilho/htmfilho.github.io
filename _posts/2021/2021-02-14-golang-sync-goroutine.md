---
layout: post
title:  "Using Goroutines to Search Prices in Parallel"
date: 2021-02-14 12:00:00 +0200
categories: golang sync goroutine waitgroup pattern
---

![Stock Prices](/images/posts/golang-sync-goroutine.jpg)

My very first job was in an Internet Service Provider. I was a technical support co-op solving connectivity issues in a time connectivity was an issue that didn't solve by itself. My boss was known by his incredible talent to concentrate in multiple things at the same time. He challenged every theory about focus and could talk to you while listening to a sales representative, answering emails and thinking about the weekend. He was and I think he still is multi-threaded. When practising sports, instead of picking running or swimming or biking, he went for triathlon, iron-man, ultra-man, you name it. I can only admire him because I personally have a single focus ability and leave multi-threading for computers. Coincidence or not, my focus today is multi-threading in Go.

<!-- more -->

In my previous post, I applied [the Strategy Pattern to get stock prices from different sources in Go](https://www.hildeberto.com/2021/02/golang-strategy-pattern.html). The code was designed to visit one stock exchange service at a time, but depending on the number of services to connect to, the response time could increase linearly, even with the trick to search stocks in bulks.

Looking closely, no record is processed by more than one exchange. So, the data is certainly [sharded](https://en.wikipedia.org/wiki/Shard_(database_architecture)) by exchange. It means they can be processed in parallel without the risk of concurrent access that may lead to race conditions. On the other hand, we have to find a way that processes wait for one another until the stocks are filled with prices, and then return to the caller.

With these non-functional requirements in mind, what is the impact of this design change on the [code](https://play.golang.org/p/pL7qtlgPwqL)? Surprisingly minimal. Since we adhered to the strategy pattern contract, the strategies are kept unchanged and we only need to adapt the caller, which is the function `searchStocks()`.  Let's take a look at the original implementation:

{% highlight go %}
func searchStocks(exchangeFactory *ExchangeFactory, stocks []*Stock) []*Stock {
  for _, exchange := range exchangeFactory.exchanges {
    err := exchange.search()
    if err != nil {
      fmt.Printf("Couldn't fetch prices from %s.\n", exchange.getName())
    }
  }
  return stocks
}
{% endhighlight %}

The following optimized implementation preserves the existing code and adds a few more lines related to the way Go implements multithreading - known as [Goroutines](https://gobyexample.com/goroutines). The function signature is preserved and only the body changes. It means there is no impact outside of its scope.

{% highlight go %}
func searchStocks(exchangeFactory *ExchangeFactory, stocks []*Stock) []*Stock {
  errors := make(chan error, 2)
  var wg sync.WaitGroup
  for _, exchange := range exchangeFactory.exchanges {
    wg.Add(1)
    go func(exchange Pricing) {
      defer wg.Done()
      err := exchange.search()
      if err != nil {
        errors <- err
        fmt.Printf("Couldn't fetch prices from %s.\n", exchange.getName())
        return
      }
    }(exchange)
  }
  wg.Wait()
  close(errors)

  for err := range errors {
    println(err.Error())
  }

  return stocks
}
{% endhighlight %}

The function starts creating a channel, which is a way to collect and share data among goroutines. In this case, the channel collects eventual errors to be handled later. In the sequence, it creates a [WaitGroup](https://golang.org/pkg/sync/#WaitGroup), one of Go's synchronisation primitives, that waits for a collection of goroutines to finish. In the loop, we launch a goroutine for each exchange strategy (`go func()`), fetching prices in parallel. After the loop, `wg.Wait()` waits for all goroutines to finish before continuing.

In theory, working on one thing at a time isn't always the fastest way to finish a task, but we need to demonstrate goroutines will actually make a difference. Fortunately, we don't have to look elsewhere because Go offers benchmarking out of the box. It is part of the Go [testing package](https://golang.org/pkg/testing/). To make a fair comparison, we are going to make a few changes:

1. Make the sequential and parallel versions of the function `searchStocks` available. For that, we need to give them different names:
  - `searchStocksInSequence()`
  - `searchStocksInParallel()`

2. Add an extra caller to match the two available functions:
   
{% highlight go %}
    func getPricesInSequence(stocks []*Stock) []*Stock {
      exchangeFactory := prepareExchangeStrategies(stocks)
      return searchStocksInSequence(exchangeFactory, stocks) 
    }

    func getPricesInParallel(stocks []*Stock) []*Stock {
      exchangeFactory := prepareExchangeStrategies(stocks)
      return searchStocksInParallel(exchangeFactory, stocks)
    }
{% endhighlight %}
       
Now we are ready to write the benchmarking functions, one for each of the above functions:

{% highlight go %}
package main

import "testing"

var stocks = []*Stock{
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

func BenchmarkGetPricesInSequence(b *testing.B) {
  for n := 0; n < b.N; n++ {
    stocks = getPricesInSequence(stocks)
  }
}

func BenchmarkGetPricesInParallel(b *testing.B) {
  for n := 0; n < b.N; n++ {
    stocks = getPricesInParallel(stocks)
  }
}
{% endhighlight %}

Benchmark is part of testing so it is placed and written like such. To create a benchmark, we prefix a function with `Benchmark` and put it in a `_test.go` file. The difference from a test is that each function runs several times. The value of b.N increases at every call until the runner is satisfied with the stability of the benchmark. Assuming that our main package is in the file `pricing.go` and the test file `pricing_test.go` is right beside it, we can execute the benchmark this way:

    $ go test -bench=.

The `.` matches all benchmarks in the main (`trade`) package. The result of the execution looks like this:

```
$ go test -bench=.

  goos: linux
  goarch: amd64
  pkg: trade
  BenchmarkGetPricesInSequence-8        1802668        607 ns/op
  BenchmarkGetPricesInParallel-8         390738       2883 ns/op
  PASS
  ok      trade   4.005s
```

It starts showing the operating system (`goos: linux`), the processor architecture (`goarch: amd64`), and the main package name (`pkg: trade`), giving some context about where the benchmark was executed. Then it lists all the executed benchmarks where each line shows the executed benchmark (`BenchmarkGetPricesInParallel`), the number of CPUs involved (`8`), the number of times it was executed (`390738`), and how long it took in nanoseconds (`2883 ns`).

The results look blazingly fast because there is nothing in the `search()` methods. But the impact of adding goroutines to the code is noticiable, with a difference of 2276 nanoseconds (or 0.002 miliseconds). That's the price we have to pay to run the searches in parallel. If there isn't much to do then this price might be expensive (up to 4.7 times more expensive), but what happens if each search method takes 1 ms to run? We added `time.Sleep(time.Millisecond)` in there and look at what we get:

```
$ go test -bench=.

  goos: linux
  goarch: amd64
  pkg: trade
  BenchmarkGetPricesInSequence-8        344        3475598 ns/op
  BenchmarkGetPricesInParallel-8       1022        1209255 ns/op
  PASS
  ok      trade   2.911s
```
The `GetPricesInParallel` is now almost 3x faster, which is the expected result, since the three `search()` methods are running at the same time. So, we don't have to do much to start enjoying the benefits of goroutines. They are so low cost that a single cpu can do a decent job too:

```
$ go test -bench=. -cpu=1
  BenchmarkGetPricesInSequence        348        3460908 ns/op
  BenchmarkGetPricesInParallel       1036        1183913 ns/op
```

A full implementation of the benchmarked code is available in my [Blog Examples Repo](https://github.com/htmfilho/blog-examples/tree/d4d109d453c4f44a80ad294fa9f8c226a403fa9a/trade).

In addition to presenting Goroutines, I also wanted to show that it was a delightful experience to maintain a code designed with patterns. [Donald E. Knuth once said](https://pic.plover.com/knuth-GOTO.pdf) that "__premature optization is the root of all evil__" because it may lead to abuse, with a strong negative impact on debugging and maintenance. So, considering optimization in a second moment has shown how little we changed to achieve a better result.