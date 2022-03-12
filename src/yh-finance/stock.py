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
    querystring = {
        "symbol": symbol
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_upgrades_downgrades(symbol: str, region: str, api_key: str):
    """
    Get upgrade and downgrade data.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-upgrades-downgrades"
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


def get_chart(interval: str, symbol: str, time_range: str, region: str, include_pre_post: bool, use_yahoo_id: bool,
              include_adj_close: bool, events: str, api_key: str):
    """
    Get data to draw full screen chart.

    :param interval: One of the following: 1m, 2m, 5m, 15m, 30m, 60m, 1d, 1wk, 1mo.
    :param symbol: The symbol to get data for.
    :param time_range: One of the following: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param include_pre_post: Whether to include pre post.
    :param use_yahoo_id: Whether to use yahoo finance ID.
    :param include_adj_close: Whether to include adjust close.
    :param events: One of the following: capitalGain, div, split, earn, history. Separated by commas for multiple events.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-chart"
    querystring = {
        "interval": interval,
        "symbol": symbol,
        "range": time_range,
        "region": region,
        "includePrePost": include_pre_post,
        "useYfid": use_yahoo_id,
        "includeAdjustedClose": include_adj_close,
        "events": events
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_statistics(symbol: str, api_key: str):
    """
    Get data in statistics section.

    :param symbol: The symbol to get data for.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-statistics"
    querystring = {
        "symbol": symbol
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
