---
layout: post
title: "Suggestions to Improve Texmaker"
date: 2010-11-04 15:41:00 +0200
categories: latex research user interface
---

[Texmaker](http://www.xm1math.net/texmaker/) is a Latex editor used to write well structured documents. [Latex](http://www.latex-project.org/) is a text processing language not so trivial, but once mastering it the writer gets very good results on the overall quality of his/her documents.

![texmaker-300x173.png](/images/posts/texmaker-300x173.png)

I have been using Texmaker for a while, but only recently I could experience most of its features. I spent a long time using it to write my thesis and I figured out some possible improvements that would make this tool more usable. The evaluated version was the 2.0 one, but the latest version is currently the 2.1 one. Maybe some of my suggestions are already available. I didn’t have time to check yet. Anyway, the improvements are:

1. Restoring the previous session is really an interesting feature. I personally think that it is better than creating a project, as other tools do, because it preserves the simplicity of Texmaker. However, besides saving last opened files and the master document in the application session, I would suggest to **save all bookmarks** as well. It is useful because when we are working in a large document it is difficult to find exactly the point where we have stopped working last time and bookmarks were the first thing I thought that might be solving this problem.

2. It think it is quite easy to detect which document is the master. It is basically about to find documentclass at the beginning of the document. So, if Texmaker would be able to **set the master document automatically instead of forcing us to do so**, it would be a great usability improvement. I understand that there is the case when more than one candidate for master is opened. In this case, I would suggest the following rules to decide which document is the master one before compiling the document:

  - _only one file is open and this file can be a master_: define it automatically as a master.
  - _many files are open, but only one of them can be a master and others are just inclusions (include{})_: define as a master the only one that can be a master.
  - _many files are open and there are more than one candidate for master_: select one of the candidates for master and compile it to define it as the master. If another candidate is selected and the compilation is invoked, then the current selection will become the new master. If the selected file is not a master and the compilation is invoked, then the last selected master is considered.

3. The spell check works fine, but It would be nice to **add new words to the dictionary in order to avoid red underlines** in words that we are tired to know they are right. I can imagine how hard it could be to avoid verifying Latex keywords and parameters, so I got used to spell checks’ highlights there, but in my text it’s a bit annoying.

4. Texmaker is doing a great job presenting the structure of the tex file. Clicking on any item brings the corresponding point in the text to the user, helping a lot on the navigation of long texts. The problem is: why doesn’t it do the same for “bib” files? bib files are as much structured as any other latex file, so Texmaker would **implement the visualization of bib files on the structure view**, simplifying the navigation through this file, which is usually long.

Hey! Wait a minute! Texmaker is open source. Why don’t I just make all these contributions to the project? For the moment I can’t. I wish I could, but to invest time in C++ might not be so strategic for my carrier right now. I’ve tried to find some Latex tool implemented in Java, but I found just some immature projects unfinished. Anyway, I’m quite confident that an usability evaluation can be also considered as a contribution to a open source project, don’t you think so? 😉

<ol></ol>
