# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:55:36 2021

@author: alokb
"""

import yfinance as yf
import pandas as pd
import numpy as np

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}

    
for ticker in stocks:
    temp = yf.download(ticker, period="1mo", interval="15m")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp
    
    
def RSI(DF, a=14):
    df = DF.copy()
    df["change"] = df["Adj Close"]-df["Adj Close"].shift(1)
    df["gain"] = np.where(df["change"]>=0, df["change"], 0)
    df["loss"] = np.where(df["change"]<0, -1*df["change"], 0)
    
    df["avg_gain"] = df["gain"].ewm(alpha=1/a, min_periods=a).mean()
    df["avg_loss"] = df["loss"].ewm(alpha=1/a, min_periods=a).mean()
    
    df["RS"] = df["avg_gain"]/df["avg_loss"]
    df["RSI"] = 100 - (100/(1+df["RS"]))
    return df["RSI"]

for ticker in ohlcv_data:
    ohlcv_data[ticker]["RSI"] = RSI(ohlcv_data[ticker])