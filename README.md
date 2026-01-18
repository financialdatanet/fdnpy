# **fdnpy**

Complete Python SDK for [FinancialData.Net](https://financialdata.net/) API

## **Installation**

```
pip install fdnpy
```
## **Usage Example**

```python
from fdnpy import FinancialDataClient

# Replace 'YOUR_API_KEY' with your actual key  
client = FinancialDataClient(api_key='YOUR_API_KEY')

# Get stock prices for Microsoft  
prices = client.get_stock_prices(identifier='MSFT')  
print(prices[0], end='\n\n')

# Get Microsoft's balance sheet  
balance_sheet = client.get_balance_sheet_statements(identifier='MSFT', period='year')  
print(balance_sheet[0])  
```

## Overview

`FinancialDataClient` is the main entry point for interacting with FinancialData.Net API v1.  
The client uses `requests` under the hood and supports automatic pagination, retries with exponential backoff, and structured access to financial data endpoints.


## Core Methods

### make_request(endpoint, params)

Low-level HTTP request handler with retries.

### get_data(endpoint, params, limit)

Handles pagination and aggregates all available records.


## API Endpoints

### Symbol Lists
- get_stock_symbols()
- get_international_stock_symbols()
- get_etf_symbols()
- get_commodity_symbols()
- get_otc_symbols()

### Market Data
- get_stock_quotes(identifiers)
- get_stock_prices(identifier)
- get_international_stock_prices(identifier)
- get_minute_prices(identifier, date)
- get_latest_prices(identifier)
- get_commodity_prices(identifier)
- get_otc_prices(identifier)
- get_otc_volume(identifier)

### Market Indexes
- get_index_symbols()
- get_index_quotes(identifiers)
- get_index_prices(identifier)
- get_index_constituents(identifier)

### Derivatives Data
- get_option_chain(identifier)
- get_option_prices(identifier)
- get_option_greeks(identifier)
- get_futures_symbols()
- get_futures_prices(identifier)

### Crypto Currencies
- get_crypto_symbols()
- get_crypto_information(identifier)
- get_crypto_quotes(identifiers)
- get_crypto_prices(identifier)
- get_crypto_minute_prices(identifier, date)

### Forex Data
- get_forex_symbols()
- get_forex_quotes(identifiers)
- get_forex_prices(identifier)
- get_forex_minute_prices(identifier, date)

### Basic Information
- get_company_information(identifier)
- get_international_company_information(identifier)
- get_key_metrics(identifier)
- get_market_cap(identifier)
- get_employee_count(identifier)
- get_executive_compensation(identifier)
- get_securities_information(identifier)

### Financial Statements
- get_income_statements(identifier, period=None)
- get_balance_sheet_statements(identifier, period=None)
- get_cash_flow_statements(identifier, period=None)
- get_international_income_statements(identifier, period=None)
- get_international_balance_sheet_statements(identifier, period=None)
- get_international_cash_flow_statements(identifier, period=None)

### Financial Ratios
- get_liquidity_ratios(identifier, period=None)
- get_solvency_ratios(identifier, period=None)
- get_efficiency_ratios(identifier, period=None)
- get_profitability_ratios(identifier, period=None)
- get_valuation_ratios(identifier, period=None)

### Event Calendars
- get_earnings_calendar(date)
- get_ipo_calendar(date)
- get_splits_calendar(date)
- get_dividends_calendar(date)
- get_economic_calendar(date)

### Insider Trading
- get_insider_transactions(identifier)
- get_proposed_sales(identifier)
- get_senate_trading(identifier)
- get_house_trading(identifier)

### Institutional Trading
- get_institutional_investors()
- get_institutional_holdings(identifier)
- get_institutional_portfolio_statistics(identifier)

### ETF Data
- get_etf_quotes(identifiers)
- get_etf_prices(identifier)
- get_etf_holdings(identifier)

### Mutual Funds

- get_mutual_fund_symbols()
- get_mutual_fund_holdings(identifier)
- get_mutual_fund_statistics(identifier)

### ESG Data
- get_esg_scores(identifier)
- get_esg_ratings(identifier)
- get_industry_esg_scores(date)

### Investment Advisers
- get_investment_adviser_names()
- get_investment_adviser_information(identifier)

### Miscellaneous Data
- get_earnings_releases(identifier)
- get_initial_public_offerings(identifier)
- get_stock_splits(identifier)
- get_dividends(identifier)
- get_short_interest(identifier)


## Return Values

All endpoint methods return lists of dictionaries parsed directly from the API JSON responses.

## API Documentation

#### Introduction

Here you can find a list of all API endpoints, along with their descriptions, required or optional query parameters, and sample responses.

When making requests, ensure that each URL ends with ?key=API\_KEY. If the URL already contains other query parameters, use &key=API\_KEY when adding the API key.

Some API endpoints may specify a limit on records to be retrieved per API call. To retrieve all the data available from these endpoints, use the offset parameter. For example, if the record limit is 500, then with the first API call, you will retrieve records 0–499, with the second API call records 500–999, etc.

#### Stock Symbols <code>Free Subscription</code>

Get a list of stock symbols for publicly traded US and international companies. The list contains thousands of trading symbols as well as the names of the companies whose shares they identify. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/stock-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "A",
      "registrant_name": "AGILENT TECHNOLOGIES, INC."
    },
    {
      "trading_symbol": "AA",
      "registrant_name": "Alcoa Corp"
    },
    {
      "trading_symbol": "AACB",
      "registrant_name": "Artius II Acquisition Inc."
    },
    ...
  ]
  ```

#### International Stock Symbols <code>Free Subscription</code>

Retrieve a list of stock symbols for publicly traded international companies. Data is available for the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-stock-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "000080.KS",
      "registrant_name": "HiteJinro Co., Ltd."
    },
    {
      "trading_symbol": "000100.KS",
      "registrant_name": "Yuhan Corporation"
    },
    {
      "trading_symbol": "000120.KS",
      "registrant_name": "CJ Logistics Corporation"
    },
    ...
  ]
  ```

#### Etf Symbols <code>Free Subscription</code>

An exchange-traded fund (ETF) is a type of investment fund that trades on the stock exchange. ETFs own financial assets such as stocks, bonds, currencies, futures contracts, or commodities. Our API can provide you with a list of a few thousand ETF trading symbols, together with their descriptions. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/etf-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AAA",
      "description": "AAF First Priority CLO Bond ETF"
    },
    {
      "trading_symbol": "AADR",
      "description": "AdvisorShares Dorsey Wright ADR ETF"
    },
    {
      "trading_symbol": "AALL",
      "description": "GraniteShares 2x Long AAL Daily ETF"
    },
    ...
  ]
  ```

#### Commodity Symbols <code>Free Subscription</code>

The commodity market covers the trading of raw materials like oil, gold, coffee, etc. This API endpoint provides trading symbols and additional information for major commodities.

- ###### Endpoint

  `https://financialdata.net/api/v1/commodity-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "BZ",
      "description": "Brent Crude Oil Futures (NYMEX)"
    },
    {
      "trading_symbol": "CJ",
      "description": "Cocoa Futures (NYMEX)"
    },
    {
      "trading_symbol": "CL",
      "description": "Crude Oil Futures (NYMEX)"
    },
    ...
  ]
  ```

#### Otc Symbols <code>Free Subscription</code>

The over-the-counter (OTC) market is where securities are traded through a network of brokers and dealers rather than on a centralized exchange. OTC stocks typically indicate ownership of equity in smaller companies that do not meet the requirements for regular listings. Our API gives you access to thousands of OTC symbols and additional information about them. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/otc-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AAALY",
      "title_of_security": "Aareal Bank AG Unsponsored American Depository Receipt (Germany)"
    },
    {
      "trading_symbol": "AABB",
      "title_of_security": "Asia Broadband Inc Common Stock"
    },
    {
      "trading_symbol": "AABVF",
      "title_of_security": "Aberdeen International Inc Ordinary Shares"
    },
    ...
  ]
  ```

#### Stock Quotes <code>Premium subscription</code>

