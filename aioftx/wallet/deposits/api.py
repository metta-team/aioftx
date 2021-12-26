from typing import Optional
from aioftx.aioftx.session import FTXClientSession
from .schemas import (
    Deposit,
    GetDepositAddressRequest,
    GetDepositAddressResponse,
    GetDepositAddressListRequest,
    GetDepositAddressListResponse,
)


async def get_deposit_address(
    session: FTXClientSession, *, coin: str, method: Optional[str] = None
) -> Deposit:
    """
    Get the deposit address from the FTX API
    """
    request = GetDepositAddressRequest(coin=coin, method=method)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetDepositAddressResponse(**data).data()


async def get_deposit_address_list(
    session: FTXClientSession, *, coin: str, method: Optional[str] = None
) -> list[Deposit]:
    """
    Get the deposit address list from the FTX API
    """
    request = GetDepositAddressListRequest(coin=coin, method=method)
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return GetDepositAddressListResponse(**data).data()
