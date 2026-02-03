from dataclasses import dataclass
import os


@dataclass(frozen=True)
class BotConfig:
    api_key: str
    api_secret: str
    testnet: bool
    enable_live_trading: bool
    base_currency: str
    quote_currency: str
    trade_amount: float
    prediction_threshold: float
    timeframe: str
    ohlcv_limit: int


    @staticmethod
    def from_env() -> "BotConfig":
        return BotConfig(
            api_key=os.getenv("BINANCE_API_KEY", ""),
            api_secret=os.getenv("BINANCE_API_SECRET", ""),
            testnet=os.getenv("BINANCE_TESTNET", "true").lower() == "true",
            enable_live_trading=os.getenv("ENABLE_LIVE_TRADING", "false").lower()
            == "true",
            base_currency=os.getenv("BASE_CURRENCY", "BTC"),
            quote_currency=os.getenv("QUOTE_CURRENCY", "USDT"),
            trade_amount=float(os.getenv("TRADE_AMOUNT", "0.001")),
            prediction_threshold=float(os.getenv("PREDICTION_THRESHOLD", "0.002")),
            timeframe=os.getenv("TIMEFRAME", "1h"),
            ohlcv_limit=int(os.getenv("OHLCV_LIMIT", "120")),
        )
