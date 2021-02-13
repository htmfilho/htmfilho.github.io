---
layout: post
title:  "Using Goroutines to Search Prices in Parallel"
date: 2021-02-10 12:00:00 +0200
categories: golang sync goroutine waitgroup
---

![Stock Prices](/images/posts/golang-sync-goroutine.jpg)

My very first job was in an Internet Service Provider. I was a technical support co-op solving connectivity issues in a time connectivity was an issue that didn't solve by itself. My boss was known by his incredible talent to concentrate in multiple things at the same time. He challenged every theory about focus and could talk to you while listening to a sales representative, answering emails and thinking about the weekend. He was and I think he still is multi-threaded. When practising sports, instead of picking running or swimming or biking, he went for triathlon, iron-man, ultra-man, you name it. I can only admire him because I personally keep my single focus ability and leave multi-threads for computers. Coincidence or not, that's what we're going to talk today.

<!-- more -->

In my previous post, I applied [the Strategy Pattern to get prices from different sources in Go](https://www.hildeberto.com/2021/02/golang-strategy-pattern.html). The code was designed to visit one stock exchange service at a time, but depending on the number of services to connect to, the response time could increase linearly even with the trick to search stocks in bulks.

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

The following optimized implementation preserves the existing code and adds a few more lines related to the way Go implements multithreading - known as Goroutines. The function signature is preserved and only the body changes. It means there is no impact outside of its scope.

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

The function starts creating a channel, which is a way to collect and share data among goroutines. In this case, the channel collects eventual errors to be handled later. Then it creates a WaitGroup, one of Go's synchronisation primitives, that waits for a collection of goroutines to finish. In the loop, we launch a goroutine for each exchange strategy, running the prices fatchings in parallel.

In theory, working on one thing at a time isn't always the fastest way to finish a task. So, we need to demonstrate that using goroutines will actually make a difference. For our fortune, Go leverage benchmarks
