---
layout: post
title:  "Applying the Strategy Pattern to Get Prices from Different Sources in Go"
date: 2021-02-04 12:00:00 +0200
categories: golang pattern finance
---

![Stock Prices](/images/posts/golang-strategy-pattern.png)

I keep searching for concrete examples in my quest to convince you that Go is a great language for business. I found in finance a great source of ideas to prove my point. I already explored this subject twice ([1](https://www.hildeberto.com/2020/04/dealing-with-money.html) and [2](https://www.hildeberto.com/2021/01/azure-function-golang.html)) and today I'm going to explore it again.

<!-- more -->

We

```
package main

import "fmt"

// Supported exchanges
const (
  NASDAQ = "NASDAQ"
  NYSE   = "NYSE"
  TSX    = "TSX"
)

// Stock represents an investment
type Stock struct {
  Exchange string
  Ticker   string
  Name     string
  Price    int32
}

func main() {
  stocks := []*Stock{
    {
      Exchange: NASDAQ,
      Ticker:   "GOOGL",
      Name:     "Alphabet Inc.",
    }, {
      Exchange: NYSE,
      Ticker:   "GE",
      Name:     "General Electric CO",
    }, {
      Exchange: TSX,
      Ticker:   "SHOP",
      Name:     "Shopify Inc.", 
    }, {
      Exchange: NASDAQ,
      Ticker:   "AAPL",
      Name:     "Apple Inc.",
    }, {
      Exchange: TSX,
      Ticker:   "BMO",
      Name:     "Bank of Montreal",
    }, {
      Exchange: TSX,
      Ticker:   "CP",
      Name:     "Canadian Pacific Raiway Ltd.",
    },
  }

  stocks = getPrices(stocks)

  for _, stock := range stocks {
    fmt.Printf("%s: %d\n", stock.Ticker, stock.Price)
  }
}

func getPrices(stocks []*Stock) []*Stock {
  var exchangesPricing ExchangesPricing
  for _, stock := range stocks {
    pricing := exchangesPricing.GetExchangePricing(stock)
    pricing.addStock(stock)
  }

  for _, exchange := range exchangesPricing.exchanges {
    exchange.search()
  }

  return stocks
}
```
Even if prices are obtained from different sources in a different order, it is expected that the stocks are returned to the caller in the same order they were informed. To acomplish that, we simply pass the original list by reference (*) and mutate the prices.

```
// Pricing shapes the strategy pattern to be applied to specialized structs.
type Pricing interface {
  addStock(stock *Stock)
  search() ([]*Stock, error)
}

// ExchangesPricing holds the pricing strategies for the duration of the execution.
type ExchangesPricing struct {
  exchanges map[string]Pricing
}

// GetExchangePricing returns the Pricing based on the stock exchange.
func (ep *ExchangesPricing) GetExchangePricing(stock *Stock) Pricing {
  if ep.exchanges == nil {
    ep.exchanges = make(map[string]Pricing)
    ep.exchanges[NASDAQ] = new(NasdaqPricing)
    ep.exchanges[NYSE] = new(NYSEPricing)
    ep.exchanges[TSX] = new(TsxPricing)
  }
  return ep.exchanges[stock.Exchange]
}
```
The strategy pattern is implemented below, defining a family of algorithms to search prices on different sources.

### NASDAQ Strategy Pattern Implementation

```
// NasdaqPricing is the strategy implementation to get prices from Nasdaq.
type NasdaqPricing struct {
  stocks []*Stock
}

func (np *NasdaqPricing) addStock(stock *Stock) {
  np.stocks = append(np.stocks, stock)
}

func (np *NasdaqPricing) search() ([]*Stock, error) {
  np.stocks[0].Price = 2344500
  np.stocks[1].Price = 5439990
  return np.stocks, nil
}
```

### NYSE Strategy Pattern Implementation
```
// NYSEPricing is the strategy implementation to get prices from NYSE.
type NYSEPricing struct {
  stocks []*Stock
}

func (nyp *NYSEPricing) addStock(stock *Stock) {
  nyp.stocks = append(nyp.stocks, stock)
}

func (nyp *NYSEPricing) search() ([]*Stock, error) {
  nyp.stocks[0].Price = 344500
  return nyp.stocks, nil
}
```

### TSX Strategy Pattern Implementation
```
// TsxPricing is the strategy implementation to get prices from Tsx.
type TsxPricing struct {
  stocks []*Stock
}

func (tp *TsxPricing) addStock(stock *Stock) {
  tp.stocks = append(tp.stocks, stock)
}

func (tp *TsxPricing) search() ([]*Stock, error) {
  tp.stocks[0].Price = 8344500
  tp.stocks[1].Price = 239990
  tp.stocks[2].Price = 39990
  return tp.stocks, nil
}
```