Get real-time stock quotes, including the last price, change, and percentage change. The data covers several thousand US and international companies. The timezone used for time values is EST (Eastern Standard Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/stock-quotes?identifiers=MSFT,AAPL`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifiers | string | The trading symbols for the securities. | MSFT,AAPL |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AAPL",
      "registrant_name": "Apple Inc.",
      "time": "2025-09-02 15:56:00",
      "price": 238.08,
      "change": 8.36,
      "percentage_change": 3.64
    },
    {
      "trading_symbol": "MSFT",
      "registrant_name": "MICROSOFT CORP",
      "time": "2025-09-02 15:55:57",
      "price": 502.42,
      "change": -2.7,
      "percentage_change": -0.53
    }
  ]
  ```

#### Stock Prices <code>Free Subscription</code>

The API endpoint provides more than 10 years of daily historical stock prices and volumes. The data covers several thousand US and international companies. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/stock-prices?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "date": "2024-12-04",
      "open": 433.03,
      "high": 439.67,
      "low": 432.63,
      "close": 437.42,
      "volume": 26009430.0
    },
    {
      "trading_symbol": "MSFT",
      "date": "2024-12-03",
      "open": 429.84,
      "high": 432.47,
      "low": 427.74,
      "close": 431.2,
      "volume": 18301990.0
    },
    ...
  ]
  ```

#### International Stock Prices <code>Standard subscription</code>

Get more than 10 years of daily historical stock prices and volumes. Data is available for the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-stock-prices?identifier=SHEL.L`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | SHEL.L |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SHEL.L",
      "date": "2025-05-02",
      "open": 2493.0,
      "high": 2543.5,
      "low": 2461.5,
      "close": 2486.5,
      "volume": 12476281.0
    },
    {
      "trading_symbol": "SHEL.L",
      "date": "2025-05-01",
      "open": 2405.0,
      "high": 2446.0,
      "low": 2373.0,
      "close": 2436.5,
      "volume": 4203522.0
    },
    ...
  ]
  ```

#### Minute Prices <code>Standard subscription</code>

The API endpoint provides more than 7 years of one-minute historical prices and volumes. The data is available for over 10,000 securities, including US stocks, international stocks, and exchange-traded funds. The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/minute-prices?identifier=MSFT&date=2020-01-15`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | date | string | The date in YYYY-MM-DD format. | 2020-01-15 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "time": "2020-01-15 20:59:00",
      "open": 163.14,
      "high": 163.26,
      "low": 163.1,
      "close": 163.25,
      "volume": 5633.0
    },
    {
      "trading_symbol": "MSFT",
      "time": "2020-01-15 20:58:00",
      "open": 163.065,
      "high": 163.18,
      "low": 163.055,
      "close": 163.145,
      "volume": 15777.0
    },
    ...
  ]
  ```

#### Latest Prices <code>Premium subscription</code>

Get one-minute stock prices and trading volumes for the current week. Data is available for more than 10,000 securities, including US stocks, international stocks, and exchange-traded funds (ETFs). The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/latest-prices?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "time": "2025-11-04 20:59:00",
      "open": 514.74,
      "high": 514.89,
      "low": 514.38,
      "close": 514.71,
      "volume": 19328.0
    },
    {
      "trading_symbol": "MSFT",
      "time": "2025-11-04 20:58:00",
      "open": 514.36,
      "high": 514.74,
      "low": 514.33,
      "close": 514.74,
      "volume": 9980.0
    },
    ...
  ]
  ```

#### Commodity Prices <code>Free Subscription</code>

The commodity market comprises the trading of raw materials such as oil, gold, coffee, etc. Our API offers over ten years of end-of-day historical prices and volumes for major commodities. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/commodity-prices?identifier=ZC`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a commodity. | ZC |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "ZC",
      "date": "2024-12-03",
      "open": 425.0,
      "high": 428.0,
      "low": 422.75,
      "close": 423.25,
      "volume": 4078.0
    },
    {
      "trading_symbol": "ZC",
      "date": "2024-12-02",
      "open": 423.0,
      "high": 425.5,
      "low": 420.75,
      "close": 424.5,
      "volume": 3877.0
    },
    ...
  ]
  ```

#### Otc Prices <code>Free Subscription</code>

The over-the-counter (OTC) market is a market in which securities are traded through a network of brokers and dealers rather than on a centralized exchange. OTC stocks often represent ownership of equity in smaller companies that do not meet the requirements for regular listings. The API endpoint provides over ten years of daily historical prices and volumes for more than 10,000 OTC securities. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/otc-prices?identifier=AABB`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | AABB |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AABB",
      "date": "2024-12-04",
      "open": 0.0271,
      "high": 0.0271,
      "low": 0.024,
      "close": 0.0248,
      "volume": 6592169.0
    },
    {
      "trading_symbol": "AABB",
      "date": "2024-12-03",
      "open": 0.0235,
      "high": 0.029,
      "low": 0.0235,
      "close": 0.0265,
      "volume": 6828867.0
    },
    ...
  ]
  ```

#### Otc Volume <code>Free Subscription</code>

Over-the-counter (OTC) stocks typically represent ownership of equity in smaller companies that do not meet the criteria for regular listings. Some stocks may not be liquid at all. The API endpoint provides information about the monthly share volume traded for a certain security.

- ###### Endpoint

  `https://financialdata.net/api/v1/otc-volume?identifier=AABB`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | AABB |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AABB",
      "title_of_security": "Asia Broadband Inc Common Stock",
      "month_start_date": "2024-10-01",
      "monthly_volume": 140366022,
      "previous_monthly_volume": 263720143,
      "volume_year_to_date": 2237440816
    },
    {
      "trading_symbol": "AABB",
      "title_of_security": "Asia Broadband Inc Common Stock",
      "month_start_date": "2024-09-01",
      "monthly_volume": 263720143,
      "previous_monthly_volume": 692420804,
      "volume_year_to_date": 2097074794
    },
    ...
  ]
  ```

#### Index Symbols <code>Standard subscription</code>

A market index measures the value of a portfolio of holdings with certain market characteristics. The API endpoint allows you to get a list of the trading symbols and names of the major market indexes.

- ###### Endpoint

  `https://financialdata.net/api/v1/index-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "000001.SS",
      "index_name": "SSE Composite Index"
    },
    {
      "trading_symbol": "DE000SLA30S3.SG",
      "index_name": "Solactive Equal Weight Canada Oil & Gas Index"
    },
    {
      "trading_symbol": "DX-Y.NYB",
      "index_name": "US Dollar Index"
    },
    ...
  ]
  ```

#### Index Quotes <code>Premium subscription</code>

Get real-time market index quotes, including the last price, change, and percentage change. The data covers major market indexes. The timezone used for time values is EST (Eastern Standard Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/index-quotes?identifiers=^GSPC,^DJI`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifiers | string | The trading symbols for the indexes. | ^GSPC,^DJI |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "^GSPC",
      "index_name": "S&P 500",
      "time": "2025-09-23 15:19:59",
      "price": 6656.92,
      "change": -36.83,
      "percentage_change": -0.55
    },
    {
      "trading_symbol": "^DJI",
      "index_name": "Dow Jones Industrial Average",
      "time": "2025-09-23 15:19:59",
      "price": 46292.78,
      "change": -88.76,
      "percentage_change": -0.19
    }
  ]
  ```

#### Index Prices <code>Standard subscription</code>

Our API allows you to retrieve more than 10 years of daily historical market index prices and trading volumes. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/index-prices?identifier=^GSPC`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for an index. | ^GSPC |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "^GSPC",
      "date": "2025-06-13",
      "open": 6000.56,
      "high": 6026.16,
      "low": 5963.21,
      "close": 5976.97,
      "volume": 5258910000.0
    },
    {
      "trading_symbol": "^GSPC",
      "date": "2025-06-12",
      "open": 6009.9,
      "high": 6045.43,
      "low": 6003.88,
      "close": 6045.26,
      "volume": 4669500000.0
    },
    ...
  ]
  ```

#### Index Constituents <code>Standard subscription</code>

Index constituents are the individual components that comprise a market index. These can be stocks, bonds, or other financial instruments. The API endpoint returns a list of constituents for a specific index. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/index-constituents?identifier=^GSPC`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for an index. | ^GSPC |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "^GSPC",
      "index_name": "S&P 500",
      "constituent_symbol": "COIN",
      "constituent_name": "Coinbase",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "date_added": "2025-05-19"
    },
    {
      "trading_symbol": "^GSPC",
      "index_name": "S&P 500",
      "constituent_symbol": "DASH",
      "constituent_name": "DoorDash",
      "sector": "Consumer Discretionary",
      "industry": "Specialized Consumer Services",
      "date_added": "2025-03-24"
    },
    ...
  ]
  ```

#### Option Chain <code>Standard subscription</code>

Options chains display a list of all available option contracts for a specific underlying security. The API endpoint provides option chain data for several thousand US and international companies. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/option-chain?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "contract_name": "MSFT271217P00660000",
      "expiration_date": "2027-12-17",
      "put_or_call": "Put",
      "strike_price": 660.0
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "contract_name": "MSFT271217C00660000",
      "expiration_date": "2027-12-17",
      "put_or_call": "Call",
      "strike_price": 660.0
    },
    ...
  ]
  ```

#### Option Prices <code>Standard subscription</code>

Stock options give the right to buy or sell shares of a specific stock at a predetermined price and date. The API endpoint provides daily historical stock option prices and volumes. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/option-prices?identifier=MSFT250417C00400000`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The contract name for a stock option. | MSFT250417C00400000 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "contract_name": "MSFT250417C00400000",
      "date": "2025-03-07",
      "open": 11.45,
      "high": 11.9,
      "low": 8.75,
      "close": 11.25,
      "volume": 1005.0
    },
    {
      "contract_name": "MSFT250417C00400000",
      "date": "2025-03-06",
      "open": 11.65,
      "high": 16.0,
      "low": 11.5,
      "close": 13.86,
      "volume": 1299.0
    },
    ...
  ]
  ```

#### Option Greeks <code>Standard subscription</code>

Option Greeks provide a way to measure the sensitivity of an option's price to numerous factors such as the underlying asset price, time till expiration, market volatility, and so on. Our API provides daily historical option Greek values. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/option-greeks?identifier=MSFT250417C00400000`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The contract name for a stock option. | MSFT250417C00400000 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "contract_name": "MSFT250417C00400000",
      "date": "2025-03-07",
      "delta": 0.163203703354078,
      "gamma": 0.000139524283246703,
      "theta": -0.0218808916622069,
      "vega": 0.324904955132613,
      "rho": 0.0716368104421749
    },
    {
      "contract_name": "MSFT250417C00400000",
      "date": "2025-03-06",
      "delta": 0.40771043689382,
      "gamma": 0.000216457024980538,
      "theta": -0.041187033759887,
      "vega": 0.52266727480074,
      "rho": 0.184554341455875
    },
    ...
  ]
  ```

#### Futures Symbols <code>Standard subscription</code>

Futures contracts are contracts to purchase or sell a particular underlying asset at a future date. The API endpoint returns a list of futures symbols along with their descriptions. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/futures-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "10Y",
      "description": "10-Year Yield Futures",
      "type": "Interest Rates"
    },
    {
      "trading_symbol": "1OZ",
      "description": "1-Ounce Gold Futures",
      "type": "Metals"
    },
    {
      "trading_symbol": "2GT",
      "description": "BTIC on E-mini Russell 2000 Growth Index Futures",
      "type": "Equities"
    },
    ...
  ]
  ```

