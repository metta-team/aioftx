from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import (
    FundingPayment,
    GetFundingPaymentsRequest,
    GetFundingPaymentsResponse,
)


async def get_funding_payments(
    session: FTXClientSession,
    *,
    future: Optional[str] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[FundingPayment]:
    """
    Get the funding payments from the FTX API
    """
    request = GetFundingPaymentsRequest(
        future=future,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFundingPaymentsResponse(**data).data()
