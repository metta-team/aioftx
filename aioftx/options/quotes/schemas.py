import datetime
from typing import Optional

from aioftx.http import HTTPMethod, PaginatedResponse, Request, Response
from aioftx.types import Side
from pydantic import BaseModel, Field

from ..shared.schemas import Option


class Quote(BaseModel):
    id: int
    option: Option
    status: str
    collateral: float
    price: float
    quote_expiry: Optional[datetime.datetime]
    quoter_side: Side
    time: datetime.datetime
    request_id: Optional[int]
    request_side: Optional[Side]


class GetQuotesRequest(Request):
    path = "/options/requests/{request_id}/quotes"

    request_id: str = Field(..., path=True)


class GetQuotesResponse(Response[Quote]):
    pass


class GetMyQuotesRequest(Request):
    path = "/options/my_quotes"


class GetMyQuotesReponse(PaginatedResponse[Quote]):
    pass


class CreateQuoteRequest(Request):
    http_method = HTTPMethod.POST
    path = "/options/requests/{request_id}/quotes"

    request_id: str = Field(..., path=True)
    price: float


class CreateQuoteResponse(Response[Quote]):
    pass


class CancelQuoteRequest(Request):
    http_method = HTTPMethod.DELETE
    path = "/options/quotes/{quote_id}"

    quote_id: str = Field(..., path=True)


class CancelQuoteResponse(Response[Quote]):
    pass


class AcceptQuoteRequest(Request):
    http_method = HTTPMethod.POST
    path = "/options/quotes/{quote_id}/accept"

    quote_id: str = Field(..., path=True)


class AcceptQuoteResponse(Response[Quote]):
    pass
