---
layout: post
title:  "Bye WordPress. Nice to meet you, Jekyll!"
date: 2017-07-04 19:32:05 +0200
categories: jekyll wordpress python
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
to migrate to [Jekyll](http://jekyllrb.com), a static website generator written
in Ruby that transforms plain markdown content into modern web content.

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
WordPress website. To start, let's create a Jekyll website on your home folder
and test it using the following commands:

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

If you liked the result, great! You can get rid of Jekyllfly until the next
migration from WordPress to Jekyll. To proceed, go back to the website root
folder and delete Jekyllfly:

    $ cd ..
    $ rm -rf jekyllfly

If not, then let's talk. The code works in my case, but maybe it has some issues
in your case. The best thing to do is to describe your problem in the repo's
[issue tracking](https://github.com/htmfilho/jekyllfly/issues). I would be happy
to make it work for your case.

## Publishing on GitHub

Now, the posts of your website are pure text and there is no database neither
PHP anymore. While you are working on the content everything seems dynamic, but
in reality, Jekyll is constantly generating static content for you. When you
finish a post, either you publish the generated static content to your hosting
provider or you push everything on GitHub. Well known as a Ruby shop, GitHub can
recognize Jekyll and generate the static content for you. This way I can keep
everything (site and content) under version control.

To have a website associated with your GitHub account, create an empty
repository named `[username].github.io`. Go to your local website root folder
and perform the following commands to add the local website to the repository:

```
    $ git init
    $ echo "_site" >> .gitignore
    $ echo ".sass-cache" >> .gitignore
    $ echo ".jekyll-metadata" >> .gitignore
    $ git add .
    $ git commit -m "Initial commit"
    $ git remote add origin "https://github.com/[username]/[username].github.io.git"
    $ git push origin master
```

Check your repository at https://github.com/[username]/[username].github.io to
see if your local files were properly added to the repository. If everything
looks fine then check your new website at https://[username].github.io. If not,
then let me know, so we can figure it out together.

## Side effects

Jekyllfly works but it isn't perfect. It depends a lot on the quality of the
data. Some posts were not imported correctly because the HTML had some
inconsistent tags. Some images were downloaded, properly referenced in the
markdown content, but they were also surrounded by other html tags such as
`<a>`, `<span>` and `table`, that were used to show a legend. Those tags were
hiding the images in the posts. Unfortunately, they are not that easy to remove,
so I did it manually because it impacted just a dozen posts. There are still
some formatting issues in very old posts that I will gradually fix as I find
time to do so. The good new is that I finally have the opportunity
to preserve the quality of the content that I have produced through all these
years.
