---
layout: post
title: "Preparing Ubuntu to Write Latex Documents"
date: 2010-11-22 14:54:00 +0200
categories: latex operating system research
---

That’s a self-reference post that might be useful for you too. I just installed Ubuntu in a new laptop and I was surprised by how easy is to install a Latex editor and the packages needed to compile and render documents. As a Texmaker user, I’m going to explain the installation using this editor.

On Ubuntu 10.04 or higher, go to Applications – Ubuntu Software Center. Type “Texmaker” in the search field on the top right. Texmaker will appear in the list, then you can click on “Info” to get more information about it, as shown in the figure below.

![Screenshot-Ubuntu-Software-Center-300x186.png](/images/posts/Screenshot-Ubuntu-Software-Center-300x186.png)

Press “Install” and have Texmaker and its dependencies installed on your Ubuntu system. <a href="http://www.tug.org/texlive/">TeX Live</a> is the Latex system installed. Notice that you don’t have to do anything to install TeX Live, it will just come together with Texmaker. The installation process will take some time because TeX Live is a big package and you will probably need a good internet connection.

<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=c03ce-20&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=0137081308&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="align: left; height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe>Unfortunately, just a basic version of TeX Live is installed and you will probably have problems trying to write some little advanced texts. To handle that, I suggest the installation of additional texlive packages, which are:

<ul>
<li>texlive-bibtex-extra</li>
<li>texlive-fonts-extra</li>
<li>texlive-fonts-recommended</li>
<li>texlive-math-extra</li>
<li>texlive-science</li>
</ul>
Go to System – Administration – Synaptic Package Manager. Use the search box to find the packages above and check them for installation. That’s all you have to do to start writing high quality documents.