#### Futures Prices <code>Standard subscription</code>

Get over 10 years of historical end-of-day futures prices and volumes. Data is available for major agricultural, energy, equity, FX, interest rate, and metal futures. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/futures-prices?identifier=ZN`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a futures contract. | ZN |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "ZN",
      "date": "2025-03-07",
      "open": 110.81,
      "high": 111.28,
      "low": 110.47,
      "close": 110.55,
      "volume": 6317.0
    },
    {
      "trading_symbol": "ZN",
      "date": "2025-03-06",
      "open": 110.64,
      "high": 110.91,
      "low": 110.39,
      "close": 110.78,
      "volume": 6317.0
    },
    ...
  ]
  ```

#### Crypto Symbols <code>Standard subscription</code>

Cryptocurrency is a digital currency that is secured through cryptography and exists on decentralised networks utilising blockchain technology. The API endpoint returns a list of cryptocurrency pair symbols and related information. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/crypto-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "1000CATUSD",
      "base_asset": "1000CAT",
      "quote_asset": "USD"
    },
    {
      "trading_symbol": "1000CHEEMSUSD",
      "base_asset": "1000CHEEMS",
      "quote_asset": "USD"
    },
    {
      "trading_symbol": "1000SATSUSD",
      "base_asset": "1000SATS",
      "quote_asset": "USD"
    },
    ...
  ]
  ```

#### Crypto Information <code>Standard subscription</code>

Retrieve basic information about the cryptocurrency, such as its market cap, total supply, ledger start date, and various other key facts. The API endpoint provides basic information for major cryptocurrencies.

- ###### Endpoint

  `https://financialdata.net/api/v1/crypto-information?identifier=BTC`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The symbol (code) for a cryptocurrency. | BTC |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "BTC",
      "crypto_name": "Bitcoin",
      "market_cap": 2275103042119.0,
      "fully_diluted_valuation": 2275103042119.0,
      "total_supply": 19900334.0,
      "max_supply": 21000000.0,
      "circulating_supply": 19900334.0,
      "highest_price": 122838.0,
      "highest_price_date": "2025-07-14",
      "lowest_price": 67.81,
      "lowest_price_date": "2013-07-06",
      "hash_function": "SHA-256",
      "block_time": "10 minutes",
      "ledger_start_date": "2009-01-03",
      "website": "http://www.bitcoin.org",
      "description": "Bitcoin is the first decentralized cryptocurrency, operating on a peer-to-peer network without central authority. It uses blockchain technology to enable secure, transparent transactions. Known as digital gold, Bitcoin has a capped supply of 21 million coins. Its primary use cases include store of value and cross-border payments. Mining secures the network through proof-of-work consensus."
    }
  ]
  ```

#### Crypto Quotes <code>Premium subscription</code>

Get real-time cryptocurrency pair quotes, including the last price, change, and percentage change. Change is the price difference within a 24-hour time frame. The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/crypto-quotes?identifiers=BTCUSD,ETHUSD`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifiers | string | The trading symbols for the cryptocurrency pairs. | BTCUSD,ETHUSD |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "BTCUSD",
      "base_asset": "BTC",
      "quote_asset": "USD",
      "time": "2025-09-02 21:01:00",
      "price": 111394.68,
      "change": 2563.62,
      "percentage_change": 2.356
    },
    {
      "trading_symbol": "ETHUSD",
      "base_asset": "ETH",
      "quote_asset": "USD",
      "time": "2025-09-02 21:01:00",
      "price": 4314.39,
      "change": 27.29,
      "percentage_change": 0.637
    }
  ]
  ```

#### Crypto Prices <code>Standard subscription</code>

This API endpoint allows you to retrieve daily historical cryptocurrency prices and trading volumes. The data covers major cryptocurrency pairs. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/crypto-prices?identifier=BTCUSD`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for the cryptocurrency pair. | BTCUSD |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "BTCUSD",
      "date": "2025-07-30",
      "open": 117950.75,
      "high": 118792.0,
      "low": 115796.23,
      "close": 117840.3,
      "volume": 15586.73631
    },
    {
      "trading_symbol": "BTCUSD",
      "date": "2025-07-29",
      "open": 118062.32,
      "high": 119273.36,
      "low": 116950.75,
      "close": 117950.76,
      "volume": 15137.93445
    },
    ...
  ]
  ```

#### Crypto Minute Prices <code>Standard subscription</code>

The API endpoint allows you to retrieve one-minute historical cryptocurrency prices and volumes. The data covers major cryptocurrency pairs. The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/crypto-minute-prices?identifier=BTCUSD&date=2025-01-15`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for the cryptocurrency pair. | BTCUSD |
  | date | string | The date in YYYY-MM-DD format. | 2025-01-15 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "BTCUSD",
      "time": "2025-01-15 23:59:00",
      "open": 100497.35,
      "high": 100497.36,
      "low": 100497.35,
      "close": 100497.35,
      "volume": 8.7986
    },
    {
      "trading_symbol": "BTCUSD",
      "time": "2025-01-15 23:58:00",
      "open": 100510.02,
      "high": 100510.02,
      "low": 100457.36,
      "close": 100497.35,
      "volume": 34.48309
    },
    ...
  ]
  ```

#### Forex Symbols <code>Premium subscription</code>

Forex (foreign exchange) is a global decentralized marketplace for trading national currencies, facilitated by an interconnected network of banks and financial institutions. The API endpoint returns a list of forex currency pairs and corresponding data.

- ###### Endpoint

  `https://financialdata.net/api/v1/forex-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AUDCAD",
      "base_asset": "AUD",
      "quote_asset": "CAD"
    },
    {
      "trading_symbol": "AUDCHF",
      "base_asset": "AUD",
      "quote_asset": "CHF"
    },
    {
      "trading_symbol": "AUDHKD",
      "base_asset": "AUD",
      "quote_asset": "HKD"
    },
    ...
  ]
  ```

#### Forex Quotes <code>Premium subscription</code>

Get real-time forex quotes, including the last price, change, and percentage change. The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/forex-quotes?identifiers=EURUSD,GBPUSD`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifiers | string | The trading symbols for the currency pairs. | EURUSD,GBPUSD |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "EURUSD",
      "base_asset": "EUR",
      "quote_asset": "USD",
      "time": "2025-12-22 14:43:32",
      "price": 1.17631,
      "change": 0.00527,
      "percentage_change": 0.45
    },
    {
      "trading_symbol": "GBPUSD",
      "base_asset": "GBP",
      "quote_asset": "USD",
      "time": "2025-12-22 14:43:32",
      "price": 1.34504,
      "change": 0.00754,
      "percentage_change": 0.56
    }
  ]
  ```

#### Forex Prices <code>Premium subscription</code>

This API endpoint allows you to retrieve daily historical forex prices and trading volumes. The data covers major currency pairs. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/forex-prices?identifier=EURUSD`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for the currency pair. | EURUSD |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "EURUSD",
      "date": "2025-12-23",
      "open": 1.17896,
      "high": 1.18072,
      "low": 1.17718,
      "close": 1.17748,
      "volume": 89168.0
    },
    {
      "trading_symbol": "EURUSD",
      "date": "2025-12-22",
      "open": 1.1753,
      "high": 1.18014,
      "low": 1.17521,
      "close": 1.17924,
      "volume": 101718.0
    },
    ...
  ]
  ```

#### Forex Minute Prices <code>Premium subscription</code>

The API endpoint allows you to retrieve one-minute historical forex prices and volumes. The data covers major currency pairs. The timezone used for time values is UTC (Coordinated Universal Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/forex-minute-prices?identifier=EURUSD&date=2025-01-15`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for the currency pair. | EURUSD |
  | date | string | The date in YYYY-MM-DD format. | 2025-01-15 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "EURUSD",
      "time": "2025-01-15 23:59:00",
      "open": 1.02944,
      "high": 1.02948,
      "low": 1.02939,
      "close": 1.02945,
      "volume": 42.0
    },
    {
      "trading_symbol": "EURUSD",
      "time": "2025-01-15 23:58:00",
      "open": 1.02941,
      "high": 1.02943,
      "low": 1.02941,
      "close": 1.02942,
      "volume": 17.0
    },
    ...
  ]
  ```

#### Company Information <code>Standard subscription</code>

This API endpoint provides basic information about the company, such as its LEI number, industry, contact information, and other key facts. The data covers a few thousand US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/company-information?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "isin_number": "US5949181045",
      "lei_number": null,
      "ein_number": "911144442",
      "exchange": "Nasdaq",
      "sic_code": "7372",
      "sic_description": "Services-Prepackaged Software",
      "fiscal_year_end": "0630",
      "state_of_incorporation": "WA",
      "address_street": "ONE MICROSOFT WAY",
      "address_city": "REDMOND",
      "address_state": "WA",
      "address_zip_code": "98052-6399",
      "address_country": "UNITED STATES",
      "address_country_code": "US",
      "phone_number": "425-882-8080",
      "mailing_address": "ONE MICROSOFT WAY, REDMOND, WA, 98052-6399",
      "business_address": "ONE MICROSOFT WAY, REDMOND, WA, 98052-6399",
      "former_name": null,
      "industry": "Information technology",
      "founding_date": "1975-04-04",
      "chief_executive_officer": "Satya Nadella",
      "number_of_employees": 228000,
      "website": "https://www.microsoft.com/",
      "market_cap": 2800000000000.0,
      "shares_issued": null,
      "shares_outstanding": 7434880776,
      "description": "Microsoft Corporation is an American multinational technology conglomerate headquartered in Redmond, Washington. Founded in 1975, the company became highly influential in the rise of personal computers through software like Windows, and the company has since expanded to Internet services, cloud computing, video gaming and other fields. Microsoft is the largest software maker, one of the most valuable public U.S. companies, and one of the most valuable brands globally."
    }
  ]
  ```

