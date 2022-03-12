import os
import unittest

from src.yh_finance.default import *


class TestDefaultEndpoints(unittest.TestCase):
    def test_auto_complete(self):
        """
        Test that the auto_complete function is communicating with the YH Finance API.
        """
        json_resp = auto_complete(query='tesla',
                                  region='US',
                                  api_key=os.environ.get('YH_FINANCE_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
