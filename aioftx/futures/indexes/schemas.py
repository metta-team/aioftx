from pydantic import BaseModel, Field

from aioftx.http import PaginatedRequest, PaginatedResponse, Request, Response


class IndexWeight(BaseModel):
    BCH: float
    BNB: float
    BSV: float
    EOS: float
    ETH: float
    LTC: float
    XRP: float


class GetIndexWeightsRequest(Request):
    path = "/indexes/{index_name}/weights"
    index_name: str = Field(..., path=True)


class GetIndexWeightsResponse(Response[IndexWeight]):
    pass


class Index(BaseModel):
    close: float
    high: float
    low: float
    open: float
    start_time: str
    volume: float


class GetHistoricalIndexRequest(PaginatedRequest):
    path = "/indexes/{market_name}/candles"
    market_name: str = Field(..., path=True)
    resolution: int


class GetHistoricalIndexResponse(PaginatedResponse[Index]):
    pass