#### International Company Information <code>Standard subscription</code>

Our API provides basic information about the international company, such as its exchange, industry, employee count, and other key facts. Data is available for the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-company-information?identifier=SHEL.L`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | SHEL.L |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SHEL.L",
      "registrant_name": "Shell PLC",
      "exchange": "London Stock Exchange",
      "isin_number": "GB00BP6MXD84",
      "industry": "Energy",
      "founding_date": "1907",
      "chief_executive_officer": "Wael Sawan",
      "number_of_employees": 90000,
      "website": "https://www.shell.com/",
      "description": "Shell PLC is a British multinational oil and gas company, headquartered in London, England. Shell is a public limited company with a primary listing on the London Stock Exchange (LSE) and secondary listings on Euronext Amsterdam and the New York Stock Exchange. A core component of Big Oil, Shell is the second largest investor-owned oil and gas company in the world by revenue (after ExxonMobil), and among the world's largest companies out of any industry. Measured by both its own emissions, and the emissions of all the fossil fuels it sells, Shell was the ninth-largest corporate producer of greenhouse gas emissions in the period 1988–2015."
    }
  ]
  ```

#### Key Metrics <code>Standard subscription</code>

The API endpoint returns key financial metrics such as price-to-earnings ratio, price-to-book ratio, free cash flow, etc. This information is particularly important for value investors looking to identify undervalued stocks. Data is available for several thousand US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/key-metrics?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "period_end_date": "2024-06-30",
      "earnings_per_share": 11.86,
      "earnings_per_share_forecast": 13.33,
      "price_to_earnings_ratio": 38.5101180438449,
      "forward_price_to_earnings_ratio": 34.2633158289572,
      "earnings_growth_rate": 22.0164609053498,
      "price_earnings_to_growth_ratio": 1.74915115601015,
      "book_value_per_share": 36.1293231059077,
      "price_to_book_ratio": 12.6415321610417,
      "ebitda": 136758000000.0,
      "enterprise_value": 3351003630000.0,
      "dividend_yield": 0.00656931603829476,
      "dividend_payout_ratio": 0.252972678587637,
      "debt_to_equity_ratio": 0.17575434767224,
      "capital_expenditures": 62237000000.0,
      "free_cash_flow": 56311000000.0,
      "return_on_equity": 0.328281379782998,
      "one_year_beta": 1.19353548418252,
      "three_year_beta": 1.25034202198802,
      "five_year_beta": 1.19116942054093
    },
    ...
  ]
  ```

#### Market Cap <code>Standard subscription</code>

Market capitalization, or market cap, is the total value of a company's outstanding common shares held by investors. Market cap is calculated by multiplying the market price per common share by the total number of common shares outstanding. Our API provides historical market cap data for a few thousand companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/market-cap?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "market_cap": 2800000000000.0,
      "change_in_market_cap": 1000000000000.0,
      "percentage_change_in_market_cap": 55.5555555555556,
      "shares_outstanding": 7433038381,
      "change_in_shares_outstanding": 3274659,
      "percentage_change_in_shares_outstanding": 0.0440748740138738
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2023",
      "market_cap": 1800000000000.0,
      "change_in_market_cap": -700000000000.0,
      "percentage_change_in_market_cap": -28.0,
      "shares_outstanding": 7429763722,
      "change_in_shares_outstanding": -28128150,
      "percentage_change_in_shares_outstanding": -0.377159530907181
    },
    ...
  ]
  ```

#### Employee Count <code>Standard subscription</code>

This API endpoint returns the total number of company employees for a particular year. The historical data covers several thousand US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/employee-count?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "employee_count": 228000
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2023",
      "employee_count": 221000
    },
    ...
  ]
  ```

#### Executive Compensation <code>Standard subscription</code>

Executive compensation includes both financial and non-financial benefits provided by their employer. It is usually a combination of a base salary, variable performance-based bonuses, and other benefits. The API endpoint provides historical executive compensation data for several thousand US and international companies. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/executive-compensation?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "executive_name": "Christopher D. Young",
      "executive_position": "Executive Vice President",
      "fiscal_year": "2024",
      "salary": 850000.0,
      "bonus": 0.0,
      "stock_awards": 9040931.0,
      "incentive_plan_compensation": 2023680.0,
      "other_compensation": 120092.0,
      "total_compensation": 12034703.0
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "executive_name": "Bradford L. Smith",
      "executive_position": "Chair, President",
      "fiscal_year": "2024",
      "salary": 1000000.0,
      "bonus": 0.0,
      "stock_awards": 18684175.0,
      "incentive_plan_compensation": 3642750.0,
      "other_compensation": 112868.0,
      "total_compensation": 23439793.0
    },
    ...
  ]
  ```

#### Securities Information <code>Standard subscription</code>

A security is a tradable financial instrument. The term may refer to a variety of investments, including stocks, bonds, notes, limited partnership interests, investment contracts, and others. This API endpoint provides basic information about the securities, such as their trading symbol, issuer, local and international identification numbers, and other details.

- ###### Endpoint

  `https://financialdata.net/api/v1/securities-information?identifier=AAPL`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | One of the following values: a security's trading symbol, the CUSIP (Committee on Uniform Securities Identification Procedures) number, or the ISIN (International Securities Identification Number). | AAPL, 594918104, US5949181045 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AAPL",
      "issuer_name": "APPLE INC",
      "cusip_number": "037833100",
      "isin_number": "US0378331005",
      "figi_identifier": "BBG000B9XRY4",
      "security_type": "Common Stock"
    }
  ]
  ```

#### Income Statements <code>Standard subscription</code>

An income statement, also called a profit and loss statement, is a financial statement that shows a company's income and expenses over a period of time. It indicates how revenue is turned into net income, or profit. Using our API, you can access all the individual financial items that make up an income statement. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/income-statements?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "revenue": 245122000000.0,
      "cost_of_revenue": 74114000000.0,
      "gross_profit": 171008000000.0,
      "research_and_development_expenses": 29510000000.0,
      "general_and_administrative_expenses": 7609000000.0,
      "operating_expenses": null,
      "operating_income": 109433000000.0,
      "interest_expense": 2935000000.0,
      "interest_income": 3157000000.0,
      "net_income": 88136000000.0,
      "earnings_per_share_basic": 11.86,
      "earnings_per_share_diluted": 11.8,
      "weighted_average_shares_outstanding_basic": 7431000000,
      "weighted_average_shares_outstanding_diluted": 7469000000
    },
    ...
  ]
  ```

#### Balance Sheet Statements <code>Standard subscription</code>

A balance sheet, often known as a statement of financial position, summarizes an individual or organization's financial balances. A typical corporate balance sheet has two sides: assets on the left and financing on the right, which itself includes liabilities and equity. Our API allows you to access all of the individual financial items that comprise a balance sheet statement. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/balance-sheet-statements?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "cash_and_cash_equivalents": 90143000000.0,
      "marketable_securities_current": 57228000000.0,
      "accounts_receivable": 56924000000.0,
      "inventories": 1246000000.0,
      "non_trade_receivables": null,
      "other_assets_current": 26021000000.0,
      "total_assets_current": 159734000000.0,
      "marketable_securities_non_current": 14600000000.0,
      "property_plant_and_equipment": 135591000000.0,
      "other_assets_non_current": 36460000000.0,
      "total_assets_non_current": 301369000000.0,
      "total_assets": 512163000000.0,
      "accounts_payable": 21996000000.0,
      "deferred_revenue": 57582000000.0,
      "short_term_debt": 2249000000.0,
      "other_liabilities_current": 19185000000.0,
      "total_liabilities_current": 125286000000.0,
      "long_term_debt": 44937000000.0,
      "other_liabilities_non_current": 27064000000.0,
      "total_liabilities_non_current": 118400000000.0,
      "total_liabilities": 243686000000.0,
      "common_stock": 100923000000.0,
      "retained_earnings": 173144000000.0,
      "accumulated_other_comprehensive_income": -5590000000.0,
      "total_shareholders_equity": 268477000000.0
    },
    ...
  ]
  ```

#### Cash Flow Statements <code>Standard subscription</code>

A cash flow statement is a financial statement that indicates how changes in balance sheet accounts and income affect cash and cash equivalents, breaking down the analysis into operating, investing, and financing activities. Essentially, the cash flow statement is concerned with the flow of cash into and out of the business. Our API allows you to access all of the individual financial items that compose a cash flow statement. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/cash-flow-statements?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "depreciation_and_amortization": 22287000000.0,
      "share_based_compensation_expense": 10734000000.0,
      "deferred_income_tax_expense": -4738000000.0,
      "other_non_cash_income_expense": null,
      "change_in_accounts_receivable": 7191000000.0,
      "change_in_inventories": -1284000000.0,
      "change_in_non_trade_receivables": null,
      "change_in_other_assets": null,
      "change_in_accounts_payable": 3545000000.0,
      "change_in_deferred_revenue": 5348000000.0,
      "change_in_other_liabilities": null,
      "cash_from_operating_activities": 118548000000.0,
      "purchases_of_marketable_securities": 17732000000.0,
      "sales_of_marketable_securities": 24775000000.0,
      "acquisition_of_property_plant_and_equipment": 44477000000.0,
      "acquisition_of_business": null,
      "other_investing_activities": 1298000000.0,
      "cash_from_investing_activities": -96970000000.0,
      "tax_withholding_for_share_based_compensation": 5300000000.0,
      "payments_of_dividends": 22296000000.0,
      "issuance_of_common_stock": 2002000000.0,
      "repurchase_of_common_stock": 17254000000.0,
      "issuance_of_long_term_debt": null,
      "repayment_of_long_term_debt": null,
      "other_financing_activities": -1309000000.0,
      "cash_from_financing_activities": -37757000000.0,
      "change_in_cash": -16389000000.0,
      "cash_at_end_of_period": 90143000000.0,
      "income_taxes_paid": 23400000000.0,
      "interest_paid": 1700000000.0
    },
    ...
  ]
  ```

