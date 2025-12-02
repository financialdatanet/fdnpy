import os
import unittest
from typing import List, Dict, Callable, Any
from fdnpy import FinancialDataClient

class TestFinancialDataClient(unittest.TestCase): 

    test_kwargs = {'stock_quotes': {'identifiers': ['AAPL', 'MSFT']},
                   'stock_prices': {'identifier': 'MSFT'},
                   'international_stock_prices': {'identifier': 'SHEL.L'},
                   'minute_prices': {'identifier': 'MSFT', 'date': '2020-01-15'},
                   'latest_prices': {'identifier': 'MSFT'},
                   'commodity_prices': {'identifier': 'ZC'},
                   'otc_prices': {'identifier': 'AABB'},
                   'otc_volume': {'identifier': 'AABB'},
                   'index_quotes': {'identifiers': ['^GSPC', '^DJI']},
                   'index_prices': {'identifier': '^GSPC'},
                   'index_constituents': {'identifier': '^GSPC'},
                   'option_chain' : {'identifier': 'MSFT'},
                   'option_prices': {'identifier': 'MSFT250417C00400000'},
                   'option_greeks': {'identifier': 'MSFT250417C00400000'},
                   'futures_prices': {'identifier': 'ZN'},
                   'crypto_information': {'identifier': 'BTC'},
                   'crypto_quotes': {'identifiers': ['BTCUSD', 'ETHUSD']},
                   'crypto_prices': {'identifier': 'BTCUSD'},
                   'crypto_minute_prices': {'identifier': 'BTCUSD', 'date': '2025-01-15'},
                   'company_information': {'identifier': 'MSFT'},
                   'international_company_information': {'identifier': 'SHEL.L'},
                   'key_metrics': {'identifier': 'MSFT'},
                   'market_cap': {'identifier': 'MSFT'},
                   'employee_count': {'identifier': 'MSFT'},
                   'executive_compensation': {'identifier': 'MSFT'},
                   'securities_information': {'identifier': 'MSFT'},
                   'income_statements': {'identifier': 'MSFT', 'period': 'year'},
                   'balance_sheet_statements': {'identifier': 'MSFT', 'period': 'year'},
                   'cash_flow_statements': {'identifier': 'MSFT', 'period': 'year'},
                   'international_income_statements': {'identifier': 'SHEL.L', 'period': 'year'},
                   'international_balance_sheet_statements': {'identifier': 'SHEL.L', 'period': 'year'},
                   'international_cash_flow_statements': {'identifier': 'SHEL.L', 'period': 'year'},
                   'liquidity_ratios': {'identifier': 'MSFT', 'period': 'year'},
                   'solvency_ratios': {'identifier': 'MSFT', 'period': 'year'},
                   'efficiency_ratios': {'identifier': 'MSFT', 'period': 'year'},
                   'profitability_ratios': {'identifier': 'MSFT', 'period': 'year'},
                   'valuation_ratios': {'identifier': 'MSFT', 'period': 'year'},
                   'earnings_calendar': {'date': '2025-10-31'},
                   'ipo_calendar': {'date': '2025-10-31'},
                   'splits_calendar': {'date': '2025-10-29'},
                   'dividends_calendar': {'date': '2025-10-29'},
                   'economic_calendar': {'date': '2025-10-19'},
                   'insider_transactions': {'identifier': 'MSFT'},
                   'proposed_sales': {'identifier': 'MSFT'},
                   'senate_trading': {'identifier': 'MSFT'},
                   'house_trading': {'identifier': 'MSFT'},
                   'institutional_holdings': {'identifier': 'MSFT'},
                   'institutional_portfolio_statistics': {'identifier': '0000102909'},
                   'etf_quotes': {'identifiers': ['SPY', 'QQQ']},
                   'etf_prices': {'identifier': 'SPY'},
                   'etf_holdings': {'identifier': 'SPY'},
                   'mutual_fund_holdings': {'identifier': 'VTSAX'},
                   'mutual_fund_statistics': {'identifier': 'VTSAX'},
                   'esg_scores': {'identifier': 'MSFT'},
                   'esg_ratings': {'identifier': 'MSFT'},
                   'industry_esg_scores': {'date': '2025-01-01'},
                   'investment_adviser_information': {'identifier': 'BLACKROCK INVESTMENT MANAGEMENT, LLC'},
                   'earnings_releases': {'identifier': 'MSFT'},
                   'initial_public_offerings': {'identifier': 'ABNB'},
                   'stock_splits': {'identifier': 'MSFT'},
                   'dividends': {'identifier': 'MSFT'},
                   'short_interest': {'identifier': 'MSFT'}}
    
    @classmethod
    def get_method_names(cls) -> List[str]:
       
        method_names = []
        for name in dir(FinancialDataClient):
           if not name.startswith('__') and name not in ['make_request', 'get_data']:
              attr = getattr(FinancialDataClient, name)
              if callable(attr):
                  method_names.append(name)

        assert len(method_names) == 73

        return sorted(method_names)

    @classmethod
    def create_test_method(cls, method_name: str) -> Callable:
        
        def test(self):
            
            key = method_name.split('_', 1)[1]
            kwargs = self.test_kwargs.get(key, {})          
            print('Testing %s with kwargs: %s' % (method_name, kwargs))
            
            try:
                method = getattr(self.client, method_name)
                result = method(**kwargs)               
                self.assertIsInstance(result, list, 'Result for %s is not a list' % method_name)
                
                if result:
                    self.assertIsInstance(result[0], dict, 'Elements in %s result are not dictionaries' % method_name)
                    print('SUCCESS: %s returned %d records' % (method_name, len(result)))
                else:
                    self.fail('%s returned an empty list' % method_name)
                    
            except Exception as e:
                self.fail('Unexpected exception for %s: %s' % (method_name, e))

        test.__name__ = 'test_%s' % method_name
        return test

    @classmethod
    def initialize(cls):

        api_key = os.environ.get('FINANCIAL_DATA_API_KEY', None)
        if api_key is None:
            unittest.SkipTest('API key not set, skipping tests')
        
        cls.client = FinancialDataClient(api_key=api_key)
        method_names = cls.get_method_names()
        
        for method_name in method_names:
            test_method = cls.create_test_method(method_name)
            setattr(cls, test_method.__name__, test_method)

TestFinancialDataClient.initialize()
if __name__ == '__main__':
    print('Starting API Tests...')
    unittest.main()

