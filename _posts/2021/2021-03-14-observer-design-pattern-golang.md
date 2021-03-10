---
layout: post
title:  "Reacting to File Changes in Go through the Observer Design Pattern"
date: 2021-03-14 12:00:00 +0200
categories: golang design pattern observer
---

Science has shown that shy people are clever because they spend more time listening and observing and less time speaking and showing off. They absorb more information and spend countless hours reasoning them. They do it quietly and are rarely recognized by their intellects. What science has not shown is that the Observer Design Pattern is also a humble part of a well designed software, but rarely recognized as such.

<!-- more -->

You know you are in front of a observer implementation when an event happens and one or multiple routines react to that. The event source is normally called **publisher** and the code that reacts to that is called **subscriber**. You can actually have a propagation of events where subscribers also act as publishers, triggering other subscribers in a chain reaction just like in a nuclear reactor.

The [fsnotify] library watches for changes in the file system