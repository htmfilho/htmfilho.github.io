---
layout: post
title: "Yet Another System for Multimedia Information Management – YASMIM"
date: 2010-05-02 11:04:00 +0200
categories: enterprise application integration java javafx open source research software architecture web services
---

As part of my research, I’m developing a system for media archiving with features that makes it a media information management. I figured out a nice acronym for this system: Yet Another System for Multimedia Information Management – YASMIM. The reason why it is “Yet Another System” is because there are several multimedia archiving systems out there and I’m going to create one more (I’m so brave! :P). It is not just a multimedia archiving system, but also a system to organize all information possibly related to the content of the media.

This system has 3 personal goals:

<ol>
<li>demonstrate my scientific contributions to the field of multimedia systems;</li>
<li>update my expertise on enterprise systems and manipulation of large datasets to get ready to the market again; and</li>
<li>share my acquired knowledge with people interested in <a href="http://www.amazon.com/Beginning-Java-trade-Platform-GlassFish/dp/1430219548?ie=UTF8&amp;tag=c03ce-20&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">JEE6</a>![ir?t=c03ce-20&l=btl&camp=213689&creative=392969&o=1&a=1430219548](/images/posts/ir?t=c03ce-20&l=btl&camp=213689&creative=392969&o=1&a=1430219548) (EJB3, JPA, JSF) server applications and <a href="http://www.amazon.com/Pro-JavaFX-trade-Platform-Technology/dp/1430218754?ie=UTF8&amp;tag=c03ce-20&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">JavaFX</a>![ir?t=c03ce-20&l=btl&camp=213689&creative=392969&o=1&a=1430218754](/images/posts/ir?t=c03ce-20&l=btl&camp=213689&creative=392969&o=1&a=1430218754) desktop applications because the best way to learn is sharing and teaching.</li>
</ol>
According to my plans, I’m going to finish my PhD in October, 2010. I’m writing the thesis right now and it is all about the YASMIM system. it’s planned to support several kinds of media, including images, videos, audios, and 3D models. The main differentials are the possibility to segment and annotate all these kinds of media within only one integrated system and provide these features through a web service interface, in addition to the conventional web interface. This system is open source, but I can only make it fully available after my thesis defense. However, I have published an initial (but compilable) source on <a href="http://github.com/htmfilho/Yasmim">GitHub</a>. If you wish, you can help me to develop it and we can figure out together many other innovative aspects. 😉

![yasmim-images-300x184.png](/images/posts/yasmim-images-300x184.png)

Why did I chose JEE6 and JavaFX? The first reason is that I’m supposed to get into the market soon and I have to update my knowledge of enterprise systems, which was what I used to work before the PhD. But of course, I cannot put in the thesis this reason. Better to find reasonable technical reasons. So, the technical reasons to choose JEE6 were:

<ul>
<li>the architecture allows the expansion of available resources without redesigning the code;</li>
<li>support for multiple user sessions;</li>
<li>support for authentication and authorization and I just have to worry about the content sensitiveness;</li>
<li> totally based on POJO, so I can keep the code as simple as possible while focusing on the algorithm part; and</li>
<li>the support for web services is native and implemented by Java annotations.</li>
</ul>
The technical reasons to choose JavaFX as the client technology were:

<ul>
<li>vectorial user interface rendering;</li>
<li>multi-platform, including mobile devices; and</li>
<li>good support for media playback.</li>
</ul>
An alternative platform to implement this system would be Adobe Flash. However, a basic technical problem prevented me to choose this platform: I use a Linux 64 bits operating system and it doesn’t work appropriately on it. Thus, besides having a bigger number of machines supporting Flash, some platforms do not support it well. Considering JavaFX, most platforms support it well, however, less machines have it installed. So, my decision was in favor of more compatibility.

If you are interested in this kind of application, not only for multimedia processing, but also to learn about Enterprise Java and JavaFX, be my guest and get involved on <a href="http://github.com/htmfilho/Yasmim">http://github.com/htmfilho/Yasmim</a>.
