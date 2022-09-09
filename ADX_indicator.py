# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 23:04:01 2022

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
    
def ATRcalc(DF, a = 14):
    df = DF.copy()
    df["H-L"] = df["High"]-df["Low"]
    df["H-PC"] = df["High"]-df["Adj Close"].shift(1)
    df["L-PC"] = df["Low"]-df["Adj Close"].shift(1)
    
    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(span=a, min_periods=a).mean()
    return df["ATR"];


def ADX(DF, n=20):
    df = DF.copy()
    df["ATR"] = ATRcalc(df, n)
    df["upMove"] = df["High"]-df["High"].shift(1)
    df["downMove"] = df["Low"].shift(1)-df["Low"]
    df["+dm"] = np.where( (df["upMove"]>df["downMove"]) & (df["upMove"] > 0), df["upMove"], 0)
    df["-dm"] = np.where( (df["downMove"]>df["upMove"]) & (df["downMove"] > 0), df["downMove"], 0)
    df["+di"] = 100* (df["+dm"]/df["ATR"]).ewm(span=n, min_periods=n).mean()
    df["-di"] = 100* (df["-dm"]/df["ATR"]).ewm(span=n, min_periods=n).mean()
    df["ADX"] = 100 * abs((df["+di"]-df["-di"])/(df["+di"]+df["-di"])).ewm(span=n, min_periods=n).mean()
    return df["ADX"]


for ticker in ohlcv_data :
    ohlcv_data[ticker]["ADX"] = ADX(ohlcv_data[ticker])












    
    