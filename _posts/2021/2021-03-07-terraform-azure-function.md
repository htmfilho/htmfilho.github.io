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

Let's use Terraform to provision the resources we created when [Deploying an Azure Function in Go](/2021/01/azure-function-golang-2.html). In that post, when we were [publishing to Azure](/2021/01/azure-function-golang-2.html#publishing-to-azure), we ran several Azure CLI commands to create a [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#what-is-a-resource-group), a [storage account](https://docs.microsoft.com/en-us/azure/storage/), an [application service plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans), and a [function app](https://docs.microsoft.com/en-us/azure/azure-functions/). Now, here is how it look like in Terraform:

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
  name     = "buyersmarket"
  location = "eastus"
}

resource "azurerm_storage_account" "sa" {
  name                     = "buyersmarketstore"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_app_service_plan" "asp" {
  name                = "buyersmarketasp"
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
  name                       = "buyersmarketfunction"
  resource_group_name        = azurerm_resource_group.rg.name
  location                   = azurerm_resource_group.rg.location
  app_service_plan_id        = azurerm_app_service_plan.asp.id
  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  https_only                 = true
}
{% endhighlight %}

This is the Terraform Configuration Language, not [turing complete](https://simple.wikipedia.org/wiki/Turing_complete) but clear about what it is doing. It is using the Azure Resource Manager (azurerm), an extension that speaks with Azure's APIs. It creates the 4 resources required by the function. To run this code, we need Terraform installed and available in the command line. Download it from the [Terraform website](https://www.terraform.io/downloads.html), unzip the downloaded file and put the executable in any folder declared in the `$PATH` environment variable. On a Mac, we can simply run `$ brew install terraform`. 

    $ terraform import azurerm_resource_group.rg /subscriptions/e71bf673-899a-4cb2-b2c3-fb4863674003/resourceGroups/buyersmarket
    
Configuring Terraform CLI for Switcheroo
Step 1
In the command line, navigate to Switcherro local repo, then into the infra folder:

  $ cd ~/src/work/switcheroo/infra/nprd
Step 2
Initialize the local setup. Among other things, the following command install all required plugins and modules:

  $ terraform init
Once initialized, the folder .terraform is created, preserving the state of the modules and plugins. In case of changes in the modules that benefit the project, go to infra/nprd/.terraform and delete the folder of the updated module. It will force the reinstallation of that module next time you run $ terraform init.

Step 3
Login to portal.azure.com to complete a two-factor authentication and then login to azure cli:

  $ az login
It gives a list of subscriptions. Make sure you select the pccsub-us-nprd one:

  $ az account set --subscription <subscription_id>
Step 4
Run the terraform plan to see the list of changes planned to be implemented:

  $ terraform plan
Step 5
Apply terraform changes:

  $ terraform apply
Step 6
If necessary, all changes can be removed:

  $ terraform destroy
Step 7
Build the Switcheroo Jenkins job for the branch dev to have the function deployed to nprd or build the branch master to deploy to prod.

Step 8
Login to Azure Portal and locate the resource group rg-us-nprd-np-swoo-app for QA or rg-us-prod-pa-swoo-app for PROD. That's the most reliable way to access the resources, preventing confusion.

Step 9
Select the function nprdswitcheroo, then select the option "App keys", click on the default key and set a key recognized by the applications or get the existing key and replace the one in the applications.

Step 10
Still in the function nprdswitcheroo, go to the option "Identity", select the tab "User assigned", click on "Add" and select mi-fa-swoo-app.

Key Vaults
The name of the secrets are the same for nprd and prod, but the key vaults are named differently.

NPRD: kv-use2-nprd-np-swoo
Secrets:

drug-library-authkey
swoo-postgres-password
PROD: kv-use2-prod-pa-swoo
Secrets:

swoo-postgres-password
