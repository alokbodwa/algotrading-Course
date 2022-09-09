# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:40:46 2022

@author: alokb
"""

import yfinance as yf
allDetails = yf.Ticker("BAJFINANCE.NS")
infi = allDetails.info
print(f"Market Cap : {allDetails.info['marketCap']}\n")
print(f"Employees : {allDetails.info['fullTimeEmployees']}\n")
print(f"Business Summary : \n{allDetails.info['longBusinessSummary']}")
pd = allDetails.history(period='12mo')

# determining the name of the file
file_name = 'PriceData.xlsx'
  
# saving the excel
pd.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
