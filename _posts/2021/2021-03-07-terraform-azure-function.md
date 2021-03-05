---
layout: post
title:  "Provisioning Azure Function Resources Using Terraform"
date: 2021-03-07 12:00:00 +0200
categories: saas cloud automation terraform azure
---

![Facade](/images/posts/2021-02-28-adapter-go-redis.png)

The [Azure Portal](https://portal.azure.com) is an intuitive web app to manage cloud resources. It is so easy to use that sometimes I feel like I have years of Azure experience. As every good web app, it keeps evolving and simplifying our work, but this constant evolution makes the life of bloggers very hard. If I try to give detailed instructions about the steps to create resources there, it will be obsolete in a matter of weeks. Yet, if I don't explain the cloud side of my articles, they end up being incomplete, frustrating my readers. So, how can I possibly solve this problem? Long story short: Infrastructure as Code.

<!-- more -->

Short story long: A way to be precise about cloud infrastructure while keeping articles useful for longer is to use code. This is the thing in technology that takes longer to become obsolete. Good programming languages evolve over time but also preserve backwards compatibility, making sure that old software still compiles in modern technology. When it is time break compatibility, they try to do it gracefully, giving developers time to adapt. 

Using code to build infrastructure is a practice known as "**Infrastructure as Code**". Cloud providers have been serving APIs to create and maintain resources for years now. But some clever people out there have built tools that take care of the hard part and make available domain-specific languages to better describe cloud resources. The most popular tools out there are [Ansible](https://www.ansible.com) and [Terraform](https://www.terraform.io). Ansible is cool, but I'm going to work with Terraform because it is written in [Go](https://golang.org), a language that I'm particularly passionate about.

Let's use Terraform to provision the resources we created when [Deploying an Azure Function in Go](/2021/01/azure-function-golang-2.html). In that post, when we were [publishing to Azure](/2021/01/azure-function-golang-2.html#publishing-to-azure), we ran several Azure CLI commands to create a resource group, a storage account, and a function app. Now, we are going to do the same thing, 

