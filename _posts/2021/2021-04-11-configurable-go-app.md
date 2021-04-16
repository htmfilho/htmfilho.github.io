---
layout: post
title: "Making a Configurable Go App"
date: 2021-04-11 12:00:00 +0200
categories: golang config
---

When we [observed changes in the file system](/2021/03/observer-design-pattern-golang.html) -- creating, modifying, and deleting files and directories -- we hard-coded the location where we wanted to observe changes. If we wanted to observe a different location we would need to change the code and recompile it. The world is simply not that static, so we better provide some flexibility to users. We can do it through flags, configuration files, and environment variables.

<!-- more -->

A configurable application adapts to different contexts, from specific user needs (home, work, etc.) to multiple deployment environments (development, staging, production, etc.). Anything that changes from a context to another or would push you to change the code to enable a new installation is a candidate to a configuration entry. Classical examples are database connections, credentials, file system paths, encryption keys, etc. The importance of configuration has been emphasized as the third factor in [The Twelve-Factor](https://12factor.net/config) methodology, which is used to design software-as-a-service.

## Flags

Flags are the simplest yet the most verbose way of passing values to applications. They are passed only once, at the time of startup, as arguments in the command line.

    $ ./mywebapp --port=8080

They are recommended when the values don't change during the entire execution or when it isn't convenient to have a configuration file, such as in ephemeral environments where resources are recreated at every deployment. In some cases, flags are the best option, like when indicating the location of a configuration file. However, it is not recommended to use them for secret values because command lines leave traces in log files and automation tools like [Jenkins](https://www.jenkins.io).

In the following example we see how a flag is implemented in Go:

{% highlight go %}
package main

import {
    "fmt"
    "flag"
}

var (
    // flag name, default value in case the flag is not used and documentation
    flgConfigPath = flag.String("cfg", "./config.toml", "Path to configuration file")
)
{% endhighlight %}

The `flag.String` function looks for a flag `cfg` in the command line. If it doesn't find one then it returns `./config.toml`, which is default value. Using the [file system observer](/2021/03/observer-design-pattern-golang.html) example: 

    $ ./liftbox --cfg=../../config.toml

The example shows the use of a configuration file in a different directory. It is possible that some flags are redundant in configuration files and environment variables. When it happens, it is reasonable to assume that the flag takes precedence over the others. It allows temporarily bypassing a config entry for experimentation.

## Configuration Files

Configuration files are the most maintainable way of keeping the configuration. They are text files, in a structured format, with documentation, and validation. They can be versioned, but in a different repository because using the same repository of the application would propagate changes to all environments, and expose secrets (e.g. database password).

Go developers like to use [Viper](https://github.com/spf13/viper) to manage the app's configuration. It supports YAML, JSON, TOML, HCL, and even Java properties files. It also covers flags and environment variables. In the following example, Viper takes the path from the flag to find the config file. It loads the file and makes its entries available to the application.

{% highlight go %}
package main

import {
    "fmt"
    "flag"
    "github.com/spf13/viper"
}

var configuration *viper.Viper

var (
    // flag name, default value in case the flag is not used and documentation
    flgConfigPath = flag.String("cfg", "./config.toml", "Path to configuration file")
)

func main() {
    configuration = viper.New()
    configuration.SetConfigFile(flgConfigPath)

    observedRootPath := configuration.GetString("observer.rootpath")
}
{% endhighlight %}

The content of the `config.toml` looks like this:

    [observer]
    rootpath = "/home/username/liftbox"

So, instead of hard coding the root path as we did before, we make it configurable. Even better, if the entry changes during the app execution it is dynamically loaded like this:

{% highlight go %}
...
configuration.SetConfigFile(flgConfigPath)

configuration.WatchConfig()
configuration.OnConfigChange(func(e fsnotify.Event) {
    log.Printf("config file changed: %v", e.Name)
})
{% endhighlight %}

## Environment Variables

Environment variables are a popular alternative to flags and config files. They are a language- and OS-agnostic standard and keep the installation pretty clean. However, if not well documented, they can be missed and never used.