from pydantic import BaseModel, Field

from aioftx.utils.schemas import PaginatedRequest, PaginatedResponse


class Price(BaseModel):
    close: float
    high: float
    low: float
    open: float
    start_time: str
    volume: float


class GetPricesRequest(PaginatedRequest):
    path = "/markets/{market_name}/candles"
    market_name: str = Field(..., path=True)
    resolution: int


class GetPricesResponse(PaginatedResponse[Price]):
    pass
