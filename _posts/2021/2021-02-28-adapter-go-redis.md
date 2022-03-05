---
layout: post
title:  "Taking Advantage of the Adapter Design Pattern"
date: 2021-02-28 12:00:00 +0200
image: /images/posts/2021-02-28-adapter-go-redis.png
categories: golang design pattern adapter cache library
---

![Facade](/images/posts/2021-02-28-adapter-go-redis.png)

We have discussed about the [Adapter Design Pattern in Go](/2021/02/adapter-design-pattern-golang.html) and we wrapped the [Redigo](https://github.com/gomodule/redigo) library to illustrate the concept. During my research I discovered that Redigo has a strong competitor called [Go-Redis](https://github.com/go-redis/redis). I spent sometime playing with it and my first impression was that the code became more concise with Go-Redis. It is also [better documented](https://redis.uptrace.dev/). I didn't compare their performance, but if we find out that Go-Redis is better than Redigo, what would be the overall impact of switching to Go-Redis?

<!-- more -->

Well, not much. Since we are using the adapter pattern to hide the caching mechanism from the rest of the code, we know that only a delimited part of the code is assigned to deal with Redis. This part is the [struct](https://github.com/htmfilho/blog-examples/blob/main/caching/caching.go#L21) that implements our [Cache](https://github.com/htmfilho/blog-examples/blob/main/caching/caching.go#L10) interface. But before starting the changes, we need to cover the existing code with unit tests. Here is a sample of the unit tests written for each method of our Cache interface:

{% highlight go %}
package main

import (
  "testing"
)

func TestRedisCache_Get(t *testing.T) {
  cache := GetCachingMechanism()
  cache.Put("single", "Single Record")
  if "Single Record" != cache.Get("single") {
    t.Fail()
  }
}

func TestRedisCache_Put(t *testing.T) {
  cache := GetCachingMechanism()
  cache.Put("single", "Single Record")
  if "Single Record" != cache.Get("single") {
    t.Fail()
  }
}
...
{% endhighlight %}

The complete set of tests is available in the [blog's repo](https://github.com/htmfilho/blog-examples/blob/main/caching/caching_test.go). With the tests, we want to ensure that the new code with Go-Redis still works like the one with Redigo. It also illustrates how to use the Cache interface, so if we don't change the tests after moving to Go-Redis then the Adapter Pattern has served its purpose.

The following code is the Go-Redis implementation:

{% highlight go %}
type RedisCache struct {
  conn *redis.Client
  ctx  context.Context
}

// GetCachingMechanism initializes and returns a caching mechanism.
func GetCachingMechanism() Cache {
  cch := &RedisCache{
    conn: redis.NewClient(&redis.Options{
      Addr:     "localhost:6379",
      Password: "",
      DB:       0,
    }),
  }

  cch.ctx = context.Background()

  return cch
}

// Put adds an entry in the cache.
func (rc *RedisCache) Put(key string, value interface{}) {
  if err := rc.conn.Set(rc.ctx, key, value, 0); err != nil {
    fmt.Println(err)
  }
}

// PutAll adds the entries of a map in the cache.
func (rc *RedisCache) PutAll(entries map[string]interface{}) {
  for k, v := range entries {
    rc.Put(k, v)
  }
}

// Get gets an entry from the cache.
func (rc *RedisCache) Get(key string) interface{} {
  value, err := rc.conn.Get(rc.ctx, key).Result()
  if err != nil {
    fmt.Println(err)
    return ""
  }
  return value
}

// GetAll gets all the entries of a map from the cache.
func (rc *RedisCache) GetAll(keys []string) map[string]interface{} {
  entries := make(map[string]interface{})
  for _, k := range keys {
    entries[k] = rc.Get(k)
  }

  return entries
}

// Clean cleans a entry from the cache.
func (rc *RedisCache) Clean(key string) {
  if err := rc.conn.Del(rc.ctx, key); err != nil {
    fmt.Println(err)
  }
}

// CleanAll cleans the entire cache.
func (rc *RedisCache) CleanAll() {
  rc.conn.FlushDB(rc.ctx)
}
{% endhighlight %}

Comparing to the [Redigo implementation](https://github.com/htmfilho/blog-examples/tree/b2f9e8b69cfe2d08befc78ee428859bccdeea686/caching), we only changed the body of the methods and kept the signatures intact. A complete example of this code is available in the [blog's repo](https://github.com/htmfilho/blog-examples/tree/ed29864a4ea3d30875f7d3b9375e823b543cc025/caching). To check whether everything is still working, I run the tests:

    $ cd blog-examples/caching
    $ go test

All unit tests pass without changes. It means the application can gracefully evolve over time with the freedom to upgrade existing libraries or move to better ones all together without concerns. Of course, moving to another library requires you to perform more tests including integration and performance, but doing it without further code changes is a huge gain.