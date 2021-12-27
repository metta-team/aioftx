from enum import Enum


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"


class LiquidityType(str, Enum):
    TAKER = "taker"
    MAKER = "maker"
