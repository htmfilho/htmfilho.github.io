---
layout: post
title:  "Synchronizing the Results of Multiple Goroutines"
date: 2021-02-10 12:00:00 +0200
categories: golang sync goroutine waitgroup
---

![Stock Prices](/images/posts/golang-sync-goroutine.jpg)

My very first job was in an Internet Service Provider. I was a technical support co-op solving connectivity issues in a time connectivity was an issue that didn't solve by itself. My boss was known by his incredible talent to concentrate in multiple things at the same time. He challenged every theory about focus and could talk to you while listening to a sales representative, answering emails and thinking about the weekend. He was and I think he still is multi-threaded. When practicing sports, instead of picking running or swimming or biking, he went for triatlon, ironman, ultraman, you name it. I can only admire him because I personally keep my single focus hability and leave multi-threads for computers. Coincidence or not, that's what we're going to talk today.

<!-- more -->

In my previous post, I applied [the Strategy Pattern to get prices from different sources in Go](https://www.hildeberto.com/2021/02/golang-strategy-pattern.html). The code was designed to visit one stock exchange service at a time, but depending on the number of services to connect to, the response time could increase linearly even with the trick to search stocks in bulks.

Looking closely, no record is processed by more than one exchange. So, the data is certainly sharded by exchange. It means they can be processed in parallel, doing simultaneous calls to the involved services. But what is the impact of this design change on the [code](https://play.golang.org/p/pL7qtlgPwqL)? Surprisingly minimal. Because we adhered to the pattern contract, the strategies are kept unchanged and we only need to adapt the caller.

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

  return stocks
}
{% endhighlight %}