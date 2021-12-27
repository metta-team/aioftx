from enum import Enum
from typing import Optional
from pydantic import BaseModel
from aioftx.utils.schemas import PaginatedRequest, PaginatedResponse


class LiquidityType(str, Enum):
    TAKER = "taker"
    MAKER = "maker"


class ResponseOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class Fill(BaseModel):
    fee: float
    fee_currency: str
    fee_rate: float
    future: str
    id: int
    liquidity: str
    market: str
    base_currency: str
    quote_currency: str
    order_id: int
    trade_d: int
    price: float
    side: str
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
