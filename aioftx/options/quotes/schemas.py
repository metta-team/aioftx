import datetime
from enum import Enum
from typing import Optional

from aioftx.shared.schemas import Side
from aioftx.utils.schemas import HTTPMethod, PaginatedResponse, Request, Response
from pydantic import BaseModel, Field
from pydantic.networks import HttpUrl

from ..quote_request.schemas import Option


class Quote(BaseModel):
    id: int
    option: Option
    status: str
    collateral: float
    price: float
    quote_expiry: Optional[datetime.datetime]
    quoter_side: Side
    time: datetime.datetime
    request_id: int
    request_side: Side


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
