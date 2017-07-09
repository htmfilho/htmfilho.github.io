---
layout: post
title: "Suggestions to Improve Texmaker"
date: 2010-11-04 15:41:00 +0200
categories: uncategorized latex research user interface
---

<a href="http://www.xm1math.net/texmaker/">Texmaker</a> is a Latex editor used to write well structured documents. <a href="http://www.latex-project.org/">Latex</a> is a text processing language not so trivial, but once mastering it the writer gets very good results on the overall quality of his/her documents.

<div style="clear: both; text-align: center;"><a href="http://69.89.31.239/~hildeber/wp-content/uploads/2010/11/texmaker.png" style="margin-left: 1em; margin-right: 1em;">![texmaker-300x173.png](/images/posts/texmaker-300x173.png)</a></div>
I have been using Texmaker for a while, but only recently I could experience most of its features. I spent a long time using it to write my thesis and I figured out some possible improvements that would make this tool more usable. The evaluated version was the 2.0 one, but the latest version is currently the 2.1 one. Maybe some of my suggestions are already available. I didn’t have time to check yet. Anyway, the improvements are:

<ol>
<li>Restoring the previous session is really an interesting feature. I personally think that it is better than creating a project, as other tools do, because it preserves the simplicity of Texmaker. However, besides saving last opened files and the master document in the application session, I would suggest to <b>save all bookmarks</b> as well. It is useful because when we are working in a large document it is difficult to find exactly the point where we have stopped working last time and bookmarks were the first thing I thought that might be solving this problem.</li>
<li>It think it is quite easy to detect which document is the master. It is basically about to find documentclass at the beginning of the document. So, if Texmaker would be able to <b>set the master document automatically instead of forcing us to do so</b>, it would be a great usability improvement. I understand that there is the case when more than one candidate for master is opened. In this case, I would suggest the following rules to decide which document is the master one before compiling the document:
<ul>
<li><i>only one file is open and this file can be a master</i>: define it automatically as a master.</li>
<li><i>many files are open, but only one of them can be a master and others are just inclusions (include{})</i>: define as a master the only one that can be a master.</li>
<li><i>many files are open and there are more than one candidate for master</i>: select one of the candidates for master and compile it to define it as the master. If another candidate is selected and the compilation is invoked, then the current selection will become the new master. If the selected file is not a master and the compilation is invoked, then the last selected master is considered.</li>
</ul>
</li>
<li>The spell check works fine, but It would be nice to <b>add new words to the dictionary in order to avoid red underlines</b> in words that we are tired to know they are right. I can imagine how hard it could be to avoid verifying Latex keywords and parameters, so I got used to spell checks’ highlights there, but in my text it’s a bit annoying.</li>
<li>Texmaker is doing a great job presenting the structure of the tex file. Clicking on any item brings the corresponding point in the text to the user, helping a lot on the navigation of long texts. The problem is: why doesn’t it do the same for “bib” files? bib files are as much structured as any other latex file, so Texmaker would <b>implement the visualization of bib files on the structure view</b>, simplifying the navigation through this file, which is usually long.</li>
</ol>
<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=c03ce-20&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=0321173856&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe>Hey! Wait a minute! Texmaker is open source. Why don’t I just make all these contributions to the project? For the moment I can’t. I wish I could, but to invest time in C++ might not be so strategic for my carrier right now. I’ve tried to find some Latex tool implemented in Java, but I found just some immature projects unfinished. Anyway, I’m quite confident that an usability evaluation can be also considered as a contribution to a open source project, don’t you think so? 😉

<ol></ol>