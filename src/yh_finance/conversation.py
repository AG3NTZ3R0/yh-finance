import requests


def get_conversation_list(symbol: str, message_board_id: str, region: str, user_activity: str, sort_by: str, off: str,
                          api_key: str):
    """
    Get conversations list relating to a symbol.

    :param symbol: The symbol to get data for.
    :param message_board_id: The value of messageBoardId field returned in get_quotes.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param user_activity: Whether to return current number of interacting users or not.
    :param sort_by: One of the following: createdBy, popular.
    :param off: The offset to start loading messages, fixed at 10 messages returned per response. Ex : 0 -> 9 -> 19
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/conversations/list"
    querystring = {
        "symbol": symbol,
        "messageBoardId": message_board_id,
        "region": region,
        "userActivity": user_activity,
        "sortBy": sort_by,
        "off": off
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "d73bb60f82mshbe3e55c57b941abp1abe67jsn7d7492f26dee"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
