import os
import unittest

from src.yh_finance.conversation import *


class TestGetConversationList(unittest.TestCase):
    def test_json_resp(self):
        """
        Test that it is communicating with the YH Finance API.
        """
        json_resp = get_conversation_list(symbol='AAPL',
                                          message_board_id='finmb_24937',
                                          region='US',
                                          user_activity='true',
                                          sort_by='createdAt',
                                          off='0',
                                          api_key=os.environ.get('YH_FINANCE_API_KEY'))
        self.assertEqual(type(json_resp), dict)


if __name__ == '__main__':
    unittest.main()
