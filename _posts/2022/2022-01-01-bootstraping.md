---
layout: post
title: "Bootstrapping my Repositories"
date: 2022-01-01 12:00:00 +0200
categories: repository java spring python django golang rust cargo elixir phoenix clojure lenlingen
---

![Snowman](/images/posts/snowman.png)

[RMM Level 2](/2021/12/repositories-portfolio.html#repository-maturity-model-rmm) starts today with the bootstrap of the repositories. Creating the minimal code necessary to run the apps. We're not fulfilling any requirements yet or discussing design decisions, just initializing the projects using the tools in the ecosystem of each programming language, getting pure and simple skeletons. I'm curious to know which technology offers the best experience!

<!-- more -->

Programming languages suffer strong influence from their creators. Some creators are open to other people's ideas - as we can see in Python, Java and Rust - incorporating them on demand. Other creators are more conservative, evolving their languages but limiting other people's influence. These creators are known as opinionated. Users must agree with their opinions to feel comfortable with their programming experience. This is the case of Go, Clojure, and Elixir. The same phenomenon happens with frameworks as well. Developers are pushed in a lower or higher level of compliance to a pre-defined design.

Actually, the more opinionated a language is the easier it is to learn. It also has less issues with backwards compatibility, since it tends to have just enough features. Less opinionated languages like Python, Java, and Rust are popular but they are pretty hard to master due to their abundance of features. Too many features lead to breaking changes, which happened from Python 2 to Python 3 and from Java 8 to Java 11. Rust is still new but some evidences show that [they make syntax changes without breaking compatibility](https://www.reddit.com/r/rust/comments/9hf2qy/the_future_of_rusts_backwards_compatibility/), which means they are increasing the compiler complexity to keep this guarantee.

In the framework space, the opinionated ones are easier to learn but harder to maintain. Entire systems were ruined by frameworks that were discontinued - like [JBoss Seam](https://www.seamframework.org) - or redesigned - like [Apache Struts 1 to Struts 2](https://www.infoq.com/news/migrating-struts2/) - or had backwards incompatibilities - like the [struggle of Github to migrate from Rails 3.2 to 5.2](https://github.blog/2018-09-28-upgrading-github-from-rails-3-2-to-5-2/). Instead of opting for a framework, one could opt to compose libraries. This approach takes longer, is more complex, but the issues are limited to individual libraries, which can be upgraded or even replaced without major issues. A large scale library issue recently happened with [Log4j security vulnerabilities](https://logging.apache.org/log4j/2.x/security.html). Some people opted to upgrading it to newer versions. Others decided to replace it with [Logback](https://logback.qos.ch/). No changes are required in the code if the library is properly integrated, which is the case when the project uses [SLF4j](https://www.slf4j.org), an interface for log libraries. In summary, opinionated languages are easier to master, but opinionated frameworks may be challenging.

We are going to navigate through tools and frameworks in the context of the repositories. We start with [Digger](https://github.com/htmfilho/digger) and [Minimily](https://github.com/htmfilho/minimily), since they were already bootstrapped, but we're revisiting them without pushing any code. Then we bootstrap [Controlato](https://github.com/htmfilho/controlato), [Pycific](/2022/01/never-soon-change.html), [SpitFHIR](https://github.com/htmfilho/spitfhir), [Roma](https://github.com/htmfilho/roma), and [Liftbox](/2022/01/never-soon-change.html), pushing the resulting code.

## Digger

Digger is written in Java, with the help of frameworks like [Spring Boot](https://spring.io) and [Hibernate](https://hibernate.org), and connectivity with [H2](https://www.h2database.com), [PostgreSQL](https://www.postgresql.org/), and [Microsoft SQL Server](https://www.microsoft.com/en-ca/sql-server) databases. We bootstrapped it in August 2019, using [Spring Initializr](https://start.spring.io), which is still in use nowadays. It consists on visiting that website, fill in a form with information about the project, list all dependencies, and generate a zip file with a Spring Boot application ready to run.

![Digger Spring Initializr](/images/posts/spring-initializr.png)

After unzipping the file locally, we can run `mvn spring-boot:run` and visit `http://localhost:8080` to see it serving. Java is not opinionated at all, but Spring is just a little bit. The zip contains all it takes to have dependency injection, convention over configuration, dependencies, but developers have autonomy to make all other design decisions.

## Minimily

Minimily is written in Clojure with the help of libraries, not frameworks. In this case, the language is opinionated but the choices and combination of libraries is totally up to the developer, who is the opinionated one. We bootstrapped Minimily in November 2016, using [Leningen](https://leiningen.org). There are more options out there but Leiningen remains the most popular, just like its old friend [Maven](https://maven.apache.org). Here is a basic example:

    $ lein new minimily

It generates just the minimal necessary to write a library or a little tool. We can follow templates to do more elaborated apps using [Pedestal](https://pedestal.io):

    $ lein new pedestal-service minimily
 
Some templates support wiring dependencies at the command line, like [Luminus](https://luminusweb.com):

    $ lein new luminus minimily +h2 +immutant

Looks like the more options we add to `lein new` the more opinionated the project becomes. But at least we come to decide which opinion we agree with. If we run the latest command and then:

    $ cd minimily
    $ lein run

we get the following page at [http://localhost:3000](http://localhost:3000):

![Luminus Bootstrap App](/images/posts/luminus-bootstrap-page.png)

Luminus generates just enough content to start with, competing here with Phoenix and Django.

## Controlato

Controlato is going to be developed in Elixir, using the [Phoenix Framework](https://www.phoenixframework.org). Both are heavily opinionated, which means they believe they are offering the state of the art in terms of design. Phoenix generates the directory structure and all the files we need for our application using the following command:

    $ mix phx.new controlato
      * creating ...
      
      Fetch and install dependencies [Yn] Y

The output of this command also explains the next steps:

      We are almost there! The following steps are missing:

        $ cd controlato

      Then configure your database in config/dev.exs and run:

        $ mix ecto.create

      Start your Phoenix app with:

        $ mix phx.server

There is a caveat here. The command `mix ecto-create` only works if the password of the user `postgres` is `postgres`. We're simply changing the password to `postgres` to move forward. Here is what we got in the browser after completing the steps:

![Phoenix Bootstrap App](/images/posts/phoenix-bootstrap-page.png)

The Controlato repository now contains hundreds of files in different formats and languages, doing different things. If we agree with them or not, it doesn't matter. We just have a lot of stuff to digest.

## SpitFHIR

SpitFHIR is going to be written in Go, which is the most opinionated language in my portfolio. They hardly accept new language features from the community with the intent to keep is as simple as possible. On the other hand, to do what we want to do, we will need all design knowledge we have accumulated over the years because there is no opinionated framework to generate tons of files for us. Here, we have to carefully pick the libraries and make them work together. All we can do for now is to clone the repository, initialize it as a Go module, and create a main.go file, which will be the entry point of the app.

    $ git clone git@github.com:htmfilho/spitfhir.git
    $ cd spitfhir
    $ go mod init
    $ mkdir -p cmd/spitfhir
    $ touch cmd/spitfhir/main.go

We opened  the `main.go` file and added the following Go code:

    package main

    import "fmt"

    func main() {
        fmt.Println("SpitFHIR")
    }

Then we built it and ran:

    $ go build cmd/spitfhir/main.go
    $ ./main

      SpitFHIR

It will take time until we reach the equivalent of Phoenix, but at least it will contain only what is needed and we will fully understand it.

## Pycific

We will write Pycific in Python and Django. Python is not opinionated, but Django is as much as Phoenix. It makes a lot of decisions for us. The advantage of Django over the competition is a full featured admin application that gives full control over the database to the administrator. It definitely saves a lot of time. Here are the commands we used to bootstrap the repository:

    $ git clone git@github.com:htmfilho/pycific.git
    $ cd pycific
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ python -m pip install Django
    $ pip freeze > requirements.txt
    $ django-admin startproject pycific .
    $ python manage.py runserver

The process was straightforward and more refined than Phoenix. Once completed, we can see the result at [http://127.0.0.1:8000](http://127.0.0.1:8000):

![Django Bootstrap App](/images/posts/django-bootstrap-page.png)

## Roma and Liftbox

Roma and Liftbox are bootstraped the same way because they are both Rust standalone applications. They are simple projects, so, no big bootstrap needs. Cargo do the entire job for us:

    $ git clone git@github.com:htmfilho/roma.git
    $ cd roma
    $ cargo init
    $ cargo run
      
      Hello, world!

At least, `cargo init` generates the first hello world code, something that `go mod init` doesn't.

## Thoughts

On the bright side, Clojure and Leiningen offered the best bootstrap experience. We can range from a very basic library to a complex web app, using the same tooling and just changing the arguments. That's very elegant. Python and Django offered the best framework experience. Rust and Cargo were just fine. On the dark side, Java and Spring depend on a website to do a decent job. Go required some background to write the first code, since it didn't generate any. Elixir and Phoenix were expecting the database to be configured according to their own rules.

I don't like when I don't understand what is behind the scene. At this point, I don't know what Phoenix and Django are doing to serve those pages. It doesn't matter how nice they were trying to save my time, but I still have to understand the whole mechanism, otherwise I won't be able to solve problems, do upgrades, and investigate root causes. I like the fact that Spring doesn't generate too much stuff. I still need to write the controller, the components, the services, the repository, etc, but I feel some level of discomfort about what all those annotations are hiding from me in the code. What I really like - and this is personal - is how Clojure, Go, and Rust let me think about the design without telling me what to do. I understand that I will need a lot of training before I come even close to what Django and Phoenix already put on my plate. But at least I'm forced to do it. What is my motivation to do the same for Django and Phoenix? None. I feel like jumping into the requirements already.
