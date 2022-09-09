# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:17:07 2021

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
    
# filling NaN values
#cl_price.fillna({ "FB": 0, "GOOGL": "1"})  #this does not changes the actual dataset. Run this line only using fn + F9
cl_price.fillna(method='bfill',axis=0,inplace=True) #backfill ; inplace changes the data in original dataframe


#dropping NaN values, if any value in vertical axis is NaN, just drop it
cl_price.dropna(axis=0,how='any')

cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()
cl_price.head(10)
cl_price.tail()


daily_change = cl_price.pct_change()

# cl_price.shift(1) # shifts the entire dataFrame by 1; you may pass -ve values ie -3, -4 etc
cl_price/cl_price.shift(1) - 1 # equivalent to pct_change()

daily_change.mean()
daily_change.std()
daily_change.describe()








