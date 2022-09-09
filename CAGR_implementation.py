# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 02:38:19 2022

@author: alokb
"""

import yfinance as yf
import pandas as pd

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}

    
for ticker in stocks:
    temp = yf.download("AMZN", period="7mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp


def CAGR(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    #252 is the total no of trading days in a year, since we r working with daily data, we are taking total trading days
    n = len(df)/252  #gives the fraction of years we have traded, the CAGR formula uses the years
    CAGR = (df["cum_return"][-1])**n - 1
    return CAGR

for ticker in ohlcv_data:
    print("The Stock {} generated a return of {}".format(ticker, CAGR(ohlcv_data[ticker])))


