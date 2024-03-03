import os
import unittest

from src.yh_finance.stock import *


class TestStockEndpoints(unittest.TestCase):
    def test_get_summary(self):
        """
        Test that the get_summary function is communicating with the YH Finance API.
        """
        json_resp = get_summary(symbol='AMRN',
                                region='US',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_recommendations(self):
        """
        Test that the get_recommendations function is communicating with the YH Finance API.
        """
        json_resp = get_recommendations(symbol='INTC',
                                        api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_upgrades_downgrades(self):
        """
        Test that the get_upgrades_downgrades function is communicating with the YH Finance API.
        """
        json_resp = get_upgrades_downgrades(symbol='INTC',
                                            region='US',
                                            api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_chart(self):
        """
        Test that the get_chart function is communicating with the YH Finance API.
        """
        json_resp = get_chart(interval='1mo',
                              symbol='AMRN',
                              time_range='1y',
                              region='US',
                              include_pre_post='false',
                              use_yahoo_id='true',
                              include_adj_close='true',
                              events='capitalGain,div,split',
                              api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_statistics(self):
        """
        Test that the get_statistics function is communicating with the YH Finance API.
        """
        json_resp = get_statistics(symbol='JD',
                                   api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_historical(self):
        """
        Test that the get_historical function is communicating with the YH Finance API.
        """
        json_resp = get_historical_data(symbol='AMRN',
                                        region='US',
                                        api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_profile(self):
        """
        Test that the get_profile function is communicating with the YH Finance API.
        """
        json_resp = get_profile(symbol='AMRN',
                                region='US',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_financials(self):
        """
        Test that the get_financials function is communicating with the YH Finance API.
        """
        json_resp = get_financials(symbol='AMRN',
                                   region='US',
                                   api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_timeseries(self):
        """
        Test that the get_timeseries function is communicating with the YH Finance API.
        """
        json_resp = get_timeseries(symbol='AMRN',
                                   start_date='493578000',
                                   end_date='1625011200',
                                   region='US',
                                   api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_cash_flow(self):
        """
        Test that the get_cash_flow function is communicating with the YH Finance API.
        """
        json_resp = get_cash_flow(symbol='AMRN',
                                  region='US',
                                  api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_balance_sheet(self):
        """
        Test that the get_balance_sheet function is communicating with the YH Finance API.
        """
        json_resp = get_balance_sheet(symbol='AMRN',
                                      region='US',
                                      api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_analysis(self):
        """
        Test that the get_analysis function is communicating with the YH Finance API.
        """
        json_resp = get_analysis(symbol='AMRN',
                                 region='US',
                                 api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_options(self):
        """
        Test that the get_options function is communicating with the YH Finance API.
        """
        json_resp = get_options(symbol='AMRN',
                                date='1562284800',
                                region='US',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_holders(self):
        """
        Test that the get_holders function is communicating with the YH Finance API.
        """
        json_resp = get_holders(symbol='AMRN',
                                region='US',
                                api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_holdings(self):
        """
        Test that the get_holdings function is communicating with the YH Finance API.
        """
        json_resp = get_holdings(symbol='AMRN',
                                 api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_insights(self):
        """
        Test that the get_insights function is communicating with the YH Finance API.
        """
        json_resp = get_insights(symbol='AAPL',
                                 api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_insider_transactions(self):
        """
        Test that the get_insider_transactions function is communicating with the YH Finance API.
        """
        json_resp = get_insider_transactions(symbol='AMRN',
                                             region='US',
                                             api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)

    def test_get_insider_roster(self):
        """
        Test that the get_insider_roster function is communicating with the YH Finance API.
        """
        json_resp = get_insider_roster(symbol='AMRN',
                                       region='US',
                                       api_key=os.environ.get('RAPID_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
