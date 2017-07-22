---
layout: page
title: Books
permalink: /books/
---

Books are among my greatest passions. I buy more books than I can possibly read.
I read books in a daily basis, but I know I will never catch up because I can't
help buying more and more. Here I share with you my reading experience. Come
back whenever you need a reading recommentation.<br><br>

## What I'm Reading

{% assign reading = site.data.books[0] %}
<div class="row">
  <div class="col-xs-6 col-md-3">
    <a target="_blank"  href="{{ reading.link }}" class="thumbnail"><img border="0" src="{{ reading.image }}" ></a><img src="{{ reading.another_image }}" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
  </div>
  <h3>{{ reading.title }} <small>by {{ reading.author }}</small></h3>
  <p>{{ reading.description }}</p>
</div><br>

## Latest Review

{% assign reviewed = site.data.books[1] %}
<div class="row">
  <div class="col-xs-6 col-md-3">
    <a target="_blank"  href="{{ reviewed.link }}" class="thumbnail"><img border="0" src="{{ reviewed.image }}" ></a><img src="{{ reviewed.another_image }}" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
  </div>
  <h3>{{ reviewed.title }} <small>by {{ reviewed.author }}</small></h3>
  <p>{{ reviewed.description }}</p>
</div><br>

## Bookshelf

My bookshelf is organized chronologically, from the most recently read to the
oldest one. I try to compile here my favority books, the ones I've enjoyed
reading and would certainly recommend to you.

<table class="table">
{% tablerow book in site.data.books limit:12 offset:2 cols:4 %}
  <a target="_blank"  href="{{ book.link }}"><img border="0" src="{{ book.image }}"></a><img src="{{ book.another_image }}" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
{% endtablerow %}
</table>

### Other Books

{% for book in site.data.books offset:14 %}
- <a href="{{ book.link }}">{{ book.title }}</a> by {{ book.author }}
{% endfor %}
