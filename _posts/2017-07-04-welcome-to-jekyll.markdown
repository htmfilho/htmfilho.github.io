---
layout: post
title:  "Bye Wordpress. Nice to meet you, Jekyll!"
date: 2017-07-04 19:32:05 +0200
categories: jekyll wordpress python
---

This is the second large migration of my blog to another technology. It was
initially hosted at Blogger, but its features to write about programming were
very limited at that time. I couldn't actually use a custom plugin, css or
JavaScript file. Then I moved everything to Wordpress, managed by myself in a
private hosting service. There, I've got more flexibility in terms of content,
but it was significantly slower than Blogger. The combination PHP + MySQL is
known as low cost, but I was actually moving from free to $200/y, which is too
expensive for a slow website. After years annoyed with performance, I've decided
to migrate to Jekyll, a static website generator that transform plain markdown
content into modern web content.

While the migration from Blogger to Wordpress was quite straightforward, the
migration to Jekyll is definitely a challenge. You are looking at my 3rd and
last attempt to do it. I've succeed because I've decided to have fun, writing it
myself in Python. This post explains how I've done it using Jekyll, Python and
GitHub without having any access to the Wordpress database, using any exported
data or accessing the server file system, by simply using a web crawling
technique.

## Getting started

The code I'm about to explain is available under the Apache License on a GitHub
repository. It is organized in three files:

1. `wordpress.py`: implementation of a simple web crawler that navigates through
   the posts of a Wordpress blog from the most recent to the oldest one. It is
   possible because at the end of every post there is a link to the previous
   one.
2. `jekyll.py`: transforms the data extracted from wordpress.py in a format
   understandable by Jekyll and save them in locations of a Jekyll project to
   have them published.
3. `importer.py`: launch the whole migration process.

{% highlight python %}
def get_articles(current_post, articles=None):
    print(current_post)
    if articles is None:
        articles = []

    html_content = get_html_content(current_post)

    if html_content:
        articles.append(build_article(html_content))
        link_previus = get_previous_post(html_content)
        if link_previus:
            return get_articles(link_previus, articles)

    return articles
{% endhighlight %}
