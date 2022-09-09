# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 03:03:29 2022

@author: alokb
"""

import yfinance as yf
import pandas as pd
import numpy as np

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}

    
for ticker in stocks:
    temp = yf.download("BAJFINANCE.NS", period="7mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp
    
def volatility(DF) :
    df = temp.copy()
    df["return"] = df["Adj Close"].pct_change()
    vol = (df["return"].std()) * np.sqrt(252)
    return vol

for ticker in ohlcv_data:
    print("the volatility of {} is {}".format(ticker, volatility(ohlcv_data[ticker])))