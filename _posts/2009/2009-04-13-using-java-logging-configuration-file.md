---
layout: post
title: "Using the Java Logging Configuration File Without Command Line"
date: 2009-04-13 10:00:00 +0200
categories: java
---

By the way, I found a solution to my problem with the [logging](http://java.sun.com/j2se/1.4.2/docs/guide/util/logging/overview.html) configuration file that I reported [here](/2009/04/suns-new-slogan-i-must-have-forgotten-something.html). The problem was to find an evidence that the logging configuration file could be referenced without changing the command line to add the parameter:

    -Djava.util.logging.config.file=logging.properties

Why not change the command line? Basically, because I want to avoid command lines and continue clicking twice on the `.jar` file to open the application or enable a personalized logging if the application is distributed by [Java Webstart](http://java.sun.com/javase/technologies/desktop/javawebstart/index.jsp).

If the logging configuration file doesn’t exist, I want to generate this file according to the initial needs of the application. A basic need is to store logging files in a separate folder called `log`, placed in the same folder where the application is executed (working directory). The content of this file should be in xml to be processed afterwards by a logging analyzer. So, I implemented the following code in the main class (class where I implement the `main` method to initialize the application):

{% highlight java %}
// this method is invoked in the main method
// to initialize the logging.
public static void prepareLogging() {
  File loggingConfigurationFile = new File("logging.properties");
  logger = Logger.getLogger(Main.class.getName());

  // it only generates the configuration file
  // if it really doesn't exist.
  if(!loggingConfigurationFile.exists()) {
    Writer output = null;
    try {        
      output = new BufferedWriter(
                    new FileWriter(loggingConfigurationFile));
      // The configuration file is a property file.
      // The Properties class gives support to
      // define and persist the logging configuration.
      Properties logConf = new Properties();
      logConf.setProperty("handlers",
           "java.util.logging.FileHandler",
           "java.util.logging.ConsoleHandler");
      logConf.setProperty(".level", "INFO");
      logConf.setProperty(
           "java.util.logging.ConsoleHandler.level",
           "INFO");
      logConf.setProperty(
           "java.util.logging.ConsoleHandler.formatter",
           "java.util.logging.SimpleFormatter");
      logConf.setProperty(
           "java.util.logging.FileHandler.level",
           "ALL");
      logConf.setProperty(
           "java.util.logging.FileHandler.pattern",
           "log/application.log");
      logConf.setProperty(
           "java.util.logging.FileHandler.limit",
           "50000");
      logConf.setProperty(
           "java.util.logging.FileHandler.count", "1");
      logConf.setProperty(
           "java.util.logging.FileHandler.formatter",
           "java.util.logging.XMLFormatter");
      logConf.store(output, "Generated");
    }
    catch (IOException ex) {
      logger.log(Level.WARNING,
                 "Logging configuration file not created", ex);
    }
    finally {
      try {
        output.close();
      }
      catch (IOException ex) {
        logger.log(Level.WARNING,
              "Problems to save " +
              "the logging configuration file in the disc",
              ex);
      }
    }
  }

  // This is the way to define the system
  // property without changing the command line.  
  // It has the same effect of the parameter
  // -Djava.util.logging.config.file
  Properties prop = System.getProperties();
  prop.setProperty(
     "java.util.logging.config.file",
     "logging.properties");

  // It creates the log directory if it doesn't exist  
  // In the configuration file above we specify this
  // folder to store log files:
  // logConf.setProperty(
  //         "java.util.logging.FileHandler.pattern",  
  //         "log/application.log");
  File logDir = new File("log");
  if(!logDir.exists()) {
    logger.info("Creating the logging directory");
    logDir.mkdir();
  }
  // It overwrites the current logging configuration
  // to the one in the configuration file.
  try {
    LogManager.getLogManager()
      .readConfiguration();
  }
  catch (IOException ex) {
    logger.log(Level.WARNING,
      "Problems to load the logging "+
      "configuration file", ex);
  }
}
{% endhighlight %}

This way, you can enable and better organize the logging of your application without any additional configuration. If you want to execute the application by command line it is still simple:

    java -jar myapp.jar

Or simply click twice on the file in most of the cases. The point about this post is not only teach you about logging stuff, but also motivate you to keep things simple to the final user.
