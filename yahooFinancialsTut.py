# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:11:59 2021

@author: alokb
"""

from yahoofinancials import YahooFinancials

ticker = 'EDELWEISS.NS'
yahoo_financials = YahooFinancials(ticker)

data = yahoo_financials.get_historical_price_data('2020-12-09', '2021-12-09', "daily")