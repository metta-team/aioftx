from typing import Optional

from aioftx.session import FTXClientSession

from .schemas import (
    Balance,
    GetAllBalancesRequest,
    GetAllBalancesResponse,
    GetBalancesRequest,
    GetBalancesResponse,
)


async def get_balances(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None
) -> list[Balance]:
    """
    Get the balances for a specific account from the FTX API
    """
    request = GetBalancesRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetBalancesResponse(**data).data()


async def get_all_balances(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None
) -> dict[str, list[Balance]]:
    """
    Get the balances for all accounts from the FTX API
    """
    request = GetAllBalancesRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetAllBalancesResponse(**data).data()
