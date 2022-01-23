---
layout: post
title: "Usability Problem in the Netbeans Subversion Feature"
date: 2009-02-14 12:34:00 +0200
categories: ide java netbeans user interface
---

These days I will complete one year using [Netbeans](http://www.netbeans.org/) uninterruptedly in all my projects. I mean, 12 months without any successful attempt to go back to [Eclipse](http://www.eclipse.org/). Fortunately, the company that I work for (University) doesn’t force me to use Eclipse like many others I have seen. The priority here is creativity and not the IDE. For that you can use whatever you want.

However, this marriage is not so perfect. One of these problems is the current Netbeans support for [Subversion](http://subversion.tigris.org/) that I want to describe now. Take a look on the figure below. We are going to analyze the usability of this screen in particular.

![netbeans-subversion-usability-300x245.jpg](/images/posts/netbeans-subversion-usability-300x245.jpg)

Before starting you should be awere about Subversion. It is one of the most popular control version systems, widely used in open source projects and inside organizations. A control version system is essencial for sharing resources in a team, giving a second chance to recover that deleted file by mistake, identifying changes made since the last modifications, and so on. Netbeans 6.5 supports Subversion by default between others such as CVS and Mercurial. I am not going to explore other features or make any comparison between supported control version systems. I just want to show how hard it’s to submit my changes after the work is done.

In the figure above you can see a submission dialog. There is a text area on the top to write a comment about all modifications made and a table listing all available files in the project to sync with the server repository. In the table you see a list of files to synchronize, the status of each file in comparison with the repository, the action to be taken when submitting changes and the complete path of each file in the repository. In my opinion, these are enough information for a developer in his/er daily work.

Unfortunately, this user interface is not easy to use, which makes me avoid using this functionality. The main problem is that it always assumes that all files in the project should be in the repository. Then, if your application generates temporary files or it uses an embedded database, many files will be checked to be added in the repository and you have to uncheck all of them because you care about the organization of the repository. You can see in the figure many files “.dat”, which are JavaDB files embedded in my application. Of course I don’t want to commit them. To avoid it, I have to change the action of each file and they are many. I have no time for that at all. But imagine you don’t have so many files to add, then you can change the action easily. Unfortunately, you will have to do it every time you try o submit your project again because it doesn’t save your last actions.

In order to be more productive, I have to use [TortoiseSVN](http://www.blogger.com/www.tortoisesvn.net), a very good SVN client but external to the IDE. It really fulfills my needs in terms of usability, perfectly solving the problems I have with Netbeans. You may notice in the figure below that all those “.dat” files are unchecked for addition, saving my time a lot.

![tortoisesvn-usability-300x256.jpg](/images/posts/tortoisesvn-usability-300x256.jpg)

I hope this message helps the Netbeans team to improve this important functionality in a near release.
