from pydantic import BaseModel, Field

from aioftx.http import Request, Response


class Orderbook(BaseModel):
    asks: list[float]
    bids: list[float]


class GetOrderbookRequest(Request):
    path = "/markets/{market_name}/orderbook"
    market_name: str = Field(..., path=True)
    depth: int = 20


class GetOrderbookResponse(Response[Orderbook]):
    pass
