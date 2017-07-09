---
layout: post
title: "Acessing Resources Inside of Jar Files"
date: 2008-12-20 22:17:00 +0200
categories: uncategorized java user interface
---

A short post to document a special detail in swing applications that causes an annoying waste of time. As a clever programmer, you always distribute your applications in JAR (Java achieve) packages, but you also put nice icons in your application to make it more attractive for final users and put some default configurations for basic initializations. The annoying problem (but easy to solve) is to package images and other files in a JAR file and create portable links to those files.

If you need to access a text file inside a JAR, the code is not self evident, but easy. To load an XML file, for example, you have to use the code below:

<span style="font-family:'courier new';"><span style="font-size:small;">ClassLoader cl = this.getClass().getClassLoader();<br/>java.io.InputStream in = cl.getResourceAsStream(“properties.xml”);</span></span>

The file “properties.xml” is inside the “application.jar” file, in the same package of the class where it is called. You can put this file in another package, but it will be more difficult to define the exact location of it. It’s easier and coherent if you keep the caller and the resource in the same place.

When you want to access images from the jar file the code is a little bit different. The example below shows how to create an image icon to illustrate swing components.

<span style="font-size:small;"><span style="font-family:'courier new';">JButton btRemove = new JButton(new ImageIcon(SearchTab.class.getResource(“remove.png”));</span></span>

Again, the figure “remove.png” is in the same package of the class “SearchTab.class”.

<div>
<div>The Java API doesn’t provide one form to change files inside jar files. We can read and manipulate the content, but not save it back in the same file. So, this is a solution for read-only needs.</div>
</div>