---
layout: post
title: "My Knowledge Portfolio"
date: 2021-12-16 12:00:00 +0200
categories: domain programming java python golang rust elixir clojure portfolio
---

![Gopher reading](/images/posts/gopher-reading.png)

In my opinion, the most insightful section in the book "[The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)" is "Your Knowledge Portfolio", where the author makes the point that knowledge must be treated as investments, thus it requires a diversified portfolio for better results. This post is an attempt to build my knowledge portfolio.

<!-- more -->

I'm a software engineer who likes to work on products. It puts scripts and automation tools as second-class citizens - or technologies that I fully rely on [Stack Overflow](https://stackoverflow.com) to make something happen. I like to build products that I can use myself, but I'm not particularly inclined to build infra-structure software like databases, web servers, compilers, and networking tools. For these, I'm merely a user. I like working with data, moving, transforming, mapping, exchanging, storing, retrieving, partitioning, merging, replicating, etc. But I'm not yet comfortable dealing with a lot of data, like big data, data mining, training data, and so on. I wish I had time to follow along with the trends in technology, but as I get older, time becomes precious, making me stick to things I'm truly passionate about, which are not necessarily the most popular frameworks, languages and tools.

There are many things I have to learn to build my products, but the fundamentals ones are:

- **Programming Languages**: I believe there is a programming language for every problem but sometimes multiple programming languages compete for the same problem. C and C++ compete in system programming, PHP and Ruby compete in web development, Java and C# compete in business applications. On the other hand, Python is the best for data analysis, Go is the best for cloud and networking, JavaScript is the best for user interfaces, Erlang is the best for high availability, and so on. I want to put in my portfolio enough programming languages to cover all the problems I like to solve.

- **Domains**: The problems I like to solve are in 3 domains:

  - _Healthcare_: that's my professional domain, the one that pays my bills. I worked in many domains throughout my career, but healthcare is the most fascinating one for me. My contributions directly translates into increased life expectancy of the population, even a tiny little bit. 
  - _Home Automation_: I bought a new home a year ago and there is nothing more exciting than modernizing it.
  - _Sports_: (_[Deprecated](/2022/01/never-soon-change.html)_) sports are an important part of my family's activities. I'm a runner, my wife too, my older soon is a swimmer, and my yonger dauther is a gymnast. I'm very much involved in those activities, specially swimming, for which I'm training to become an official.
  - _Utilities_: From time to time, I find opportunities to improve something in my work. I end up creating several small productivity tools to explore those opportunities.

In the range of programming languages, these are my choices:

- **[Clojure](https://clojure.org)**: The JVM is a remarkable platform for business applications. Its main language is Java, but I already use it at work. I need something different that runs on top of the JVM and radically improves productivety. My choice is Clojure, a dialect of Lisp that solves problems in an elegant way. It is very different from other languages, but it is also minimalistic. I remember when I decided to learn it, I had fifteen days of strugle and then a spark, a WOW moment that changed me forever. Some people may ask: "Why not Kotlin or Scala?". They are similar to Java and sometime more complex. So, no thanks.

- **[Python](https://www.python.org)**: here is a language that offers what Java can't: readability, expressiveness, productivity, and utility. The community and the spectrum of problems Python can solve are so vast that one can feel compelled to adopt it as the only language in their portfolio. But that's a trap because Python depends on C/C++ to perform well and has known multiplatform issues. Having said that, Python is my first choice when it comes to data processing and analysis.

- **[Go](https://go.dev)**: Python's readability can only go as far as the code we write ourselves. Languages like Python, Java, and Rust offer too many ways to solve the same problem in the name of expressiveness, but reading the code written by others also comes with a learning curve. Go solves this problem with a minimalist syntax that once learned, can make everybody's code pretty similar. Its minimalism also pays off in the form of super fast compilation. The code is multiplatform, but the binary is platform-specific, self-contained, with an embedded virtual machine that makes Go applications memory-safe. Go's performance is comparable to Java with the advantage of using far less computational resources. It is by far my favourite language.

- **[Rust](https://www.rust-lang.org)**: I have been avoiding Rust for quite a while. Its syntax and compiler are just awful. But there is still something there that captivates me: the ability to write a program that doesn't require a virtual machine and is still safe to run. A VM is this high interest you pay in runtime to stop caring about the memory the application consumes. We see very simple Java applications out there consuming gigabytes of memory just during the start up. This is gigabytes before serving the first user. Go minimizes this waste but it still comes with the infamous pauses for garbage collection. With Rust, it is possible to write memory-safe programs without doing it manually like C/C++, thanks to its ruthless compiler. It has a modern syntax, with good expressiveness, and a fantastic tooling experience. Unfortunately, there is a price to pay. It is immutable by default and comes with unprecedented features to enable its memory safety - like ownership and borrowing - substantially increasing its learning curve. Some people suggest to read the entire "The Book" before any adventure in the language to avoid getting frustrated. I will give it a vote of confidence next year. Let's see what happens.

- **[Elixir](https://elixir-lang.org)**: The languages I picked so far are very different from each other, not just in terms of syntax but also in terms of implementation. Elixir adds to this list, offering yet another unique approach. It's a hosted language on top of the Bean VM, the one that also runs Erlang. What makes it special is its fault-tolerance design. It devides the application in hundreds, sometimes thousands of processes and if some of them fail they're killed and restarted, while the application remains up and running. The programer doesn't need to do anything to make it happen. This is an extra feature of this VM that no other has. Bean also consumes less memory and optimaly uses all CPUs. Elixir feels like Ruby, but it is fundamentally different because it is functional like Clojure.

In my portfolio, I have two functional languages (Clojure and Elixir), one object-oriented (Python) and two imperatives (Go and Rust) ones. I think they cover all modern concepts of programming and are aligned with what the market expects. The next challenge is to put them in practice. So, I'm going to create an open source repository for each one of them on [Github](https://github.com/htmfilho) and share my learning process here. Stay tuned!
