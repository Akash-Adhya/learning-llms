import yfinance as yf
import pandas as pd

# List of top 10 global company tickers
top_10_tickers = [
    "AAPL",    # Apple
    "MSFT",    # Microsoft
    "GOOGL",   # Alphabet / Google
    "AMZN",    # Amazon
    "NVDA",    # NVIDIA
    "TSLA",    # Tesla
    "META",    # Meta Platforms (Facebook)
    "BRK-B",   # Berkshire Hathaway
    "LLY",     # Eli Lilly
    "JPM"      # JPMorgan Chase
]

for ticker in top_10_tickers:
    print(f"Downloading data for {ticker}...")
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="max")

        history.drop(columns=["Dividends", "Stock Splits"], inplace=True, errors='ignore')


        history["Tomorrow"] = history["Close"].shift(-1)
        history["Target"] = (history["Tomorrow"] > history["Close"]).astype(int)


        filename = f"{ticker.replace('-', '_')}_stock_price_data.csv"
        history.to_csv(filename)
        print(f"Saved to {filename}")

    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
