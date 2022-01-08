---
layout: post
title: "Never Too Soon to Change Plans"
date: 2022-01-08 12:00:00 +0200
categories: portfolio repository python django elixir phoenix
---

![Gopher With Many Doubts](/images/posts/gopher-doubts.png)

I didn't even go too far building my portfolio and I'm already rethinking my [repositories](/2021/12/repositories-portfolio.html). After some meditation, I didn't feel compelled enough to pursuit one of [the domains](/2021/12/knowledge-portfolio.html) and I noticed that two repositories were covering the same feature. Maybe it's better to change my mind now, when things are still unclear than later, when I may end up abandoning repositories for lack of enthusiasm. So, what is about to change?

<!-- more -->

The first change is giving up the domain of **sports**. I remain excited about running and I have a marathon scheduled for the end of May, but I don't think I need more than what Strava and Garmin Connect already do for me. They are integrated with 1easy-to-carry devices, collecting real-time data about my heart beats, location, pace, elevation, etc. These apps also support multiple sports and are relatively cheap. It would take a long time to reach the same level of maturity and by then, they would be far more advanced. In summary, an unfruitful effort.

The domain of sports was covered by **Pycific**, but this repository needs to be repurposed now. I'm going to explore something that is also part of my daily routine: **reading**. I currently use Goodreads, a social network of writers and readers. This app doesn't evolve for a long time and has very limited features. The only one I care about is keeping track of the books I read. And even that doesn't fulfill my needs. So I decided to approach this problem with **SampleReads**: an app that keeps track of the book I read entirely or - and here is its differential - partially. I can register that I read from page 47 to 81, make notes, write reviews, all counting for my reading stats. I also want to add books that are not in public databases, like my car's driver manual, or a magazine or an obscure e-book.

SampleReads is going to be simple. In this case, I would whether use a technical stack that I'm not so familiar with to avoid getting stuck with complications. I want to use Elixir/Phoenix instead of Python/Django, the stack that was previously used in Pycific. However, I already use Elixir/Phoenix in Controlato. I guess I will have to migrate Controlato to Python/Django then. It actually makes sense because Controlato is a complex application and it would be hard to complete it as a beginner in Elixir/Phoenix. Also, Controlato deals with data analysis, which is better supported by Python.

The third and last change, for the time being, is the discontinuation of Liftbox, a simple tool originally planned to replace my Dropbox subscription. I realized, when I was writing my previous post about bootstrapping my repositories, that Minimily already implements this feature with AWS. All I have to do is to complete and make it cloud agnostic. In this case, Roma remains as the only repository in Rust.

Now, I'm going back to the repositories to update all the information we wrote before.