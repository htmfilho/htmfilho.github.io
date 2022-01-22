---
layout: post
title: "Never Too Soon to Change Plans"
date: 2022-01-08 12:00:00 +0200
categories: portfolio repository python django elixir phoenix
---

![Gopher With Many Doubts](/images/posts/gopher-doubts.png)

I didn't even go too far building my portfolio and I'm already rethinking my [repositories](/2021/12/repositories-portfolio.html). After some meditation, I didn't feel compelled enough to pursue one of [the domains](/2021/12/knowledge-portfolio.html) and I noticed that two repositories were covering the same feature. Maybe it's better to change my mind now, when things are still unclear than later, when I may end up abandoning repositories for lack of enthusiasm. So, what is about to change?

<!-- more -->

The first change is giving up the domain of **sports**. I remain excited about running and I'm booked to a marathon at the end of May, but I don't think I need more than what [Strava](https://www.strava.com) and [Garmin Connect](https://www.garmin.com) already offer me. They are integrated with easy-to-carry devices, collecting real-time data about my heart beats, location, pace, elevation, etc. These apps also support multiple sports and are relatively cheap. It would take a long time to reach the same level of maturity and by then, they would be far more advanced. In summary, an unfruitful effort.

The domain of sports was covered by **Pycific**, but this repository needs to be repurposed now. I'm going to explore something that is also part of my daily routine: **reading**. I currently use [Goodreads](https://www.goodreads.com), a social network of writers and readers. This app hasn't evolved for a long time and has limited features. The only one I care about is keeping track of the books I read. And even that doesn't fulfill my needs. So I decided to approach this problem with [SampleReads](https://github.com/htmfilho/samplereads): an app that keeps track of the book I read entirely or - and here is its differential - partially. I can register I read from page 47 to 81, make notes, write reviews, all counting to my reading stats. I also want to add books that are not in public databases, like my car's driver manual, or a magazine or an obscure e-book.

SampleReads is going to be simple. So, I would rather approach a simple problem with a technical stack that I'm not familiar with. Since I don't know enough of Elixir/Phoenix, I'm going to use it instead of Python/Django, the stack previously used in Pycific. However, I already use Elixir/Phoenix in [Controlato](https://github.com/htmfilho/controlato). Well, I guess I have to migrate Controlato to Python/Django then. It actually makes sense because Controlato is a complex application and it would be harder to complete it in Elixir/Phoenix. Also, Controlato deals with data analysis, which is better supported by Python.

The third and last change, for the time being, is the discontinuation of **Liftbox**, a simple tool originally planned to replace my [Dropbox](https://www.dropbox.com) subscription. I realized, when I was writing my [previous post](/2022/01/bootstraping.html), that [Minimily](https://github.com/htmfilho/minimily) already implements this feature with [AWS](aws.amazon.com). All I have to do is to make it cloud agnostic. After discontinuing Liftbox, [Roma](https://github.com/htmfilho/roma) is now the only repository in Rust.

By this time, all changes were implemented in the repositories and all broken links in previous posts were changed to point to this post as a form of clarification.
