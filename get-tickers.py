#!/usr/bin/env python

'''
get-tickers.py
Author: tecknoh19
Description: Create a CSV file of all available stock tickers on NASDAQ
'''

import pandas as pd
from yahoo_fin.stock_info import tickers_nasdaq

def get_top_nasdaq_tickers():
    return tickers_nasdaq()

def save_to_csv(tickers, filename):
    df = pd.DataFrame(tickers, columns=["Ticker"])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    top_tickers = get_top_nasdaq_tickers()
    save_to_csv(top_tickers, "nasdaq_tickers.csv")
    print("CSV file saved successfully.")
