from typing import Optional

from aioftx.session import FTXClientSession

from .schemas import Airdrop, GetAirdropsRequest, GetAirdropsResponse


async def get_airdrops(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None
) -> list[Airdrop]:
    """
    Get the list of all airdrops from the FTX API
    """
    request = GetAirdropsRequest(start_time=start_time, end_time=end_time)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetAirdropsResponse(**data).data()
