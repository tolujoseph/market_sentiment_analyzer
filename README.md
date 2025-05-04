# 📈 Market Sentiment Analyzer

A Python tool for traders and analysts that combines real-time market data, technical indicators, and sentiment analysis to deliver powerful insights for stocks and cryptocurrencies.

---

## 🚀 Features

- ✅ Pulls live market data (via [yfinance])
- 📊 Calculates key technical indicators:
  - Moving Averages (SMA, EMA)
  - Relative Strength Index (RSI)
- 🧠 Analyzes sentiment from recent news headlines using NLP
- 💬 Telegram bot integration for automated updates (optional)
- 🛠️ CLI-ready and easily extendable

---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/market_sentiment_analyzer.git
   cd market_sentiment_analyzer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables (if using Telegram bot)**
   ```bash
   export TELEGRAM_BOT_TOKEN="your_token"
   export TELEGRAM_CHAT_ID="your_chat_id"
   ```

5. **Run the script**
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
market_sentiment_analyzer/
├── main.py                 # Main logic
├── utils.py                # Helper functions
├── sentiment.py            # NLP-based sentiment scoring
├── indicators.py           # Technical analysis tools
├── config.py               # Config and tokens
├── requirements.txt
└── README.md
```

---

## 📷 Sample Output

- Price & indicator summary
- Recent news headlines with sentiment scores
- Buy/sell signal suggestion (basic logic)
- Optional Telegram alert with summary message

---

## 📌 TODOs

- [ ] Add support for more data sources (e.g., Binance API)
- [ ] Improve sentiment analysis with financial-specific models
- [ ] Create a Streamlit dashboard version

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, suggest improvements, or submit pull requests.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more info.
