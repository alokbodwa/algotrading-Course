# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:57:51 2021

@author: alokb
"""

import yfinance as yf
import pandas as pd

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}

    
for ticker in stocks:
    temp = yf.download(ticker, period="1mo", interval="15m")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp
    

def ATRcalc(DF, a = 14):
    df = DF.copy()
    df["H-L"] = df["High"]-df["Low"]
    df["H-PC"] = df["High"]-df["Adj Close"].shift(1)
    df["L-PC"] = df["Low"]-df["Adj Close"].shift(1)
    
    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(span=a, min_periods=a).mean()
    return df["ATR"];

for ticker in ohlcv_data:
    ohlcv_data[ticker]["ATR"] = ATRcalc(ohlcv_data[ticker])
    
    