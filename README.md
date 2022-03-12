# yh_finance

A Python package that wraps YH Finance API endpoints and returns financial data in JSON format. The API queries markets, stocks, news and conversations on Yahoo! Finance in real time to streamline the development of financial applications.

<table><tr><td>

#### IMPORTANT LEGAL DISCLAIMER

---

yh-finance is **not** affiliated, endorsed, or vetted by Yahoo, Inc. It is
an open-source tool that uses a publicly available API and is
intended for research and educational purposes.
</td></tr></table>

## Install

```shell
pip install yh_finance
```

## [Subscribe to YH Finance API](https://rapidapi.com/apidojo/api/yh-finance/ 'YH Finance API')

## Tutorial

```python
import yh_finance as yhf
```

### Default

```python
json_resp = yhf.auto_complete(query='tesla', 
                              region='US', 
                              api_key='YOUR_API_KEY')
```

### Market

```python
json_resp = yhf.get_quotes(region='US',
                           symbols='AMD,IBM,AAPL',
                           api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_movers(region='US',
                           lang='en-US',
                           count=5,
                           api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_summary(region='US',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_spark(symbols='AMZN,AAPL,WDC,REYN,AZN',
                          interval='1m',
                          time_range='1d',
                          api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_earnings(region='US',
                             start_date='1585155600000',
                             end_date='1589475600000',
                             size=10,
                             api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_trending_tickers(region='US',
                                     api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_popular_watchlists(api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_watchlist_performance(user_id='X3NJ2A7VDSABUI4URBWME2PZNM',
                                          portfolio_id='the_berkshire_hathaway_portfolio',
                                          symbols='^GSPC',
                                          region='US',
                                          api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_watchlist_detail(user_id='X3NJ2A7VDSABUI4URBWME2PZNM',
                                     portfolio_id='the_berkshire_hathaway_portfolio',
                                     api_key='YOUR_API_KEY')
```

### Stock

```python
json_resp = yhf.get_summary(symbol='AMRN',
                            region='US',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_recommendation(symbol='INTC',
                                   api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_upgrades_downgrades(symbol='INTC',
                                        region='US',
                                        api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_chart(interval='1mo',
                          symbol='AMRN',
                          time_range='1y',
                          region='US',
                          include_pre_post='false',
                          use_yahoo_id='true',
                          include_adj_close='true',
                          events='capitalGain,div,split',
                          api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_statistics(symbol='JD',
                               api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_historical_data(symbol='AMRN',
                                    region='US',
                                    api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_profile(symbol='AMRN',
                            region='US',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_financials(symbol='AMRN',
                               region='US',
                               api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_timeseries(symbol='AMRN',
                               start_date='493578000',
                               end_date='1625011200',
                               region='US',
                               api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_cash_flow(symbol='AMRN',
                              region='US',
                              api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_balance_sheet(symbol='AMRN',
                                  region='US',
                                  api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_analysis(symbol='AMRN',
                             region='US',
                             api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_options(symbol='AMRN',
                            date='1562284800',
                            region='US',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_holders(symbol='AMRN',
                            region='US',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_holings(symbol='AMRN',
                            api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_insights(symbol='AAPL',
                             api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_insider_transactions(symbol='AMRN',
                                         region='US',
                                         api_key='YOUR_API_KEY')
```

```python
json_resp = yhf.get_insider_roster(symbol='AMRN',
                                   region='US',
                                   api_key='YOUR_API_KEY')
```

### Conversation

```python
json_resp = yhf.get_conversation_list(symbol='AAPL',
                                      message_board_id='finmb_24937',
                                      region='US',
                                      user_activity='true',
                                      sort_by='createdAt',
                                      off='0')
```
