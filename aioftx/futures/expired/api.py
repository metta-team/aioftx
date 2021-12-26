from typing import Optional
from aioftx.aioftx.session import FTXClientSession
from .schemas import ExpiredFuture, GetExpiredFuturesRequest, GetExpiredFuturesResponse


async def get_expired_futures(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[ExpiredFuture]:
    """
    Get the expired futures from the FTX API
    """
    request = GetExpiredFuturesRequest(
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetExpiredFuturesResponse(**data).data()
