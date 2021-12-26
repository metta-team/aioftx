from typing import Optional
from aioftx.aioftx.session import FTXClientSession
from .schemas import (
    GetMarketsRequest,
    GetMarketsResponse,
    GetMarketResponse,
    GetMarketRequest,
    Market,
)


async def get_markets(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None
) -> list[Market]:
    """
    Get the list of all markets from the FTX API
    """
    request = GetMarketsRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetMarketsResponse(**data).data()


async def get_market(session: FTXClientSession, *, market_name: str) -> Market:
    """
    Get the details of a specific market from the FTX API
    """
    request = GetMarketRequest(market_name=market_name)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetMarketResponse(**data).data()
