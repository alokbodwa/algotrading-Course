# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 00:02:16 2022

@author: alokb
"""

import yfinance as yf
import pandas as pd
from stocktrends import Renko

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}
hour_data = {}
renko_data = {}

    
for ticker in stocks:
    temp = yf.download(ticker, period="1mo", interval="15m")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp
    temp = yf.download(ticker, period="1y", interval="1h")
    temp.dropna(how="any", inplace=True)
    hour_data[ticker] = temp
    
def ATRcalc(DF, a = 14):
    df = DF.copy()
    df["H-L"] = df["High"]-df["Low"]
    df["H-PC"] = df["High"]-df["Adj Close"].shift(1)
    df["L-PC"] = df["Low"]-df["Adj Close"].shift(1)
    
    df["TR"] = df[["H-L", "H-PC", "L-PC"]].max(axis=1, skipna=False)
    df["ATR"] = df["TR"].ewm(span=a, min_periods=a).mean()
    return df["ATR"];


def renko_calc(DF, hourly_df):
    df = DF.copy()
    hourly_df_copy = hourly_df.copy()
    df.drop('Close', axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    df2 = Renko(df)
    df2.brick_size = 3 * round(ATRcalc(hourly_df, 120).iloc[-1], 0)
    renko_df = df2.get_ohlc_data()
    return renko_df

for ticker in ohlcv_data:
    # uptrend = true means green bricks and false means red bricks
    ohlcv_data[ticker] = renko_calc(ohlcv_data[ticker], hour_data[ticker])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    