---
layout: post
title: "Integrating Jira with Netbeans"
date: 2012-05-06 11:26:00 +0200
categories: agile cejug ide integration java netbeans open source
---

One of the advantages of hosting your open source project at Java.net is the availability of <a href="http://www.atlassian.com/software/jira/overview">Jira</a> to track your issues. Jira is one of the most popular issue tracking system available on the market, which drives tool developers to support it. This is the case of <a href="http://www.netbeans.org/">Netbeans</a>, my working IDE, and also the case of <a href="http://www.eclipse.org/" target="_blank">Eclipse</a>.

I recently configured my Netbeans to access <a href="http://java.net/projects/cejug/sources/jug-management/show" target="_blank">Jug Manangement</a>‘s issues. If you want to do the same, or with another project hosted on Java.net or even connect to the Jira available on your company’s Intranet, then the following instructions may help you.

The first step is to install Jira plugin on Netbeans. In the menu, select <i>Tools</i> and then <i>Plugins</i>. Go to the tab <i>Available Plugins</i> and select <i>JIRA</i>. Follow the installation procedure and restart the IDE at the end. The figure below shows the plugin already installed. You may check as well if <i>JIRA</i> is in your list of <i>Installed</i> plugins to make sure everything went well.

<div style="clear: both; text-align: center;"><a href="http://69.89.31.239/~hildeber/wp-content/uploads/2012/05/netbeans-jira-plugin-installation.png" style="margin-left: 1em; margin-right: 1em;">![netbeans-jira-plugin-installation-300x169.png](/images/posts/netbeans-jira-plugin-installation-300x169.png)</a></div>
In the view <i>Services</i>, where we connect to databases, webservers and others, we also find a new kind of service called <i>Issue Trackers</i>. By clicking with the right button on this service, you are about to create a connection to a issue tracker. A dialog like the following figure appears. Give any name to your connection, since this is not a predefined value. In case of Java.net, use the URL https://java.net/jira and the credentials you use to authenticate in the portal. Click on <i>Validate</i> to make sure that you input the values correctly and the connection with the server is working. Click on <i>Ok</i> to finish.

<div style="clear: both; text-align: center;"><a href="http://69.89.31.239/~hildeber/wp-content/uploads/2012/05/netbeans-jira-configuration.png" style="margin-left: 1em; margin-right: 1em;">![netbeans-jira-configuration.png](/images/posts/netbeans-jira-configuration.png)</a></div>
Now, you are connected but not ready to work yet. The next step is to find the issues. For that, click with the right button on the issue tracker that you just created and select the option <i>Find Issues</i>. It opens a new tab in the editor area where you are able to build your query as you usually do using Jira on a web browser. When you build the best query for your needs you can save it to constantly work with that. In the following figure I built a query that shows me all open issues of the project jug-management.

<div style="clear: both; text-align: center;"><a href="http://69.89.31.239/~hildeber/wp-content/uploads/2012/05/netbeans-jira-query.png" style="margin-left: 1em; margin-right: 1em;">![netbeans-jira-query-300x233.png](/images/posts/netbeans-jira-query-300x233.png)</a></div>
You can do something similar to your project and control your issues directly from the IDE. One of the main benefits of this approach is that, by restricting the use of the browser, we reduce the probability of losing the focus on the work due to other entertainment activities on the web such as news, social networks, chatting and so on.
