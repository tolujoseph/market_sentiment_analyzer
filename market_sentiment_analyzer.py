import yfinance as yf
import pandas as pd
import ta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# --- CONFIG ---
ASSET = "BTC-USD"  # Change to stock symbol like "AAPL" or "ETH-USD"
PERIOD = "3mo"
INTERVAL = "1d"

def fetch_market_data(symbol, period="3mo", interval="1d"):
    print(f"[INFO] Fetching market data for {symbol}")
    df = yf.download(symbol, period=period, interval=interval)
    df.dropna(inplace=True)
    return df

def calculate_indicators(df):
    print("[INFO] Calculating indicators")
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    return df

def plot_chart(df, symbol):
    print("[INFO] Plotting chart")
    df[['Close', 'SMA_20']].plot(title=f"{symbol} Price and SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()

def fetch_news_sentiment(query):
    print(f"[INFO] Fetching sentiment for {query}")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.google.com/search?q={query}+stock+news&tbm=nws"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = [item.text for item in soup.select('div.BNeawe.vvjwJb.AP7Wnd')][:5]

    analyzer = SentimentIntensityAnalyzer()
    scores = [analyzer.polarity_scores(headline)['compound'] for headline in headlines]

    avg_score = sum(scores) / len(scores) if scores else 0
    sentiment = (
        "Bullish" if avg_score > 0.2 else
        "Bearish" if avg_score < -0.2 else
        "Neutral"
    )
    return sentiment, headlines

def decision_logic(df, sentiment):
    rsi = df['RSI'].iloc[-1]
    close = df['Close'].iloc[-1]
    sma = df['SMA_20'].iloc[-1]

    print(f"\n[TECHNICAL ANALYSIS]")
    print(f"Last Close: {close:.2f}")
    print(f"RSI: {rsi:.2f} → {'Overbought' if rsi > 70 else 'Oversold' if rsi < 30 else 'Neutral'}")
    print(f"Price vs SMA20: {'Above' if close > sma else 'Below'}")

    print(f"\n[SENTIMENT ANALYSIS]")
    print(f"Sentiment: {sentiment}")

    if sentiment == "Bullish" and close > sma and rsi < 70:
        recommendation = "BUY"
    elif sentiment == "Bearish" and close < sma and rsi > 30:
        recommendation = "SELL"
    else:
        recommendation = "HOLD"
    print(f"\n[DECISION] Recommended Action: {recommendation}")

def main():
    df = fetch_market_data(ASSET, PERIOD, INTERVAL)
    df = calculate_indicators(df)
    plot_chart(df, ASSET)

    sentiment, headlines = fetch_news_sentiment(ASSET.split('-')[0])
    print("\nTop Headlines:")
    for h in headlines:
        print(f"- {h}")

    decision_logic(df, sentiment)

if __name__ == "__main__":
    main()
