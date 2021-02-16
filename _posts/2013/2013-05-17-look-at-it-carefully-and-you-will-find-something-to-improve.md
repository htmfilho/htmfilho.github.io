---
layout: post
title: "Look At It Carefully And You Will Find Something To Improve"
date: 2013-05-17 08:05:00 +0200
categories: java refactoring
---

I propose you an exercise: when you come back to work tomorrow morning, navigate through the source code of your project and try to find opportunities of refactoring. Do it even if your boss didn’t ask for it. Do it because you want some exciting time at work.

**Refactoring is the art of changing what is already working fine**. But to do refactoring you need an excuse. It could be design improvement, performance issues, security roles, and many other reasons. That’s a risk you take to reduce the technical debit of the application, making it more stable and, somehow, improving your own productivity in the future.

This is not about being nice with the company or with the boss, but being nice with yourself. Why? Because problems tend to accumulate and, at some point, you will lose the control of your code. You will face hard times to deliver results and it will ruin your career.

Well, let’s see this from a brighter perspective instead. You will learn a lot in the process and will soon realize that you are producing better code than you ever did before. The more refactoring you do, the more clever you become until a point where you may reach the level of innovation. But, what does it mean and how do you know you are getting there?

Innovation happens when you find a clear opportunity for improvement on what you are doing and you realize nobody else did it so far (at least you couldn’t find it). That’s not easy, but it usually happens when you do something repeatedly and you find yourself thinking about what would you do to do the same thing faster or cleaner. Let me illustrate this with a true story.

It was about String concatenation in Java: a classical issue stressed by numerous specialists throughout the years and probably ignored nowadays. Before JDK 1.5, despite its readability and simplicity, String concatenation using the operator `+` could produce a very inefficient code. Behind the scene, this operator was replaced by the bytecode equivalent of [StringBuffer](http://docs.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html), which actually implemented the concatenation. The more you used the “+” operator the more instances of String and StringBuffer you would have in memory as well as a good amount of processing time to manage all those objects. Because of that, developers were pushed to use StringBuffer straight away and ignore the `+` operator. Look at the following example:

{% highlight java %}
String title = "Mr.";
String name = "John";
String familyName = "Smith";

String message = "Dear " + title + " " + name + " " + familyName + ",";
{% endhighlight %}

Developers were used to write like that, but they were pushed to write this instead:

{% highlight java %}
StringBuffer sb = new StringBuffer();
sb.append("Dear ");
sb.append(title);
sb.append(" ");
sb.append(name);
sb.append(" ");
sb.append(familyName);
sb.append(",");
{% endhighlight %}

You may agree with me that the first example is more readable than the second one. It’s just natural for developers to use the `+` operator when concatenating strings, thus it was unfair to abandon that syntax. Fortunately, compiler guys did something about it, making sure that the JDK 1.5 would optimize concatenations. Instead of using StringBuffer, a thread-safe class, they created a new one called [StringBuilder](http://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html) (non thread-safe, thus faster) and they made sure that a single instance of it would handle all concatenations as illustrated in the first example. That’s an important move because they favored elegance instead of technicalities. The first example is automatically transformed at compile time into something like this:

{% highlight java %}
StringBuilder sb = new StringBuilder();
sb.append("Dear ").append(title).append(" ")
  .append(name).append(" ").append(familyName)
  .append(",");
{% endhighlight %}

However, concatenations within a non trivial logic still require you to write StringBuilder in your code because the compiler is not that smart yet. For example:

{% highlight java %}
List students = studentBean.findStudents();
String intro = "The following students were approved:";
String listedNames = "";
String separator = "";
for(Student student: students) {
  if(student.approved()) {
    if(!listedNames.isEmpty()) {
      separator = ", ";
    }
    listedNames += separator + student.getName();
  }
}
String msg = intro + listedNames;
messengerBean.sendMessage(msg);
{% endhighlight %}

would be more efficient if written like that:

{% highlight java %}
List students = studentBean.findStudents();</span>
String intro = "The following students were approved:";
StringBuilder listedNames = new StringBuilder();
String separator = "";
for(Student student: students) {
  if(student.approved()) {
    if(!listedNames.length() > 0) {
      separator = ", ";
    }
    listedNames.append(separator)
               .append(student.getName());
  }
}
String msg = intro + listedNames.toString();
messengerBean.sendMessage(msg);
{% endhighlight %}

Ups! Did you noticed anything strange up there? It might not be obvious at a first look, but see how they check if the variable `listedNames` is empty before defining the separator. The class String has a nice readable method `isEmpty()` introduced in JDK 1.6, but StringBuilder still uses that pretty old way of comparison. Why didn’t they do it for StringBuilder and StringBuffer as well?

[Discussing the issue at the core-lib-dev mailing list](http://mail.openjdk.java.net/pipermail/core-libs-dev/2013-February/014433.html), it turns out there is no apparent reason why they didn’t do that before. Perhaps they simply forgot it. Thanks to a large refactoring, trying to improve inefficient uses of string concatenation, it was possible to find such inconsistency. I believe they still have time to fix that for Java 8, which is coming out next year. And they would fix that by adding the method `isEmpty()` in the interface [CharSequence](http://docs.oracle.com/javase/7/docs/api/java/lang/CharSequence.html) to make sure that every other implementation will be equally elegant.

That might be a simple thing, but every single detail matters when Java is under heavy criticism for being such a verbose language. So, go for some refactoring and find opportunities to improve your code as well as the language you use to write it! Let’s move Java forward!
