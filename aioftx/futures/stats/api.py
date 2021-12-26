from aioftx.aioftx.session import FTXClientSession
from .schemas import FutureStats, GetFutureStatsRequest, GetFutureStatsResponse


async def get_future_stats(
    session: FTXClientSession,
    *,
    future_name: str,
) -> FutureStats:
    """
    Get a specific future from the FTX API
    """
    request = GetFutureStatsRequest(
        future_name=future_name,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFutureStatsResponse(**data).data()
