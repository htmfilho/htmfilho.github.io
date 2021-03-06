---
layout: post
title:  "Deploying an Azure Function in Go"
date: 2021-01-21 12:00:00 +0200
categories: serverless golang api
---

![Golang Serverless](/images/posts/golang-serverless.jpg)

In the [first part](/2021/01/azure-function-golang.html), we have built a simple Go web application that calculates the maximum bid we can make when negotiating a house. Again, this is about Go, not real estate. So, be careful when using this calculation in real life. We expect to publish that app on Azure without changes because there is nothing special in the code that makes it suitable for Azure. Yet, it can be deployed and served as an Azure Function, as we are going to witness in this article.

<!-- more -->

The Azure response to serverless computing is called [Azure Functions](https://azure.microsoft.com/en-ca/services/functions/). It is a straightforward service, highly configurable, priced by the second and free for up to a million requests per month ([consumption plan](https://azure.microsoft.com/en-ca/pricing/details/functions/)). It offers [language handlers](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages) for C#, Java, JavaScript, Python, and PowerShell out of the box. Other languages like Go and Rust are supported through a [custom handler](https://docs.microsoft.com/en-us/azure/azure-functions/functions-custom-handlers), which is a lightweight web server that receives events from the Functions host. Since Go implements [HTTP primitives](https://golang.org/pkg/net/http/), it can use a custom handler.

While it may be possible to run web applications using custom handlers, Azure Functions is not a standard reverse proxy. Some features such as response streaming, HTTP/2, and WebSockets are not available. The application may also experience excessive cold start.

To build a smooth development integration with Azure, we need 2 tools:

- [Azure CLI](https://docs.microsoft.com/en-ca/cli/azure/): a set of commands to create and manage Azure resources. We will use it to create the resources required by the function, such as the resource group, storage, application insights and the functions host.
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash): enable developing and testing functions on a local computer and deploying it to the cloud.

## Azure CLI

You can find steps to install Azure CLI on your operating system in the [Azure Command-Line Interface (CLI) Documentation](https://docs.microsoft.com/en-ca/cli/azure/). I use Ubuntu so these were the steps I followed:

1. Install Azure CLI:

       $ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

2. Login to Azure:

       $ az login

The default web browser opens at https://login.microsoftonline.com/common/oauth2/authorize an asks for your Azure credentials. After a successful sign in, Azure CLI prints out information about the user's subscriptions: 

{% highlight json %}
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
{% endhighlight %}

## Azure Functions Core Tools

You can find steps to install Azure Functions Core Tools on your operating system in the [Azure Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local). I use Ubuntu so these were the steps I followed:

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

Buyersmarket is the app created in [part 1](/2021/01/azure-function-golang.html). We want to prepare it to run as an Azure function. Let's start by going to the root of the project and running the Azure Functions Core Tools to generate the artifacts for a custom handler:

    $ cd /path/to/azure/function
    $ func init --worker-runtime custom

It generates the files:

    /host.json
    /local.settings.json
    /.vscode/extensions.json

`host.json` configures the app on Azure and `local.settings.json` stores settings used by the app and local development tools. The `.vscode/extensions.json` just prepares the project to be opened in VSCode with Azure extension. The only file we need to change for the time being is `host.json`. Here it is:

{% highlight json %}
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
{% endhighlight %}

Open the file and:

- set the `defaultExecutablePath` parameter with the binary file name, in this case `buyersmarket`, obtained after running `go build buyersmarket`.
- add the `enableForwardingHttpRequest` parameter under `customHandler` and set it to `true`. It indicates that this is a HTTP-only function, making the handler work directly with the HTTP request and response.

## The Azure Function

A application may contain several Azure Functions. In Buyersmarket, we are going to start with `offer` as our first Azure Function. For that, let's create the file `function.json` in the folder `/offer/` with the following content:

{% highlight json %}
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
{% endhighlight %}

Notice that all we did so far was setting up configuration files without touching a single line of Go code that we already have written in [part 1](/2021/01/azure-function-golang.html). To see the complete setup, take a look at [Buyersmaket repository](https://github.com/htmfilho/buyersmarket).

Now, we are ready to test the `offer` Function locally. Let's run it using Azure Functions Core Tools:

    $ go build buyersmarket.go
    $ func start

After a few seconds, call the URL:

    $ curl 'http://localhost:7071/api/offer?savings=134507&listingPrice=700000&downPayment=10&closingCosts=17000'

Expect the same response as if you were running the Go app directly:

{% highlight json %}
{
  "savings": 100000,
  "listingPrice": 600000,
  "downPayment": 10,
  "closingCosts": 20000,
  "maximumBid": 620000,
  "margin": 20000
}
{% endhighlight %}

## Publishing to Azure

If the Function successfully run with Azure Function Core Tool then it is likely to run on the cloud without issues. Here we follow the steps to deploy Buyersmarket on Azure. We start by creating all necessary resources required by the function. The first one is the resource group, which helps us to keep all resources together. The following command creates the "buyersmarket" resource group:

    $ az group create --name buyersmarket --location eastus

Notice that we have selected the location `eastus` because it is one of those that supports Functions. Not all locations support Functions, so make sure the one you chose supports it, otherwise the command above will fail.

Let's create an exclusive Azure storage account called `buyersmarketstore`:

    $ az storage account create --name buyersmarketstore --location eastus --resource-group buyersmarket --sku Standard_LRS

Then create the Functions app:

    $ az functionapp create --name buyersmarket --storage-account buyersmarketstore --consumption-plan-location eastus --resource-group buyersmarket --runtime custom --os-type Linux --functions-version 3

Finally, let's deploy the Functions app:

    $ func azure functionapp publish buyersmarket

After a few seconds, call the URL:

    $ curl 'https://buyersmarket.azurewebsites.net/api/offer?savings=134507&listingPrice=700000&downPayment=10&closingCosts=17000'

Expect the same response as if we were calling the Function locally.

I would like to highlight three characteristics that makes Go suitable to write Azure Functions:

1. **Perfect mariage between Function and Go package**: creating a Function in an app consists on creating a folder with the name of the function and adding a `function.json` file in it. Coincidently, folders are also Go packages. So, we keep the code and the function descriptor together, indicating that that package is actually the function implementation, which is great for consistency.

2. **Fast migration to Functions**: if your current Go application already follows the design principles of highly scalable apps then it is likely ready to migrate to a more cost effective cloud solution like Azure Functions.

3. **No Lock-In**: if you discover late in the project that Functions are not the answer to your business need or you hit some technical limitation, then it is easy to move out to something more flexible because there is nothing in the code that locks you in.

Deploying applications as Azure Functions is the most cost effective solution available on the cloud. This is the state-of-the-art implementation of the on-demand service concept: making the app available only when called and automatically scaling it to very large demand. It might have some flaws today, but it is a matter of time to see it become mainstream.