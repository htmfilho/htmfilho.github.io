---
layout: post
title: "Knowledge Portfolio 2023"
date: 2023-01-01 12:00:00 +0200
image: /images/posts/knowledge-portfolio-2023.png
categories: domain programming golang rust kotlin clojure portfolio
---

![Github commits in the last 12 months](/images/posts/knowledge-portfolio-2023.png)

A year ago I wrote an article about my [Knowledge Portfolio in 2022](/2021/12/knowledge-portfolio.html). Indeed, knowledge is an investment, but I changed my mind about diversifying it. At the time, I described the domains, the programming languages, and the projects I planned to spend time with. To this day, some of them flourished and others failed. Since time is a valuable asset, spending it with a limited set of subjects will lead to mastery sooner. I'm trying to downsize this year, so let's talk about what happened in 2022 and what to expect in 2023.

<!-- more -->

First, let's look at the projects. [Digger](https://github.com/htmfilho/digger) is a tool that I actively use at work to document everything I discovered in relational databases. It evolves very slowly, with only 46 commits in 2022, mostly dependency upgrades, issues with the embedded H2 database, security advisories, and the gradual migration from Java to [Kotlin](https://kotlinlang.org). No new features were added in 2022, but I'm planning to finish the migration to Kotlin and implement the model synchronization in 2023. Today, Digger only stores the elements that are documented. The rest of the model is dynamically loaded throw an active database connection. What we want to do is to store the entire model and keep it in sync with detected database changes, making an active connection optional or on-demand.

[Minimily](https://github.com/htmfilho/minimily) is another project that didn't evolve at all. I didn't even used it in 2022, which was a bad idea. It helps managing my finances and home inventory, which are really necessary in times of crisis. As a new year's resolution, I decided to put it up and running and start using it from January 1st. To my surprise, it is working just fine, but I confess that I need a little recap of [Clojure](https://clojure.org) to make sense of the code again. In 2023, I'm going to evolve it according to my needs and implement the concept of "Family" as a group of users with access to the same accounts and assets.

[CSVSource](https://github.com/htmfilho/csvsource) was the only project I started in 2022 and implemented all features as planned. It works as a [command-line tool](https://www.hildeberto.com/csvsource/), but also as a [library](https://crates.io/crates/csvsource). Apart from solving a data engineering problem, this project also helped me to learn [Rust](https://www.rust-lang.org), a complex language that delivers the satisfaction of a memory-safe app without the burden of garbage collection. In 2023, I intend to document it better, increase test coverage, and support NoSQL databases as well.

[Controlato](https://github.com/htmfilho/controlato) didn't leave the conceptual phase in 2022. It's an idea that I like very much, but I'm just not motivated anymore to move it forward with Python. Maybe, if I change the stack in 2023 I can finally get it done, but I have no decision made yet. It will just wait for the right time.

Two projects were completely abandoned: SampleReads and SpitFHIR. The first was planned to be developed in [Elixir](https://elixir-lang.org), but I only found time to learn one new programming language, which was Rust. The project was abandoned after the initial bootstrap and will be deleted in the coming days. SpitFHIR was also abandoned after the initial bootstrap because its goal was too ambitious. The [FHIR standard](/2022/02/fhir-standard.html) is very large and complex, leaving no room to low budget implementations. The project will also be deleted in the coming days. Future projects will likely be very small, focused on automation opportunities.

From the list of knowledge domains, only home automation and utilities remain active. Healthcare and sports are now deprecated. From the list of programming languages, only Clojure, Go, Kotlin, and Rust will have a chance in 2023. Rust is probably the one that will get most of my attention.

![Rust books](/images/posts/knowledge-portfolio-2023.jpg)

Finally, I'm going to migrate this blog from [Jekyll](https://jekyllrb.com) to [Hugo](https://gohugo.io). I'm tired of dealing with Ruby issues, a technology that I don't even use myself. Hugo is extremely fast and has a nicer template engine that allows me to easily share the same custom template among my blogs. The only caveat is that Github automatically builds any Jekyll website without extra configuration, while Hugo requires a Github action. As long as it does its job, I'm ok with that.