#### International Income Statements <code>Premium subscription</code>

Get all the individual financial items that comprise an income statement. Data is available for several thousand international companies whose shares are traded on the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-income-statements?identifier=SHEL.L&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | SHEL.L |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SHEL.L",
      "registrant_name": "Shell plc",
      "fiscal_period": "FY",
      "period_end_date": "2024-12-31",
      "currency_code": "USD",
      "revenue": 284312000000.0,
      "cost_of_revenue": 238371000000.0,
      "gross_profit": 45941000000.0,
      "research_and_development_expenses": 1099000000.0,
      "general_and_administrative_expenses": 12439000000.0,
      "operating_expenses": 15949000000.0,
      "operating_income": 29992000000.0,
      "interest_expense": 4858000000.0,
      "interest_income": 2461000000.0,
      "net_income": 16094000000.0,
      "earnings_per_share_basic": 2.55,
      "earnings_per_share_diluted": 2.53,
      "weighted_average_shares_outstanding_basic": 6299600000,
      "weighted_average_shares_outstanding_diluted": 6363700000
    },
    ...
  ]
  ```

#### International Balance Sheet Statements <code>Premium subscription</code>

Get all individual financial items that make up a balance sheet statement. Data is available for several thousand international companies whose shares are traded on the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-balance-sheet-statements?identifier=SHEL.L&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | SHEL.L |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SHEL.L",
      "registrant_name": "Shell plc",
      "fiscal_period": "FY",
      "period_end_date": "2024-12-31",
      "currency_code": "USD",
      "cash_and_cash_equivalents": 37836000000.0,
      "accounts_receivable": 31041000000.0,
      "inventories": 23426000000.0,
      "other_assets_current": null,
      "total_assets_current": 127926000000.0,
      "property_plant_and_equipment": 185219000000.0,
      "other_assets_non_current": null,
      "total_assets_non_current": 259683000000.0,
      "total_assets": 387609000000.0,
      "accounts_payable": 29767000000.0,
      "short_term_debt": 6920000000.0,
      "other_liabilities_current": null,
      "total_liabilities_current": 95034000000.0,
      "long_term_debt": 41456000000.0,
      "other_liabilities_non_current": null,
      "total_liabilities_non_current": 112407000000.0,
      "total_liabilities": 207441000000.0,
      "common_stock": 178307000000.0,
      "retained_earnings": 158834000000.0,
      "total_shareholders_equity": 178307000000.0
    },
    ...
  ]
  ```

#### International Cash Flow Statements <code>Premium subscription</code>

Access all the individual financial items that compose a cash flow statement. Data is available for several thousand international companies whose shares are traded on the following stock exchanges: Toronto, London, Frankfurt, Euronext Paris, Euronext Amsterdam, Tokyo, Hong Kong, Singapore, Indonesia, Malaysia, Korea, Brazil, Mexico, India, Bombay. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/international-cash-flow-statements?identifier=SHEL.L&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | SHEL.L |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SHEL.L",
      "registrant_name": "Shell plc",
      "fiscal_period": "FY",
      "period_end_date": "2024-12-31",
      "currency_code": "USD",
      "depreciation_and_amortization": 22703000000.0,
      "share_based_compensation_expense": null,
      "change_in_accounts_receivable": null,
      "change_in_inventories": 1273000000.0,
      "change_in_other_assets": null,
      "change_in_accounts_payable": null,
      "change_in_other_liabilities": null,
      "cash_from_operating_activities": 54687000000.0,
      "acquisition_of_property_plant_and_equipment": null,
      "acquisition_of_business": -1404000000.0,
      "cash_from_investing_activities": -15155000000.0,
      "payments_of_dividends": -8668000000.0,
      "issuance_of_common_stock": null,
      "repurchase_of_common_stock": -14687000000.0,
      "issuance_of_long_term_debt": 363000000.0,
      "repayment_of_long_term_debt": -9672000000.0,
      "cash_from_financing_activities": -38435000000.0,
      "change_in_cash": 1097000000.0,
      "cash_at_end_of_period": 39110000000.0
    },
    ...
  ]
  ```

#### Liquidity Ratios <code>Standard subscription</code>

Liquidity ratios evaluate how quickly assets can be turned into cash to meet the company's short-term obligations. The API endpoint provides key liquidity ratios calculated based on data obtained from the company's financial statements. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/liquidity-ratios?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "working_capital": 34448000000.0,
      "current_ratio": 1.27495490318152,
      "cash_ratio": 0.719497789058634,
      "quick_ratio": 1.63062912057213,
      "days_of_inventory_outstanding": 2.97460668699571,
      "days_sales_outstanding": 90.1168295787404,
      "days_payables_outstanding": 117.05619046334,
      "cash_conversion_cycle": -23.9647541976042,
      "sales_to_working_capital_ratio": 6.77619284569028,
      "cash_to_current_liabilities_ratio": 1.17627667895854,
      "working_capital_to_debt_ratio": 0.730047047853177,
      "cash_flow_adequacy_ratio": 1.06121206695909,
      "sales_to_current_assets_ratio": 1.53456371217149,
      "cash_to_current_assets_ratio": 0.922602576783903,
      "cash_to_working_capital_ratio": 2.61678471899675,
      "inventory_to_working_capital_ratio": 0.0344446287388732,
      "net_debt": -42957000000.0
    },
    ...
  ]
  ```

#### Solvency Ratios <code>Standard subscription</code>

Solvency ratios evaluate a company's ability to meet its long-term debts and obligations. The API endpoint returns key solvency ratios calculated using data from the company's financial statements. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/solvency-ratios?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "equity_ratio": 0.524202255922431,
      "debt_coverage_ratio": null,
      "asset_coverage_ratio": 8.24664095282499,
      "interest_coverage_ratio": null,
      "debt_to_equity_ratio": 0.17575434767224,
      "debt_to_assets_ratio": 0.0921308255379635,
      "debt_to_capital_ratio": 0.149482200954816,
      "debt_to_income_ratio": null,
      "cash_flow_to_debt_ratio": 2.51235535964057
    },
    ...
  ]
  ```

#### Efficiency Ratios <code>Standard subscription</code>

Efficiency ratios, also known as activity financial ratios, are used to evaluate how effectively a company uses its assets and resources. The API endpoint provides key efficiency ratios calculated using data obtained from the company's financial statements. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/efficiency-ratios?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "asset_turnover_ratio": 0.478601538963182,
      "inventory_turnover_ratio": 122.705298013245,
      "accounts_receivable_turnover_ratio": 4.05029783788696,
      "accounts_payable_turnover_ratio": 3.17218166901571,
      "equity_multiplier": 1.90766061897295,
      "days_sales_in_inventory": 2.97460668699571,
      "fixed_asset_turnover_ratio": 1.55308101463922,
      "days_working_capital": 51.2949470059807,
      "working_capital_turnover_ratio": 7.11571063632141,
      "days_cash_on_hand": null,
      "capital_intensity_ratio": 2.08942077822472,
      "sales_to_equity_ratio": 0.913009308059908,
      "inventory_to_sales_ratio": 0.00246407911162605,
      "investment_turnover_ratio": 0.77653066719888,
      "sales_to_operating_income_ratio": 2.23992762694982
    },
    ...
  ]
  ```

#### Profitability Ratios <code>Standard subscription</code>

