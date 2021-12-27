from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import Fill, GetFillsReponse, GetFillsRequest, ResponseOrder


async def get_fills(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
    order: Optional[ResponseOrder] = None,
    order_id: Optional[int] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[Fill]:
    """
    Get the fills from the FTX API
    """
    request = GetFillsRequest(
        market=market,
        order=order,
        order_id=order_id,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetFillsReponse(**data).data()
