import datetime
from enum import Enum
from typing import Optional

from aioftx.shared.schemas import Side
from aioftx.utils.schemas import HTTPMethod, PaginatedResponse, Request, Response
from pydantic import BaseModel, Field


class OptionType(str, Enum):
    CALL = "call"
    PUT = "put"


class OptionStatus(str, Enum):
    OPEN = "open"


class Option(BaseModel):
    underlying: str
    type: OptionType
    strike: float
    expiry: str


class Quote(BaseModel):
    id: int
    status: OptionStatus
    collateral: float
    price: float
    quote_expiry: Optional[datetime.datetime]
    time: datetime.datetime


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
