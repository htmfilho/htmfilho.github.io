---
layout: post
title: "Applets are not surviving, they are restarting!"
date: 2008-06-15 09:59:00 +0200
categories: uncategorized browser conference enterprise application java jvm web
---

A long time ago, I had used Applets in the Planexstrategy application to render statistical charts, such as bars, lines, pizza and so on. I developed these charts by myself and they were perfectly suitable for the system’s needs.

Unfortunately, <a href="http://www.sun.com/">Sun Microsystems</a> and <a href="http://www.microsoft.com/">Microsoft</a> got into a patent fight and the first serious consequence was that Microsoft stopped distributing the Java Virtual Machine as a plug in of the Internet Explorer :(. Actually, after this disagreement, to distribute the JVM became very difficult for three reasons: first, Java was not widely known by non-technical people, thus they don’t know about the existence of a certain JVM. Second, even if they know what is a JVM, it is very heavy to download it, considering the lower internet speed at that time, and also difficult to install. Third, a concurrent technology called Flash, created by Macromedia Inc. (Incorporated by Adobe nowadays), entered into the game to definitively kill the need for Applets in the field of interactive web pages.

The applet adoption had gone to a critical situation with the advent of a set of technologies under an umbrella called Ajax. The combination of HTML, XHTML, XML, SVG, JavaScript, SCC, XSLT, canvas and the main catalyst, XMLHttpRequest, allows the development of dynamic content without needing to refresh the whole web page. Now, the web page can adapt itself according to the user behavior. The problem of this model is the incompatibility of an Ajax code between web browsers, like Microsoft Explorer, Firefox, Opera, Safari and others. Every code should be tested with all of them before the production phase and it takes a lot of time. 

To address this problem, people started to develop frameworks, previously tested with all those browsers, offering a large set of widgets to be easily used on the web development. <a href="http://code.google.com/webtoolkit/">Google Web Toolkit</a> (GWT), <a href="http://developer.yahoo.com/yui/">Yahoo User Interface Library</a> (YUI) and <a href="http://getahead.org/dwr/overview/dwr">Direct Web Remoting</a> (DWR) are the main frameworks currently adopted. The problem now is the ability to add new components according to specific needs of the software. It’s too complicated for most developers to change a framework that mixes so many technologies. It is also difficult to be aligned with future versions of these frameworks.

Parallel to this revolution, the Flash technology has gained more and more attention with the possibility to create interactive applications on the web with the flexibility of a full featured scripting language, the Action Script. They saw an opportunity on the browser incompatibilities and created <a href="http://www.adobe.com/products/flex/">Flex</a> to simplify the development of interactive web applications. In addition, they introduced <a href="http://www.adobe.com/products/air/">Adobe Air</a>, a runtime to execute Flash application directly on the desktop.

Flex and Air are technologies that show the future of web applications. Future? Well, the idea behind Flex was available on Java Applets for years! We can develop high quality web applications with incredible features using swing. With the availability of the web today, Applets are not valued just because of marketing reasons. Sun Microsystems just stopped to promote Applets.

However, in <a href="http://www.javaone.com/">JavaOne’08</a>, Sun brought a very important news: Applets will implement the <a href="http://www.javafx.com/">JavaFX</a> technology and the development of interactive applications will become even more efficient and gorgeous! It will simplify even more the model proposed by Flex + Air. Watch the video below and see what I mean!

<object data="http://i.zdnet.com/flash/cnb_video.swf" height="350" type="application/x-shockwave-flash" width="400"><param name="FlashVars" value="vidFile=8n0507_Java_Applet.flv&amp;br=2&amp;autoplay=false&amp;still=http://i.zdnet.com/gallery/200561-400-300.jpg"/><param name="movie" value="http://i.zdnet.com/flash/cnb_video.swf"/><param name="wmode" value="transparent"/></object>
