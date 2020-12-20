---
layout: post
title: "Preparing Ubuntu to Write Latex Documents"
date: 2010-11-22 14:54:00 +0200
categories: latex operating system research
---

That’s a self-reference post that might be useful for you too. I just installed Ubuntu in a new laptop and I was surprised by how easy is to install a Latex editor and the packages needed to compile and render documents. As a Texmaker user, I’m going to explain the installation using this editor.

On Ubuntu 10.04 or higher, go to Applications – Ubuntu Software Center. Type “Texmaker” in the search field on the top right. Texmaker will appear in the list, then you can click on “Info” to get more information about it, as shown in the figure below.

![Texmaker](/images/posts/texmaker.png)

Press “Install” and have Texmaker and its dependencies installed on your Ubuntu system. [TeX Live](http://www.tug.org/texlive/) is the Latex system installed. Notice that you don’t have to do anything to install TeX Live, it will just come together with Texmaker. The installation process will take some time because TeX Live is a big package and you will probably need a good internet connection.

Unfortunately, just a basic version of TeX Live is installed and you will probably have problems trying to write some little advanced texts. To handle that, I suggest the installation of additional texlive packages, which are:

- texlive-bibtex-extra
- texlive-fonts-extra
- texlive-fonts-recommended
- texlive-science

Go to System – Administration – Synaptic Package Manager. Use the search box to find the packages above and check them for installation. That’s all you have to do to start writing high quality documents.
