---
layout: post
title: "Fluffy Encryption of Numbers Within URLs"
date: 2016-03-19 17:44:46 +0200
categories: development algorithm clojure math security
---

In the REST web services world, a resource is anything that’s important enough to be referenced as a thing in itself. It is something that can be stored on a computer and represented as a stream of bits such as a document, a row in a database, or the result of running an algorithm. The book <a href="http://www.amazon.com/gp/product/B00F5BS966/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=B00F5BS966&amp;linkCode=as2&amp;tag=c03ce-20&amp;linkId=QGNNPO3PYOG4DEFO">RESTful Web APIs</a>![ir?t=c03ce-20&l=as2&o=1&a=B00F5BS966](/images/posts/ir?t=c03ce-20&l=as2&o=1&a=B00F5BS966) explains very well that every resource has to have at least one URI, which is the name and address of that resource. The URL to a resource in a typical web application looks like `{database-table-name}/{record-id}`. For example: `/blogs/myblog/entries/134` goes from the general to the specific, from a list of blogs to a particular blog, to the entries in that blog, to a particular entry.

I don’t know about you, but when I look at those URLs and see those record ids I feel very uncomfortable. I’m not sure if it has security implications, but it’s strange to let everybody know that they are dealing with the product number 14 or the order number 35. Maybe I’m being paranoid, but it is worth sharing a trick to replace those ids by fake ones.

The method is simple. We will need two secret numbers that should be configurable for each installation of an application. The secret numbers compose a formula to encrypt a number, as illustrated in <a href="http://clojure.org" target="_blank">Clojure</a>:

```

(def secret-n1 345)
(def secret-n2 3)

(defn encrypt [id] 
  (bit-xor (* id secret-n1) 
           secret-n2))

(encrypt 35)
>> 12072
```

The id is multiplied by the first secret number (secret-n1) and the result is used to perform a <a href="https://en.wikipedia.org/wiki/Bitwise_operation#XOR" target="_blank">binary XOR</a> (bitwise exclusive or) with the second secret number (secret-n2). The result is a number that gives no clue about the id it is hiding. Here is an example of applying the function `encrypt`:

```

; Original URL
(def id 35)
(def url-entries "http://mywebsite.com/myblog/entries/%d")
(def url-entry (format url-entries id))
(format "Original URL: %s" url-entry)
>> Original URL: http://mywebsite.com/myblog/entries/35

; Modified URL
(def url-entry (format url-entries (encrypt id)))
(format "Modified URL: %s" url-entry)
>> Modified URL: http://mywebsite.com/myblog/entries/12072
```

Notice that 35 is not exposed anymore. In its place we have 12072, which is not a real id or it’s not related to the current record. But how can we recover the original id after processing the request with 12072? Now comes the decrypt function to recover the original id:

```

(defn decrypt [request-id] 
  (/ (bit-xor request-id secret-n2) 
     secret-n1))

(decrypt 12072)
>> 35
```

The secret numbers are used here as well but inverting the calculation. This time, we perform the binary XOR first, with the id that comes in the request and the second secret number (secret-n2), and we divide (instead of multiply) the result by the first secret number (secret-n1).

These ids are maybe meaningless to concern us so much, but what about a global user id or a social security number or even a phone number? This method can protect them all. 

The only downside I have identified for this technique is that in the event of compromising the security of the secret numbers, all URLs will change when at least one secret number changes. It means that these URLs are not permanent, thus useless to bookmark them. This is not a serious concern, but you should think about the implications before adopting it.
