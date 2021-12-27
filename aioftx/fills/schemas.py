from enum import Enum
from typing import Optional

from aioftx.http import PaginatedRequest, PaginatedResponse
from aioftx.types import LiquidityType, Side
from pydantic import BaseModel


class Fill(BaseModel):
    fee: float
    fee_currency: str
    fee_rate: float
    future: str
    id: int
    liquidity: LiquidityType
    market: str
    base_currency: str
    quote_currency: str
    order_id: int
    trade_d: int
    price: float
    side: Side
    size: float
    time: str
    type: str


class GetFillsRequest(PaginatedRequest):
    path = "/fills"
    market: Optional[str]
    order: Optional[ResponseOrder]
    order_id: Optional[int]


class GetFillsReponse(PaginatedResponse[Fill]):
    pass
