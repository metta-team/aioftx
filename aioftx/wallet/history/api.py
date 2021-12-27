from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import (GetDepositHistoryRequest, GetDepositHistoryResponse,
                      GetWithdrawalHistoryRequest,
                      GetWithdrawalHistoryResponse, HistoryItem)


async def get_deposit_history(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[HistoryItem]:
    """
    Get the deposit history from the FTX API
    """
    request = GetDepositHistoryRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetDepositHistoryResponse(**data).data()


async def get_withdrawal_history(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[HistoryItem]:
    """
    Get the withdrawal history from the FTX API
    """
    request = GetWithdrawalHistoryRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetWithdrawalHistoryResponse(**data).data()
