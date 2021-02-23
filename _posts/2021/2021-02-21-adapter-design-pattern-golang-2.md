---
layout: post
title:  "Taking Advantage of the Adapter Design Pattern"
date: 2021-02-21 12:00:00 +0200
categories: golang design pattern adapter cache library
---

![Facade](/images/posts/adapter-pattern.png)

We have discussed about the [Adapter Design Pattern in Go](/2021/02/adapter-design-pattern-golang.html) and we wrapped the [Redigo](https://github.com/gomodule/redigo) library to illustrate it. It turns out, despite its popularity, Redigo is poorly documented. So, that post is somehow helping Redigo after an extensive research for working code on Stack Overflow. We could keep going with Redigo, but for the long term, it is better to rely on a well documented library with more contributors and users. This is the case of [Go Redis](https://github.com/go-redis/redis).

<!-- more -->
