---
layout: post
title: "Finally a JavaFX Application in Production Out There"
date: 2009-12-12 07:19:00 +0200
categories: javafx web
---

For the first time ever, I finally saw a JavaFX application in production. I received this news from someone I’m following on Twitter. Check it out and come back for my comments:

http://www.vancouver2010.com/olympic-medals/geo-view/

This is the website of the 2010 Winter Games that will be held in Vancouver, Canada. Looking at the center of the figure, you can see a Java logo, indicating that an applet is loading and soon a JavaFX application is going to load in that area. Well, this was the good news. Let’s go to the bad ones.

![vancouver-website-300x162.png](/images/posts/vancouver-website-300x162.png)

The JavaFX applet takes sometime to load, even for me who has a 4MB/Sec connection at home. But this is not actually a problem. The problem is that users has no idea of how long they still have to wait. The Java logo animation is cute, but totally useless. A good approach is to show the progress of the download, a percentage figure very common in thousands of Flash applications.

When the applet finishes loading, look at the top-right and see the JavaFx logo. Come on! Why? It seems to me that they used JavaFx instead of other technologies because SUN sponsored the development of the applet. Is there any channel at SUN where I can ask them to develop an applet for me? I need it too. Or maybe the developer is so passionate about JavaFx that he put the JavaFx logo there and nobody said anything. That’s great! JavaFx is unanimous. 😛
