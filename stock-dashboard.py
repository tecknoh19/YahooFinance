#!/usr/bin/env python

'''
stock-dashboard.py
Author: tecknoh19
Description: Create a price graph image for a given ticker symbel and date range
'''

import warnings, sys
import matplotlib.pyplot as plt
from yahoo_fin.stock_info import get_data, get_quote_table, get_live_price

def get_stock_price(ticker):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            price = get_live_price(ticker)
        return price
    except Exception as e:
        return None

def get_historical_prices(ticker, start_date, end_date):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            data = get_data(ticker, start_date=start_date, end_date=end_date)
        return data
    except Exception as e:
        return None

def get_financial_metrics(ticker):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            metrics = get_quote_table(ticker)
        return metrics
    except Exception as e:
        return None

def plot_historical_prices(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data["close"], label="Close Price", color="blue")
    plt.title("Historical Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

def main():
    ticker = input("Enter the ticker symbol of the stock: ").upper()
    
    # Fetch latest stock price
    price = get_stock_price(ticker)
    if price is not None:
        print(f"The current price of {ticker} is ${price:.2f}")
    else:
        print("Error: Unable to fetch stock price. Please check the ticker symbol.")
        sys.exit()
    
    # Fetch historical prices
    start_date = input("Enter start date (YYYY-MM-DD) for historical data: ")
    end_date = input("Enter end date (YYYY-MM-DD) for historical data: ")
    historical_data = get_historical_prices(ticker, start_date, end_date)
    if historical_data is not None:
        plot_historical_prices(historical_data)
    else:
        print("Error: Unable to fetch historical data.")
        sys.exit()
    
   

if __name__ == "__main__":
    main()
