import os
import unittest

from src.yh_finance.market import *


class TestMarketEndpoints(unittest.TestCase):
    def test_get_quotes(self):
        """
        Test that the get_quotes function is communicating with the YH Finance API.
        """
        json_resp = get_quotes(region='US',
                               symbols='AMD,IBM,AAPL',
                               api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_movers(self):
        """
        Test that the get_movers function is communicating with the YH Finance API.
        """
        json_resp = get_movers(region='US',
                               lang='en-US',
                               count=5,
                               api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_summary(self):
        """
        Test that the get_summary function is communicating with the YH Finance API.
        """
        json_resp = get_summary(region='US',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_spark(self):
        """
        Test that the get_spark function is communicating with the YH Finance API.
        """
        json_resp = get_spark(symbols='AMZN,AAPL,WDC,REYN,AZN',
                              interval='1m',
                              time_range='1d',
                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_earnings(self):
        """
        Test that the get_earnings function is communicating with the YH Finance API.
        """
        json_resp = get_earnings(region='US',
                                 start_date='1585155600000',
                                 end_date='1589475600000',
                                 size=10,
                                 api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_trending_tickers(self):
        """
        Test that the get_trending_tickers function is communicating with the YH Finance API.
        """
        json_resp = get_trending_tickers(region='US',
                                         api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_popular_watchlists(self):
        """
        Test that the get_popular_watchlists function is communicating with the YH Finance API.
        """
        json_resp = get_popular_watchlists(api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_watchlist_performance(self):
        """
        Test that the get_watchlist_performance function is communicating with the YH Finance API.
        """
        json_resp = get_watchlist_performance(user_id='X3NJ2A7VDSABUI4URBWME2PZNM',
                                              portfolio_id='the_berkshire_hathaway_portfolio',
                                              symbols='^GSPC',
                                              region='US',
                                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_watchlist_detail(self):
        """
        Test that the get_watchlist_detail function is communicating with the YH Finance API.
        """
        json_resp = get_watchlist_detail(user_id='X3NJ2A7VDSABUI4URBWME2PZNM',
                                         portfolio_id='the_berkshire_hathaway_portfolio',
                                         api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
