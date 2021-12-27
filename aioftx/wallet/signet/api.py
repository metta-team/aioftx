from aioftx.session import FTXClientSession

from .schemas import (
    RegisterSignetDepositRequest,
    RegisterSignetDepositResponse,
    RegisterSignetWithdrawalRequest,
    RegisterSignetWithdrawalResponse,
)


async def register_signet_deposit(
    session: FTXClientSession, *, signet_link_id: int, size: float
) -> str:
    """
    Register a new signet deposit
    """
    request = RegisterSignetDepositRequest(signet_link_id=signet_link_id, size=size)
    async with session.post(request.url, json=request.json()) as resp:
        data = await resp.json()
        return RegisterSignetDepositResponse(**data).data()


async def register_signet_withdrawal(
    session: FTXClientSession, *, signet_link_id: int, size: float
) -> str:
    """
    Register a new signet withdrawal
    """
    request = RegisterSignetWithdrawalRequest(signet_link_id=signet_link_id, size=size)
    async with session.post(request.url, json=request.json()) as resp:
        data = await resp.json()
        return RegisterSignetWithdrawalResponse(**data).data()
