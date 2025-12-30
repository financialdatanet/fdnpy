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