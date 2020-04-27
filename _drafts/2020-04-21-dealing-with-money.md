---
layout: post
title:  "Dealing With Money"
date: 2020-04-26 12:00:00 +0200
categories: golang rust java python ruby money
---

![Dealing With Money](/images/posts/dealing-with-money.png)

Some time ago I was teaching my kid about money, as an extra activity on top of his home work. He has some savings in a little safe box and we decided to count how much he has accumulated so far. We took the coins out and started counting them, one by one. 10¢, 20¢, ... 80¢, 90¢, 1$. "One?", he asked, "but we are about to count to a hundred, why one now?". I didn't expect that. What I took for granted all this time came as a realization that money is not like the other numbers. It's a sub-class of numbers with special rules.

<!-- more -->

On the spur of the moment, we could tell that's just a matter of scale, but this is not the case. Comparing to the metric system, we can have a table that measures 100cm x 150cm or 1m x 1,5m. In athletics 1500m is a middle-distance, not 1.5km. I'm 1.80m tall, but the measuring tape tells me 150cm. In currency, cents range from 0 to 99¢. Nobody has 230¢ cents in their pockets. They have 2 dollars and 30 cents instead. Any value greater than 99¢ is in dollars, some times followed by fractions in cents. These rules are applicable for the majority of currencies around the world.

The the world of money, arithmetic doesn't make

It turns out sum, subtraction, and multiplication can be handled by float32 base 1, but the division is a whole new world. Not even integers can handle this alone. Money can only be split, not divided I think it would be a good idea to include a requirement in the challenge to split some amount to see how the candidate would handle the case: by dividing or splitting.

![Tin Can Telephone](/images/posts/float-rounding-go-other-lang.png)

A few rules/thoughts for money:
never use float/double or any variation of floating point - (Don’t ask how many times I see 321.31000000001 come back in an API)
64 bit integers are good, as long as you remember that some currencies have 3 decimal places.
Remember that some currencies are very different 1 CAD = 16,000 VND (it can be worse, when a country goes hyper inflation)
We currently have our DB scaled at NUMERIC(19,3) for amounts
You rarely need performance around amounts - so worrying about float/int/arbitrary-percision is mis placed
Amounts mean nothing without a currency code attached
Strings make for good serializations, since you don’t need to worry about the receivers “number” type.
The reference to shopstring/decimal looks good, but have no direct experience.
