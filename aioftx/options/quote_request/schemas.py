import datetime
from typing import Optional

from aioftx.types import Side
from aio.http import HTTPMethod, PaginatedResponse, Request, Response
from pydantic import BaseModel, Field

from ..quotes.schemas import Quote
from ..shared.schemas import Option, OptionStatus, OptionType


class QuoteRequest(BaseModel):
    id: int
    option: Option
    side: Side
    size: float
    time: datetime.datetime
    request_expiry: datetime.datetime
    status: OptionStatus
    limit_price: Optional[float]


class MyQuoteRequest(BaseModel):
    id: int
    option: Option
    side: Side
    size: float
    time: datetime.datetime
    request_expiry: datetime.datetime
    status: OptionStatus
    limit_price: Optional[bool]
    quotes: list[Quote]
    hide_limit_price: bool


""" Methods """


class GetQuoteRequestsRequest(Request):
    path = "/options/requests"


class GetQuoteRequestsResponse(PaginatedResponse[QuoteRequest]):
    pass


class GetMyQuoteRequestsRequest(Request):
    path = "/options/my_requests"


class GetMyQuoteRequestsResponse(PaginatedResponse[MyQuoteRequest]):
    pass


class CreateQuoteRequestRequest(Request):
    http_method = HTTPMethod.POST
    path = "/options/requests"

    underlying: str
    type: OptionType
    strike: float
    expiry: int
    side: Side
    size: float
    limit_price: Optional[float]
    hide_limit_price: bool = True
    request_expiry: Optional[int] = None  # unix timestamp
    counterparty_id: Optional[
        int
    ] = None  # when specified, makes the request private to the specified counterparty


class CreateQuoteRequestResponse(Response[QuoteRequest]):
    pass


class DeleteQuoteRequestRequest(Request):
    http_method = HTTPMethod.DELETE
    path = "/options/requests/{request_id}"

    request_id: int = Field(..., path=True)


class DeleteQuoteRequestResponse(Response[QuoteRequest]):
    pass
