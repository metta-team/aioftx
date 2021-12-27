from aioftx.http import Request, Response
from pydantic import BaseModel


class AccountOptionsInfo(BaseModel):
    usd_balance: float
    liquidation_price: float
    liquidating: bool


class GetAccountOptionsInfoRequest(Request):
    path = "/options/account_info"

    usd_balance: float
    liquidation_price: float
    liquidated: bool
    maintenance_margin_requirement: float
    initial_margin_requirement: float


class GetAccountOptionsInfoResponse(Response[AccountOptionsInfo]):
    pass
