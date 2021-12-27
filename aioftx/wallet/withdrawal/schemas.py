from typing import Optional

from pydantic import BaseModel

from aioftx.http import HTTPMethod, Request, Response


class Withdrawal(BaseModel):
    coin: str
    address: str
    tag: Optional[str]
    fee: int
    id: int
    size: float
    status: str
    time: str
    txid: Optional[str]


class WithdrawalFee(BaseModel):
    method: str
    fee: float
    congested: bool


class CreateWithdrawalRequest(Request):
    http_method = HTTPMethod.POST
    coin: str
    size: float
    address: str
    tag: Optional[str]
    method: Optional[str]
    password: Optional[str]
    code: Optional[str]


class CreateWithdrawalResponse(Response[Withdrawal]):
    pass


class GetWithdrawalFeeRequest(Request):
    http_method = HTTPMethod.POST
    path = "/wallet/withdrawal_fee"

    coin: str
    size: float
    address: str
    tag: Optional[str]


class GetWithDrawalFeeResponse(Response[WithdrawalFee]):
    pass
