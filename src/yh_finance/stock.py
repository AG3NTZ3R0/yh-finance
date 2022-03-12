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


def get_chart(interval: str, symbol: str, time_range: str, region: str, include_pre_post: str, use_yahoo_id: str,
              include_adj_close: str, events: str, api_key: str):
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


def get_historical_data(symbol: str, region: str, api_key: str):
    """
    Get data in historical data section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"
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


def get_profile(symbol: str, region: str, api_key: str):
    """
    Get data in profile section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-profile"
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


def get_financials(symbol: str, region: str, api_key: str):
    """
    Get income statement and annual data in financial section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-financials"
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


def get_timeseries(symbol: str, start_date: str, end_date: str, region: str, api_key: str):
    """
    Get quarterly data in financial section.

    :param symbol: The symbol to get data for.
    :param start_date: Epoch timestamp in milliseconds. The value must be different from end_date and the value must be the start of a day to get all the data from the day.
    :param end_date: Epoch timestamp in milliseconds. The value must be different from start_date and the value must be the start of the next day to get all the data from the previous day.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-timeseries"
    querystring = {
        "symbol": symbol,
        "period1": start_date,
        "period2": end_date,
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_cash_flow(symbol: str, region: str, api_key: str):
    """
    Get cash flow data in financial section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-cash-flow"
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


def get_balance_sheet(symbol: str, region: str, api_key: str):
    """
    Get balance sheet data in financial section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-balance-sheet"
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


def get_analysis(symbol: str, region: str, api_key: str):
    """
    Get data in analysis section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-analysis"
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


def get_options(symbol: str, date: str, region: str, api_key: str):
    """
    Get data in options section.

    :param symbol: The symbol to get data for.
    :param date: Epoch timestamp in seconds. The value must be at the start of a day to get all data.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-options"
    querystring = {
        "symbol": symbol,
        "date": date,
        "region": region
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_holders(symbol: str, region: str, api_key: str):
    """
    Get major holders in holders section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-holders"
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


def get_holdings(symbol: str, api_key: str):
    """
    Get data in holdings section. The symbol must be a mutual fund stock.

    :param symbol: The symbol to get data for.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-holdings"
    querystring = {
        "symbol": symbol
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_insights(symbol: str, api_key: str):
    """
    Get brief reports relating to the symbol.

    :param symbol: The symbol to get data for.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-insights"
    querystring = {
        "symbol": symbol
    }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    return response


def get_insider_transactions(symbol: str, region: str, api_key: str):
    """
    Get insider transaction data in the holders section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-insider-transactions"
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


def get_insider_roster(symbol: str, region: str, api_key: str):
    """
    Get insider roster data in the holders section.

    :param symbol: The symbol to get data for.
    :param region: One of the following: US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, SG.
    :param api_key: An API key from YH Finance API.

    :return: API response in JSON.
    """
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-insider-roster"
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
