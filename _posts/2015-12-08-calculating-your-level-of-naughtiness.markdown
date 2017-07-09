---
layout: post
title: "Calculating Your Level of Naughtiness"
date: 2015-12-08 23:04:54 +0200
categories: development clojure culture music
---

To motivate his students, a computer science teacher of the <a href="http://www.quixada.ufc.br/" target="_blank">Federal University of Ceará</a> has challenged his class to develop an algorithm to calculate how naughty you are based on your birth date. The challenge is very silly, but it became a <a href="http://g1.globo.com/ceara/noticia/2015/12/professor-cita-wesley-safadao-em-questao-de-logica-e-vira-hit-na-web.html" target="_blank">Brazilian hit</a>.

The teacher said his original intention was to teach students to call functions from other functions, which is as much silly as the goal of the challenge, but no doubt that the idea is pretty effective on motivating young students.

<a href="http://www.hildeberto.com/wp-content/uploads/2015/12/safadao_questao_materia.jpg">![safadao_questao_materia.jpg](/images/posts/safadao_questao_materia.jpg)</a>

The problem consists on writing a function that calculates the percentage of naughtiness and the remaining level of innocence of a person based on his/er birth date. The formula to calculate the level of naughtiness is:

`naughtiness = incremental_sum(month) + (year / 100) * (50 - day)`

where `incremental_sum` is a function that, given a number, calculates de sum of all numbers from 1 to the informed number included. The solution below is written in <a href="http://clojure.org" target="_blank">Clojure</a>:

```

(defn inc-sum [num]
  (reduce + (range (inc num))))

(defn naughtness [day month year]
  (let [naughty (+ (* (- 50 day) (/ year 100.0)) (inc-sum month)) 
        angel (-  100 naughty)] 
    {:naughty naughty 
     :angel angel}))

(naughtness 10 9 78)
=> {:naughty 76.2, :angel 23.8}

```

The formula has absolutely no sense and doesn’t have any scientific foundation, but the result of the function is great fun to play with friends! Maybe the subject can push you to learn Clojure, doesn’t it?! 😉
