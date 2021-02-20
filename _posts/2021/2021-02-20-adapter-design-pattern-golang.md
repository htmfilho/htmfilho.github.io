---
layout: post
title:  "Using The Adapter Design Pattern to Protect your Go App"
date: 2021-02-21 12:00:00 +0200
categories: golang design pattern adapter cache
---

![Facade](/images/posts/adapter-pattern.png)

A major benefit of Go is the explicitness of the code. There is no magic going on, no annotations doing implicit work. The flow is clear about what it is happening with the data while elegantly minimizing boilerplate code and maximizing readability. Maybe, that's the reason why frameworks are not popular among Go developers. We prefer using libraries that do one thing and one thing only, so we can compose them as we think they fit. This is great for mature developers and painful for beginners who expect an opinionated archetype to start with, but [Mandalorians](https://www.starwars.com/news/this-is-the-way-the-mandalorian-art) think this is not the way.

<!-- more -->

Using libraries directly may look simple with `got get` and `import`, but we need more than that to keep applications weakly coupled with third-party dependencies. We want to prevent too many changes in the application when a library is discontinued, a faster and secure alternative is available or even when the license becomes incompatible with the project.

To illustrate that, we are going to apply the Adapter Design Pattern to abstract a caching mechanism. The rest of the code should profit from caching features, but should not be aware of what we are using to cache data. The Adapter Pattern is good for that because it makes available just enough features from the third-party library for the precise needs of the application. Everything else is hidden. The `Cache` interface defines the required features that can be provided by ourselves or third-party libraries.

```go
type Cache interface {
  Put(key string, value interface{})
  PutAll(map[string]interface{})
  Get(key string) interface{}
  GetAll(keys []string) map[string]interface{}
  Clean(key string)
  CleanAll()
}
```

The follow implementation of the `Cache` interface is specialized on Redis. It encapsulates all the complexity behind it by adapting the interface brought by the Redis library to the interface known by the application. 

```go
type RedisCache struct {
  conn *redis.Pool
}

func (rc *RedisCache) Put(key string, value interface{}) {
  _, err := rc.conn.Get().Do("SET", key, value)
  if err != nil {
    fmt.Println(err)
  }
}

func (rc *RedisCache) PutAll(map[string]interface{}) {

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
  return nil
}

func (rc *RedisCache) Clean(key string) {

}

func (rc *RedisCache) CleanAll() {

}
```

We don't want the rest of the code to know they are using Redis. So we use a factory function to provide the supported caching implementation to callers.

```go
func GetCachingMechanism() Cache {
  cache := &RedisCache{
    conn: &redis.Pool{
      MaxIdle:     7,
      MaxActive:   30,
      IdleTimeout: 60 * time.Second,
      Dial: func() (redis.Conn, error) {
        conn, err := redis.Dial("tcp", "localhost:6379")
        if err != nil {
          fmt.Println(err)
          return nil, err
        }

        if _, err := conn.Do("SELECT", 0); err != nil {
          conn.Close()
          fmt.Println(err)
          return nil, err
        }

        return conn, nil
      },
      TestOnBorrow: func(conn redis.Conn, t time.Time) error {
        if time.Since(t) < time.Minute {
          return nil
        }
        _, err := conn.Do("PING")
        fmt.Println(err)
        return err
      },
    },
  }
  
  return cache
}
```

This factory can evolve in the future to support more caching mechanism

The caller:

```go
cache := caching.GetCachingMechanism()

cache.Put("")
```

