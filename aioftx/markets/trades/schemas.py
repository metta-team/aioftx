from pydantic import BaseModel

from aioftx.shared.schemas import Side
from aioftx.utils.schemas import PaginatedRequest, PaginatedResponse


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
