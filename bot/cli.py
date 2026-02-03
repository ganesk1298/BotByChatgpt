import argparse
import logging
from typing import List

from .config import BotConfig
from .exchange import create_exchange
from .strategy import generate_signal


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_prices(exchange, symbol: str, timeframe: str, limit: int) -> List[float]:
    candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    return [candle[4] for candle in candles]


def place_order(exchange, symbol: str, action: str, amount: float, live: bool) -> None:
    if not live:
        logging.info("Paper trade: would %s %s of %s", action, amount, symbol)
        return

    if action == "buy":
        exchange.create_market_buy_order(symbol, amount)
        logging.info("Live trade: bought %s of %s", amount, symbol)
    elif action == "sell":
        exchange.create_market_sell_order(symbol, amount)
        logging.info("Live trade: sold %s of %s", amount, symbol)


def run_bot(config: BotConfig, symbol: str | None = None) -> None:
    exchange = create_exchange(config)
    trading_symbol = symbol or f"{config.base_currency}/{config.quote_currency}"

    prices = fetch_prices(exchange, trading_symbol, config.timeframe, config.ohlcv_limit)
    signal = generate_signal(prices, config.prediction_threshold)

    logging.info(
        "Signal for %s: %s (predicted %.2f vs last %.2f)",
        trading_symbol,
        signal.action,
        signal.predicted_price,
        signal.last_price,
    )

    if signal.action in {"buy", "sell"}:
        place_order(
            exchange,
            trading_symbol,
            signal.action,
            config.trade_amount,
            config.enable_live_trading,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Binance AI trading bot")
    parser.add_argument("--symbol", help="Trading pair symbol, e.g., BTC/USDT")
    args = parser.parse_args()

    run_bot(BotConfig.from_env(), symbol=args.symbol)
