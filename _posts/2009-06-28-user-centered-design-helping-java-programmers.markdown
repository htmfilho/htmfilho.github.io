---
layout: post
title: "User-centered Design Helping Java Programmers"
date: 2009-06-28 21:00:00 +0200
categories: uncategorized java research user interface
---

In general, analysts and programmers spend time taking care of user interfaces but researchers at Carnegie Mellon University’s <a href="http://www.cs.cmu.edu/">School of Computer Science</a> decided to focus on the user experience of those analysts and programmers instead. They developed the tools <a href="http://edelstein.pebbles.cs.cmu.edu/jadeite/">Jadeite</a> and <a href="http://edelstein.pebbles.cs.cmu.edu/apatite/">Apatite</a> which are intended to help Java developers exploring the language API (Application Programming Interface) using human-centered design techniques.

A basic feature of the Jadeite tool is to collaboratively improve the Java API by allowing developers to suggest modifications according to their needs. For instance, if you think that a class doesn’t have a method you were expecting or a parameter missing in a method signature then you are allowed to add them as you wish. This feature may help API designers to improve their libraries but programmers may still miss the implementation of those modifications, of course. The tool also increases the size of the font according to the frequency of use. This frequency is based on the number of Google hits, the crowdsource which well represents what most of people are doing. I think it is useful to help developers to decide what to use from the API, since most people are using these possible choices too.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2009/06/jadeite.jpg">![jadeite-300x272.jpg](/images/posts/jadeite-300x272.jpg)</a>

The Apatite tool takes a different approach, allowing programmers to browse APIs by association, which helps them to see packages, classes and methods that tend to go with each other. It also uses statistics about the popularity of each item to provide weighted views of the most relevant items, representing them as a cloud of tags.

To get more information visit <a href="http://www.cmu.edu/news/archive/2009/June/june17_javatools.shtml">http://www.cmu.edu/news/archive/2009/June/june17_javatools.shtml</a>.
