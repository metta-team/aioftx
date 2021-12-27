from typing import Optional

from aioftx.session import FTXClientSession

from .schemas import Coin, GetCoinsRequest, GetCoinsResponse


async def get_coins(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None
) -> list[Coin]:
    """
    Get the coins from the FTX API
    """
    request = GetCoinsRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetCoinsResponse(**data).data()
