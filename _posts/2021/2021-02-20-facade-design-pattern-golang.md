---
layout: post
title:  "Using Redis Cache Through the Facade Design Pattern in Go"
date: 2021-02-21 12:00:00 +0200
categories: golang design pattern facade cache
---

![Facade](/images/posts/facade-pattern.png)

A major benefit of Go is the explicitness of the code. There is no magic going on, no annotations doing implicit work. The flow is clear about what it is happening with the data while elegantly minimizing boilerplate code and maximizing readability. Maybe, that's the reason why frameworks are not popular among Go developers. We prefer using libraries that do one thing and one thing only, so we can compose them as we think they fit. This is great for mature developers and painful for beginners who expect an opinionated archetype to start with, but [Mandalorians](https://www.starwars.com/news/this-is-the-way-the-mandalorian-art) think this is not the way.

<!-- more -->

Using libraries directly may look simple with `got get` and `import`, but we need more than that to keep applications weakly coupled with third-party dependencies. We want to prevent too many changes in the application when a library is discontinued, a faster and secure alternative is available or even when the license becomes incompatible with the project.

To illustrate that, we are going to apply the Façade design pattern to abstract a caching mechanism backed by Redis. The rest of the code should profit from caching features, but should not be aware that we are using Redis behind the scene. The Façade pattern is good for that because it makes available just enough features from the third-party library for the precise needs of the application. Everything else is hidden.

```go
type Cache interface {
    Put(key string, value {}interface)
    PutAll(map[string]{}interface)
    Get(key string) {}interface
    GetAll(keys []string) map[string]{}interface
    Clean(key string)
    CleanAll()
}
```

