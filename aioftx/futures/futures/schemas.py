from pydantic import BaseModel, Field

from aioftx.http import PaginatedRequest, PaginatedResponse, Request, Response


class Future(BaseModel):
    ask: float
    bid: float
    change_1h: float
    change_24h: float
    change_bod: float
    volume_usd_24h: float
    volume: float
    description: str
    enabled: bool
    expired: bool
    expiry: str
    index: float
    imf_factor: float
    last: float
    lower_bound: float
    mark: float
    name: str
    open_interest: float
    open_interest_usd: float
    perpetual: bool
    position_limit_weight: float
    post_only: bool
    price_increment: float
    size_increment: float
    underlying: str
    upper_bound: float
    type: str


class GetFuturesRequest(PaginatedRequest):
    path = "/futures"


class GetFuturesResponse(PaginatedResponse[Future]):
    pass


class GetFutureRequest(Request):
    path = "/futures/{future_name}"
    future_name: str = Field(..., path=True)


class GetFutureResponse(Response[Future]):
    pass
