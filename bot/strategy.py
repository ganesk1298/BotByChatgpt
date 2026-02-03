from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class SignalResult:
    action: str
    predicted_price: float
    last_price: float


def linear_regression_predict(prices: List[float]) -> float:
    if len(prices) < 2:
        return prices[-1]
    x = np.arange(len(prices))
    y = np.array(prices)
    slope, intercept = np.polyfit(x, y, 1)
    next_index = len(prices)
    return float(slope * next_index + intercept)


def generate_signal(prices: List[float], threshold: float) -> SignalResult:
    last_price = prices[-1]
    predicted_price = linear_regression_predict(prices)
    upper = last_price * (1 + threshold)
    lower = last_price * (1 - threshold)

    if predicted_price > upper:
        action = "buy"
    elif predicted_price < lower:
        action = "sell"
    else:
        action = "hold"

    return SignalResult(
        action=action,
        predicted_price=predicted_price,
        last_price=last_price,
    )
