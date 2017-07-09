---
layout: post
title: "My Netbeans 6.1 Personal Issues"
date: 2008-06-01 20:11:00 +0200
categories: uncategorized ide java netbeans
---

After an intensive work with <a href="http://www.netbeans.org/">Netbeans 6.1</a> in all my projects this year, I was able to create my personal list of annoying issues. It doesn’t mean I will leave Netbeans. Far from that! What I really want is to draw attention for those issues in order to get them solved on the next Netbeans version (probably 6.5 in October 2008). So, lets have fun!

<span style="font-weight: bold;">Absolute References to Libraries in a Shareable File</span>

If you add jar files, which are independent from those libraries managed by Netbeans, to your project, Netbeans will store absolute references for them in the <span style="font-style: italic;">nbproject/project.properties</span> file. The problem is that Netbeans tries to share this file when you configure the project to commit versions to a SVN repository (I don’t know about CVS, but it could be a common problem). Sharing this file will cause problems for other team members, mainly for those who use Linux, OpenSolaris and other ones that implement a different path syntax. My suggestion is to create a lib folder, as important as the test folder is, copy all independent libraries to that folder and store relative paths in the <span style="font-style: italic;">nbproject/project.properties</span> file.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2008/06/netbeans-project-library.png">![netbeans-project-library-300x254.png](/images/posts/netbeans-project-library-300x254.png)</a>

<span style="font-weight: bold;">JSP Auto-complete </span><span style="font-weight: bold;">Doesn’t Work Very Well</span>

I’m developing some JSF pages these days using <a href="http://facelets.dev.java.net/">Facelets</a>, which adopts XHTML (XML based) format to code the view. I found a simple but very significant issue, as you can see in the figure below. When you finish to type a tag, which name follows the camel notation, the auto-complete feature doesn’t understand that the closing tag should also follow the camel notation. If it’s able to recognize the tag, why doesn’t it just reuse its name instead of invoking a String.toLowerCase() method before? Then we press enter to confirm the auto-completing suggestion and the issue remains there.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2008/06/netbeans-issue.png">![netbeans-issue-300x161.png](/images/posts/netbeans-issue-300x161.png)</a>

It seems to be a very simple issue, but if you are writing hundreds and hundreds of code, it is absolutely annoying.

Another XML auto-complete issue is shown in the figure below.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2008/06/netbeans-issue-2.png">![netbeans-issue-2-300x58.png](/images/posts/netbeans-issue-2-300x58.png)</a>

If you see carefully, the tag <h:outputtext> doesn’t have a body because there is a “/” character at the end, but the auto-complete suggests to add one</h:outputtext>. It’s a minor problem because I can go on just pressing “Esc”, but it’s still inconsistent. The figure is pretty illustrative because it shows the previous issue as well, since the camel notation is not respected.

<span style="font-weight: bold;">Performance Issue: Divide and Conquer</span>

One of the most important advantages reported about the version 6.1 was the startup time reduction. They succeeded to reduce in 40% the time to start the IDE since the previous version. However, this apparent performance improvement was resultant from an on-demand loading, since resources load when the user asks for them. The figure below shows the exact moment of a project being loaded when the user selects it in the project tab.

<a href="http://69.89.31.239/~hildeber/wp-content/uploads/2008/06/netbeans-performance.png">![netbeans-performance-300x143.png](/images/posts/netbeans-performance-300x143.png)</a>

So, you wait less time to load the IDE, but you wait the same time to start working. It’s important to mention that the performance issue is only an issue at the beginning. During the work, the IDE behaves very well.

<span style="font-weight: bold;">Issues in the Netbeans SQL Command Tab</span>

I have heard that <a href="http://www.netbeans.org/community/releases/roadmap.html">Netbeans 6.5</a> will have considerable evolutions on the database support. I hope so, because I’m having some troubles with the current one. Actually, it is not usable, since you have to resize the resulting columns all the time. Take a look at the video below.

<object class="" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" height="266" id="BLOG_video-8b8a9b32c38a0ee4" width="320"><param name="movie" value="//www.youtube.com/get_player"/><param name="bgcolor" value="#FFFFFF"/><param name="allowfullscreen" value="true"/><param name="flashvars" value="flvurl=http://redirector.googlevideo.com/videoplayback?id%3D8b8a9b32c38a0ee4%26itag%3D5%26source%3Dblogger%26app%3Dblogger%26cmo%3Dsensitive_content%253Dyes%26ip%3D0.0.0.0%26ipbits%3D0%26expire%3D1398602655%26sparams%3Did,itag,source,ip,ipbits,expire%26signature%3D8EEE5FA1FEC85BEA81FD86F30D03958BE7BA0918.11548D74FBAB2BADED9CC0B0705BADF9844DCE53%26key%3Dck2&amp;iurl=http://video.google.com/ThumbnailServer2?app%3Dblogger%26contentid%3D8b8a9b32c38a0ee4%26offsetms%3D5000%26itag%3Dw160%26sigh%3DwXOXTXVVFaeBK7VxckU46DsNrzg&amp;autoplay=0&amp;ps=blogger"/><embed allowfullscreen="true" bgcolor="#FFFFFF" flashvars="flvurl=http://redirector.googlevideo.com/videoplayback?id%3D8b8a9b32c38a0ee4%26itag%3D5%26source%3Dblogger%26app%3Dblogger%26cmo%3Dsensitive_content%253Dyes%26ip%3D0.0.0.0%26ipbits%3D0%26expire%3D1398602655%26sparams%3Did,itag,source,ip,ipbits,expire%26signature%3D8EEE5FA1FEC85BEA81FD86F30D03958BE7BA0918.11548D74FBAB2BADED9CC0B0705BADF9844DCE53%26key%3Dck2&amp;iurl=http://video.google.com/ThumbnailServer2?app%3Dblogger%26contentid%3D8b8a9b32c38a0ee4%26offsetms%3D5000%26itag%3Dw160%26sigh%3DwXOXTXVVFaeBK7VxckU46DsNrzg&amp;autoplay=0&amp;ps=blogger" height="266" src="//www.youtube.com/get_player" type="application/x-shockwave-flash" width="320"/></object>

As you can see, there are a lot of space available to show data on the right. The table should use all these space and also use a fixed size font, because sometimes we need to compare the size of the data in number of characters. A reload button is also useful if we want to execute the query again, keeping the last configured columns’ size.

That’s all for now. I reinforce that issues are present in our lives and they will stay for a long time. However, somebody should notice and expose them in order to get  solutions and improvements to be even more productive and happy with Java programming.
