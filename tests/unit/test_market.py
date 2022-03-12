import os
import unittest

from src.yh_finance.market import *


class TestMarketEndpoints(unittest.TestCase):
    def test_get_quotes(self):
        """
        Test that it is communicating with the YH Finance API.
        """
        json_resp = get_quotes(region='US',
                               symbols='AMD,IBM,AAPL',
                               api_key=os.environ.get('YH_FINANCE_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_movers(self):
        """
        Test that it is communicating with the YH Finance API.
        """
        json_resp = get_movers(region='US',
                               lang='en-US',
                               count=5,
                               api_key=os.environ.get('YH_FINANCE_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
