import os
import unittest

from src.yh_finance.stock import *


class TestStockEndpoints(unittest.TestCase):
    def test_get_summary(self):
        """
        Test that it is communicating with the YH Finance API.
        """