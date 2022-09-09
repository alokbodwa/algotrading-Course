# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:31:05 2021

@author: alokb

Link to the blog referenced in the lecture video:

https://pbpython.com/effective-matplotlib.html


Matplotlib Tutorial:

https://matplotlib.org/tutorials/introductory/lifecycle.html
"""

import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AMZN","MSFT","FB","GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe which will be filled with closing prices of each stock

# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    
    
cl_price.fillna(method='bfill',axis=0,inplace=True)

daily_change = cl_price.pct_change()


fig, ax = plt.subplots()
plt.style.available
plt.style.use('ggplot')
ax.set(title="mean daily return of stock", xlabel="stock_name", ylabel="mean return")
plt.bar(x=daily_change.columns, height=daily_change.mean())
# ax.set(title="standar Deviation of returns of stock", xlabel="stock_name", ylabel="std deviation return")
# plt.bar(x=daily_change.columns, height=daily_change.std())
