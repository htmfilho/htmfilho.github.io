---
layout: post
title:  "Bye Wordpress. Nice to meet you, Jekyll!"
date: 2017-07-04 19:32:05 +0200
categories: jekyll wordpress python
---

This blog used to be a Wordpress website. That's the second large migration over
the period of 10 years. It was initially hosted at Blogger, but its features to
write about programming were very limited at that time. I couldn't actually use
a custom plugin, css or JavaScript file. Then I moved everything to Wordpress,
managed by myself in a private hosting service. There, I've got more flexibility
in terms of content, but it was significantly slower than Blogger. The
combination PHP + MySQL is known as low cost, but I was actually moving from
free to $200/y, which is too expensive for a slow website. After years annoyed
with performance, I've decided to migrate to Jekyll, a static website generator
that transform plain markdown content into modern web content.

While the migration from Blogger to Wordpress was quite straightforward, the
migration to Jekyll was definitely a challenge. You are looking at my 3rd and
last attempt to do it. I've succeed because I've decided to have fun, writing it
myself in Python. This post explains how I've done it using Jekyll, Python and
GitHub without having any access to the Wordpress database, neither using any
exported data or accessing the server file system. I did it by simply using a
web crawling technique.

## What you have to know

I consider that you know what Jekyll is, how to install it and you have a
Wordpress blog publicly available on the web. You don't need to have access
to Wordpress' database or any exported files, but you do need a way to navigate
chronologically through posts using links like "Previous" or "Next". You also
need some knowledge of Git and a GitHub account to be able to version your code
and reuse existing code. At last, but not least, you should be able prepare a
Python runtime environment and run Python scripts with it.

Python is an extremely useful programming language. The combination of a
readable and expressive syntax with a rich collection of libraries make it one
of the most powerful languages available. It can also be severely criticized but
I have been working with it since 2015, achieving amazing results so far.

## Getting everything set up

To start, let's create a Jekyll site on your home folder and test it using the
following commands:

    $ jekyll new website
    $ cd website
    $ jekyll serve

A minimalist version of a Jekyll website is generated and made available at the
local address http://locahost:4000. In case you have something else using the
port 4000, you can add the config below to the `_config.yml` file to change the
default port:

    port: 4001

During the migration process, all your posts will be copied to the folder
`_posts/` and all the images to the folder `images/posts`. If those folders
don't exist they will be created automatically. If you want something different
from these then you can customize them in the Jekyllfly config file later on.

The next step is to clone the GitHub repository that actually does the job. Run
the following command in the same folder of the website you just created:

    $ git clone https://github.com/htmfilho/jekyllfly.git

It creates the subfolder `jekyllfly/` that contains the Python scripts that does
the migration job.

## The code

The code is organized in three modules (In Python a file is actually called a
module):

1. `wordpress.py`: implementation of a simple web crawler that navigates through
   the posts of a Wordpress blog from the most recent to the oldest one. It is
   possible because at the end of every post there is a link to the previous
   one.
2. `jekyll.py`: transforms the data extracted from wordpress.py in a format
   understandable by Jekyll and save them in locations of a Jekyll project to
   have them published.
3. `migration.py`: launch the whole migration process.
4. `config.py`: configuration file, where we define the url of the source blog.

The execution starts at the `migration.py` module, which simply loads the config
and calls the module `wordpress.py`.

{% highlight python %}
import wordpress
import config

wordpress.import_articles(config.wordpress_url)
{% endhighlight %}

The function `import_articles` in the module `wordpress` iterates recursively
through the posts in descendent chronological order. While doing this, it
extracts the content of each post, analyze the extracted content, creates an
object with the extracted content and saves them in Jekyll's folders.

{% highlight python %}
def import_article(current_post_url, recursive=False):
    content_html = get_content_html(current_post_url)

    if content_html:
        save_article(build_article(current_post_url, content_html))
        if recursive:
            previous_post_url = get_previous_post_url(content_html)
            if previous_post_url:
                import_article(previous_post_url, recursive)


def import_articles(post_url):
    import_article(post_url, True)
{% endhighlight %}



Before running the script, we have to configure it properly. Open the
`config.py` module and inform the permanent url of the most recent post
published on the Wordpress blog. At the time of this migration, I have
configured the parameter `wordpress_url` like that:

    wordpress_url = "http://www.hildeberto.com/2017/02/cleaner-code-with-functional-programming.html"
