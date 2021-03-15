---
layout: post
title:  "Reacting to File Changes Using the Observer Design Pattern in Go"
date: 2021-03-14 12:00:00 +0200
categories: golang design pattern observer
---

![Gopher Observer](/images/posts/observer-design-pattern.png)

Science has shown that shy people are clever because they spend more time listening and observing and less time speaking and showing off. They absorb more information and spend countless hours reasoning them. They do it quietly and are rarely recognized by their intellects. What science has not shown is that the Observer Design Pattern is also a humble part of a crafted designed software but rarely recognized as well.

<!-- more -->

You know you are in front of a observer implementation when an event happens and one or multiple routines react to that. The source of the event is normally called **publisher** and the code that reacts to that is called **subscriber**. You can actually have a propagation of events where subscribers also act as publishers, triggering other subscribers in a chain reaction. These two concepts are also popular in messaging systems, which is a way to implement the observer pattern in a distributed and decoupled fashion.

To illustrate the observer pattern in Go, we are going to watch for changes in a local folder. Every time a folder or a file is created, modified, or removed, an event is published and propagated to subscribers. To watch the local file system we rely on [fsnotify](https://github.com/fsnotify/fsnotify). When something happens, we get events from fsnotify and propage the event to our subscribers. The full implementation is available in my [Github repo](https://github.com/htmfilho/blog-examples/tree/18ab6b7de55a9e11e6068d6e9ef64f878e71efe8/azure/storage). Let's review it, starting with two interfaces:

{% highlight go %}
type Publisher interface {
  register(subscriber *Subscriber)
  unregister(subscriber *Subscriber)
  notify(path, event string)
  observe()
}

type Subscriber interface {
  receive(path, event string)
}
{% endhighlight %}

The `Publisher` interface requires the implementer to `register()` and `unregister()` subscribers, and `notify()` subscribers about events. The `observe()` behaviour is specific for this case because the publisher is also a subscriber of **fsnotify** events. To be honest, the Publisher interface is not really necessary but, as we saw in the article about the [adapter design pattern](http://localhost:4001/2021/02/adapter-design-pattern-golang.html), it helps to encapsulate the fsnotify library.

The `Subscriber` interface is simpler, pushing the implementation of a `receive()` method that gets the message from the publisher. Let's first look at the Publisher implementation: the `PathWatcher` struct.

{% highlight go %}
// PathWatcher observes changes in the file system and works as a Publisher for
// the application by notifying subscribers, which will perform other operations.
type PathWatcher struct {
  subscribers []*Subscriber
  watcher     fsnotify.Watcher
  rootPath    string
}

// register subscribers to the publisher
func (pw *PathWatcher) register(subscriber *Subscriber) {
  pw.subscribers = append(pw.subscribers, subscriber)
}

// unregister subscribers from the publisher
func (pw *PathWatcher) unregister(subscriber *Subscriber) {
  length := len(pw.subscribers)

  for i, sub := range pw.subscribers {
    if sub == subscriber {
      pw.subscribers[i] = pw.subscribers[length-1]
      pw.subscribers = pw.subscribers[:length-1]
      break
    }
  }
}

// notify subscribers that a event has happened, passing the path and the type
// of event as message.
func (pw *PathWatcher) notify(path, event string) {
  for _, sub := range pw.subscribers {
    (*sub).receive(path, event)
  }
}

// observe changes to the file system using the fsnotify library
func (pw *PathWatcher) observe() {
  watcher, err := fsnotify.NewWatcher()
  if err != nil {
    fmt.Println("Error", err)
  }
  defer watcher.Close()

  if err := filepath.Walk(pw.rootPath, 
                          func(path string, info os.FileInfo, err error) error {
    if info.Mode().IsDir() {
      return watcher.Add(path)
    }

    return nil
  }); err != nil {
    fmt.Println("ERROR", err)
  }

  done := make(chan bool)

  go func() {
    for {
      select {
        case event := <-watcher.Events:
          pw.notify(event.Name, event.Op.String())
        case err := <-watcher.Errors:
          fmt.Println("Error", err)
      }
    }
  }()

  <-done
}
{% endhighlight %}

The `observe()` method get a watcher from the `fsnotify` library and, with the help of `filepath.Walk()`, watches the target path and all its sub-folders. Then, a goroutine starts an infinite loop, waiting for events from the file system. When they happen, the `notify()` method is called with information about the event.

We have two subscribers for this publisher: the `PathIndexer`, which would keep a database of references to the files, and the `PathFileMD5`, which would calculate the checksum of the files for consistence checks.

{% highlight go %}
type PathIndexer struct {}

func (pi *PathIndexer) receive(path, event string) {
  fmt.Printf("Indexing: %v, %v\n", path, event)
}

type PathFileMD5 struct {}

func (pfm *PathFileMD5) receive(path, event string) {
  fmt.Printf("Syncing: %v, %v\n", path, event)
}
{% endhighlight %}

These subscribers are not fully implemented because the goal is to show the observer pattern, but we will eventually implement them to push files to an [Azure Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview). For the moment, let's see how the publisher and the subscribers are put together in the `main()` function.

{% highlight go %}
func main() {
  var pathWatcher Publisher = &PathWatcher{
    rootPath: "/home/username/liftbox",
  }

  var pathIndexer Subscriber = &PathIndexer{}
  pathWatcher.register(&pathIndexer)

  var pathFileMD5 Subscriber = &PathFileMD5{}
  pathWatcher.register(&pathFileMD5)

  pathWatcher.observe()
}
{% endhighlight %}

The publisher is created with the attribute `rootPath` set with the absolute path to the folder we want to watch. Then we create the subscribers and add them to the publisher. Finally, we call `pathWatcher.observer()` to start observing the file system for changes.

As usual, you can find the full implementation in my [Github repo](https://github.com/htmfilho/blog-examples/tree/18ab6b7de55a9e11e6068d6e9ef64f878e71efe8/azure/storage). When you find some time, run the application with:

    $ cd azure/storage
    $ go run .

and in another console, run these commands:

In a console, run some basic operations:

    $ cd /home/[username]/liftbox
    $ mkdir pictures
    $ echo "Blog Post" > post.txt
    $ rm post.txt

Liftbox produces the following output:

    Indexing: /home/htmfilho/liftbox/pictures, CREATE
    Checksuming: /home/htmfilho/liftbox/pictures, CREATE
    Indexing: /home/htmfilho/liftbox/post.txt, CREATE
    Checksuming: /home/htmfilho/liftbox/post.txt, CREATE
    Indexing: /home/htmfilho/liftbox/post.txt, WRITE
    Checksuming: /home/htmfilho/liftbox/post.txt, WRITE
    Indexing: /home/htmfilho/liftbox/post.txt, REMOVE
    Checksuming: /home/htmfilho/liftbox/post.txt, REMOVE

This experience of revisiting the design patterns in Go has been an amazing experience so far. The challenge is to come up with ideas to describe them through realistic use cases. I take this challenge with pleasure because it is really cool to see useful cases materialized in Go.