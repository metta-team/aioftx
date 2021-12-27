from pydantic import BaseModel

from aioftx.types import Side
from aioftx.http import PaginatedRequest, PaginatedResponse


class Trade(BaseModel):
    id: int
    liquidation: bool
    price: float
    side: Side
    size: float
    time: str


class GetTradesRequest(PaginatedRequest):
    path = "/markets/{market_name}/trades"
    market_name: str


class GetTradesResponse(PaginatedResponse[Trade]):
    pass
