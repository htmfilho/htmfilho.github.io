---
layout: post
title: "TomEE-CLI: An Alternative To Manage TomEE"
date: 2015-04-15 22:39:46 +0200
categories: development clojure configuration management enterprise application java ee open source
---

About a year ago, when I was looking for alternatives to replace our Glassfish servers ([why?](/2013/11/glassfish-is-now-a-javaee-toy.html)), I had the chance to evaluate [TomEE](http://tomee.apache.org/apache-tomee.html). Talking to TomEE’s team was indeed a pleasant experience. By far, the best support you can get from a JavaEE player. Just to give you an idea, they replied all questions in less than 24 hours, while we had to wait over a month to get the first feedback from RedHat about JBoss EAP. We had multiple evaluation criteria and, unfortunately, TomEE didn’t go well in the management part. JBoss offered redundant ways to manage the server, including a web API, a command line tool and a web console. Since the infrastructure team put too much weight on the management aspect, I had to agree and formally recommend JBoss EAP. Sometimes, we have to make unpleasant decisions, but that’s business.

As an open source enthusiast, I knew I needed to do something to help TomEE. So, I thought about contributing to the documentation but I had to step back because my daughter had just been born at the time. Looking at my GitHub profile, one can see how much of my free time was filled up with paternity love. The good news is she is growing fast and becoming less demanding, leaving some room for my open source projects.

![github-contributions.png](/images/posts/github-contributions.png)

In January this year, when my brain left hemisphere was in good shape again, I decided to learn <a href="http://www.clojure.org" target="_blank">Clojure</a>, a functional programming language on the JVM. I’ve got so excited that I started telling my friends about what I would describe as a “mind-blowing experience”. One of them, <a href="https://github.com/danielsoro" target="_blank">Daniel Cunha</a>, was particularly excited about that. We were talking all the time about infinity possibilities we have at hands with Clojure. Then he suddenly came out with a project proposal I couldn’t refuse: “Let’s write a client tool for TomEE. I’m trying to write one in Java, but it’s taking too long. Let’s write it in Clojure”. And then I said “Yesss! Of course”. Daniel didn’t realise but he was giving me the chance I was looking for: solving exactly the point where TomEE didn’t do well in our analysis. I’m sure Daniel didn’t expect such enthusiasm coming from a contributor.

On April 13th 2015 <a href="https://github.com/bitmaker-software/tomee-cli/releases" target="_blank">we released the first version</a> of <a href="https://github.com/bitmaker-software/tomee-cli" target="_blank">TomEE-CLI</a>. We started our endeavour in Mars 9th and we managed to develop <a href="https://github.com/bitmaker-software/tomee-cli/wiki/Usage" target="_blank">11 functionalities</a> within a month with just 300 lines of code. No doubt Clojure and its ecosystem has made it possible. Can you imagine what we can achieve within a whole year?!

<h3>How It Works</h3>

We basically developed a Clojure API to manage TomEE instances. This API is so simple that you don’t even need to learn Clojure to use it. Clojure’s syntax to call functions is remarkably obvious. If you aren’t familiar with LISP dialects you will probably ignore the fact that you’re actually coding valid LISPs expressions to manage your server. You may ask your self: “But, it’s an API so I need to write my own Clojure code to use it, right?”. Writing your own code is actually optional because you can use the [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (Read-Eval-Print Loop) to execute Clojure expressions. In a single line of code you can call any of the functions available. Look how we use the REPL to invoke a function that installs TomEE 1.7.1 Plus in the working directory.

![clojure-repl-tomee-cli1.png](/images/posts/clojure-repl-tomee-cli1.png)

The REPL gives a real feeling of an interactive shell. That’s why we didn’t wait too long to release TomEE-CLI. It’s a basic, but valid user interface that people could start using immediately. Features like auto-complete, history and multi-line commands are also provided by the REPL. In the long run, the REPL won’t be the only way to interact with TomEE-CLI. We are planning to add a rich shell interface for experienced hackers, an in-line parameters interface for easy integration with automation tools such as Jenkins, and a web interface for beginners and remote administrators.

You can find installation instructions in the <a href="https://github.com/bitmaker-software/tomee-cli/blob/master/README.md" target="_blank">readme file</a> and a complete list of functionalities in the <a href="https://github.com/bitmaker-software/tomee-cli/wiki" target="_blank">project’s wiki</a>.

You may be surprised I’m devoting time to a JavaEE initiative after [leaving it behind](/2015/02/leaving-javaee-behind.html). Well, software development is all about people. So, even when a specification sucks, people using it are still good people, thus I’m writing it for them. Besides that, I’m happy to write Clojure code to solve real world problems faced by JavaEE developers in a daily basis.

Daniel and I understand that we may not have many contributors because the actual Clojure source code looks weird for Java developers. That’s what I thought when I first looked at it. But I can tell you that I’m not that smart and I was able to grasp the language in less than a month. Now, I’m delivering new functionalities in a short period of time, preserving the same level of performance and robustness offered by the JVM. When I became a father I realized time is my most precious resource. I simply can’t waste it anymore.

![DSC00410-1024x768.jpg](/images/posts/DSC00410-1024x768.jpg)
