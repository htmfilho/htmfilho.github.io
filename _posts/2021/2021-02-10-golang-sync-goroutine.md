---
layout: post
title:  "Synchronizing the Results of Multiple Goroutines"
date: 2021-02-10 12:00:00 +0200
categories: golang sync goroutine waitgroup
---

![Stock Prices](/images/posts/golang-strategy-pattern.png)



<!-- more -->

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