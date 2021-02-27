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

{% highlight go %}
type RedisCache struct {
  conn *redis.Pool
}

func (rc *RedisCache) Put(key string, value interface{}) {
  if _, err := rc.conn.Get().Do("SET", key, value); err != nil {
    fmt.Println(err)
  }
}

func (rc *RedisCache) PutAll(map[string]interface{}) {
  c := rc.conn.Get()
  for k, v := range entries {
    if err := c.Send("SET", k, v); err != nil {
      fmt.Println(err)
    }
  }

  if err := c.Flush(); err != nil {
    fmt.Println(err)
  }
}

func (rc *RedisCache) Get(key string) interface{} {
  value, err := redis.String(rc.conn.Get().Do("GET", key))
  if err != nil {
    fmt.Println(err)
    return ""
  }
  return value
}

func (rc *RedisCache) GetAll(keys []string) map[string]interface{} {
  // Converts []string to []interface{} since Go doesn't do it explicitly
  // because it doesn't want the syntax to hide a O(n) operation.
  intKeys := make([]interface{}, len(keys))
  for i, _ := range keys {
    intKeys[i] = keys[i]
  }

  c := rc.conn.Get()
  entries := make(map[string]interface{})
  values, err := redis.Strings(c.Do("MGET", intKeys...))
  if err != nil {
    fmt.Println(err)
    return entries
  }

  for i, k := range keys {
    entries[k] = values[i]
  }

  return entries
}

func (rc *RedisCache) Clean(key string) {
  if _, err := rc.conn.Get().Do("DEL", key); err != nil {
    fmt.Println(err)
  }
}

func (rc *RedisCache) CleanAll() {
  if _, err := rc.conn.Get().Do("FLUSHDB"); err != nil {
    fmt.Println(err)
  }
}
{% endhighlight %}