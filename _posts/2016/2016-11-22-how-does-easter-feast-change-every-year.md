---
layout: post
title: "How To Figure Out Easter Sunday Every Year?"
date: 2016-11-22 21:21:52 +0200
categories: development algorithm clojure math tdd
---

Planning a trip in a high touristic season is hard. Everything is expensive and expected to be crowded. But that’s something we can’t avoid because our vacation must coincide with school holidays. So, by now, we are already planning our vacation during Easter break to reach a fair budget in a nice place.

But, like every geek, I’ve got immediately distracted by a mystery I’ve faced right away: when Easter is going to happen next year? This is one of those holidays that changes every year, like carnival, and I wonder who determines it or how it is calculated. Like every serious procrastinator, I immediately dived into this quest. Holidays planning can wait a little bit.

Wikipedia <a href="https://en.wikipedia.org/wiki/Moveable_feast" target="_blank">defines Easter</a> as a <a href="https://en.wikipedia.org/wiki/Easter" target="_blank">moveable feast</a> because it follows lunar cycles instead of <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian</a> or <a href="https://en.wikipedia.org/wiki/Julian_calendar" target="_blank">Julian</a> calendars. I’m not going into historical details, but ancient people have determined that it comes to be the first Sunday after the full moon that occurs after the spring equinox. The equinox is a day when time is split equally into 12 hours each of light and darkness. However, the equinox doesn’t happen in the same date every year. So, they fixed March 21st to simplify calculation all over the globe.

It’s quite simple to calculate by observation. Just go outside and look at the sky for a full moon after March 21st and do the trick. But I need to know sooner than that to be able to plan our holidays. I have to figure out how to calculate it.

The goal of the calculation is simple: find a date in the Gregorian calendar that corresponds to the state of the lunar cycle in a particular date of the Gregorian calendar. But the means to achieve that are not that simple. I guess I have to calculate lunar phases and when they happen in the Gregorian calendar to compare with March 21st, then we find the first Sunday after that.

After some search on the internet, I found it quite challenging. The calculation of lunar phases is complicated and my wife was pressuring me to stop procrastinating and start planning our trip. When I was about to lose my hope, I found a sample of the book “Practical Astronomy with your Calculator or Spreadsheet”, by Peter Duffett-Smith and Jonathan Zwart, that explains in its first chapter a method devised in 1876 which first appeared in Butcher’s Ecclesiastical Calendar, and which is valid for all years from 1583 onwards. The calculation is quite simple but absolutely enigmatic. Take a look at the<br/>
following table considering `year = 2009` as input:

<table class="table">
<colgroup>
<col style="width: 66.6666%;"/>
<col style="width: 16.6666%;"/>
<col style="width: 16.6668%;"/>
</colgroup>
<thead>
<tr>
<th>Step</th>
<th>Integer part</th>
<th>Remainder</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://clojuredocs.org/clojure.core/_fs">(/ x y)</a></td>
<td><a href="https://clojuredocs.org/clojure.core/quot">(quot x y)</a></td>
<td><a href="https://clojuredocs.org/clojure.core/rem">(rem x y)</a></td>
</tr>
<tr>
<td>Divide `year` by `19`</td>
<td></td>
<td>`a = 14`</td>
</tr>
<tr>
<td>Divide `year` by `100`</td>
<td>`b = 20`</td>
<td>`c = 9`</td>
</tr>
<tr>
<td>Divide `b` by `4`</td>
<td>`d = 5`</td>
<td>`e = 0`</td>
</tr>
<tr>
<td>Divide `(b + 8)` by `25`</td>
<td>`f = 1`</td>
<td></td>
</tr>
<tr>
<td>Divide `(b - f + 1)` by `3`</td>
<td>`g = 6`</td>
<td></td>
</tr>
<tr>
<td>Divide `(19a + b - d - g + 15)` by `30`</td>
<td></td>
<td>`h = 20`</td>
</tr>
<tr>
<td>Divide `c` by `4`</td>
<td>`i = 2`</td>
<td>`k = 1`</td>
</tr>
<tr>
<td>Divide `(32 + 2e + 2i - h - k)` by `7`</td>
<td></td>
<td>`l = 1`</td>
</tr>
<tr>
<td>Divide `(a + 11h + 22l)` by `451`</td>
<td>`m = 0`</td>
<td></td>
</tr>
<tr>
<td>Divide `(h + l - 7m + 114)` by `31`</td>
<td>`n = 4`</td>
<td>`p = 11`</td>
</tr>
<tr>
<td colspan="3">The Easter day falls on `day = (p + 1) = 12`, `month = n = 4` and<br/>
`year = 2009`. Therefore 12/4/2009.</td>
</tr>
</tbody>
</table>
What the hell?! How can anyone make any sense of that?! The disturbing thing is that it works and it’s actually explained in the <a href="https://books.google.be/books?id=_sYUAAAAQAAJ&amp;hl=nl&amp;pg=PP39#v=onepage&amp;q&amp;f=false" target="_blank">Book of Common Prayer (1662)</a>. I’m completely overwhelmed by curiosity, but I have to leave it for another time. For now, I will simply explain how I’ve implemented that in Clojure.

