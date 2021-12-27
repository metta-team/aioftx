from pydantic import BaseModel

from aioftx.http import PaginatedRequest, PaginatedResponse


class Airdrop(BaseModel):
    coin: str
    id: int
    size: float
    time: str
    status: str


class GetAirdropsRequest(PaginatedRequest):
    path = "/wallet/airdrops"


class GetAirdropsResponse(PaginatedResponse[Airdrop]):
    pass
