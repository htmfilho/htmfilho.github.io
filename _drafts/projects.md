---
layout: page
title: Projects
permalink: /projects/
---

Books are among my greatest passions. I buy more books than I can possibly read.
I read books in a daily basis, but I know I will never catch up because I can't
help buying more and more. Here I share with you my reading experience. Come
back whenever you need a reading recommendation.

## [What I'm Working On](#what-iam-working-on)

{% assign working = site.data.projects[0] %}
<a href="{{ working.link }}"><img border="0" src="/images/pages/{{ working.image }}" ></a>
<h3>{{ working.title }} <small>using {{ working.tags }}</small></h3>
<p>{{ working.description }}</p>

## [Portfolio](#portfolio)

{% for project in site.data.projects %}
- <a href="{{ project.link }}">{{ project.title }}</a> using {{ project.tags }}
{% endfor %}
