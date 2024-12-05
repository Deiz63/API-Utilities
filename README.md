AlpacaTickerSimple.py
This Python program fetches historical OHLCV (Open, High, Low, Close, Volume) stock data from the Alpaca API. It allows users to specify a stock symbol and a time period (in minutes) for the candlestick data. 
The program then displays detailed trading information for each candlestick, including price levels, volume, and timestamp.

Stock Symbol: User enters the desired stock ticker symbol (e.g., AAPL).
Time Period: User specifies the time interval in minutes for the candlestick data (1, 5, 10, 15, or 30 minutes).

Uses the Alpaca Market Data API to retrieve OHLCV, etc data for the specified stock and time period.
For each candlestick, it prints the following:
Close price (c)
High price (h)
Low price (l)
Number of trades (n)
Open price (o)
Timestamp (t)
Volume (v)
Volume Weighted Average Price (vw)