Profitability ratios evaluate a company's ability to generate profits from sales or operations, balance sheet assets, or shareholder equity. The API endpoint provides key profitability ratios calculated using data from the company's financial statements. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/profitability-ratios?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "ebit": 114471000000.0,
      "ebitda": 136758000000.0,
      "profit_margin": 0.35955972944085,
      "gross_margin": 0.697644438279714,
      "operating_margin": 0.446442995732737,
      "operating_cash_flow_margin": 0.483628560471928,
      "return_on_equity": 0.328281379782998,
      "return_on_assets": 0.172085839859576,
      "return_on_debt": 1.86784215657186,
      "cash_return_on_assets": 0.231465373328413,
      "cash_turnover_ratio": 2.71925718025803
    },
    ...
  ]
  ```

#### Valuation Ratios <code>Standard subscription</code>

Valuation ratios determine how appropriately shares in a company are valued and what type of return an investor is likely to obtain. The API endpoint provides key valuation ratios calculated using data obtained from the company's financial statements. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/valuation-ratios?identifier=MSFT&period=year`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | period | string | (Optional) The accounting period for which the entity's financial statements are prepared. By default, statements are returned for all accounting periods. | year, quarter |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "fiscal_year": "2024",
      "fiscal_period": "FY",
      "period_end_date": "2024-06-30",
      "dividends_per_share": 3.00040371417037,
      "dividend_payout_ratio": 0.252985136102055,
      "book_value_per_share": 36.1293231059077,
      "retention_ratio": 0.747027321412363,
      "net_fixed_assets": 113304000000.0
    },
    ...
  ]
  ```

#### Earnings Calendar <code>Premium subscription</code>

An earnings release is an official announcement of a company's financial results that often moves its stock price based on performance. Our API allows you to retrieve a list of upcoming earnings releases, including the release date, earnings call time, EPS forecast, etc. The timezone used for time values is EST (Eastern Standard Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/earnings-calendar?date=2025-10-31`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-10-31 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "XOM",
      "registrant_name": "EXXON MOBIL CORP",
      "fiscal_quarter_end_date": "2025-09",
      "report_date": "2025-10-31",
      "conference_call_time": "2025-10-31 08:30:00",
      "earnings_per_share_forecast": 1.78
    }
    {
      "trading_symbol": "ABBV",
      "registrant_name": "AbbVie Inc.",
      "fiscal_quarter_end_date": "2025-09",
      "report_date": "2025-10-31",
      "conference_call_time": "2025-10-31 08:00:00",
      "earnings_per_share_forecast": 1.79
    },
    ...
  ]
  ```

#### Ipo Calendar <code>Premium subscription</code>

An initial public offering (IPO) marks the first time a private company offers its shares to the public, allowing it to raise capital from investors. The API endpoint allows you to retrieve a list of upcoming initial public offerings and additional information, such as the pricing date, offering value, shares offered, and more.

- ###### Endpoint

  `https://financialdata.net/api/v1/ipo-calendar?date=2025-10-31`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-10-31 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "NAVN",
      "registrant_name": "Navan, Inc.",
      "exchange": "NASDAQ Global Select",
      "pricing_date": "2025-10-31",
      "share_price": 29.9,
      "shares_offered": 36924406,
      "offering_value": 1104039716.0
    },
    {
      "trading_symbol": "NOMA",
      "registrant_name": "Nomadar Corp.",
      "exchange": "NASDAQ Capital",
      "pricing_date": "2025-10-31",
      "share_price": null,
      "shares_offered": 13268718,
      "offering_value": null
    }
  ]
  ```

#### Splits Calendar <code>Premium subscription</code>

A stock split occurs when a company increases its outstanding shares to enhance liquidity, deliberately reducing the share price to make the stock more affordable. Our API provides a list of upcoming stock splits, as well as additional information like the split execution date and multiplier, indicating how many new shares investors will receive per existing share.

- ###### Endpoint

  `https://financialdata.net/api/v1/splits-calendar?date=2025-10-29`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-10-29 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "LINK",
      "registrant_name": "INTERLINK ELECTRONICS INC",
      "execution_date": "2025-10-29",
      "multiplier": 1.5
    },
    {
      "trading_symbol": "NVA",
      "registrant_name": "Nova Minerals Ltd",
      "execution_date": "2025-10-29",
      "multiplier": 5.0
    }
  ]
  ```

#### Dividends Calendar <code>Premium subscription</code>

A dividend is a portion of a company's profits distributed to shareholders, typically paid quarterly in cash or additional shares. This API endpoint allows you to get a list of upcoming dividend payments as well as additional information, like record date, payment date, dividend amount, etc.

- ###### Endpoint

  `https://financialdata.net/api/v1/dividends-calendar?date=2025-10-29`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-10-29 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "APOG",
      "registrant_name": "APOGEE ENTERPRISES, INC.",
      "amount": 0.26,
      "declaration_date": "2025-10-09",
      "ex_date": "2025-10-29",
      "record_date": "2025-10-29",
      "payment_date": "2025-11-13"
    },
    {
      "trading_symbol": "PSEC",
      "registrant_name": "PROSPECT CAPITAL CORP",
      "amount": 0.045,
      "declaration_date": "2025-08-22",
      "ex_date": "2025-10-29",
      "record_date": "2025-10-29",
      "payment_date": "2025-11-18"
    },
    ...
  ]
  ```

#### Economic Calendar <code>Premium subscription</code>

Get a schedule of upcoming economic events and major indicator announcements, including Gross Domestic Product (GDP), Consumer Price Index (CPI), unemployment rate, retail sales, etc. Details include event time, country, and previous and actual indicator values. The timezone used for time values is EST (Eastern Standard Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/economic-calendar?date=2025-10-19`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-10-19 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "event_name": "GDP Y/Y (Q3)",
      "country": "CHINA",
      "country_code": "CN",
      "time": "2025-10-19 21:00:00",
      "previous_value": 5.2,
      "actual_value": 4.8
    },
    {
      "event_name": "GDP Q/Q SA (Q3)",
      "country": "CHINA",
      "country_code": "CN",
      "time": "2025-10-19 21:00:00",
      "previous_value": 1.1,
      "actual_value": 1.1
    },
    ...
  ]
  ```

#### Insider Transactions <code>Premium subscription</code>

Federal securities laws require insiders, including officials, directors, and those holding more than 10% of a company's securities, to report their purchases, sales, and holdings. The API endpoint gives comprehensive information about each of the transactions. The data is available for a few thousand US companies. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/insider-transactions?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "insider_name": "Numoto Takeshi",
      "insider_central_index_key": "0001899931",
      "relationship_to_issuer": "EVP, Chief Marketing Officer",
      "is_derivatives_transaction": false,
      "title_of_security": "Common Stock",
      "transaction_date": "2024-12-04",
      "transaction_code": "S",
      "transaction_description": "Open market or private sale of non-derivative or derivative security",
      "amount_of_securities": 2000,
      "price_per_security": 437.317,
      "acquired_or_disposed": "D",
      "title_of_underlying_security": null,
      "amount_of_underlying_securities": null,
      "securities_owned_following_transaction": 51851,
      "ownership_form": "D",
      "nature_of_indirect_ownership": null
    },
    ...
  ]
  ```

#### Proposed Sales <code>Premium subscription</code>

When an executive officer, director, or affiliate of a company places an order to sell its stock within a three-month period in which the sale exceeds 5,000 shares or the aggregate sales price exceeds $50,000, the order must be reported to the US Securities and Exchange Commission. Our API provides comprehensive information for each of these transactions. The data is available for a few thousand US companies. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/proposed-sales?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "seller_name": "Althoff Judson",
      "relationship_to_issuer": "Officer",
      "title_of_security": "Common",
      "broker_name": "Fidelity Brokerage Services LLC",
      "amount_of_securities_to_be_sold": 25000,
      "market_value": 10425000.0,
      "amount_of_securities_outstanding": 7434880776,
      "approximate_date_of_sale": "2024-11-22",
      "exchange": "NASDAQ",
      "acquisition_period_start": "2023-08-30",
      "acquisition_period_end": "2023-08-31",
      "nature_of_acquisition_transaction": "Restricted Stock Vesting",
      "names_of_persons_from_whom_acquired": "Issuer"
    },
    ...
  ]
  ```

#### Senate Trading <code>Premium subscription</code>

Members of the United States Senate are required to disclose any purchase, sale, or exchange of a stock, bond, commodity future, or other security when the transaction exceeds $1,000. The API endpoint provides detailed data about each of the transactions made. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/senate-trading?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "name_of_reporting_person": "Thomas H Tuberville",
      "type_of_reporting_person": "Senator",
      "report_date": "2024-11-15",
      "transaction_number": "5",
      "transaction_type": "Sale (Full)",
      "transaction_date": "2024-10-29",
      "owner_type": "Joint",
      "trading_symbol": "MSFT",
      "asset_name": "Microsoft Corporation - Common Stock",
      "asset_type": "Stock",
      "amount": "$15,001 - $50,000",
      "comment": null
    },
    {
      "name_of_reporting_person": "Shelley M Capito",
      "type_of_reporting_person": "Senator",
      "report_date": "2024-10-05",
      "transaction_number": "4",
      "transaction_type": "Sale (Partial)",
      "transaction_date": "2024-09-20",
      "owner_type": "Spouse",
      "trading_symbol": "MSFT",
      "asset_name": "Microsoft Corp",
      "asset_type": "Stock",
      "amount": "$1,001 - $15,000",
      "comment": null
    },
    ...
  ]
  ```

#### House Trading <code>Premium subscription</code>

Members of the US House of Representatives are obliged to disclose any transactions involving stocks, bonds, commodities futures, or other securities worth more than $1,000. The API endpoint provides comprehensive data about each transaction completed. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/house-trading?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "name_of_reporting_person": "Marjorie Taylor Mrs Greene",
      "report_date": "2024-11-27",
      "state": "GA14",
      "transaction_number": "13",
      "transaction_type": "Purchase",
      "transaction_date": "2024-11-25",
      "owner_type": null,
      "trading_symbol": "MSFT",
      "asset_name": "Microsoft Corporation - Common Stock",
      "asset_type": "Stocks (including ADRs)",
      "amount": "$1,001 - $15,000",
      "notification_date": "2024-11-26"
    },
    {
      "name_of_reporting_person": "Josh Gottheimer",
      "report_date": "2024-11-06",
      "state": "NJ05",
      "transaction_number": "28",
      "transaction_type": "Sale (Partial)",
      "transaction_date": "2024-10-03",
      "owner_type": "Joint",
      "trading_symbol": "MSFT",
      "asset_name": "Microsoft Corporation - Common Stock",
      "asset_type": "Stocks (including ADRs)",
      "amount": "$1,001 - $15,000",
      "notification_date": "2024-11-05"
    },
    ...
  ]
  ```

#### Institutional Investors <code>Premium subscription</code>

An institutional investor is a company or organization that invests money on behalf of other people. Mutual funds, pensions, and insurance firms are among the examples. Our API provides a list of institutional investors that have invested at least $100 million. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/institutional-investors`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "central_index_key": "0000702007",
      "registrant_name": " CALDWELL SUTTER CAPITAL, INC."
    },
    {
      "central_index_key": "0000315189",
      "registrant_name": " DEERE & CO"
    },
    {
      "central_index_key": "0002011427",
      "registrant_name": " FOGEL CAPITAL MANAGEMENT, INC."
    },
    ...
  ]
  ```

#### Institutional Holdings <code>Premium subscription</code>

Institutional holdings are the securities in an investment portfolio owned by investment or pension funds, insurance companies, investment firms, or other large organizations that manage funds on behalf of others. The API endpoint provides data on institutional investors with holdings of at least $100 million. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/institutional-holdings?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol or CUSIP number of a security, or the institutional investor's central index key. The latter is assigned to the investor by the US Securities and Exchange Commission. | MSFT, 594918104, 0001067983 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "investor_name": "ASSET PLANNING CORPORATION",
      "central_index_key": "0000007773",
      "period_of_report": "2024-09-30",
      "issuer_name": "MICROSOFT CORP",
      "trading_symbol": "MSFT",
      "cusip_number": "594918104",
      "title_of_security": "COM",
      "market_value": 1401566.0,
      "amount_of_securities": 3257,
      "price_per_security": 430.324224746699,
      "shares_or_principal": "SH",
      "put_or_call": "N/A",
      "investment_discretion": "SOLE",
      "portfolio_weight": 0.00914628336823397
    },
    ...
  ]
  ```

