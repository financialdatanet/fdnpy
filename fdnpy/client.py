import sys
import time
import requests
from datetime import timedelta
from typing import List, Dict, Any

class FinancialDataClient:

    def __init__(self, api_key: str) -> Any:

        self.base_url = 'https://financialdata.net/api/v1/'
        self.api_key = api_key
        self.session = requests.Session()

    def make_request(self, endpoint: str, params: Dict[str, Any]) -> List[Dict]:
  
        params['key'] = self.api_key
        url = self.base_url + endpoint

        backoff = 1
        while 1:
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                return response.json()

            except Exception as e:
                if response.status_code in [429, 500, 503]:
                    print('%s\nRetrying after %s' % (e, timedelta(seconds=backoff)))
                    time.sleep(backoff)
                    backoff *= 2
                else:
                    raise e

    def get_data(self, endpoint: str, params: Dict[str, Any] = None, limit: int = sys.maxsize) -> List[Dict]:

        params = params or {}
        params['offset'] = 0

        data = []
        while 1:
            partial_data = self.make_request(endpoint, params)
            data.extend(partial_data)
            count = len(partial_data)

            if count < limit:
                break
            else:
                params['offset'] += limit

        return data 

    # ==========================================
    # Symbol Lists
    # ==========================================

    def get_stock_symbols(self) -> List[Dict]:

        return self.get_data('stock-symbols', limit=500)

    def get_international_stock_symbols(self) -> List[Dict]:

        return self.get_data('international-stock-symbols', limit=500)

    def get_etf_symbols(self) -> List[Dict]:

        return self.get_data('etf-symbols', limit=500)

    def get_commodity_symbols(self) -> List[Dict]:

        return self.get_data('commodity-symbols')

    def get_otc_symbols(self) -> List[Dict]:

        return self.get_data('otc-symbols', limit=500)

    # ==========================================
    # Market Data
    # ==========================================

    def get_stock_quotes(self, identifiers: List[str]) -> List[Dict]:

        params = {'identifiers': ','.join(identifiers)}
        return self.get_data('stock-quotes', params=params, limit=300)

    def get_stock_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('stock-prices', params=params, limit=300)

    def get_international_stock_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('international-stock-prices', params=params, limit=300)

    def get_minute_prices(self, identifier: str, date: str) -> List[Dict]:

        params = {'identifier': identifier, 'date': date}
        return self.get_data('minute-prices', params=params, limit=300)

    def get_latest_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('latest-prices', params=params, limit=300)

    def get_commodity_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('commodity-prices', params=params, limit=300)

    def get_otc_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('otc-prices', params=params, limit=300)

    def get_otc_volume(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('otc-volume', params=params)

    # ==========================================
    # Market Indexes
    # ==========================================

    def get_index_symbols(self) -> List[Dict]:

        return self.get_data('index-symbols')

    def get_index_quotes(self, identifiers: List[str]) -> List[Dict]:

        params = {'identifiers': ','.join(identifiers)}
        return self.get_data('index-quotes', params=params, limit=300)

    def get_index_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('index-prices', params=params, limit=300)

    def get_index_constituents(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('index-constituents', params=params, limit=300)

    # ==========================================
    # Derivatives Data
    # ==========================================

    def get_option_chain(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('option-chain', params=params, limit=300)

    def get_option_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('option-prices', params=params, limit=300)

    def get_option_greeks(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('option-greeks', params=params, limit=300)

    def get_futures_symbols(self) -> List[Dict]:

        return self.get_data('futures-symbols', limit=500)

    def get_futures_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('futures-prices', params=params, limit=300)

    # ==========================================
    # Crypto Currencies
    # ==========================================

    def get_crypto_symbols(self) -> List[Dict]:

        return self.get_data('crypto-symbols', limit=500)

    def get_crypto_information(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('crypto-information', params=params)

    def get_crypto_quotes(self, identifiers: List[str]) -> List[Dict]:

        params = {'identifiers': ','.join(identifiers)}
        return self.get_data('crypto-quotes', params=params, limit=300)

    def get_crypto_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('crypto-prices', params=params, limit=300)

    def get_crypto_minute_prices(self, identifier: str, date: str) -> List[Dict]:

        params = {'identifier': identifier, 'date': date}
        return self.get_data('crypto-minute-prices', params=params, limit=300)

    # ==========================================
    # Forex Data
    # ==========================================

    def get_forex_symbols(self) -> List[Dict]:

        return self.get_data('forex-symbols')

    def get_forex_quotes(self, identifiers: List[str]) -> List[Dict]:

        params = {'identifiers': ','.join(identifiers)}
        return self.get_data('forex-quotes', params=params, limit=300)

    def get_forex_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('forex-prices', params=params, limit=300)

    def get_forex_minute_prices(self, identifier: str, date: str) -> List[Dict]:

        params = {'identifier': identifier, 'date': date}
        return self.get_data('forex-minute-prices', params=params, limit=300)

    # ==========================================
    # Basic Information
    # ==========================================

    def get_company_information(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('company-information', params=params)

    def get_international_company_information(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('international-company-information', params=params)

    def get_key_metrics(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('key-metrics', params=params)

    def get_market_cap(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('market-cap', params=params)

    def get_employee_count(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('employee-count', params=params)

    def get_executive_compensation(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('executive-compensation', params=params, limit=100)

    def get_securities_information(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('securities-information', params=params)

    # ==========================================
    # Financial Statements
    # ==========================================

    def get_income_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('income-statements', params=params, limit=50)

    def get_balance_sheet_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('balance-sheet-statements', params=params, limit=50)

    def get_cash_flow_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('cash-flow-statements', params=params, limit=50)

    def get_international_income_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('international-income-statements', params=params, limit=50)

    def get_international_balance_sheet_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('international-balance-sheet-statements', params=params, limit=50)

    def get_international_cash_flow_statements(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('international-cash-flow-statements', params=params, limit=50)

    # ==========================================
    # Financial Ratios
    # ==========================================

    def get_liquidity_ratios(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('liquidity-ratios', params=params, limit=50)

    def get_solvency_ratios(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('solvency-ratios', params=params, limit=50)

    def get_efficiency_ratios(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('efficiency-ratios', params=params, limit=50)

    def get_profitability_ratios(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('profitability-ratios', params=params, limit=50)

    def get_valuation_ratios(self, identifier: str, period: str = None) -> List[Dict]:

        params = {'identifier': identifier} if period is None else {'identifier': identifier, 'period': period}
        return self.get_data('valuation-ratios', params=params, limit=50)

    # ==========================================
    # Event Calendars
    # ==========================================

    def get_earnings_calendar(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('earnings-calendar', params=params, limit=300)

    def get_ipo_calendar(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('ipo-calendar', params=params)

    def get_splits_calendar(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('splits-calendar', params=params)

    def get_dividends_calendar(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('dividends-calendar', params=params)

    def get_economic_calendar(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('economic-calendar', params=params, limit=300)

    # ==========================================
    # Insider Trading
    # ==========================================

    def get_insider_transactions(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('insider-transactions', params=params, limit=50)

    def get_proposed_sales(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('proposed-sales', params=params, limit=100)

    def get_senate_trading(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('senate-trading', params=params, limit=100)

    def get_house_trading(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('house-trading', params=params, limit=100)

    # ==========================================
    # Institutional Trading
    # ==========================================

    def get_institutional_investors(self) -> List[Dict]:

        return self.get_data('institutional-investors', limit=500)

    def get_institutional_holdings(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('institutional-holdings', params=params, limit=100)

    def get_institutional_portfolio_statistics(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('institutional-portfolio-statistics', params=params, limit=50)

    # ==========================================
    # ETF Data
    # ==========================================

    def get_etf_quotes(self, identifiers: List[str]) -> List[Dict]:

        params = {'identifiers': ','.join(identifiers)}
        return self.get_data('etf-quotes', params=params, limit=300)

    def get_etf_prices(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('etf-prices', params=params, limit=300)

    def get_etf_holdings(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('etf-holdings', params=params, limit=50)

    # ==========================================
    # Mutual Funds
    # ==========================================

    def get_mutual_fund_symbols(self) -> List[Dict]:

        return self.get_data('mutual-fund-symbols', limit=500)

    def get_mutual_fund_holdings(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('mutual-fund-holdings', params=params, limit=50)

    def get_mutual_fund_statistics(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('mutual-fund-statistics', params=params, limit=50)

    # ==========================================
    # ESG Data
    # ==========================================

    def get_esg_scores(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('esg-scores', params=params)

    def get_esg_ratings(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('esg-ratings', params=params)

    def get_industry_esg_scores(self, date: str) -> List[Dict]:

        params = {'date': date}
        return self.get_data('industry-esg-scores', params=params)

    # ==========================================
    # Investment Advisers
    # ==========================================

    def get_investment_adviser_names(self) -> List[Dict]:

        return self.get_data('investment-adviser-names', limit=1000)

    def get_investment_adviser_information(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('investment-adviser-information', params=params)

    # ==========================================
    # Miscellaneous Data
    # ==========================================

    def get_earnings_releases(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('earnings-releases', params=params)

    def get_initial_public_offerings(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('initial-public-offerings', params=params)

    def get_stock_splits(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('stock-splits', params=params)

    def get_dividends(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('dividends', params=params)

    def get_short_interest(self, identifier: str) -> List[Dict]:

        params = {'identifier': identifier}
        return self.get_data('short-interest', params=params, limit=100)