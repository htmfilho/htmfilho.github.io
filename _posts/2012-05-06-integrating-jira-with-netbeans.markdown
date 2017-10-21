---
layout: post
title: "Integrating Jira with Netbeans"
date: 2012-05-06 11:26:00 +0200
categories: agile cejug ide integration java netbeans open source
---

One of the advantages of hosting your open source project at Java.net is the availability of [Jira] to track your issues. Jira is one of the most popular issue tracking system available on the market, which drives tool developers to support it. This is the case of [Netbeans], my working IDE, and also the case of [Eclipse].

I recently configured my Netbeans to access Yougi‘s issues. If you want to do the same, or with another project hosted on Java.net or even connect to the Jira available on your company’s Intranet, then the following instructions may help you.

The first step is to install Jira plugin on Netbeans. In the menu, select _Tools_ and then _Plugins_. Go to the tab _Available Plugins_ and select _JIRA_. Follow the installation procedure and restart the IDE at the end. The figure below shows the plugin already installed. You may check as well if _JIRA_ is in your list of _Installed_ plugins to make sure everything went well.

![netbeans-jira-plugin-installation](/images/posts/netbeans-jira-plugin-installation-300x169.png)

In the view _Services_, where we connect to databases, web servers and others, we also find a new kind of service called _Issue Trackers_. By clicking with the right button on this service, you are about to create a connection to a issue tracker. A dialog like the following figure appears. Give any name to your connection, since this is not a predefined value. In case of Java.net, use the URL https://java.net/jira and the credentials you use to authenticate in the portal. Click on _Validate_ to make sure that you input the values correctly and the connection with the server is working. Click on _Ok_ to finish.

![netbeans-jira-configuration.png](/images/posts/netbeans-jira-configuration.png)

Now, you are connected but not ready to work yet. The next step is to find the issues. For that, click with the right button on the issue tracker that you just created and select the option _Find Issues_. It opens a new tab in the editor area where you are able to build your query as you usually do using Jira on a web browser. When you build the best query for your needs you can save it to constantly work with that. In the following figure I built a query that shows me all open issues of the project jug-management.

![netbeans-jira-query-300x233.png](/images/posts/netbeans-jira-query-300x233.png)

You can do something similar to your project and control your issues directly from the IDE. One of the main benefits of this approach is that, by restricting the use of the browser, we reduce the probability of losing the focus on the work due to other entertainment activities on the web such as news, social networks, chatting and so on.

[Eclipse]: http://www.eclipse.org
[Jira]: http://www.atlassian.com/software/jira/overview
[Netbeans]: http://www.netbeans.org
