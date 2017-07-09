---
layout: post
title: "Using the Java Logging Configuration File Without Command Line"
date: 2009-04-13 10:00:00 +0200
categories: uncategorized java
---

By the way, I found a solution to my problem with the <a href="http://java.sun.com/j2se/1.4.2/docs/guide/util/logging/overview.html">logging</a> configuration file that I reported <a href="http://69.89.31.239/~hildeber/?p=126">here</a>. The problem was to find an evidence that the logging configuration file could be referenced without changing the command line to add the parameter: 

<span style="font-family:courier new;"><span style="font-size:85%;">-Djava.util.logging.config.file=logging.properties</span></span> 

Why not change the command line? Basically, because I want to avoid command lines and continue clicking twice on the <span style="font-family:courier new;"><span style="font-size:85%;">.jar</span></span> file to open the application or enable a personalized logging if the application is distributed by <a href="http://java.sun.com/javase/technologies/desktop/javawebstart/index.jsp">Java Webstart</a>.

If the logging configuration file doesn’t exist, I want to generate this file according to the initial needs of the application. A basic need is to store logging files in a separate folder called <span style="font-size:85%;"><span style="font-family:courier new;">log</span></span>, placed in the same folder where the application is executed (working directory). The content of this file should be in xml to be processed afterwards by a logging analyzer. So, I implemented the following code in the main class (class where I implement the <span style="font-family:courier new;"><span style="font-size:85%;">main</span></span> method to initialize the application):

<span style="color:#3366ff;"><span style="font-size:85%;"><span style="font-family:courier new;">// this method is invoked in the main method<br/></span></span><span style="font-size:85%;"><span style="font-family:courier new;">// to initialize the logging.</span></span></span><span style="font-size:85%;"><span style="font-family:courier new;"><br/>public static void prepareLogging() {<br/>        File loggingConfigurationFile =<br/></span></span><span style="font-size:85%;"><span style="font-family:courier new;">           new File(“logging.properties”);<br/></span></span>

<span style="font-size:85%;"><span style="font-family:courier new;">        logger = Logger.getLogger(Main.class.getName());</span></span>

</p