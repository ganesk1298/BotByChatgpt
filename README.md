# BotByChatgpt

Binance spot trading bot with a lightweight AI signal (linear regression on recent closes) and optional live trading via CCXT.

## Features
- Fetches recent OHLCV data from Binance.
- Generates buy/sell/hold signals from a simple predictive model.
- Paper-trade by default; enable live trading with an environment toggle.
- Configurable via environment variables.

## Setup
1. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` with your Binance API credentials.

> **Warning**
> Live trading is disabled by default. Ensure you understand the risks before enabling `ENABLE_LIVE_TRADING=true`.

## Usage
```bash
python -m bot.cli --symbol BTC/USDT
```

If `--symbol` is omitted, it uses `BASE_CURRENCY/QUOTE_CURRENCY` from the environment.

## Notes
- This bot uses a simple linear regression model for demonstration purposes.
- Use Binance testnet keys when `BINANCE_TESTNET=true`.