#### Institutional Portfolio Statistics <code>Premium subscription</code>

The API endpoint provides statistics about an institutional investor's portfolio. It gives information on how many securities the investor currently holds, the portfolio's worth, the rate of return, and other valuable information. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/institutional-portfolio-statistics?identifier=0000102909`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The institutional investor's central index key. The latter is assigned to the investor by the US Securities and Exchange Commission. | 0000102909 |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "investor_name": "VANGUARD GROUP INC",
      "central_index_key": "0000102909",
      "period_of_report": "2024-09-30",
      "portfolio_size": 4350,
      "added_securities": 100,
      "removed_securities": 163,
      "portfolio_value": 5584478889704.0,
      "sales_value": 15140587732.0,
      "purchases_value": 16120894488.0,
      "change_in_portfolio_value": 378921068541.0,
      "percentage_change_in_portfolio_value": 7.27916357014633,
      "portfolio_turnover": 0.280640152350018,
      "period_return": 239362343762.767,
      "period_rate_of_return": 4.59820737730832,
      "annual_return": 961687486225.572,
      "annual_rate_of_return": 23.6231073944963,
      "return_since_inception": 43869374603244.0,
      "rate_of_return_since_inception": 4607.04844618722
    },
    ...
  ]
  ```

#### Etf Quotes <code>Premium subscription</code>

Get real-time exchange-traded fund (ETF) quotes, including the last price, change, and percentage change. The data covers several thousand major ETFs. The timezone used for time values is EST (Eastern Standard Time). There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/etf-quotes?identifiers=SPY,QQQ`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifiers | string | The trading symbols for the ETFs. | SPY,QQQ |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SPY",
      "description": "SPDR S&P 500 ETF Trust",
      "time": "2025-09-02 15:59:30",
      "price": 642.41,
      "change": 2.14,
      "percentage_change": 0.33
    },
    {
      "trading_symbol": "QQQ",
      "description": "Invesco QQQ Trust Series I",
      "time": "2025-09-02 15:59:21",
      "price": 568.12,
      "change": 2.5,
      "percentage_change": 0.44
    }
  ]
  ```

#### Etf Prices <code>Premium subscription</code>

An exchange-traded fund (ETF) is a type of investment fund that trades on the stock exchange. ETFs own financial assets such as stocks, bonds, currencies, futures contracts, or commodities. Our API provides more than 10 years of end-of-day historical prices and volumes for major exchange-traded funds. There is a limit of 300 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/etf-prices?identifier=SPY`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for an ETF. | SPY |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 300 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "SPY",
      "date": "2024-12-03",
      "open": 603.39,
      "high": 604.16,
      "low": 602.341,
      "close": 603.91,
      "volume": 26906630.0
    },
    {
      "trading_symbol": "SPY",
      "date": "2024-12-02",
      "open": 602.97,
      "high": 604.32,
      "low": 602.47,
      "close": 603.63,
      "volume": 31745990.0
    },
    ...
  ]
  ```

#### Etf Holdings <code>Premium subscription</code>

An exchange-traded fund (ETF) is an investment fund holding a collection of assets that trades on the stock exchange just like an individual share. Our API provides information on the securities held by exchange-traded funds. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/etf-holdings?identifier=SPY`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol of an exchange-traded fund. | SPY |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "central_index_key": "0000884394",
      "registrant_name": "SPDR S&P 500 ETF TRUST",
      "period_of_report": "2025-06-30",
      "etf_name": "SPDR S&P 500 ETF TRUST",
      "etf_symbol": "SPY",
      "series_id": "N/A",
      "class_id": "N/A",
      "issuer_name": "Johnson & Johnson",
      "lei_number": "549300G0CFPGEF6X2043",
      "title_of_security": "Johnson & Johnson",
      "trading_symbol": "JNJ",
      "cusip_number": "478160104",
      "isin_number": "US4781601046",
      "amount_of_units": 29181009,
      "description_of_units": "NS",
      "denomination_currency": "USD",
      "value_in_usd": 4457399124.75,
      "percentage_value_compared_to_assets": 0.699985772661,
      "payoff_profile": "Long",
      "asset_type": "EC",
      "issuer_type": "CORP",
      "country_of_issuer_or_investment": "US",
      "is_restricted_security": false,
      "fair_value_level": 1,
      "is_cash_collateral": false,
      "is_non_cash_collateral": false,
      "is_loan_by_fund": false
    },
    ...
  ]
  ```

#### Mutual Fund Symbols <code>Premium subscription</code>

A mutual fund is an investment fund that pools money from multiple investors to buy securities. Mutual funds are not traded on stock exchanges but can be purchased and sold through brokerage firms or fund companies. This API endpoint returns a few thousand fund symbols, along with additional information. There is a limit of 500 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/mutual-fund-symbols`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 500 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "AAAAX",
      "fund_name": "DWS RREEF Real Assets Fund, Class A"
    },
    {
      "trading_symbol": "AAAEX",
      "fund_name": "Virtus KAR Health Sciences Fund, P"
    },
    {
      "trading_symbol": "AAAIX",
      "fund_name": "STRATEGIC ALLOCATION: AGGRESSIVE FUND, I CLASS"
    },
    ...
  ]
  ```

#### Mutual Fund Holdings <code>Premium subscription</code>

A mutual fund is an investment fund that pools money from numerous investors to purchase securities. Mutual funds are not traded on stock exchanges, but they can be bought and sold through brokerage firms or fund companies. Our API provides information on the securities held by mutual funds. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/mutual-fund-holdings?identifier=VTSAX`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol of a mutual fund. | VTSAX |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "central_index_key": "0000036405",
      "registrant_name": "VANGUARD INDEX FUNDS",
      "period_of_report": "2025-06-30",
      "fund_name": "Admiral Shares",
      "fund_symbol": "VTSAX",
      "series_id": "S000002848",
      "class_id": "C000007806",
      "issuer_name": "Frequency Electronics Inc",
      "lei_number": "549300S56SO2JB5JBE31",
      "title_of_security": "FREQUENCY ELECT",
      "trading_symbol": "FEIM",
      "cusip_number": "358010106",
      "isin_number": "US3580101067",
      "amount_of_units": 228179,
      "description_of_units": "NS",
      "denomination_currency": "USD",
      "value_in_usd": 5181945.09,
      "percentage_value_compared_to_assets": 0.000271384232,
      "payoff_profile": "Long",
      "asset_type": "EC",
      "issuer_type": "CORP",
      "country_of_issuer_or_investment": "US",
      "is_restricted_security": false,
      "fair_value_level": 1,
      "is_cash_collateral": false,
      "is_non_cash_collateral": false,
      "is_loan_by_fund": true
    },
    ...
  ]
  ```

#### Mutual Fund Statistics <code>Premium subscription</code>

The API endpoint provides statistics about mutual funds. It gives essential information about fund assets, liabilities, returns, realized gains, and so on. There is a limit of 50 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/mutual-fund-statistics?identifier=VTSAX`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol of a mutual fund. | VTSAX |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 50 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "central_index_key": "0000036405",
      "registrant_name": "VANGUARD INDEX FUNDS",
      "period_of_report": "2025-06-30",
      "fund_name": "Admiral Shares",
      "fund_symbol": "VTSAX",
      "series_id": "S000002848",
      "class_id": "C000007806",
      "total_assets": 1915212703487.01,
      "total_liabilities": 5763123365.99,
      "net_assets": 1909449580121.02,
      "return_preceding_month1": -0.6729,
      "return_preceding_month2": 6.3455,
      "return_preceding_month3": 5.07574,
      "realized_gain_preceding_month1": 983065935.64,
      "change_in_unrealized_appreciation_preceding_month1": -11394591977.19,
      "realized_gain_preceding_month2": 287029511.93,
      "change_in_unrealized_appreciation_preceding_month2": 105734824564.66,
      "realized_gain_preceding_month3": 2243886605.76,
      "change_in_unrealized_appreciation_preceding_month3": 87596494350.2,
      "share_sale_preceding_month1": 30533447572.6504,
      "share_redemption_preceding_month1": 9354960674.63,
      "share_sale_preceding_month2": 9024030148.45996,
      "share_redemption_preceding_month2": 9833704993.95,
      "share_sale_preceding_month3": 12681244786.0796,
      "share_redemption_preceding_month3": 12999259996.1
    },
    ...
  ]
  ```

