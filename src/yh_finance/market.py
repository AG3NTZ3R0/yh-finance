import requests


def get_quotes(region: str, symbols: str, api_key: str):
    """
    Get live price quotes.

    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param symbols: One or more comma seperated ticker symbols.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON
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
    :param lang: One of the following: en-US, pt-BR, en-AU, en-CA, fr-FR, de-DE, zh-Hant-HK, en-IN, it-IT, es-ES,
    en-GB, en-SG.
    :param count: The number of items per response for paging purpose (max 25).
    :param api_key: An API Key from YH Finance API.
    :param start: The starting offset for paging purpose.

    :return: API response in JSON
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

    :return: API response in JSON
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-summary"
    querystring = {"region": region}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
