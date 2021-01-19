---
layout: post
title:  "Developing an Azure Function in Go: Part 2"
date: 2021-01-24 12:00:00 +0200
categories: serverless golang api
---

![Golang Serverless](/images/posts/golang-serverless.jpg)

In the [first part](https://www.hildeberto.com/2021/01/azure-function-golang.html) of this series, we have built a simple Go web application that calculates the maximum bid we can make when negociating a house. Again, this is about Go, not real estate. So, be careful when using this calculation in real life. There is nothing special in that code base that makes it suitable for Azure. can be deployed and served as an Azure Function. This time, we are going to deploy this app on Azure.

<!-- more -->

To build a smooth development integration with Azure, we need to install Azure CLI and [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash).

## Azure CLI

You can find steps to install Azure CLI in your operating system on the [Azure Command-Line Interface (CLI) Documentation](https://docs.microsoft.com/en-ca/cli/azure/). I use Ubuntu so these are the commands I run:

1. Install Azure CLI:

       $ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

2. Login to Azure:

       $ az login

The default web browser opens at https://login.microsoftonline.com/common/oauth2/authorize an asks for your Azure credentials. After a successful sign in, Azure CLI prints out information about your subscriptions: 

    [
      {
        "cloudName": "AzureCloud",
        "homeTenantId": "2e6a8af3-h68a-9j2h-vbgh-s456da4gh1a8",
        "id": "ef789013-g6y8-svj8-24rt-123ujmgf74003",
        "isDefault": true,
        "managedByTenants": [],
        "name": "subscriptionname",
        "state": "Enabled",
        "tenantId": "3t7j9s33-f7j9-4w2g-vbgh-s456da4gh1a8",
        "user": {
          "name": "user@example.com",
          "type": "user"
        }
      }
    ]

## Azure Functions Core Tools

You can find steps to install Azure Functions Core Tools at https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local. I use Ubuntu so these are the commands I run:

1. Install the Microsoft package repository GPG key, to validate package integrity:

       $ curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
       $ sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg

2. Set up the APT source list:

       $ sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'

3. Update APT source:

       $ sudo apt-get update

4. Install the Core Tools Package:

       $ sudo apt-get install azure-functions-core-tools-3

## Buyersmarket

Go to Buyersmarket project, run the command below and select the option 5 (custom):

    $ cd /path/to/buyersmarket
    $ func init

It generates the files:

    /host.json
    /local.settings.json
    /.vscode/extensions.json

`host.json` configures the app on Azure and `local.settings.json` stores app settings and settings used by local development tools. The `.vscode/extensions.json` just prepares the project to be openned in VSCode with Azure extension. The only file we need to change for the time being is `host.json`. Here is its content:

    {
      "version": "2.0",
      "logging": {
        "applicationInsights": {
          "samplingSettings": {
            "isEnabled": true,
            "excludedTypes": "Request"
          }
        }
      },
      "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[1.*, 2.0.0)"
      },
      "customHandler": {
        "description": {
          "defaultExecutablePath": "buyersmarket",
          "workingDirectory": "",
          "arguments": []
        },
        "enableForwardingHttpRequest": true
      }
    }

All we need to change is:

- set the `defaultExecutablePath` parameter with the binary file name, in this case `buyersmarket`
- add the `enableForwardingHttpRequest` parameter under `customHandler` and set it to `true`

## The Azure Function

A application may contain several Azure Functions. In Buyersmarket, we are going to start with `offer` as our first Azure Function. For that, let's create the file `function.json` in the folder `/offer/` with the following content:

    {
      "bindings": [
        {
          "authLevel": "anonymous",
          "type": "httpTrigger",
          "direction": "in",
          "name": "req",
          "methods": [
            "get"
          ]
        },
        {
          "type": "http",
          "direction": "out",
          "name": "res"
        }
      ]
    }

Notice that all we did so far was setting up configuration files without touching a single line of Go code that we have already writen in part 1. Now, we are ready to test the `offer` Function locally. Let's run it using Azure Functions Core Tools:

    $ go build buyersmarket.go
    $ func start

After a few seconds call the URL:

    $ curl 'http://localhost:7071/api/offer?savings=134507&listingPrice=700000&downPayment=10&closingCosts=17000'

Expect the same response as if we were running the Go app directly:

    {
        "savings": 100000,
        "listingPrice": 600000,
        "downPayment": 10,
        "closingCosts": 20000,
        "maximumBid": 620000,
        "margin": 20000
    }

## Publishing to Azure

If you don't have a resource group then create one:

    $ az group create --name buyersmarket --location eastus

Let's create an exclusive Azure storage account:

    $ az storage account create --name buyersmarketstore --location eastus --resource-group buyersmarket --sku Standard_LRS

Now, let's create the Function app:

    $ az functionapp create --name buyersmarket --storage-account buyersmarketstore --consumption-plan-location eastus --resource-group buyersmarket --runtime custom --os-type Linux --functions-version 3

Finally, let's deploy the Function:

    $ func azure functionapp publish buyersmarket

After a few seconds call the URL:

    $ curl 'https://buyersmarket.azurewebsites.net/api/offer?savings=134507&listingPrice=700000&downPayment=10&closingCosts=17000'

Expect the same response as if we were running the Function locally.

In part 3, we are going to explore our Function in Azure Portal. Stay tuned!