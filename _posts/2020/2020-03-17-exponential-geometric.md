---
layout: post
title:  "Exponential and Geometric Distributions: A COVID-19 Example"
date: 2020-03-17 12:00:00 +0200
categories: covid19 statistics
---

![Corona Virus](/images/posts/corona-virus.jpg)

We are going through though times facing the [COVID-19] [pandemic]. National borders are limited, business, schools, and restaurants closed, conferences, public and sport events cancelled. People and governments worldwide are doing everything they can to stop the spread of the SARS-CoV-2 virus. And it is spreading fast, exponentially fast. But how fast is something that is considered exponential?

<!-- more -->

The main mode of transmission of this virus is via respiratory droplets that people exhale when coughing or sneezing. Droplets fall on surfaces and other people touch those surfaces. Their hands become contaminated but their respiratory system is still safe as long as they wash their hands before the next time they touch their faces. The awareness around COVID-19 made me realize how frequently I touch my face. I touch it to think, to relax, to scratch, I can't help it. I also noticed at work and walking on the streets that everybody else does the same, but they may not admit. In other words, if you don't practice social distancing and don't frequently wash your hands you will eventually get sick, and worse, spread the virus out there.

The Wikipedia article states that the average number of people an infected person is likely to infect ranges from 2.13 to 4.82. Let's pick a number within this range: 3. So, if you get contaminated and symptoms start showing, you will likely contaminate 3 other people, probably within your family. Each one of those people will contaminate other 3, extending the disease outside of the house to friends and co-workers. They will contaminate their own families and so on and so on, characterizing an exponential distribution. I'm not kidding. This is real! Look at the following chart, showing the exponential spread in Italy.

![Exponential Increase](/images/posts/exponential-increase.png)

You can recognize an exponential distribution when the next point in the chart is the previous point raised to a certain power, forcing the chart to rapidly increase or decrease.

Once sick, 80% of the population gets recovered after 2 weeks, feeling just mild symptoms. 20% are immune-suppressive to some degree and remain sick in the third week with complications such as pneumonia and liver failure. Unfortunately, 4% don't make it. What we notice here is that recovery is timeboxed. The cases are closed not in the same exponential rate, but in a geometric rate. Look at the green line in the chart that shows the recovery in China.

![Geometric Increase](/images/posts/geometric-increase.png)

Geometric distributions are more general and involve performing operations on numbers such as multiplying or dividing the previous point by a factor to get the next point.

The real world doesn't follow exactly the theory described here. We can see little discrepancies in the data caused by under reporting, errors, and the randomness of nature. But the theory allows us to identify practical patterns and take appropriate measures.

[COVID-19]: https://en.wikipedia.org/wiki/Coronavirus_disease_2019
[pandemic]: https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic
