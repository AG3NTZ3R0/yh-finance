import requests


def get_summary(symbol: str, region: str, api_key: str):
    """
    Get data in summary section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"
    querystring = {
        "symbol": symbol,
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_recommendations(symbol: str, api_key: str):
    """
    Get symbols similar to the specified one.

    :param symbol: The symbol to get data for.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-recommendations"
    querystring = {"symbol": symbol}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