#### Esg Scores <code>Premium subscription</code>

ESG risk score measures a company's exposure to environmental, social, and corporate governance risks in its daily operations. The score is calculated on a numerical scale ranging from 0 (low risk) to 100 (high risk). The API endpoint returns historical ESG risk score values for several thousand US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/esg-scores?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "industry": "Software & Services",
      "date": "2025-02-01",
      "environmental_risk_score": 1.6,
      "social_risk_score": 7.6,
      "governance_risk_score": 4.2,
      "esg_risk_score": 13.5
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "industry": "Software & Services",
      "date": "2025-01-01",
      "environmental_risk_score": 1.6,
      "social_risk_score": 7.6,
      "governance_risk_score": 5.0,
      "esg_risk_score": 14.2
    },
    ...
  ]
  ```

#### Esg Ratings <code>Premium subscription</code>

ESG corporate rating is a metric used for evaluating a company's sustainability performance; ratings range from D- (poor performance) to A+ (excellent performance). ESG industry rank shows how a company's ESG risk score compares to that of other companies in the same industry. The API endpoint provides ratings for publicly traded US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/esg-ratings?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "industry": "Software & Services",
      "date": "2025-02-01",
      "esg_corporate_rating": "A",
      "esg_industry_rank": "10 out of 143"
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "industry": "Software & Services",
      "date": "2025-01-01",
      "esg_corporate_rating": "A",
      "esg_industry_rank": "15 out of 143"
    },
    ...
  ]
  ```

#### Industry Esg Scores <code>Premium subscription</code>

Industry ESG score evaluates how well an industry manages risks related to ESG (environmental, social, and governance) factors. The score is calculated on a numerical scale ranging from 0 (low risk) to 100 (high risk).

- ###### Endpoint

  `https://financialdata.net/api/v1/industry-esg-scores?date=2025-01-01`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | date | string | The date in YYYY-MM-DD format. | 2025-01-01 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "industry": "Aerospace & Defense",
      "date": "2025-01-01",
      "environmental_risk_score": 9.0,
      "social_risk_score": 14.8,
      "governance_risk_score": 6.2,
      "esg_risk_score": 30.1
    },
    {
      "industry": "Auto Components",
      "date": "2025-01-01",
      "environmental_risk_score": 4.0,
      "social_risk_score": 5.8,
      "governance_risk_score": 5.0,
      "esg_risk_score": 14.7
    },
    ...
  ]
  ```

#### Investment Adviser Names <code>Premium subscription</code>

Investment advisers are financial specialists who give investment advice or conduct security analyses for a fee. In the United States, they must register with the Securities and Exchange Commission if they handle $25 million or more in client assets. The API endpoint returns the legal names of over 15,000 registered investment advisers. There is a limit of 1000 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/investment-adviser-names`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 1000 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "legal_name": "&PARTNERS"
    },
    {
      "legal_name": "1 NORTH WEALTH SERVICES, LLC"
    },
    {
      "legal_name": "1 ROUNDTABLE PARTNERS LLC"
    },
    ...
  ]
  ```

#### Investment Adviser Information <code>Premium subscription</code>

Our API provides valuable information about registered investment advisers, including the value of assets under management, number of accounts, contact details, etc. The data covers over 15,000 registered investment advisers, with most of them managing $25 million or more in client assets.

- ###### Endpoint

  `https://financialdata.net/api/v1/investment-adviser-information?identifier=BLACKROCK INVESTMENT MANAGEMENT, LLC`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The legal name of an investment adviser. | BLACKROCK INVESTMENT MANAGEMENT, LLC |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "legal_name": "BLACKROCK INVESTMENT MANAGEMENT, LLC",
      "primary_business_name": "BLACKROCK INVESTMENT MANAGEMENT, LLC",
      "central_index_key": null,
      "lei_number": "5493006MRTEZZ4S4CQ20",
      "form_of_business": "Limited Liability Company",
      "fiscal_year_end": "December",
      "state_of_incorporation": "DE",
      "country_of_incorporation": "United States",
      "office_address": "1 UNIVERSITY SQUARE DRIVE, PRINCETON, NJ 08540, UNITED STATES",
      "office_phone_number": "609 282 2000",
      "website": "https://www.blackrock.com",
      "number_of_employees": 1483,
      "assets_under_management": 458191510749.0,
      "number_of_accounts": 46332
    }
  ]
  ```

#### Earnings Releases <code>Standard subscription</code>

An earnings release is an official public announcement revealing a company's profitability during a specific time period. It affects the share price, which rises or falls in response to the company's performance. Our API provides extensive information on the release, including actual and predicted earnings, release timing, and so on.

- ###### Endpoint

  `https://financialdata.net/api/v1/earnings-releases?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "market_cap": 3089118613620.0,
      "fiscal_quarter_end_date": "2024-09",
      "earnings_per_share": 3.3,
      "earnings_per_share_forecast": 3.08,
      "percentage_surprise": 7.14,
      "number_of_forecasts": 16,
      "conference_call_time": "2024-10-30 18:30:00"
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "market_cap": 3069639225987.0,
      "fiscal_quarter_end_date": "2024-06",
      "earnings_per_share": 2.95,
      "earnings_per_share_forecast": 2.9,
      "percentage_surprise": 1.72,
      "number_of_forecasts": 15,
      "conference_call_time": "2024-07-30 18:30:00"
    },
    ...
  ]
  ```

#### Initial Public Offerings <code>Standard subscription</code>

An initial public offering (IPO) is when shares of a private firm are made available to the public for the first time. It enables a company to raise equity capital from public investors. The API endpoint provides more than 10 years of data on all initial public offerings.

- ###### Endpoint

  `https://financialdata.net/api/v1/initial-public-offerings?identifier=ABNB`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | ABNB |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "ABNB",
      "registrant_name": "Airbnb, Inc.",
      "exchange": "NASDAQ Global Select",
      "pricing_date": "2020-12-10",
      "share_price": 68.0,
      "shares_offered": 51323531,
      "offering_value": 3490000108.0
    }
  ]
  ```

#### Stock Splits <code>Standard subscription</code>

A stock split occurs when a company increases the number of outstanding shares to improve the stock's liquidity. A company decides to do a stock split to intentionally lower the price of a single share, making the company's stock more affordable. Our API provides stock split data for several thousand US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/stock-splits?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security, or the central index key (CIK). The latter is assigned to the entity by the United States Securities and Exchange Commission. | MSFT, 0000789019 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "execution_date": "2003-02-18",
      "multiplier": 2.0
    },
    {
      "trading_symbol": "MSFT",
      "central_index_key": "0000789019",
      "registrant_name": "MICROSOFT CORP",
      "execution_date": "1999-03-29",
      "multiplier": 2.0
    },
    ...
  ]
  ```

#### Dividends <code>Standard subscription</code>

A dividend is the distribution of a company's earnings to its shareholders. Dividends are paid out quarterly and may be in the form of cash or reinvestment in additional stock. The API endpoint provides dividend information for several thousands of US and international companies.

- ###### Endpoint

  `https://financialdata.net/api/v1/dividends?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "registrant_name": "MICROSOFT CORP",
      "type": "Cash",
      "amount": 0.83,
      "declaration_date": "2024-12-03",
      "ex_date": "2025-02-20",
      "record_date": "2025-02-20",
      "payment_date": "2025-03-13"
    },
    {
      "trading_symbol": "MSFT",
      "registrant_name": "MICROSOFT CORP",
      "type": "Cash",
      "amount": 0.83,
      "declaration_date": "2024-09-16",
      "ex_date": "2024-11-21",
      "record_date": "2024-11-21",
      "payment_date": "2024-12-12"
    },
    ...
  ]
  ```

#### Short Interest <code>Standard subscription</code>

Short interest represents the number of shares of a company that are currently sold short and have not yet been covered. The short interest ratio, also known as days to cover, represents the number of days it would take for all short-sold shares to be covered or repurchased in the market. Our API provides short interest data for over 15,000 securities. There is a limit of 100 records per API call.

- ###### Endpoint

  `https://financialdata.net/api/v1/short-interest?identifier=MSFT`
- ###### Parameters

  | Name | Type | Description | Example |
  | --- | --- | --- | --- |
  | identifier | string | The trading symbol for a security. | MSFT |
  | offset | integer | (Optional) The initial position of the record subset, which indicates how many records to skip. Defaults to 0. | 100 |
  | format | string | (Optional) The format of the returned data, either JSON (JavaScript Object Notation) or CSV (Comma Separated Values). Defaults to JSON. | json, csv |
- ###### Response

  ```json
  [
    {
      "trading_symbol": "MSFT",
      "title_of_security": "Microsoft Corporation Common S",
      "market_code": "NNM",
      "settlement_date": "2024-11-15",
      "shorted_securities": 56018482,
      "previous_shorted_securities": 62516096,
      "change_in_shorted_securities": -6497614,
      "percentage_change_in_shorted_securities": -10.39,
      "average_daily_volume": 22446377,
      "days_to_cover": 2.5,
      "is_stock_split": false
    },
    {
      "trading_symbol": "MSFT",
      "title_of_security": "Microsoft Corporation Common S",
      "market_code": "NNM",
      "settlement_date": "2024-10-31",
      "shorted_securities": 62516096,
      "previous_shorted_securities": 60313798,
      "change_in_shorted_securities": 2202298,
      "percentage_change_in_shorted_securities": 3.65,
      "average_daily_volume": 20959345,
      "days_to_cover": 2.98,
      "is_stock_split": false
    },
    ...
  ]
  ```
