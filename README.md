📈 Stock AI Agent — Step 1 (With Heuristics)

This project is the first step toward building an automated Stock AI Agent that can fetch real-time market data, analyze trends using heuristics, and generate basic predictions.

This version includes:

Multi-stock tracking (AAPL, MSFT, GOOGL)

Core metrics extraction (OHLC + Volume)

Basic heuristic-based prediction engine

Automated updates every 60 seconds

🚀 Objective

The goal of Step 1 is to build the foundation of the Stock AI Agent:

Fetch stock market data using a public API

Extract daily metrics (Open, High, Low, Close, Volume)

Apply heuristic-based trend analysis

Print the report to console

Run continuously at fixed intervals

This output will later feed into ML-based prediction modules.

🧠 Why These Implementation Choices?
1. Python

Strong ecosystem for financial analysis

Easy integration with data libraries

Highly readable → ideal for interviews and demos

2. yfinance API

Free and easy to use

No API keys required

Widely used for stock research

Perfect for prototyping without rate-limit issues

3. Console-based summary

Quick and clear for demonstrations

No UI overhead in Step 1

4. Loop-based scheduling

Simple while True: loop

Behaves like a background agent

Can be replaced later by cron/APS, serverless jobs

📚 Libraries Used
Library	Purpose
yfinance	Fetch stock market data
datetime	Add timestamps
time	Interval scheduling
sys	UTF-8 log formatting
🔍 Features Included in This Version
✔ Fetch 5-day historical stock data
✔ Extract latest OHLC and Volume
✔ Apply heuristic rules:

Close > Open → bullish

Today’s Close > Yesterday’s Close → uptrend

Volume spike detection

Price above 5-day moving average

✔ Automatically updates every 60 seconds
✔ Tracks multiple stocks at once
🧩 Code (for reference)

The source code is available here:

👉 https://github.com/Rohitjiagarwal/Stock_AI_Agent

🛠 How It Works

Fetch last 5 days of historical data

Extract today’s metrics

Compare with previous day + rolling averages

Generate an interpreted prediction

Print everything neatly to console

Repeat every 60 seconds

📦 Run the Project
1. Install dependencies
pip install yfinance

2. Run the script

You'll see continuous stock summaries and predictions like:

------------------------------------------
Stock Summary for: AAPL
Time: 2025-01-12 14:30:00
------------------------------------------
Open:   186.23
High:   188.42
Low:    185.93
Close:  187.55
Volume: 51234500
------------------------------------------
Prediction: ✔ Today bullish... ✔ Above 5-day average...
------------------------------------------
Waiting 60 seconds before next update...

📌 Future Enhancements (Step 2+)

ML-based prediction models

Sentiment analysis from financial news

Daily report generator (PDF/email)

Dashboard visualization

Deploy as automated cloud agent
