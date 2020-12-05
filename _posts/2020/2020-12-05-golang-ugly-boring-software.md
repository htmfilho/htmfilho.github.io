---
layout: post
title:  "Go: Ugly and Boring for the Good of Software"
date: 2020-12-05 12:00:00 +0200
categories: golang clojure java python graalvm programming micronaut quarkus
---

![Programming Activity](/images/posts/programming-activity.png)

In most of my 20 years of software development, the Java platform has been my main focus of attention and led my market demand. But after all these years I only considered myself an real programmer in the last 5 years when I was pushed to learn other programming languages like Python, Groovy, JavaScript, Go, and Clojure. Each language gave me a different perspective, pushed me to think about approaches that were not available in Java, increased my expectations about productivity. But above all pleasuring experiences, the one that was most fullfiling was to produce a very efficient software with a minimal toolset. I have achieved that with Go.

<!-- more -->

[Go] is a terribly pragmatic, simple, minimalist language, which doesn’t succumb to pressures for new features. The community has been pushing for [generics] for a long time with the valuable argument that it would help to suppress a lot of duplicated code, but the maintainers have been pushing back proposal after proposal because of their syntax complexity or compilation/execution inefficiencies. They also keep motivating contributors to keep up with ideas because one will eventually make into the language.

Writing Go code is definitely boring. I confess I missed the expressiveness of [Clojure], but a boring language also means a shorter learning curve. Like Clojure, there is so little syntax to build our muscle memory, but unlike Clojure, there isn’t that much thinking around function composition, recursion, and pipelines when all you have is an almost pure [imperative] code. It feels more low level like C than high level like Java. That’s probably why people are reluctant to use it as a business language and more inclined to write instrumentation code, like in [Python] and [Groovy] but without the performance burden.

What really sticks people to Go is not the language in itself but the technology. It compiles extremely fast, even for large code bases, generates a native, self-contained, compact executable that also bootstraps fast. It consumes minimal memory and CPU, comparable to C/C++, while still safer with an embedded virtual machine. It performs as good as Java (after warm up) without the resource hungriness.

As happened when I was coding in Python and Clojure, it is disenchanting going back to Java after experiencing Go. Instead of lean structs I had [POJO] classes with pointless accessor methods giving a false impression of encapsulation. Instead of just functions I get classes everywhere with lost sense of abstraction, like mere method groupers. I get multiple ways to iterate when a single one would suffice. I get complex build systems with complicated dependence management while missing three simple commands that got me covered (`go get`, `go test`, and `go build`).

But not everything is lost. The Java community is catching up with the competition. Their weapon is called [Graal VM], a Java Virtual Machine that compiles to native code, generating a compact executable, just like Go. There are limitations to overcome, so not all libraries can take advantage of this new approach, which prevents frameworks like [Spring] and [JakartaEE] to exploit it right away.

Fortunately, there are some clever people out there that gathered Graal VM compatible libraries and built frameworks out of them. That’s the case of [Quarkus] and [Micronaut]. They can use any Java libraries but just a few can take full advantage of Graal VM. Still they are lean enough to take full advantage of cloud platforms such as [Kubernetes] and [Functions].

When targeting Graal VM, you will navigate in an obscrute world of configurations, environment issues, and many limitations. Go offers 10 years of efficiency with minimal configuration, fast results, countless opportunities and one of the largest programming communities in the world.

[Clojure]: https://clojure.org
[Functions]: https://en.wikipedia.org/wiki/Serverless_computing
[generics]: https://en.wikipedia.org/wiki/Generic_programming
[Go]: https://golang.org
[Graal VM]: https://www.graalvm.org
[Groovy]: https://groovy-lang.org
[imperative]: https://en.wikipedia.org/wiki/Imperative_programming
[JakartaEE]: https://jakarta.ee
[Kubernetes]: https://kubernetes.io
[Micronaut]: https://micronaut.io
[POJO]: https://en.wikipedia.org/wiki/Plain_old_Java_object
[Python]: https://www.python.org
[Quarkus]: https://quarkus.io
[Spring]: https://spring.io