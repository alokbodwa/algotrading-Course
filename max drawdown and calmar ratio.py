# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 01:19:00 2022

@author: alokb
"""

import yfinance as yf
import pandas as pd
import numpy as np

stocks = ["RELIANCE.NS", "BAJFINANCE.NS", "EDELWEISS.NS", "AMZN"]
ohlcv_data = {}

    
for ticker in stocks:
    temp = yf.download(ticker, period="7mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp
    
def CAGR(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    #252 is the total no of trading days in a year, since we r working with daily data, we are taking total trading days
    n = len(df)/252  #gives the fraction of years we have traded, the CAGR formula uses the years
    CAGR = (df["cum_return"][-1])**(1/n) - 1
    return CAGR

    
def maxDD(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    df["cum_rolling_max"] = df["cum_return"].cummax()
    #df["cum_rolling_min"] = df["cum_return"].cummin()
    df["drowdown"] = df["cum_rolling_max"] - df["cum_return"]
    maxDrawdownPct = (df["drowdown"]/df["cum_rolling_max"]).max()
    return maxDrawdownPct

#Good calmar ratio is from 3
#It indicates you can generate 3x times return on the risk you are taking
def calmarRatio(DF):
    df = DF.copy()
    return CAGR(df)/maxDD(df)

for ticker in ohlcv_data:
    print("max drawDown of {} is {}".format(ticker, maxDD(ohlcv_data[ticker])))
    print("Calmar Ratio of {} is {}".format(ticker, calmarRatio(ohlcv_data[ticker])))
