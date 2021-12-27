from aioftx.session import FTXClientSession

from .schemas import Fill, GetOptionFillsRequest, GetOptionFillsResponse


async def get_option_fills(session: FTXClientSession) -> list[Fill]:
    """
    Get the option fills from the FTX API
    """
    request = GetOptionFillsRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOptionFillsResponse(**data).data()
