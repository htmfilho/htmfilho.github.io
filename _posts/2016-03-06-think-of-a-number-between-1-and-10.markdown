---
layout: post
title: "Think of a number between 1 and 10"
date: 2016-03-06 13:26:13 +0200
categories: development clojure
---

You were probably confronted once by a friend, who claimed to be able to read your mind, doing the following trick: Think of a number between 1 and 10; multiply it by 9; sum the digits of the result (e.g. 23 -> 2 + 3 = 5); and subtract 5 from the sum. At this point you may have reached the value 4. How do I know that? Using the same trick of your friend. Let me show you using Clojure. First, we are going to write a function that sums the digits of a number:

```

(defn sum-digits [val]
  (apply + 
         (map #(Integer. (str %)) 
              (str val))))
```

The value is transformed into a string, the <strong>map</strong> function transforms each digit character into a list of integers and the function <strong>apply</strong> sums the list of integers, returning the total to the caller of the function <strong>sum-digits</strong>. We are going to use this function to compose the calculations of the trick:

```

(defn puzzle [x] 
  (- (sum-digits (* x 9)) 5))
```

The function <strong>puzzle</strong> performs the calculations in the sequence that your friend has asked you to do. First, it multiplies the number we thought by 9, then it sums the digits of result and finally subtracts the total by 5. Next, we are going to write another function to unveil the trick:

```

(defn unveil []
  (map #(puzzle %) (range 1 11)))
```

The function <strong>range</strong> produces a sequence of numbers starting from 1 to 10 where 11 is not included (1 2 3 4 5 6 7 8 9 10). The function <strong>map</strong> applies the function <strong>puzzle</strong> to each number in the list and produces another list with the results. Now, execute the function <strong>unveil</strong> to see the result:

```
(unveil)

(4 4 4 4 4 4 4 4 4 4)
```

Oh, look! For the range of 1 to 10, the result will always be 4. In other words, a pattern. Patterns are very present in multiplications and when you remove all of them you have prime numbers, as pointed by Mark Haddon in his book “<a href="http://www.amazon.com/gp/product/1400032717/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1400032717&amp;linkCode=as2&amp;tag=c03ce-20&amp;linkId=BMYAXUCPTCMGFNX4">The Curious Incident of the Dog in the Night-Time</a>![ir?t=c03ce-20&l=as2&o=1&a=1400032717](/images/posts/ir?t=c03ce-20&l=as2&o=1&a=1400032717)“. Daniel Tammet exemplify some patterns in his book “<a href="http://www.amazon.com/gp/product/1444737449/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1444737449&amp;linkCode=as2&amp;tag=hildesblog-20&amp;linkId=SZFYR4EJX4SUUWR7">Thinking in Numbers: How Maths Illuminates Our Lives</a>![ir?t=hildesblog-20&l=as2&o=1&a=1444737449](/images/posts/ir?t=hildesblog-20&l=as2&o=1&a=1444737449)“. When we multiply any even number by 5 we always get numbers ending in zero (e.g. 12 x 5 = 60) and when we do it with odd numbers we always get numbers ending in 5. In the case of 9, every time we multiple 9 by a number between 1 and 10 and we sum its digits we always get 9.

In the sequence, subtracting 5 from 9 will just distract your attention from the multiplication pattern and even improve the trick. For instance: imagine that each letter of the alphabet has a corresponding number (A – 1, B – 2, C – 3, …). Now, take the result (4) and get its respective letter; think of a country that starts with this letter; take the fourth letter of this country and think of an animal that starts with this letter. There is a high probability that your final answer will be “Denmark” and “monkey”. Before you think I’m reading your mind, let me explain what just happened.

First, there is not many countries that starts with “D”, the fourth letter of the alphabet. Among Denmark, Djibouti, Dominica, and Dominican Republic, you will easily remember Denmark. The fourth letter of Denmark is “M” and no animal that starts with “M” is more famous than the monkey, which comes immediately into your mind.

I’m having fun programming in Clojure, not just because Clojure is fun to learn and teach, but because programming is not always about serious things. Being able to program just enough code to make things happen stimulates thinking, problem solving and creativity over structure, patterns, conventions and styles. Coding is supposed to be relaxing not stressful. Enjoy it!
