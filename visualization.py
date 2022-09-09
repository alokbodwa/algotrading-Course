# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:07:13 2021

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

cl_price.plot(subplots=True, layout=(2, 2), title="Stock Price Variation Chart", grid=True)

daily_change.plot(subplots=True, layout=(2, 2), grid=True)

# cumprod return the cumulative product of each element. This is what you do in compounding.
# this chart gives a fair idea of the overall x factor return over the given time period
(1+daily_change).cumprod().plot()