from aioftx.session import FTXClientSession

from .schemas import (
    GetOptionPositionsRequest,
    GetOptionPositionsResponse,
    OptionPosition,
)


async def get_option_positions(session: FTXClientSession) -> list[OptionPosition]:
    """
    Get the option positions from the FTX API
    """
    request = GetOptionPositionsRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOptionPositionsResponse(**data).data()
