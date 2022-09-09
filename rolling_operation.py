# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:29:30 2021

@author: alokb
"""


import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","FB","GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe which will be filled with closing prices of each stock

# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    
    
cl_price.fillna(method='bfill',axis=0,inplace=True)

daily_change = cl_price.pct_change()

daily_change.rolling(window=10).mean()
daily_change.rolling(window=10).std()
daily_change.rolling(window=10).max()
daily_change.rolling(window=10).sum()

daily_change.ewm(com=10, min_periods=10).mean()









