from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import (
    CreateWithdrawalRequest,
    CreateWithdrawalResponse,
    GetWithdrawalFeeRequest,
    GetWithDrawalFeeResponse,
    Withdrawal,
    WithdrawalFee,
)


async def create_withdrawal(
    session: FTXClientSession,
    *,
    coin: str,
    size: float,
    address: str,
    tag: Optional[str] = None,
    method: Optional[str] = None,
    password: Optional[str] = None,
    code: Optional[str] = None
) -> Withdrawal:
    """
    Create a withdrawal from the FTX API
    """
    request = CreateWithdrawalRequest(
        coin=coin,
        size=size,
        address=address,
        tag=tag,
        method=method,
        password=password,
        code=code,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateWithdrawalResponse(**data).data()


async def get_withdrawal_fee(
    session: FTXClientSession,
    *,
    coin: str,
    size: float,
    address: str,
    tag: Optional[str] = None,
    method: Optional[str] = None
) -> WithdrawalFee:
    """
    Get the withdrawal fee for a specific coin from the FTX API
    """
    request = GetWithdrawalFeeRequest(
        coin=coin, size=size, address=address, tag=tag, method=method
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return GetWithDrawalFeeResponse(**data).data()
