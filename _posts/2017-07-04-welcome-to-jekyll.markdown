---
layout: post
title:  "Bye Wordpress. Nice to meet you, Jekyll!"
date:   2017-07-04 19:32:05 +0200
categories: jekyll wordpress python
---

Website

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
