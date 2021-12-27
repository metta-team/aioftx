from aioftx.http import PaginatedResponse, Request
from aioftx.types import Side
from pydantic import BaseModel

from ..shared.schemas import Option


class OptionPosition(BaseModel):
    entry_price: float
    net_size: float
    option: Option
    side: Side
    size: float


class GetOptionPositionsRequest(Request):
    path = "/options/positions"


class GetOptionPositionsResponse(PaginatedResponse[OptionPosition]):
    pass
