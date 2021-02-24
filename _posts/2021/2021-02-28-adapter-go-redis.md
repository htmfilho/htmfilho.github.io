---
layout: post
title:  "Taking Advantage of the Adapter Design Pattern"
date: 2021-02-28 12:00:00 +0200
categories: golang design pattern adapter cache library
---

![Facade](/images/posts/adapter-pattern.png)

We have discussed about the [Adapter Design Pattern in Go](/2021/02/adapter-design-pattern-golang.html) and we wrapped the [Redigo](https://github.com/gomodule/redigo) library to illustrate the concept. It turns out, despite its popularity, Redigo has a strong competitor called [Go-Redis](https://github.com/go-redis/redis). My first impression is that, compared to Go-Redis, Redigo is poorly documented. I struggled searching for working examples, but somehow I made it and that post helps starting with Redigo. We could keep going with it, but for the long term, it is better to rely on a well documented library with more contributors and users. This is the case of Go-Redis. But what is the overal impact of switching to Go-Redis after adopting Redigo?

<!-- more -->

Well, not much, since we are using the adapter pattern to hide the caching mechanism from the rest of the code. We only need to add a wrapper for Go-Redis and adapt the factory method to create it instead of the Redigo wrapper. In other words, we need to implement the following interface again:

{% highlight go %}
type Cache interface {
  Put(key string, value interface{})
  PutAll(map[string]interface{})
  Get(key string) interface{}
  GetAll(keys []string) map[string]interface{}
  Clean(key string)
  CleanAll()
}
{% endhighlight %}

It turns out Go-Redis has a dedicated caching library that can be used instead of the general purpose library. This dedicated library will certainly simplify our code, helping with readability.