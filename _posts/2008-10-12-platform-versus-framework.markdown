---
layout: post
title: "Platform versus Framework"
date: 2008-10-12 20:03:00 +0200
categories: integration java jvm research architecture
---

In the last 30 days I had the pleasure to work in the context of the
[OpenInterface] project, writing a document that delineates how the platform
will continue after the project period. They thought I could help because of my
long experience with the open source community. Actually, it was a great
challenging experience with hard and pleasant moments. The most exciting one was
in Porto, Portugal, on the border of the river, when I found inspiration to
write some killer sentences.

During the elaboration of this document, many people from the project gave
contributions, comments, critics, which was essential to get a better result at
the end. But one of them called my attention. One of the contributors, asked to
change the term "platform" to "framework", which was funny because the name
"platform" is spread through many other documents and on the website. If the
person had some fundamentals to propose this change, what are they? Then I
decided to make a short research about the difference between both concepts and
the best place to start is, of course, the dictionary.

The word "platform" has many meanings, including the computer science one. In
the Cambridge English Dictionary:

> “Platform describes the type of computer system you are using, in connection
  with the type of software you can use on it.”

This is a very generic definition, which doesn't help me at all. So, I went to
Wikipedia, where I found a definition without any alert about its sources or
impartiality:

> “In computing, a platform describes some sort of hardware architecture or
  software framework (including application frameworks), that allows software to
  run. Typical platforms include a computer’s architecture, operating system,
  programming languages and related runtime libraries or graphical user
  interface.”

Oh God! It mentions framework on the definition of platform. Is it some sort of
recursive definition? Well, let’s go to the framework’s definition:

> “A software framework is a re-usable design for a software system (or
  subsystem). A software framework may include support programs, code libraries,
  a scripting language, or other software to help develop and glue together the
  different components of a software project. Various parts of the framework may
  be exposed through an API.”

Well, better! Let’s analyze the differences. First: framework refers only to
software and ignores hardware totally. So, if you work with hardware it will
never have a framework. Second: a platform allows a software to run, which is
not a framework requirement, since it is more focused on design. For instance,
[Java] is a platform because it has a virtual machine that allows Java
applications to run in many operating systems. On the other hand, [Spring] is a
framework because it simplifies the way you design software, taking the
responsibility for a lot of things to reduce the effort and the volume of code
needed to implement the application. So, a platform doesn't aim to save your
time, but to give you one or more possibilities to run your application.

Going back to the root of the discussion, I had a long conversation with the
main developer of the OpenInterface (OI), Lionel Lawson, and we concluded that
OI is, at the same time, a platform and a framework. It means that, when
platform, OI can run your application on it. When framework, your application
can use the OI’s API to access other components. Then, we concluded that OI is
actually a technology, which is more generic and solves many integration
problems between low level components.

[Java]: http://java.sun.com
[OpenInterface]: http://www.openinterface.org
[Spring]: http://www.springframework.org
