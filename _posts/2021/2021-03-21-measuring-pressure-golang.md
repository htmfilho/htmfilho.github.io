---
layout: post
title:  "Dealing With Pressure Outside of the Workplace"
date: 2021-03-21 12:00:00 +0200
categories: golang bar psi kpa strategy pattern pressure
---

![Air Compressor Gopher](/images/posts/measuring-pressure-golang.png)

I have one of those things people call "car" that requires me to check its tires' pressure once a month. I'm not really disciplined to check them every month, but at some point I feel guilty after noticing the car bending to the left. It is 1 year old and I might have checked it three times so far, but this time I decided to understand what I was doing. For my surprise, it was not straightforward in 2021.

<!-- more -->

I went to a gas station and was confronted with an air compressor that I've never seen before. It was like a box that accepts payment with coins and cards. Once you make an payment it starts working for a certain period of time, pushing pressured air through a hose that is long enough to reach all tire of the car. I checked the recommended pressure in the driver's door and compared with the pressure chart sticked to the machine. Nice! Units matched, so I paid and got the air running, then took the hose down the tires. There is an adapter at the end that sticks to the tire's valve and also measure the tire's pressure. I'm not sure that thing is reliable though. Its unit was different from the one on the compressor, or maybe PSI divided by 10, not sure. The tire required 35 PSI, the adapter was showing 4.0, and the tire looked a bit low. Args! To put or not to put?

![Units](/images/posts/stateless-strategy-pattern-2.jpg)

Suspecting there was a calibration problem with the adapter's barometer, I decided to put 0.2 more, reaching 4.2. I suspect 4.2 is actually 42 PSI. At least the tires looked better, but I was afraid of over inflating it. So, I checked the manual and I found a way to see the pressure on the panel. It was in Bar, yet another unit.

![Dashboard](/images/posts/stateless-strategy-pattern-1.jpg)

I got 3 pressure units: PSI, Kpa, and Bar. Now I want to know their equivalence to understand how much I'm actually putting into my tires. There are thousands of unit converters online, but of course I have to write my own in [Go](golang.org). I have a feeling that it can be implemented using the strategy pattern, as [we did before](/2021/02/golang-strategy-pattern.html), but this time it would be without state. I have this book called [Functional Programming Patterns](https://pragprog.com/titles/mbfpp/functional-programming-patterns-in-scala-and-clojure/) that gives examples of how to achieve the same benefit of an object-oriented pattern in a functional language. Go is not a functional language, but it supports some functional features like higher-order functions.

[Last time](/2021/02/golang-strategy-pattern.html) we used a `struct` to keep a state while running different algorithms around it. This time we pass an algorithm by parameter, in the form of a function, applying a different one for each call. In the example below, we create a new type `Converter` that represents a function that receives a `float32` and return a `float32`:

{% highlight go %}
package main

import "fmt"

type Converter func(float32) float32
{% endhighlight %}

Then we use the new type in the `convert()` function to invoke any other function that matches the argument and the return types:

{% highlight go %}
func convert (converter Converter, value float32) float32 {
	return converter(value)
}
{% endhighlight %}

The following functions make the pressure conversions and match the type `Converter`, making it possible to pass it as argument to `convert()`.

{% highlight go %}
func BarToPSI(bar float32) float32 {
	return bar * 14.503773773
}

func PSIToBar(PSI float32) float32 {
	return PSI * 0.0689475729
}

func KPaToPSI(kPa float32) float32 {
	return kPa * 0.1450377377
}

func PSIToKPa(PSI float32) float32 {
	return PSI * 6.8947572932
}

func KPaToBar(kPa float32) float32 {
	PSI := KPaToPSI(kPa)
	return PSIToBar(PSI)
}

func BarToKPa(bar float32) float32 {
	PSI := BarToPSI(bar)
	return PSIToKPa(PSI)
}
{% endhighlight %}

We can finally call `convert()`, passing the conversion function we want and the value to convert:

{% highlight go %}
func main() {
	fmt.Printf("Bar to PSI: %v -> %v \n", 2.9,       convert(BarToPSI, 2.9))
	fmt.Printf("PSI to Bar: %v -> %v \n", 42.060944, convert(PSIToBar, 42.060944))
	fmt.Printf("kPa to PSI: %v -> %v \n", 240,       convert(KPaToPSI, 240))
	fmt.Printf("PSI to kPa: %v -> %v \n", 35,        convert(PSIToKPa, 35))
	fmt.Printf("kPa to Bar: %v -> %v \n", 240,       convert(KPaToBar, 240))
	fmt.Printf("Bar to kPa: %v -> %v ", 2.9,         convert(BarToKPa, 2.9))
}
{% endhighlight %}

The code looks pretty expressive and extensible. The function `convert()` can be extended to perform some form of rounding or formatting and new compatible conversions can be added without changing existing logic. Running this code, we get:

```
$ go run convertall.go
Bar to PSI: 2.9 -> 42.060944 
PSI to Bar: 42.060944 -> 2.9 
kPa to PSI: 240 -> 34.80906 
PSI to kPa: 35 -> 241.3165 
kPa to Bar: 240 -> 2.4000003 
Bar to kPa: 2.9 -> 290 % 
```

It shows that the barometer was well calibrated because it is consistent with the other readings. I definitely over inflated my tires.

Owning a car brought a whole set of concerns to our lives. It is a big, complex, and expensive thing to take care of, but a necessity in North America, where public transport is limited. I know a thing or two about my car though I vastly rely on maintenance services to minimize my concerns. However, tire pressure is something that I have to do myself. I'm a user with an assigned task to be able to use the car. Why don't they standardize it everywhere to a single unit? It doesn't matter that 2.6, 35, and 240 means the same thing. What matters is to get the right pressure into the tire. Period.