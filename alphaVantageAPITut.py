# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:25:45 2021

@author: alokb
"""

# BWQYTRPPEGIL1CX2 - API key

# importing libraries
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key_path = "A:\\Courses\\Udemy\\Algo Trading - Mayank Basu\\Algo Trading\\alphaVantageAPI.txt"

# extracting data for a single ticker
ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
#outputsize can be compact or full. 'full' means more than 5000 data, 'compact' means 100 data
data = ts.get_daily(symbol='MSFT', outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]
#reverse the data
data = data.iloc[::-1]


# extracting stock data (historical close price) for multiple stocks
all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG"]
close_prices = pd.DataFrame()
api_call_count = 1
#ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
start_time = time.time()
for ticker in all_tickers:
    data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')[0]
    api_call_count+=1
    data.columns = ["open","high","low","close","volume"]
    data = data.iloc[::-1]
    close_prices[ticker] = data["close"]
    if api_call_count==5:
        api_call_count = 1
        time.sleep(60 - ((time.time() - start_time) % 60.0))

'''
# extracting ohlcv data for multiple stocks
all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG",
               "FB","BA","MMM","XOM","NKE","INTC"]
ohlv_dict = {}
api_call_count = 1
ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
start_time = time.time()
for ticker in all_tickers:
    data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='compact')[0]
    api_call_count+=1
    data.columns = ["open","high","low","close","volume"]
    data = data.iloc[::-1]
    ohlv_dict[ticker] = data
    if api_call_count==5:
        api_call_count = 1
        time.sleep(60 - ((time.time() - start_time) % 60.0))
'''