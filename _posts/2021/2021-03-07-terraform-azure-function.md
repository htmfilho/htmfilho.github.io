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

We have provisioned some resources when [Deploying an Azure Function in Go](/2021/01/azure-function-golang-2.html), using [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/). We created a [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group), a [storage account](https://docs.microsoft.com/en-us/azure/storage/), an [application service plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans), and a [function app](https://docs.microsoft.com/en-us/azure/azure-functions/). We can do the same using Terraform. The subfolder `/terraform` in this [repo](https://github.com/htmfilho/blog-examples/tree/main/azure/function) contains the scripts that demonstrate that. Let's start explaining the [`main.tf`](https://github.com/htmfilho/blog-examples/blob/main/azure/function/terraform/main.tf) file:

{% highlight terraform %}
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.26"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "sa" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_app_service_plan" "asp" {
  name                = var.app_service_plan_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  kind                = "Linux"
  reserved            = true

  sku {
    size = "Standard"
    tier = "S1"
  }
}

resource "azurerm_function_app" "function" {
  name                       = var.function_name
  resource_group_name        = azurerm_resource_group.rg.name
  location                   = azurerm_resource_group.rg.location
  app_service_plan_id        = azurerm_app_service_plan.asp.id
  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  https_only                 = true
}
{% endhighlight %}

This is written in the [Terraform Configuration Language](https://www.terraform.io/docs/language/index.html). It is using the [Azure Resource Manager](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) (azurerm), an extension that speaks with Azure's APIs. It creates the 4 resources mentioned above, leaving everything ready to deploy the function. Notice that we have some variables prefixed with "var.". These variables are defined in the file [`variables.tf`](https://github.com/htmfilho/blog-examples/blob/main/azure/function/terraform/variables.tf), as you can see below:

{% highlight terraform %}
//  https://azure.microsoft.com/en-ca/global-infrastructure/geographies/
variable "location" {
  description = "Name of the location where the resources will be provisioned"
  type = string
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type = string
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type = string
}

variable "app_service_plan_name" {
  description = "Name of the application service plan"
  type = string
}

variable "function_name" {
  description = "Name of the function"
  type = string
}
{% endhighlight %}

These variables are what need to change between my environment and yours. So, you can reuse this script as long as you define unique values for these variables. We can do that by assigning values to the variables with a `.tfvars` file. My values are defined in the file [`env.tfvars`](https://github.com/htmfilho/blog-examples/blob/main/azure/function/terraform/env.tfvars).

```
location              = "eastus"
resource_group_name   = "buyersmarket"
storage_account_name  = "buyersmarketstore"
app_service_plan_name = "buyersmarketasp"
function_name         = "buyersmarketfunction"
```

Make sure the files `main.tf`, `variables.tf`, and `env.tfvars` are in a subfolder of your project. To run this code, Terraform needs to be installed and available in the command line. Download it from the [Terraform website](https://www.terraform.io/downloads.html) and follow the instructions for your operating system. In the command line, go to the folder where the scripts are located and initialize it:
    
    $ cd azure/function/terraform
    $ terraform init

The initialization creates several files that keep track of the state of your resources. Terraform uses Azure CLI to authenticate to Azure. So, make sure you are authenticated, as we did when [Deploying an Azure Function in Go](/2021/01/azure-function-golang-2.html):

    $ az login

Once authenticated, we are ready to compare what is defined in our scripts with what we have on Azure. We do it with the `path` argument:

    $ terraform plan -var-file=env.tfvars

This command lists a detailed description of everything that will be created on Azure without creating it. Review it and if everything looks good, apply it:

    $ terraform apply -var-file=env.tfvars

If necessary, all changes can be removed:

  $ terraform destroy
