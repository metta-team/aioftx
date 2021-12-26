from typing import Optional
from pydantic import BaseModel, Field
from aioftx.utils.schemas import HTTPMethod, Request, Response, PaginatedResponse


class Deposit(BaseModel):
    address: str
    tag: Optional[str]


class GetDepositAddressRequest(Request):
    path = "/wallet/deposit_address/{coin}"
    coin: str = Field(..., path=True)
    method: Optional[str]


class GetDepositAddressResponse(Response[Deposit]):
    pass


class GetDepositAddressListRequest(Request):
    http_method = HTTPMethod.POST
    path = "/wallet/deposit_address/list"
    coin: str
    method: Optional[str]


class GetDepositAddressListResponse(PaginatedResponse[Deposit]):
    pass
