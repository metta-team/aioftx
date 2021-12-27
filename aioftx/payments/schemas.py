from typing import Optional

from pydantic import BaseModel

from aio.http import PaginatedRequest, PaginatedResponse


class FundingPayment(BaseModel):
    future: str
    id: int
    payment: float
    time: str
    rate: float


class GetFundingPaymentsRequest(PaginatedRequest):
    path = "/funding_payments"
    future: Optional[str]


class GetFundingPaymentsResponse(PaginatedResponse[FundingPayment]):
    pass
