---
layout: post
title: "The Repositories of my Portfolio"
date: 2021-12-21 12:00:00 +0200
categories: programming java python golang rust elixir clojure portfolio
---

![Gopher Orchestra](/images/posts/gopher-orchestra.png)

When I [defined my knowledge portfolio](/2021/12/knowledge-portfolio.html), describing the domains and programming languages I wanted to invest in 2022, it felt like a New Year's Resolution. Nobody ever follows new year's resolutions. I prefer to call that plan my **Lifelong Learning Program**, a term I borrowed from the European Commission, an organization I worked for 11 years ago. The question is: how do I put this program into practice?

<!-- more -->

By creating GitHub repositories, of course. I have at least one for each programming language that I have chosen and they somehow cover the domains I want to focus on. And here they are:

- **[Digger](https://github.com/htmfilho/digger)** _([Java](https://openjdk.java.net), Utilities)_ : An app to help developers to document relational databases in a collaborative way. There are many legacy databases out there and teams struggle to learn the meaning of tables, views, columns and other structures. Digger helps them to keep track of what they know about the database structure. Digger is developed in Java with [Spring Boot](https://spring.io/projects/spring-boot) and [Hibernate](https://hibernate.org). This stack was not mentioned in my new knowledge portfolio, but I've been working with Java for a long time and Digger is the most mature repository I have in my GitHub profile.

- **[Minimily](https://github.com/htmfilho/minimily)** _([Clojure](https://clojure.org), Home Automation)_ : An app to manage the minimalist life of a family at home. Its controversial approach is based on workload. It means the more I consume the more I have to use the app, thus less consumption means less usage. Tools like Mint connects to your bank account, do all the heavy lift for you and leave only charts for your eyes, without giving the feeling of spending frequency and volume. Minimily requires you to register every single record manually, so you feel you are spending more or less. It does not invade your privacy and does not care about your identity. Since I adopted Minimily I was finally able to buy everything in cash, including my last three brand new cars (one at a time, of course). We also gave a good down payment in our first home and we are able to pay down the mortgage faster.

- **[Controlato](https://github.com/htmfilho/controlato)** _([Elixir](https://elixir-lang.org), Home Automation, Healthcare)_ : The original idea dates back to 2004, when we created an app called Planexstrategy. But it was too big, covering _project management_, _document management_, and _process management_. I'm taking only the process monitoring of the process management part and applying modern concepts found in the book ["Measure What Matters", by John Doerr](https://www.whatmatters.com/the-book). I'm writing it in Elixir because I'm excited to see real-time monitoring with [LifeView](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html). I personally need this tool to monitor my IoT devices, water, gas, and power consumption, and even team velocity and backlog at work. Controlato should be able to monitor from annual investment returns to heart beats.

- **[SpitFHIR](https://github.com/htmfilho/spitfhir)** _([Go](https://go.dev), Healthcare)_ : While working in the healthcare industry, I was presented to a standard called [FHIR® (Fast Healthcare Interoperability Resources)](https://hl7.org/fhir/). It is used to exchange data among healthcare systems. The more I learn FHIR® the more impressed I become. In my opinion, it is the most advanced interoperability standard for data exchange. It stands out specially in security due to the sensitivity of healthcare information. FHIR® is very popular and even used by Apple and Google to exchange data with their mobile devices like Apple Watch, Fitbit, Android, etc. There are many FHIR® implementations out there, most in mainstream programming languages to cover existing information systems - EHR (Electronic Healthcare Records). I'm advocating here the implementation in more modern languages to offer alternatives to new healthcare applications. I couldn't find a mature implementation in Go, just some sketches here and there. Maybe Go has a limitation that I'm not aware of, but I'm wiling to take the risk and write SpitFHIR, a Go implementation of the FHIR® standard. If it will ever be completed, I don't know, but I will certainly have fun writing some clever algorithms. However, if it is completed, then SpitFHIR is going to be the fastest, more productive, and maintainable implementation out there.

- **[Pycific](https://github.com/htmfilho/pycific)** _([Python](https://www.python.org), Sports)_ : Sports are an important part of my family's activities. I'm a runner, my wife is too, my older son is a swimmer, and my younger daughter is a gymnast. Curiously, I never considered writing any software for sports. Now is the time. I decided to write it in Python and [Django](https://www.djangoproject.com). Python will help me to analyze the data that Pycific collects from our activities.

- **Small Tools** _([Rust](https://www.rust-lang.org), Utilities)_ : Rust is the programming language I know the least in my portfolio. So, I'm going to start with small tools to get familiarized with its concepts. I have two repositories to explore Rust:

  - **[Liftbox](https://github.com/htmfilho/liftbox)** : a command line tool to synchronize the content of a local folder to a cloud storage. With this tool, I hope to save money by cancelling my Dropbox subscription.

  - **[Roma](https://github.com/htmfilho/roma)** : a library to generate SQL statements from CSV files. It has special features like grouping insert statements in transaction chunks and inserting multiple rows with a single insert statement.

It doesn't matter how cool these repositories are if they don't evolve with the same energy of the initial kickoff. To address this, I came out with an approach, popular in other areas, that can give me an indication of progress. I'm proposing a **Repository Maturity Model (RMM)** with 5 levels that looks like this:

1. **The repository is properly organized and documented, with a clear definition of the project, the goals, the license, the code of conduct, the license, templates, and contribution guidelines**.

2. **The codebase reaches a point of workable solution, releasing the first minimal viable product with complete documentation and demonstrations**.

3. **The codebase has reached at least 80% of test coverage and no reported defects pending in the backlog immediately after a release**.

4. **At least 10 pull requests from other individuals were merged in the last 12 months and there are at least 2 releases per year**.

5. **100 stars or watchers and active participation of users in the form of issues in the last 12 months**.

The maturity can upgrade or downgrade. For example: if the repository reaches 100 stars and has active users participation, which qualifies it to level 5, but the test coverage went down below the 80% threshold, then it downgrades to level 3.

This model will help me to measure my progress, but it can certainly be used by other repositories as well. We can even open an discussion about how to refine it [here](https://github.com/htmfilho/htmfilho.github.io/discussions/27). To achieve level 5, I will certainly need your help. If you liked any of these repositories, please go there and give a star. Also, watch them to keep up with my progress and maybe even learn with me. Thank you!