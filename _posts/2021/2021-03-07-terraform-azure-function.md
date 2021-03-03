---
layout: post
title:  "Provisioning Azure Function Resources Using Terraform"
date: 2021-03-07 12:00:00 +0200
categories: saas cloud automation terraform azure
---

![Facade](/images/posts/2021-02-28-adapter-go-redis.png)

The [Azure Portal](https://portal.azure.com) is an intuitive web app to manage cloud resources. It is so easy to use that sometimes I feel like I have years of Azure experience. As every good web app, it keeps evolving and simplifying our work, but this constant evolution makes the life of bloggers very hard. If I try to give detailed instructions about the steps to create resources here, it will certainly be obsolete in a matter of weeks. Yet, if I don't explain the cloud side of my articles, they end up being incomplete, frustrating my readers. So, how can I possibly solve this problem? Short answer: Infrastructure as Code.

<!-- more -->

Long answer: 