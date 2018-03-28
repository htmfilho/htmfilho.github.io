---
layout: post
title:  "Software Documentation as Code"
date: 2018-02-22 12:00:00 +0200
categories: git python markdown asciidoc documentation osis
---

I was 10 years old when I first touched a computer. A micro-computer, as we used to say. It was a PC Intel 386, installed at the travel agency where my sister used to work. She operated it to write texts and spreadsheets, nothing more. It was just a modern typewriter. At that time, there was no internet but computers were not that boring because it was new, different from everything I used to play. When she was not using it I was there, fascinated with a text processor called Word Perfect, from Corel. In my opinion as a curious kid, it was better than Microsoft Word. My favorite task was typing touristic brochures into Word Perfect documents, just for the sake of typing. No games, no calculations, just text. I saved my files in a flop disk my sister gave me, put it into my backpack and headed home with my parents. Then I was back the next day to continue typing during the hype of the addiction.

At that time, most of personal and small business computing use was for writing with the primary intention to print the document and do some off-line work with it. Nowadays, the enormous amount of content published on the internet shows that printing is not a priority anymore. Most of documents are less complex than before, with less formatting and variations to make them more accessible for a larger audience. The basic text formatting of HTML, far simpler than Microsoft Word, has shown to be effective to scale reading.

HTML-based content has been widely accepted and new technologies have been created, such as Markdown, Asciidoc, [reStructuredText], and others, to rival with traditional office suites. These technologies are based on plain text with a minimalist syntax, easy to memorize. Their plain text model has been proven viable with the success of LaTex in the scientific world for decades. This kind of format is largely used for technical writing these days.

Markdown is the simplest and most popular format. I use it to write this blog and the experience has been better than my previous Wordpress version. Now, my texts are cleaner, well formatted and standardized after days migrating the messy content managed by Wordpress to the elegant and efficient [Jekyll]. On the other hand, the simplicity of Markdown is also its biggest weakness.

Asciidoctor installation:

In my previous post, I explained [how to install Ruby in your machine for development purpose][ruby-installation].

    $ gem install asciidoctor
    $ gem install asciidoctor-pdf --pre

Use of Asciidoctor:

    $ asciidoctor asciidoc-file.adoc
    $ asciidoctor-pdf asciidoc-file.adoc
    $ asciidoctor-pdf -a pdf-stylesdir=resources/themes -a pdf-styles=osis asciidoctor.adoc

[Jekyll]: http://www.hildeberto.com/2018/03/installing-using-jekyll-linux.html
[reStructuredText]: http://docutils.sourceforge.net/rst.html
[ruby-installation]: http://www.hildeberto.com/2018/03/installing-using-jekyll-linux.html#installing-ruby-with-rbenv
