import ccxt

from .config import BotConfig


def create_exchange(config: BotConfig) -> ccxt.binance:
    exchange = ccxt.binance(
        {
            "apiKey": config.api_key,
            "secret": config.api_secret,
            "enableRateLimit": True,
            "options": {
                "defaultType": "spot",
            },
        }
    )
    if config.testnet:
        exchange.set_sandbox_mode(True)
    return exchange
