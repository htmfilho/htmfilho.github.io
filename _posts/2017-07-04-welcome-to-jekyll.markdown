---
layout: post
title:  "Bye WordPress. Nice to meet you, Jekyll!"
date: 2017-07-04 19:32:05 +0200
categories: jekyll WordPress python
---

This blog used to be a [WordPress](https://wordpress.com) website. That's the
second large migration over the period of 10 years. It was initially hosted at
[Blogger](https://www.blogger.com), but its features to write about programming
were very limited at that time. I couldn't actually use a custom plugin, css or
JavaScript file. Then I moved everything to WordPress, managed by myself in a
private hosting service. There, I've got more flexibility in terms of content,
but it was significantly slower than Blogger. The combination PHP + MySQL is
known as low cost, but I was actually moving from free to $200/y, which is too
expensive for a slow website. After years annoyed with performance, I've decided
to migrate to [Jekyll](http://jekyllrb.com), a static website generator that
transform plain markdown content into modern web content.

While the migration from Blogger to WordPress was quite straightforward, the
migration to Jekyll was definitely a challenge. You are looking at my 3rd and
last attempt to do it. I've succeed because I've decided to have fun, writing it
myself in [Python](https://www.python.org). This post explains how I've done it
using Jekyll, Python and [GitHub](https://www.github.com) without having any
access to the WordPress database, neither using any exported data or accessing
the server file system. I did it by simply using a web crawling technique.

## What you have to know

I consider that you know what Jekyll is, how to install it and you have a
WordPress blog publicly available on the web. You don't need to have access
to WordPress' database or any exported files, but you do need a way to navigate
chronologically through posts using links like "Previous" or "Next". You also
need some knowledge of Git and a GitHub account to be able to version your code
and reuse existing code. At last, but not least, you should be able prepare a
Python runtime environment and run Python scripts with it.

Python is an extremely useful programming language. The combination of a
readable and expressive syntax with a rich collection of libraries make it one
of the most powerful languages available. It can also be severely criticized but
I have been working with it since 2015, achieving amazing results so far.

## Getting everything set up

Here, we put together a website based on Jekyll with the help of
[Jekyllfly](https://github.com/htmfilho/jekyllfly). The second one is a Python
script that populates a Jekyll website with content extracted from a published
WordPress website. To start, let's create a Jekyll site on your home folder and
test it using the following commands:

    $ jekyll new website
    $ cd website
    $ jekyll serve

A minimalist version of a Jekyll website is generated and made available at the
local address http://locahost:4000. In case you have something else using the
port 4000, you can add the config below to the `_config.yml` file to change the
default port:

    port: 4001

The next step is to clone the GitHub repository that actually does the job. Run
the following command in the same folder of the website you just created:

    $ git clone https://github.com/htmfilho/jekyllfly.git

It creates the subfolder `jekyllfly/` that contains the Python scripts we
explains in details later. Before running it, create a configuration file based
on the available example:

    $ cd jekyllfly
    $ cp config-example.py config.py

The module `config.py` is the one that will be taken into consideration. Open it
and add a link to the most recent post of your blog. At the time of this writing
my `config.py` was configured like that:

```
wordpress_url = "http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html"
posts_path = "_posts"
images_path = "images/posts"
```

During the migration process, all your posts are copied to the folder `_posts/`
and all the images to the folder `images/posts`. If those folders don't exist
they will be created automatically. If you want something different from these
then you can customize them in the Jekyllfly config file later on.

Let's get the Python part done. As stated before, I assume you have Python
3 installed and know how to use `pip` to install dependencies. Now, go to the
Jekyllfly directory and install the dependencies:

    $ cd jekyllfly
    $ pip install -r requirements.txt

## Run it!

You're all set. Let's run it:

    $ python3 migration.py

The time it takes to finish depends on the number of posts and images published
and the speed of your internet connection. In my case, it took 4 minutes to
download 156 posts and 182 images. The script shows the path to every resource
it is downloading to give you and idea of progress. When it finished, go to
[http://localhost:4000](http://localhost:4000) to check the result.
