from aioftx.aioftx.session import FTXClientSession

from .schemas import GetPricesRequest, GetPricesResponse, Price


async def get_historical_prices(
    session: FTXClientSession,
    *,
    market_name: str,
    resolution: int,
    start_time: int,
    end_time: int
) -> list[Price]:
    """
    Get the historical prices for a specific market from the FTX API
    """
    request = GetPricesRequest(
        market_name=market_name,
        resolution=resolution,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetPricesResponse(**data).data()
