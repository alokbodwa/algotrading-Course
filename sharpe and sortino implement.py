# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 03:25:37 2022

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
    df = ohlcv_data["RELIANCE.NS"].copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    #252 is the total no of trading days in a year, since we r working with daily data, we are taking total trading days
    n = len(df)/252  #gives the fraction of years we have traded, the CAGR formula uses the years
    CAGR = (df["cum_return"][-1])**n - 1
    return CAGR

def volatility(DF) :
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    vol = (df["return"].std()) * np.sqrt(252)
    return vol

def sharpe(DF) :
    df = DF.copy()
    sharpe_ratio = (CAGR(df) - 0.0725)/volatility(df)
    return sharpe_ratio

'''def sortino(DF):
    df = DF.copy()
    df['daily_return'] = df['Adj Close'].pct_change()
    volatility = df.daily_return[df.daily_return < 0].std() * np.sqrt(365)
    return (cagr(df) - 0.027)/volatility '''

def sortino(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    negative_return = np.where(df["return"]>0, 0, df["return"])
    #delete zeroes - negative_return[negative_return != 0]
    negative_vol = pd.Series(negative_return[negative_return != 0]).std() * np.sqrt(252)
    sortino_ratio = (CAGR(df) - 0.0725)/negative_vol
    return sortino_ratio

for ticker in ohlcv_data:
    print("stock {} has sharpe ratio {} and sortino ratio {}".format(ticker, sharpe(ohlcv_data[ticker]), sortino(ohlcv_data[ticker])))

















