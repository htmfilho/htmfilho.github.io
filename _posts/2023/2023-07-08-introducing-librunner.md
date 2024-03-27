---
layout: post
title: "Introducing LibRunner"
date: 2023-07-08 12:00:00 +0200
categories: library rust opensource
---

A good deal of being a geek is to code or understand coding. We love objectivity and hate subjectivity, so coding is the ultimate objectivity sophistication. If something can be expressed in numbers and logic, then code is the best way to materialize and document it. That's why we created a programming library where we can express all the calculations related to running and let other geeks use and contribute to it.

<!-- more -->

[LibRunner](https://docs.rs/librunner/0.4.0/librunner/) is an open-source library published on [GitHub](https://github.com/geekrunners/librunner) and distributed by [creates.io](https://crates.io/crates/librunner). We decided to write it in [Rust](https://www.rust-lang.org) for the following reasons:

* **Performance**: Rust is fast, compared to C, and often replaces C/C++ in production code due to its memory safety guarantees. The domain of sports often requires real-time features, so Rust allows calculations to be as fast as they can be, without the overhead of garbage collection.

* **Popular**: Rust has been elected by an [annual Stack Overflow survey](https://insights.stackoverflow.com/survey/) as [the most loved language for 7 consecutive years](https://www.reddit.com/r/rust/comments/vi7pre/rust_tops_stackoverflow_survey_2022_as_the_most/). It has a large and strong community of users and contributors as well as a great number of sponsors, from small start-ups to global players, investing in the language and its ecosystem. It implements the state-of-the-art on developer experience, making developers happy about the process of building high-performance software.

* **Reusable**: Publishing LibRunner on [creates.io](https://crates.io) is so straightforward that we did it as soon as its first feature was available. Today, any Rust project can add it as a dependency and use it for running-related applications. In the browser space, LibRunner can be used by [WebAssembly](https://www.rust-lang.org/what/wasm) applications. In addition to that, LibRunner can also be used by other programming languages through bridges. We intend to support other languages in the future in a on demand basis, ensuring the same underline logic across platforms and technologies.

* **High Level**, yet native, writing Rust code feels like writing in a high-level language such as Kotlin, Scala, and C#. Yet, the result is native, platform-specific, and self-contained software.

LibRunner can help you calculate the average speed and pace to complete a distance within a duration, calculate the distance of a race from duration and pace, calculate the duration and distance of the race from a set of splits, calculate the pace of positive and negative splits of a race and so many other features that we are constantly adding to it as we learn more about the field. We are also open to [suggestions, demands, and contributions](https://github.com/geekrunners/librunner/issues/).

In the [LibRunner documentation](https://docs.rs/librunner/0.4.0/librunner/), we have examples of code for every feature. These examples are guaranteed to work because the testing tool runs them against the current version. You can copy and paste them into your code and make the necessary changes to the problem you are solving.

Let's go through these quick steps to get started with LibRunner. We start a Rust project from zero to unlock the way to hero:

1. visit https://rustup.rs and install rustup, an installer for the programming language Rust. Once installed, update and check the toolchain:

       $ rustup update
       $ rustc --version
       $ cargo --version

2. create your new running application:

       $ cargo new runningapp

3. a folder called `runningapp` is created. Go into it and run the project:

       $ cd runningapp
       $ cargo run

4. it prints "Hello World", meaning you have a working code to start from. Open the project in your favourite code editor and make two changes: 

   4.1. add LibRunner to the project's dependencies:
   
       $ cargo add librunner

     It adds a new dependency to your `Cargo.toml` file:

      ```toml
      [dependencies]
      librunner = "0.6.0"
      ```

   4.2. replace the content of the file `src/main.rs` with the code below:

      ```rust
      use std::time::Duration;
      use librunner::running::{Race, MetricRace, ImperialRace, Running, MetricRunning, ImperialRunning};
      use librunner::utils::converter;
      use librunner::utils::formatter;

      fn main() {
          let duration = converter::to_duration(4, 0, 0); // 04:00:00
          let m_marathon: MetricRace = Race::new(42195);
          let m_running: MetricRunning = Running::new(duration);

          println!("The pace to run {}km in {}h is approximately {}/km at {:.2}km/h", 
              converter::to_km(m_marathon.distance),
              formatter::format_duration(m_running.duration()), 
              formatter::format_duration(m_running.average_pace(&m_marathon)),
              converter::to_km_h(m_running.speed(&m_marathon)));

          let i_marathon: ImperialRace = Race::new(46112);
          let i_running: ImperialRunning = Running::new(duration);

          println!("The pace to run {} miles in {}h is approximately {}/mile at {:.2}mph", 
              converter::to_mile(i_marathon.distance), 
              formatter::format_duration(i_running.duration()),
              formatter::format_duration(i_running.average_pace(&i_marathon)),
              converter::to_mph(i_running.speed(&i_marathon)));
      }
      ```
5. then run the project again:

       $ cargo run

    which generates the following output:

       The pace to run 42.195km in 04:00:00h is approximately 05:41/km at 10.55km/h
       The pace to run 26.2 miles in 04:00:00h is approximately 09:09/mile at 6.55mph

That's it! You are now using LibRunner in no time. Keep an eye on this website to learn more about future updates and all things geeks love about running.