import yfinance as yf
import pandas as pd

def load_data(ticker_names, start=None, end=None, period=None):
    data = yf.download(' '.join(ticker_names), start=start, end=end, period=period)[['Close']]
    data.columns = data.columns.droplevel()

    return data