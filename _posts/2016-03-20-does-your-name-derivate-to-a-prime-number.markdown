---
layout: post
title: "Does Your Name Sums Up To A Prime Number?"
date: 2016-03-20 08:19:12 +0200
categories: development algorithm book clojure math
---

I just finished a wonderful book! <a href="http://www.amazon.com/gp/product/0099470438/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0099470438&amp;linkCode=as2&amp;tag=hildesblog-20&amp;linkId=ULJTKJYZNMOZOIE4">The Curious Incident Of The Dog In The Night-time</a>![ir?t=hildesblog-20&l=as2&o=1&a=0099470438](/images/posts/ir?t=hildesblog-20&l=as2&o=1&a=0099470438) is a masterpiece, written by Mark Haddon, a famous English children’s book writer who decided to write this book for adults.

<a href="http://www.amazon.com/gp/product/0099470438/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0099470438&amp;linkCode=as2&amp;tag=hildesblog-20&amp;linkId=RGTR3EMGPQEUGJWD">![q?_encoding=UTF8&ASIN=0099470438&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=hildesblog-20](/images/posts/q?_encoding=UTF8&ASIN=0099470438&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=hildesblog-20)</a>![ir?t=hildesblog-20&l=as2&o=1&a=0099470438](/images/posts/ir?t=hildesblog-20&l=as2&o=1&a=0099470438)

A curious thing is that chapters are numbered after prime numbers, rather than conventional successive numbers. The last chapter is 233, which is the 51° prime number. In the chapter 19, he describes a simple algorithm to figure out prime numbers. In his words:

> “… you write down all the positive whole numbers in the world. Then you take away all the numbers that are multiples of 2. Then you take away all the numbers that are multiples of 3. Then you take away all the numbers that are multiples of 4 and 5 and 6 and 7 and so on. The numbers that are left are prime numbers”


In one of his insights, he used to get someone’s name, give each letter a value from 1 to 26 and sum the values of each letter of the name to check whether the total is a prime number. So, I thought it would be fun to explore this unique way of seeing things using <a href="http://clojure.org" target="_blank">Clojure</a>. First, we create a map of letters and numbers, where the letters are keys in a map and numbers are their respective values:

```

(def numbered-alphabet {\a 1  \b 2  \c 3  \d 4  \e 5  \f 6 
                        \g 7  \h 8  \i 9  \j 10 \k 11 \l 12
                        \m 13 \n 14 \o 15 \p 16 \q 17 \r 18
                        \s 19 \t 20 \u 21 \v 22 \w 23 \x 24
                        \y 25 \z 26 \space 0})
```

The keys are literal characters and the numbers are positive integers. Using the map, we sum the characters of a name:

```

(defn sum-characters [name]
  ; lower-casing the name to keep the map small
  (let [name (clojure.string/lower-case name)]
    ; given a sequence of characters, reduce it to the sum
    ; of the respective numbers.
    (reduce #(+ (if (char? %1) 
                    (get numbered-alphabet %1) 
                    %1)
                (get numbered-alphabet %2)) 
            (seq name))))

(sum-characters "hildeberto")
>> 98
```

Is 98 a prime number? No, because it’s even and even numbers have at least 3 divisors: 1, 2 and itself. The algorithm that applies this one and other rules is the following:

```

(defn is-prime [x]
  (if (or (= x 2) (= x 3))
    true
    ; eliminate even numbers
    (if (even? x)
      false
      ; Number is odd, so it deserves some more attention.
      ; After eliminating even numbers, the maximum divisor
      ; of a number is less than its square root
      (let [max-div (Math/ceil (Math/sqrt x))]
        (loop [i 3]
	  (if (zero? (rem x i))
              false
	      (if (> i max-div)
                  ; it is a prime number
                  true
                  (recur (inc i)))))))))

(is-prime (sum-characters "Hildeberto"))
>> false
```

That’s a pity my own name doesn’t sum up to a prime number, but the book gave some names to test the code:

```

(is-prime (sum-characters "Jesus Christ"))
>> true
(is-prime (sum-characters "Scooby Doo"))
>> true
(is-prime (sum-characters "Sherlock Holmes"))
>> true
(is-prime (sum-characters "Doctor Watson"))
>> true

```

Wait a minute… he uses first and last names! So, let me test with mine:

```

(is-prime (sum-characters "Hildeberto Mendonca"))
>> true

```

<strong>Yeeeeeesssss! I’m prime-numered!!!</strong>
