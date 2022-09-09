# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:47:42 2021

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
    
def MACDfunc(DF, a=12, b=26, c=9):
    df = DF.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
    df["ma_slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span=c, min_periods=c).mean()
    return df.loc[:, ["macd", "signal"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][["MACD", "SIGNAL"]] = MACDfunc(ohlcv_data[ticker], a=12, b=26, c=9)
    ohlcv_data[ticker].loc[:,["MACD", "SIGNAL"]].plot()
    
    