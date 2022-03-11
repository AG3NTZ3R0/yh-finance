import requests


def get_quotes(region: str, symbols: str, api_key: str):
    """
    Get live price quotes.

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param symbols: The symbol to get data, separated by comma to get data for multiple symbols.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-quotes"
    querystring = {
        "region": region,
        "symbols": symbols
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_movers(region: str, lang: str, count: int, api_key: str, start: int = 0):
    """
    The live day gainers, losers, and actives in a specific region.

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param lang: One of the following: en-US, pt-BR, en-AU, en-CA, fr-FR, de-DE, zh-Hant-HK, en-IN, it-IT, es-ES, en-GB, en-SG.
    :param count: The number of items per response for paging purpose (Max 25).
    :param api_key: An API Key from YH Finance API.
    :param start: The starting offset for paging purpose.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-movers"
    querystring = {
        "region": region,
        "lang": lang,
        "count": count,
        "start": start
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_summary(region: str, api_key: str):
    """
    Get live summary information of market by region.

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-summary"
    querystring = {
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_spark(symbols: str, interval: str, time_range: str, api_key: str):
    """
    Used with get_trending_tickers endpoint together to draw brief chart.

    :param symbols: The symbol to get data, separated by comma to get data for multiple symbols.
    :param interval: One of the following: 5m, 15m, 1d, 1wk, 1mo.
    :param time_range: One of the following: 1d, 5d, 3mo, 6mo, 1y, 5y, max.
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-spark"
    querystring = {
        "symbols": symbols,
        "interval": interval,
        "range": time_range
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_earnings(region: str, start_date: str, end_date: str, size: int, api_key: str):
    """
    Get recent earnings in the market.

    :param region: region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param start_date: Unix timestamps in milliseconds. The value must be different from end_date and the value must be the start of a day to get all the data from the day. The interval between start and end date is up to 14 days.
    :param end_date: Unix timestamps in milliseconds. The value must be different from start_date and the value must be the start of the later day to get all the data in the previous days. The interval between start and end date is up to 14 days.
    :param size: The number of items returned (Max 100).
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-earnings"
    querystring = {
        "region": region,
        "startDate": start_date,
        "endDate": end_date,
        "size": size
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_trending_tickers(region: str, api_key: str):
    """
    Get latest trending tickers in the market (Count 20).

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-trending-tickers"
    querystring = {
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_popular_watchlists(api_key: str):
    """
    Get popular watchlists in the market.

    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-popular-watchlists"
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    response = requests.request("GET", url, headers=headers).json()

    return response


def get_watchlist_performance(user_id: str, portfolio_id: str, symbols: str, region: str, api_key: str):
    """
    Get performance information of specific watchlist.

    :param user_id: The value of userId field returned in get_popular_watchlists endpoint.
    :param portfolio_id: The value of pfId field returned in get_popular_watchlists endpoint.
    :param symbols: The value of symbol field returned in auto_complete endpoint, separated by commas for multiple entities.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-watchlist-performance"
    querystring = {
        "userId": user_id,
        "pfId": portfolio_id,
        "symbols": symbols,
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_watchlist_detail(user_id: str, portfolio_id: str, api_key: str):
    """
    Get detail information of specific watchlist.

    :param user_id: The value of userId field returned in get_popular_watchlists endpoint.
    :param portfolio_id: The value of pfId field returned in get_popular_watchlists endpoint.
    :param api_key: An API Key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-watchlist-detail"
    querystring = {
        "userId": user_id,
        "pfId": portfolio_id
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
