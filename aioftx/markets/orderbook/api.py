from aioftx.aioftx.session import FTXClientSession
from .schemas import GetOrderbookRequest, GetOrderbookResponse, Orderbook


async def get_orderbook(
    session: FTXClientSession, *, market_name: str, depth: int = 20
) -> Orderbook:
    """
    Get the orderbook for a specific market from the FTX API
    """
    request = GetOrderbookRequest(market_name=market_name, depth=depth)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOrderbookResponse(**data).data()
