---
layout: post
title:  "Showing the latest version number based on git tags"
date: 2017-07-12 19:32:05 +0200
categories: git python django
---

I haven't seen it, or I simply don't know good keywords to find on Google what
I'm about to explain to you. Yeah, I would love to see the most recent version
number in the footer of my app, but I'm too lazy to update it manually. I
actually did it in the past, but I forgot all the time to update it berore the
release, which would require a patch to fix that, something quite noisy in my
busy day.

So, I recently thought: what if I figure out how to pick it straight from git
tags, which we use to bookmark releases since the beginning? In order to do
that, the app 

{% highlight python %}
from git import Repo


def get_latest_tag(repo):
  tags = repo.tags
  head_commit = repo.head.commit
  latest_tag = None

  for tag in tags:
    if tag.commit == head_commit:
      latest_tag = tag

  return latest_tag


get_latest_tag(Repo('.'))
{% endhighlight %}
