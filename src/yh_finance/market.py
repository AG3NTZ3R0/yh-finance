import requests


def get_quotes(symbols: str, api_key: str, region: str):
    """
    Get live price quotes.

    :param symbols: One or more comma seperated ticker symbols.
    :param api_key: An API key from YH Finance API.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.

    :return: JSON API Response
    """
    url = "https://yh-finance.p.rapidapi.com/market/v2/get-quotes"
    querystring = {"region": region, "symbols": symbols}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
