from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import (
    FutureFundingRates,
    GetFutureFundingRatesRequest,
    GetFutureFundingRatesResponse,
)


async def get_future_funding_rates(
    session: FTXClientSession,
    *,
    future: Optional[str] = None,
) -> list[FutureFundingRates]:
    """
    Get the funding rates for a specific future from the FTX API
    """
    request = GetFutureFundingRatesRequest(
        future=future,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFutureFundingRatesResponse(**data).data()
