from typing import Optional
from pydantic import BaseModel
from ....utils.schemas import PaginatedRequest, PaginatedResponse


class FutureFundingRates(BaseModel):
    future: str
    rate: float
    time: str


class GetFutureFundingRatesRequest(PaginatedRequest):
    path = "/funding_rates"
    future: Optional[str] = None


class GetFutureFundingRatesResponse(PaginatedResponse[FutureFundingRates]):
    pass
