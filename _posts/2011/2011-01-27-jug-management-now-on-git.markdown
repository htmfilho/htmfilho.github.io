---
layout: post
title: "JUG Management Now on Git"
date: 2011-01-27 21:32:00 +0200
categories: cejug configuration management java open source
---

The JUG community asked and we have moved the JUG Management source code from SVN to Git. I have to admit that I’m new in Git and it seems to be a quite change of paradigm from SVN. My first feeling is that it is more complex. For the moment, my motivation to learn Git comes from the fact that there is a big probability that the market will value this knowledge.

To access the Java.net Git repository is not a trivial task 🙁 You will need SSH (Security Shell protocol) to have an encrypted connection to the server. I think this is too much for our needs, since this is not such a critical system, but this is real life, thus I followed the steps below:

<ol>
<li>Download and install a Git client according to your operating system. Clients are available at <a href="http://git-scm.com/download">http://git-scm.com/download</a>.</li>
<li>Installing Git is not enough to start working. You have to configure it, adding a public SSH key to your site profile as described in <a href="http://java.net/projects/help/pages/GeneratingAnSSHKey">Generating an SSH Key</a>. The whole process will take some time, but if you do it carefully, step by step, everything will work fine. It worked in my first attempt 😉</li>
<li>register yourself in <a href="http://cejug.java.net/">CEJUG’s project at java.net</a>. You will have access to the repository only if you are a member of the project. Registering in the project doesn’t mean you will become a CEJUG member. Actually, we use JUG Management to control our members 😉</li>
<li>When you login on Java.net and go to the <a href="http://java.net/projects/cejug/sources">source code section</a>, you will be able to see the checkout URI of JUG Management’s repository. The address contains your username. Example: ssh://[user-name]@git.java.net/cejug~jug-management.</li>
<li>Copy the URI above and go to the command line and type the following command to checkout the code: git clone ssh://[user-name]@git.java.net/cejug~jug-management. It will create a folder “cejug-jug-management” in the directory you ran the command and the full source code will be available there.</li>
</ol>
<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=c03ce-20&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=0596520123&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe> This is a good start. Now you can open the source code and try to learn the project. I will explore in the next post how to open the source code in an IDE and build a package for deployment. At the same time, I’m learning how configuration management works with Git in order to start receiving your contributions. I’m studying the book Version Control With Git by Jon Loeliger for this. I hope the idea of branch is still there, just with a different name.
