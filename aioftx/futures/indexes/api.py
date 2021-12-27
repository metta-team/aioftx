from typing import Optional

from aioftx.session import FTXClientSession

from .schemas import (
    GetHistoricalIndexRequest,
    GetHistoricalIndexResponse,
    GetIndexWeightsRequest,
    GetIndexWeightsResponse,
    Index,
    IndexWeight,
)


async def get_index_weights(
    session: FTXClientSession,
    *,
    index_name: str,
) -> IndexWeight:
    """
    Get the index weights from the FTX API
    """
    request = GetIndexWeightsRequest(
        index_name=index_name,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetIndexWeightsResponse(**data).data()


async def get_historical_index(
    session: FTXClientSession,
    *,
    market_name: str,
    resolution: int,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[Index]:
    """
    Get the historical index from the FTX API
    """
    request = GetHistoricalIndexRequest(
        market_name=market_name,
        resolution=resolution,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetHistoricalIndexResponse(**data).data()
