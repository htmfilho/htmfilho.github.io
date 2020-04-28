---
layout: post
title:  "Dealing With Money"
date: 2020-04-26 12:00:00 +0200
categories: golang rust java python ruby money
---

![Dealing With Money](/images/posts/dealing-with-money.png)

Some time ago I was teaching my kid about money, as an extra activity on top of his home work. He has some savings in a little safe box and we decided to count how much he has accumulated so far. We took the coins out and started counting them, one by one. 10¢, 20¢, ... 80¢, 90¢, 1$. "One?", he asked, "but we are about to count to a hundred, why one now?". I didn't expect that. What I took for granted all this time came as a realization that money is not like the other numbers. It's a sub-class of numbers with special rules.

<!-- more -->

On the spur of the moment, we could tell that's just a matter of scale, but this is not the case. Comparing to the metric system, we can have a table that measures 100cm x 150cm or 1m x 1,5m. In athletics 1500m is a middle-distance, not 1.5km. I'm 1.80m tall, but the measuring tape tells me 180cm. In currency, cents range from 0 to 99¢. Nobody has 230¢ cents in their pockets. They have 2 dollars and 30 cents instead. Any value greater than 99¢ is in dollars, some times followed by fractions in cents. These rules are applicable for the majority of currencies around the world.

In the world of money, arithmetic is not fully useful. Consider this simple scenario: you have 100$ and you want to fairly split it with 3 people. So, you divide 100 by 3 and get 33.3333333... but concretely, money can only represent 33.33. If you multiply 33.33 by 3 you get 99.99, which means you still have 1¢ to give, finding yourself privileging someone. As you can see, money can be split, but it is not a good idea to divide it.

The accumulation of rounding issues may have an important impact over time, specially when using computers, which are capable of processing millions of operations per second. The accumulation of rounding issues can represent millions in gains or loss for the involved parties. Because of that, programmers must be careful when dealing with money in their applications.

Care starts right in the basics. When looking at the characteristics of monetary values, it is tempting to use a primitive type with support for decimal places, such as float and double. They can't accurately be represented by 0s and 1s. For example, 5000000.02 - 5000000.01 is 0.009..., not 0.01; 165 * 1.40 is 230.9999... not 231. I run to my computer and played with these examples in several programming languages (Java, Python, Ruby, and Go), trying to find one with a different behaviour. Curiously, Go behaved like a calculator, working well with float32 without the above problems. However, the usual problems happen with float64.

![Tin Can Telephone](/images/posts/float-rounding-go-other-lang.png)

I was happy with Go float32 until I run an example I found in the book [Code Complete 2nd Ed.][code-complete]: 1.0 == (0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1) is false, but 1.0 == (0.1 * 10) is true! The reason why Go behaved well above is because numbers with decimal places are float32 by default, while in other languages they are float64 or double. By forcing Java to use float32, we get the same result: 165 * 1.40f == 231.

It is extremely common to use computers to work with monetary values, but no modern programming language implements a primitive type to properly support them. Well, the problem with money is that it is not just about arithmetic operations. It is also about currency, conversions, indexes and traceability.

A few rules/thoughts for money:

- 64 bit integers are good, as long as you remember that some currencies have 3 decimal places.
- Remember that some currencies are very different 1 CAD = 16,000 VND (it can be worse, when a country goes hyper inflation)
- We currently have our DB scaled at NUMERIC(19,3) for amounts
- You rarely need performance around amounts - so worrying about float/int/arbitrary-percision is mis placed
- Amounts mean nothing without a currency code attached
- Strings make for good serializations, since you don’t need to worry about the receivers “number” type.

The reference to shopstring/decimal looks good, but have no direct experience.

[code-complete]: https://amzn.to/3eYyu1G
