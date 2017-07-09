---
layout: post
title: "Installing Leiningen on Mac OS"
date: 2015-07-17 21:07:09 +0200
categories: development clojure jvm
---

<a href="http://www.hildeberto.com/wp-content/uploads/2015/07/leiningen-full.jpg">![leiningen-full-186x300.jpg](/images/posts/leiningen-full-186x300.jpg)</a>

I’ve been playing with <a href="http://clojure.org" target="_blank">Clojure</a> for quite sometime now. It’s a functional language hosted on the JVM, with a growing community and a very rich ecosystem. You can find libraries for every major problem, but in case you cannot find, you can count on the interoperability with Java will bridge the gap.

Nowadays, every programming language and platform offer a development environment with a build tool as foundation. Take as example <a href="https://maven.apache.org" target="_blank">Maven</a>, <a href="https://gradle.org" target="_blank">Gradle</a> and <a href="http://www.scala-sbt.org" target="_blank">Sbt</a>. It isn’t different in the Clojure world. It uses <a href="http://leiningen.org" target="_blank">Leiningen</a> as a build and project management tool. So, I would like to share with you how I’ve managed to install and configure Leiningen on my Mac.

First, create the directory `/Applications/clojure` to store Clojure’s related tools:

```
$ sudo mkdir /Applications/clojure
```

Navigate to the new directory, download the Leiningen script and give to the downloaded file permission to execute:

```
$ cd /Applications/clojure
$ sudo curl -O https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
$ sudo chmod +x lein
```

Add the new directory to the `$PATH` to be able to execute it everywhere in your system. To do that, navigate to the directory `/etc/paths.d` and create a file named `clojure.lein` with the content `/Applications/clojure`:

```
$ cd /etc/paths.d/
$ sudo echo "/Applications/clojure" >> clojure.lein
```

If the output of the command above is “permission denied” then you don’t have enough privileges to add something to `/etc/paths.d/`. In this case, you can add lein exclusively to your user profile.

```
$ cd ~
$ echo “export PATH=$PATH:/Applications/clojure” >> .bash_profile
```

Close the current terminal and open a new one to activate the changes. Execute the following command to check whether the $PATH variable was correctly modified to include Leiningen’s path:

```
echo $PATH
```

You should be able to find the path `/Applications/clojure` concatenated within the value.

Finally, execute the command `lein` for the first time to install Leiningen:

```
$ lein
```

It will download the latest version of Leiningen and make you ready to program in Clojure. Start the Clojure REPL with the following command:

```
$ lein repl
```

Have fun with Clojure and Leiningen!
