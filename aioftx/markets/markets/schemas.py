from pydantic import BaseModel, Field

from aioftx.utils.schemas import PaginatedRequest, PaginatedResponse, Request, Response


class Market(BaseModel):
    name: str
    baseCurrency: str
    quoteCurrency: str
    quoteVolume24h: float
    change1h: float
    change24h: float
    changeBod: float
    highLeverageFeeExempt: bool
    minProvideSize: float
    type: str
    underlying: str
    enabled: bool
    ask: float
    bid: float
    last: float
    postOnly: bool
    price: float
    priceIncrement: float
    sizeIncrement: float
    restricted: bool
    volumeUsd24h: float


class GetMarketsRequest(PaginatedRequest):
    path = "/markets"


class GetMarketsResponse(PaginatedResponse[Market]):
    pass


class GetMarketRequest(Request):
    path = "/markets/{market_name}"
    market_name: str = Field(..., path=True)


class GetMarketResponse(Response[Market]):
    asks: list[float]
    bids: list[float]
