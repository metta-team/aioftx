from aioftx.session import FTXClientSession

from .schemas import (
    AccountOptionsInfo,
    GetAccountOptionsInfoRequest,
    GetAccountOptionsInfoResponse,
)


async def get_account_options_info(session: FTXClientSession) -> AccountOptionsInfo:
    """
    Get account options info from the FTX API
    """
    request = GetAccountOptionsInfoRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetAccountOptionsInfoResponse(**data).data()
