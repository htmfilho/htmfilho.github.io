---
layout: post
title:  "Installing and Using Jekyll on Linux"
date: 2018-03-16 12:00:00 +0200
categories: jekyll blog linux ruby rbenv
---

![Recursion](/images/posts/installing-using-jekyll-linux.jpg)

This website looks like a dynamic web application accessing content stored in a database and relying on a PHP runtime, but it is not. As [described previously here][welcome-to-jekyll], this website is made of static resources, versioned in a Git repository, and published in a simple server without database or runtime available. I actually write the content in [Markdown], then [Jekyll][jekyll] transforms it into HTML content and generate the website for me, taking care of the entire presentation and navigation.

<!-- more -->

So far, I never took the time to explain how I installed and used Jekyll, but now it is the time because, after migrating from Ubuntu to Linux Mint, I had to reinstall Jekyll to continue writing my blog. I'm documenting here the steps I've taken.

## Installing Ruby with rbenv

Jekyll is a [Ruby] application. Most of Linux distributions come with Ruby installed. So, you are a few commands away from using Jekyll. Just jump to the [next section](#installing-jekyll) and do it. But, I personally don't like to use the version that comes with the distribution because it is too outdated. I prefer to use a more recent version and for that I use [rbenv], the Ruby environment tool, which is essential for every Ruby developer.

To begin, let's install some basic dependencies and clone `rbenv` locally:

    $ sudo apt-get install -y libssl-dev libreadline-dev zlib1g-dev
    $ git clone https://github.com/rbenv/rbenv.git ~/.rbenv

The Ruby environment lives in the hidden folder `.rbenv` that you just created at the user's home folder. The next step is to modify the variable `PATH`, adding the path to rbenv's binary folder. You can do it in the file `~/.bashrc`, but I don't like to modify it, so I do it in the file `~/.bash_aliases`:

    $ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_aliases
    $ echo 'eval "$(rbenv init -)"' >> ~/.bash_aliases

If you want to use your `~/.bashrc` file instead, simply replace all occurrences of `.bash_aliases` by `.bashrc`.

The next step is to install `ruby-build`, a rbenv plugin that makes it easy to install any version of Ruby from source:

    $ git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
    $ echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bash_aliases

To activate these configurations, run:

    $ source ~/.bashrc         # or ~/.zshrc if you have Zsh installed.

Then install Ruby:

    $ rbenv install 2.3.6
    $ rbenv global 2.3.6

At the time of this post, I installed version 2.3.6, but you can install a more recent one. Find latest versions at [Ruby's website][ruby-download].

To check if Ruby was properly installed, restart the terminal, then type:

    $ ruby -v
      ruby 2.3.6p384 (2017-12-14 revision 61254) [x86_64-linux]

## Installing and Using Jekyll

You can start from here if you already have Ruby installed. Install **Jekyll** and **Bundler** using [RubyGems][ruby-gems]:

    $ gem install jekyll bundler

Then create your first website using Jekyll:

    $ jekyll new my-new-website
    $ cd my-new-website
    $ bundle exec jekyll serve

Browse to http://localhost:4000 and see what you just created. If you already have a Jekyll website, go to its folder and build it:

    $ cd ~/writing/hildeberto-com
    $ bundle install
    $ bundle exec jekyll serve

Leave it serving the website locally and go edit the content. Every time you save a file, Jekyll builds a new version of the website with the latest changes and make it available in the local address. All you have to do is to hit refresh on the browser to see the result.

[jekyll]: https://jekyllrb.com
[Markdown]: https://daringfireball.net/projects/markdown/
[welcome-to-jekyll]: /2017/07/welcome-to-jekyll.html
[rbenv]: https://github.com/rbenv/rbenv
[Ruby]: https://www.ruby-lang.org/en/
[ruby-download]: https://www.ruby-lang.org/en/downloads/
[ruby-gems]: https://rubygems.org/
