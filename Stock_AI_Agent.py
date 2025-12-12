import yfinance as yf
from datetime import datetime
import time

# 1. Function to fetch stock data
def fetch_stock_data(symbol):
    data = yf.Ticker(symbol).history(period="5d")
    return data

# 2. Function to print summary on console
def print_summary(symbol):
    data = fetch_stock_data(symbol)
    latest = data.iloc[-1]   # most recent day's data

    print("\n------------------------------------------")
    print(f"Stock Summary for: {symbol}")
    print("Time:", datetime.now())
    print("------------------------------------------")
    print(f"Open:   {latest['Open']}")
    print(f"High:   {latest['High']}")
    print(f"Low:    {latest['Low']}")
    print(f"Close:  {latest['Close']}")
    print(f"Volume: {latest['Volume']}")
    print("------------------------------------------")

# 3. List of stocks to track
stocks = ["AAPL", "MSFT", "GOOGL"]

# 4. Run at regular intervals
print("Starting Stock Agent... (Press CTRL + C to stop)")

while True:
    for s in stocks:
        print_summary(s)