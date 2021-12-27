from typing import Optional

from pydantic import BaseModel

from aioftx.http import PaginatedRequest, PaginatedResponse


class Coin(BaseModel):
    can_deposit: bool
    can_withdraw: bool
    has_tag: bool

    id: str
    name: str
    bep_2_asset: Optional[str]
    can_convert: bool
    collateral: bool
    collateral_weight: float
    credit_to: Optional[str]
    erc_20_contract: str
    fiat: bool
    is_token: bool
    methods: list[str]
    spl_mint: str
    trc_20_contract: str
    usd_fungible: bool


class GetCoinsRequest(PaginatedRequest):
    path = "/wallet/coins"


class GetCoinsResponse(PaginatedResponse[Coin]):
    pass
