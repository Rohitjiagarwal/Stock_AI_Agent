import yfinance as yf
from datetime import datetime
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')


# 1. Function to fetch stock data
def fetch_stock_data(symbol):
    data = yf.Ticker(symbol).history(period="5d")
    return data

# 2. Function to analyze heuristics
def analyze_heuristics(data):
    latest = data.iloc[-1]
    previous = data.iloc[-2]

    today_close = latest['Close']
    today_open = latest['Open']
    yesterday_close = previous['Close']
    volume_today = latest['Volume']
    avg_volume = data['Volume'].mean()
    ma_5 = data['Close'].mean()

    prediction = ""

    # Heuristic 1: Close > Open
    if today_close > today_open:
        prediction += "✔ Today bullish (close > open). "

    else:
        prediction += "✘ Today bearish (close < open). "

    # Heuristic 2: Today close > Yesterday close
    if today_close > yesterday_close:
        prediction += "✔ Price is trending up. "
    else:
        prediction += "✘ Price is trending down. "

    # Heuristic 3: Volume unusually high
    if volume_today > avg_volume * 1.2:
        prediction += "⚠ High volume — activity spike. "

    # Heuristic 4: Above 5-day moving average
    if today_close > ma_5:
        prediction += "✔ Above 5-day average (strong). "
    else:
        prediction += "✘ Below 5-day average (weak). "

    return prediction


# 3. Function to print summary + heuristic analysis
def print_summary(symbol):
    data = fetch_stock_data(symbol)
    latest = data.iloc[-1]

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

    # Heuristic prediction
    prediction = analyze_heuristics(data)
    print("Prediction:", prediction)
    print("------------------------------------------")


# 4. Stocks to track
stocks = ["AAPL", "MSFT", "GOOGL"]

print("Starting Stock Agent with Heuristics... (Press CTRL+C to stop)")

while True:
    for s in stocks:
        print_summary(s)

    print("\nWaiting 60 seconds before next update...")
    time.sleep(60)
