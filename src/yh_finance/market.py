import requests


def get_quotes(region: str, symbols: str, api_key: str):
    """
    Get live price quotes.

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param symbols: One or more comma seperated ticker symbols.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-quotes"
    querystring = {"region": region, "symbols": symbols}
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
    querystring = {"region": region, "lang": lang, "count": count, "start": start}
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
    querystring = {"region": region}
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
    querystring = {"region": region, "startDate": start_date, "endDate": end_date, "size": size}
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

    :return: An API Key from YH Finance API.
    """
    url = "https://yh-finance.p.rapidapi.com/market/get-trending-tickers"
    querystring = {"region": region}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_popular_watchlists(api_key: str):
    url = "https://yh-finance.p.rapidapi.com/market/get-popular-watchlists"
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    response = requests.request("GET", url, headers=headers).json()

    return response



