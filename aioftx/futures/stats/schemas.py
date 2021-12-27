from pydantic import BaseModel, Field

from aio.http import Request, Response


class FutureStats(BaseModel):
    volume: float
    next_funding_rate: float
    next_funding_time: str
    expiration_price: float
    predicted_expiration_price: float
    strike_price: float
    open_interest: float


class GetFutureStatsRequest(Request):
    path = "/futures/{future_name}/stats"
    future_name: str = Field(..., path=True)


class GetFutureStatsResponse(Response[FutureStats]):
    pass
