# Hildeberto.com

The content of my [blog](https://www.hildeberto.com). To run it locally, use:

    $ bundle exec jekyll serve --future

The command above breaks every time I upgrade Ubuntu. To fix that, I ran the following commands:

    $ gem uninstall bundler
    $ gem install bundler jekyll
    $ bundle add webrick
    $ bundle install