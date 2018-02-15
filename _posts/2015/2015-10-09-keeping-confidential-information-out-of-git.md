---
layout: post
title: "Keeping Confidential Information Out Of Git"
date: 2015-10-09 11:04:23 +0200
categories: development clojure configuration management security
---

I’ve launched yet another <a href="https://github.com/htmfilho/usi4biz" target="_blank">open source project on GitHub</a> a couple of months ago and now it’s time to use it in production. For that, I had to put some confidential information in a file that is currently tracked by Git. That was the database connection credentials that I keep in a property file. Obviously, I couldn’t push that file to GitHub and I did’t want to keep that file in my staging area forever, but I still wanted to keep the file in the repository, so people could use it to configure their own development/production databases as well.

The file I’m talking about is <a href="https://github.com/htmfilho/usi4biz/blob/37bc4973c73f18e7a50494b419ab253fd492fa6b/resources/db-config.edn" target="_blank">usi4biz/resources/db-config.edn</a>. Notice that I’ve put pretty dumb credential information there just to make it work in my development environment. This file doesn’t exist anymore in the master branch. I had to do a little tweak, inspired by WordPress, to address the issue.

Before adding any confidential info, I renamed the file to `db-config-example.edn`:

```
$ git mv resources/db-config.edn resources/db-config-example.edn
$ git add resources/db-config-example.edn
$ git commit -m "Renamed the database configuration file"
```

Then, I copied the file and named it after the original name:

```
$ cp resources/db-config-example.edn resources/db-config.edn
```

I edited the new file and added the production credentials. Now, I just have to ask Git to ignore it:

```
$ echo -e "resources/db-config.edn\n" >> .gitignore
```

This way, `db-config.edn` will be always out of my staging area whenever I change it. I just have to remember that if I ever need to add a new property I have to do it in both files. For the moment, I just explained in the <a href="https://github.com/htmfilho/usi4biz/blob/master/README.md" target="_blank">README file</a> that those wiling to use the application have to copy the file `db-config-example.edn` with the name `db-config.edn` because the code refers the file `db-config.edn`.
