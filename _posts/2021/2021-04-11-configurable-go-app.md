---
layout: post
title: "Making a Configurable Go App"
date: 2021-04-11 12:00:00 +0200
categories: golang config
---

When we [observed changes in the file system](/2021/03/observer-design-pattern-golang.html) some posts ago -- creating, modifying, and deleting files and directories -- we hard-coded the location where we wanted to observe those changes. If we wanted to observe a different location we would need to change the code and recompile it. The world is simply not that static, so we better provide some flexibility to users. We can do it through flags, configuration files, and environment variables.

<!-- more -->

A configurable application adapts to different contexts, from specific user needs (home, work, etc.) to multiple deployment environments (development, staging, production, etc.). Anything that changes from a context to another or would push you to change the code to enable a new installation is a candidate to a configuration entry. Classical examples are database connections, credentials, file system paths, encryption keys, etc. The importance of configuration has been emphasized as the third factor in [The Twelve-Factor](https://12factor.net/config) methodology, which is used to design software-as-a-service.

## Flags

Flags are the simplest yet the most verbose way of passing values to applications. They are passed only once, at the time of startup, as arguments in the command line.

    $ ./mywebapp --port=8080

They are recommended when the values don't change during the entire execution or when it isn't convenient to have a configuration file, such as in ephemeral environments where resources are recreated at every deployment. In some cases, flags are the best option, like when indicating the location of a configuration file or changing the app behaviour fast. However, it is not recommended to use them for secret values because command lines leave traces in log files and automation tools like [Jenkins](https://www.jenkins.io).

In the following example we see how a flag is implemented in Go:

{% highlight go %}
package main

import {
    "fmt"
    "flag"
}

var (
    // flag name, default value in case the flag is not informed, and documentation
    flgConfigPath = flag.String("cfg", "./config.toml", "Path to configuration file")
)
{% endhighlight %}

The `flag.String` function looks for the flag `--cfg` in the command line. If it doesn't find one then it returns `./config.toml`, which is the default value. Using the [file system observer](/2021/03/observer-design-pattern-golang.html) example: 

    $ ./storage --cfg=../../config.toml

The example shows the use of a configuration file in a different directory. It is possible that some flags are redundant in configuration files and environment variables. When it happens, it is reasonable to assume that the flag takes precedence over the others. It allows temporarily bypassing a config entry for experimentation.

## Configuration Files

Configuration files are the most maintainable way of keeping the configuration. They are text files, in a structured format, with documentation, and validation. They can be versioned, but in a different repository because using the same repository of the application would propagate changes to all environments, and expose secrets (e.g. database password).

Go developers like to use [Viper](https://github.com/spf13/viper) to manage the app's configuration. It supports YAML, JSON, TOML, HCL, and even Java properties files. It also covers flags and environment variables. In the following example, Viper takes the path from the flag `--cfg` to find the config file. It loads the file and makes its entries available to the application.

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

func initConfiguration(conf *viper.Viper, filePath string) (*viper.Viper, error) {
    conf = viper.New()
    conf.SetConfigFile(filePath)

    if err := conf.ReadInConfig(); err != nil {
        if _, ok := err.(viper.ConfigFileNotFoundError); ok {
            return nil, err
        }

        return nil, fmt.Errorf("config file was found but another error ocurred: %v", err)
    }

    return conf, nil
}

func main() {
    configuration, err := initConfiguration(configuration, *flgConfigPath)
    if err != nil {
        fmt.Printf("Error initializing configuration: %v", err)
    }
    
    observedRootPath := configuration.GetString("observer.rootpath")
}
{% endhighlight %}

The content of the `config.toml` looks like this:

    [observer]
    rootpath = "/home/username/liftbox"

So, instead of hard-coding the root path  -- [as we did before](https://github.com/htmfilho/blog-examples/tree/18ab6b7de55a9e11e6068d6e9ef64f878e71efe8/azure/storage) -- we make it configurable. Configuration files tend to grow overtime and it is important to keep them organized. Most of them support grouping, which is the ability of putting together entries that are strongly related. In the examples above, the `[observer]` directive is the grouping syntax of `toml` files.

It is not usual, but Viper also supports dynamic loading of changes in the configuration file while the app is running. It requires just a couple of extra lines:

{% highlight go %}
func initConfiguration(conf *viper.Viper, filePath string) (*viper.Viper, error) {
    ...
    conf.WatchConfig()
    conf.OnConfigChange(func(e fsnotify.Event) {
        fmt.Printf("Config file changed: %v\n", e.Name)
    })
    ...
}
{% endhighlight %}

As you can see, Viper also uses [fsnotify](https://github.com/fsnotify/fsnotify) to observe the config file. 

Files are a good option to keep configurations. However, some environments are so volatile -- like Kubernetes and Docker -- that it is hard to properly manage them. That's where environment variables come into play.

## Environment Variables

Environment variables are a popular alternative to flags and configuration files. They are easy to set, language- and OS-agnostic, and keep the installation pretty clean. In the following example, Viper captures the value of the `LIFTBOX_ROOTPATH` environment variable:

{% highlight go %}
func initConfiguration(conf *viper.Viper, filePath string) (*viper.Viper, error) {
    ...
    _ = conf.BindEnv("observer.rootpath", "LIFTBOX_ROOTPATH")
    ...
}
{% endhighlight %}

The variable is set this way on Linux and Mac:

    $ export LIFTBOX_ROOTPATH=/home/username/liftbox/pictures

Viper checks for the environment variable every time a `viper.Get()` request is made. So, it doesn't require restarting the application. You can check [the changes I made in Liftbox to support configurations](https://github.com/htmfilho/blog-examples/commit/2273c89f3ffad3924ccad4b3dc022f29de33db15).