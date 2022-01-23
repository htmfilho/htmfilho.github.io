---
layout: post
title: "JavaFX Must be a Joke"
date: 2012-11-18 09:13:00 +0200
categories: java javafx jvm user interface
---

More than 3 years ago, I wrote the post [Has JavaFX a Strategy?](/2009/06/has-javafx-a-strategy.html)” saying:

> <span style="background-color: white; color: #333333; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 15px; line-height: 20px;">“</span><span style="background-color: white; color: #333333; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 15px; font-style: italic; line-height: 20px;">Don’t you think that the fastest way to spread the JavaFX adoption is allowing the improvement of existing applications? Why to spend a lot of resources to drag an applet from the browser to the desktop if we need the network anyway?</span><span style="background-color: white; color: #333333; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 15px; line-height: 20px;">“</span>


At that time, JavaFX Script was the only alternative to develop richer Java desktop applications. Guess what Oracle did right after Sun’s acquisition: they stopped evolving a pretty stupid new language which looked more like Json, which is designed for data; migrated the whole thing to a new Java library; and allowed the integration with legacy code (i.e. Swing applications). If they didn’t get inspired by my old blog post, then they just followed the sane common sense.

Meanwhile, Adobe gave up Flex and Microsoft gave up Silverlight. Strangely, Oracle kept insisting on JavaFX. We can see a lot of JavaFX demos out there, but not so much production-ready apps.  That’s a shame after all these years. The single example I have of a real world application is from a Belgian company called [Health Connect](http://www.healthconnect.be/). That’s all! Anybody else?! JavaFX evangelists would give a lot of confidence to Java developers if they promoted JavaFX applications in production. We have the impression that those evangelists are paid to have fun. This is really unexpected from Oracle, which looks like a very serious company. Take the example of Apple. They are very efficient on that. Every time they present their gadgets they also present outstanding apps developed for that device. It definitively makes developers excited!

![javafx-mobile.jpg](/images/posts/javafx-mobile.jpg)

I was about to be excited when Oracle announced JavaFX running on OS6 with an app called [JavaFX Ensemble](http://fxexperience.com/2012/10/javafx-ensemble-in-the-mac-app-store/), but when I realised that the goal of the app was simply to add more demos to the shelf, I got immediately frustrated 🙁 Is it so difficult to convince a company out there to write a useful app in JavaFX and make it available on OS6?! Come on! We are tired of demos!

Now, let’s imagine that JavaFX is a great technology and everybody is adopting it. Is everything ok now? Nooooooo! Even if everybody is convinced about JavaFX, [there is no stable, reliable and easy to use JVM out there for the client side at the moment](http://www.pcworld.com/article/261843/time_to_give_java_the_boot_.html). Therefore, we cannot efficiently distribute JavaFX apps on desktops. We have to be within a company, with full control over the network, to manage the installation, security and upgrades of the JVM in all desktops in order to distribute the application. Well, that’s silly :-/

![mise-a-jour-java-error-300x120.png](/images/posts/mise-a-jour-java-error-300x120.png)

I’m quite confident to advise you to leave JavaFX aside and go for HTML5. Most of its features are already cross-browser compatible and it’s possible to build amazing user interfaces with that. Client-side Java is over, so get used to an exclusively java server-side world soon. Surprisingly, it doesn’t make me sad, but happier 🙂
