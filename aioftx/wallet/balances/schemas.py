from pydantic import BaseModel
from ....utils.schemas import (
    PaginatedRequest,
    PaginatedResponse,
    KeyedPaginatedResponse,
)


class Balance(BaseModel):
    coin: str  # coin id
    free: float  # free amount
    spot_borrow: float  # amount borrowed using spot margin
    usd_value: float  # approximate total amount in USD
    available_without_borrow: float  # amount available without borrow


class GetBalancesRequest(PaginatedRequest):
    path = "/wallet/balances"


class GetBalancesResponse(PaginatedResponse[Balance]):
    pass


class GetAllBalancesRequest(PaginatedRequest):
    path = "/wallet/all_balances"


class GetAllBalancesResponse(KeyedPaginatedResponse[Balance]):
    pass
