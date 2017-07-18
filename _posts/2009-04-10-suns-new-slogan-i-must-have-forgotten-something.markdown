---
layout: post
title: "SUN’s new slogan: “I must have forgotten something”"
date: 2009-04-10 19:12:00 +0200
categories: cejug conference java jvm open source
---

I’m refactoring the code of a Swing application to implement the logging facilities offered by the Java Virtual Machine (JVM). It seems to be easy until you need some special feature like a personalized configuration file. Well, it is actually easy to use because we can declare the configuration file in the command line to start the application, like in the code below.

```
java -Djava.util.logging.config.file=C:\Temp\logging.properties -cp .
     myapp.business.SimpleApp
```

But if we don’t use a command line to start the application because we love the simplicity of the double click on the jar file or the facilities provided by the JavaWebstart, what the hell should we do to keep things like it always was? I couldn’t find any useful code until now to fulfill my needs. If you know any solution, please add it here as a comment to this post.

This experience opened a question in my mind: if the support for logging is so important, why this configuration file cannot be packaged like the “manifest.mf” and the “persistence.xml” files inside the META-INF folder of a jar file? Why don’t we just put this “logging.properties” there and everything works perfectly? People at SUN “must have forgotten something”. By the way, I think this is an internal slogan at SUN. 🙁

You can easily notice many minor omissions like the previous one. For example, it’s unacceptable that JavaFX cannot officially run integrated with Swing. I’m still trying to realize the need for JavaFX in my professional life. I can easily imagine how good it would be if those interesting effects could run in my current applications. They also seem not to trust their own technology, as you can see in many parts of <a href="http://www.sun.com/">SUN’s website</a>, where they use flash to reproduce videos and other media. How can they compete with flash if they cannot really demonstrate their competitiveness? I know, I know, many people don’t have the last version of the JVM, but I have it and I haven’t got the chance to see a unique website using the JavaFX technology until now. Just simple examples in <a href="http://learnjavafx.typepad.com/">websites dedicated to teach JavaFX</a>. Ups! I almost forgot to say that JavaFX produces vectorial content but the JavaFX script doesn’t have a single command to maximize the window of a JavaFX application. If you need it, you have to invoke an external code (Java). Once again, they must forgotten this simple feature.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2009/04/Dilbert-Cartoon.jpg">![Dilbert-Cartoon-268x300.jpg](/images/posts/Dilbert-Cartoon-268x300.jpg)</a>

In parallel, SUN created a social network website focused on university students, the <a href="http://osum.sun.com/">Open Source University Meetup</a> (or OSUM). You can find everything you want there except open source content. I think their intention is to wash brains of poor students with SUN technology. They forgot (again) that the biggest source of Java developers come from Java User Groups (JUG), not from universities. My JUG (<a href="http://www.cejug.org/">CEJUG</a>) is a great example. It promotes the Java technology in almost all universities in the state of Ceará (at least 10 and all of them pay to get involved, building a self sustainable model). With the OSUM initiative, SUN only gets the support of one or two universities in each city. In a whole country like Belgium, there are many university groups registered there, but none of them with more the 10 users. CEJUG has 700 members from many universities and many companies. Students talking directly with companies’ employees, feeling the marketing, adopting what the market adopts. The OSUM’s approach is not fair and not realistic because students cannot make good decisions about their technology adoption inside universities.

I admit that I was blind about SUN Microsystems, ignoring all their mistakes and keeping my faith about their recovery. I remember during the last <a href="http://devoxx.com/">Devoxx</a> when I’ve donated an idea to a SUN’s evangelist that could represent billions in profit to SUN and they ignored it or just forgot it again, again, and again. I’ve been waiting for a sunny day at SUN but now I’m tired. I can’t wait for the day when IBM will finally acquire SUN. When this day comes, I will blog about my 1 billion dollar idea and you will finally know what they forgot to do… again.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2009/04/Dilbert.jpg">![Dilbert-300x265.jpg](/images/posts/Dilbert-300x265.jpg)</a>