First, let’s write some failing unit tests to make sure we have our expectations fulfilled. As the reference explains, the algorithm only works for years equal or greater than 1583, so the first test will assure the code throws an exception otherwise.

{% highlight clojure %}
(ns cosmos.easter-test
  (:require [clojure.test :refer :all]
            [cosmos.easter :as easter]))

(deftest test-minimal-year
  (testing "exception if a year lower than 1583 is informed"
    (is (thrown? IllegalArgumentException
                 (easter/calculate-easter-date 1582)))))
{% endhighlight %}

Another test takes some examples of Easter dates from existing calendars to compare with the results. One of the chosen years must be a <a href="https://en.wikipedia.org/wiki/Leap_year" target="_blank">leap year</a> just to verify that it doesn’t affect the calculation.

{% highlight clojure %}
(deftest test-known-easter-dates
  (testing "compares known easter dates with the output"
    (is (= (easter/calculate-easter-date 2000)
           {:day 23 :month 4 :year 2000}))
    (is (= (easter/calculate-easter-date 2008)
           {:day 23 :month 3 :year 2008}))
    (is (= (easter/calculate-easter-date 2017)
           {:day 16 :month 4 :year 2017}))))
{% endhighlight %}

Now, let’s write the production code, fully based on the table above, to pass those tests.

{% highlight clojure %}
(ns cosmos.easter)

(defn calculate-easter-date [year]
  (if (< year 1583)
    (throw (IllegalArgumentException.
               "Year must be greater than 1582"))
    (let [a (rem  year 19)
          b (quot year 100)
          c (rem  year 100)
          d (quot b 4)
          e (rem  b 4)
          f (quot (+ b 8) 25)
          g (quot (+ b (- f) 1) 3)
          h (rem  (+ (* 19 a) b (- d) (- g) 15) 30)
          i (quot c 4)
          k (rem  c 4)
          l (rem  (+ 32 (* 2 e) (* 2 i) (- h) (- k)) 7)
          m (quot (+ a (* 11 h) (* 22 l)) 451)
          n (quot (+ h l (- (* 7 m)) 114) 31)
          p (rem  (+ h l (- (* 7 m)) 114) 31)]
      {:day (+ p 1) :month n :year year})))
{% endhighlight %}

Isn't it amazing?! I wonder what was the reasoning process of the author to come out with such algorithm. Was is a trial-error approach? Who knows. At least, I've got the Easter date right (24/04/2017) and now I can go back to our holiday planning. Wait a minute... what are we going to do in the carnival?! Huuum...

You can find the source code of this post in my GitHub repository <a href="https://github.com/htmfilho/cosmos" target="_blank">cosmos</a>.
