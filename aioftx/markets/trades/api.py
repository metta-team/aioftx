from aioftx.aioftx.session import FTXClientSession
from .schemas import GetTradesRequest, GetTradesResponse, Trade


async def get_trades(session: FTXClientSession, *, market_name: str) -> list[Trade]:
    """
    Get the trades for a specific market from the FTX API
    """
    request = GetTradesRequest(market_name=market_name)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetTradesResponse(**data).data()
