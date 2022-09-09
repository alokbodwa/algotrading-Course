# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:56:41 2021

@author: alokb
"""

import pandas as pd
import yfinance as yf
import datetime as dt

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()

cl_price = pd.DataFrame()
ohlcv_data = {}

for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)
    

ohlcv_data["AMZN"]["Open"]



    