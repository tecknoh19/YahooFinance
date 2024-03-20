#!/usr/bin/env python

'''
get-live-price.py
Author: tecknoh19
Description: A simple example to get live stock prices
'''

from yahoo_fin.stock_info import get_live_price

def get_stock_price(ticker):
    try:
        price = get_live_price(ticker)
        return price
    except Exception as e:
        return None

def main():
    ticker = input("Enter the ticker symbol of the stock: ").upper()
    price = get_stock_price(ticker)
    if price is not None:
        print(f"The current price of {ticker} is ${price:.2f}")
    else:
        print("Error: Unable to fetch stock price. Please check the ticker symbol.")

if __name__ == "__main__":
    main()
