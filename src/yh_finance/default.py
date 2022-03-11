import requests


def auto_complete(query: str, region: str, api_key: str):
    """
    Get auto complete suggestions by term or phrase.

    :param query: Any familiar term or phrase to get auto complete suggestions.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/auto-complete"
    querystring = {"q": query, "region": region}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response
