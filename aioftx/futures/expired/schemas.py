from pydantic import BaseModel
from ....utils.schemas import PaginatedRequest, PaginatedResponse


class ExpiredFuture(BaseModel):
    ask: float
    bid: float
    description: str
    enabled: bool
    expired: bool
    expiry: str
    expiry_description: str
    group: str
    imf_factor: float
    index: float
    last: float
    lower_bound: float
    margin_price: float
    mark: float
    move_start: str
    name: str
    perpetual: bool
    position_limit_weight: float
    post_only: bool
    price_increment: float
    size_increment: float
    type: str
    underlying: str
    underlying_description: str
    upper_bound: float


class GetExpiredFuturesRequest(PaginatedRequest):
    path = "/expired_futures"


class GetExpiredFuturesResponse(PaginatedResponse[ExpiredFuture]):
    pass
