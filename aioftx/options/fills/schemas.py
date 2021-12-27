import datetime

from aioftx.http import PaginatedRequest, PaginatedResponse, Request
from aioftx.types import LiquidityType, Side
from pydantic import BaseModel

from ..shared.schemas import Option


class Fill(BaseModel):
    fee: float
    fee_rate: float
    id: int
    liquidity: LiquidityType
    option: Option
    price: float
    quote_id: int
    side: Side
    size: float
    time: datetime.datetime


class GetOptionFillsRequest(PaginatedRequest):
    path = "/options/fills"


class GetOptionFillsResponse(PaginatedResponse[Fill]):
    pass
