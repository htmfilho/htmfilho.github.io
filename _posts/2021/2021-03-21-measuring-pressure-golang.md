---
layout: post
title:  "Using a Stateless Strategy Pattern to Deal With Pressure Outside of the Workspace"
date: 2021-03-21 12:00:00 +0200
categories: golang bar psi kpa strategy pattern
---

![Air Compressor Gopher](/images/posts/measuring-pressure-golang.png)

I have one of those things people call "car" that requires me to check its tires' pressure once a month. I'm not really disciplined to check them every month, but at some point I feel guilty after noticing the car bending to the left. It is 1 year old and I might have checked it three times so far, but this time I decided to understand what I was doing. For my surprise, it was not straightforward in 2021.

<!-- more -->

I went to a gas station and was confronted with an air compressor that I've never seen before. It was like a box that accepts payment with coins and cards. Once you make an payment it starts working for a certain period of time, pushing pressured air through a hose that is long enough to reach all tire of the car. I checked the recommended pressure in the driver's door and compared with the pressure chart sticked to the machine. Nice! Units matched, so I paid and got the air running, then took the hose down the tires. There is an adapter at the end that sticks to the tire's valve and also measure the tire's pressure. I'm not sure that thing is reliable though. Its unit was different from the one on the compressor, or maybe PSI divided by 10, not sure. The tire required 35 PSI, the adapter was showing 4.0, and the tire looked a bit low. Args! To put or not to put?

![Units](/images/posts/stateless-strategy-pattern-2.jpg)

![Dashboard](/images/posts/stateless-strategy-pattern-1.jpg)



Every party is guilty here. Me, for not checking it every single month. The gas station, for not providing more unit conversion information on the air compressor. And the car, for showing in the panel a unit different from the ones in the door. My panel has this nice 


{% highlight go %}
package main

import "fmt"

type Converter func(float32) float32

func convert (converter Converter, value float32) float32 {
	return converter(value)
}

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

func main() {
	fmt.Printf("Bar to PSI: %v -> %v \n", 2.9,       convert(BarToPSI, 2.9))
	fmt.Printf("PSI to Bar: %v -> %v \n", 42.060944, convert(PSIToBar, 42.060944))
	fmt.Printf("kPa to PSI: %v -> %v \n", 240,       convert(KPaToPSI, 240))
	fmt.Printf("PSI to kPa: %v -> %v \n", 35,        convert(PSIToKPa, 35))
	fmt.Printf("kPa to Bar: %v -> %v \n", 240,       convert(KPaToBar, 240))
	fmt.Printf("Bar to kPa: %v -> %v ", 2.9,         convert(BarToKPa, 2.9))
}
{% endhighlight %}

Owning a car brought a whole set of concerns to our lives. It is a big, complex, and expensive thing to take care of, but a necessity in North America, where public transport is limited. I know a thing or two about my car though I vastly rely on maintenance services to minimize my concerns. However, tire pressure is something that I have to do myself. I'm a user with an assigned task to be able to use the car. Why don't they standardize it everywhere to a single unit? It doesn't matter that 2.6, 35, and 240 means the same thing. What matters is to get the right pressure into the tire. Period.
