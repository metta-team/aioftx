from typing import Optional

from aioftx.session import FTXClientSession

from .schemas import (
    Future,
    GetFutureRequest,
    GetFutureResponse,
    GetFuturesRequest,
    GetFuturesResponse,
)


async def get_future(
    session: FTXClientSession,
    *,
    future_name: str,
) -> Future:
    """
    Get a specific future from the FTX API
    """
    request = GetFutureRequest(
        future_name=future_name,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFutureResponse(**data).data()


async def get_all_futures(
    session: FTXClientSession,
    *,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[Future]:
    """
    Get all futures from the FTX API
    """
    request = GetFuturesRequest(
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFuturesResponse(**data).data()
