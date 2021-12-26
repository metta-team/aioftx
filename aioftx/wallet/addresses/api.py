from typing import Optional
from ...session import FTXClientSession
from .schemas import (
    GetSavedAddressesRequest,
    GetSavedAddressesResponse,
    SavedAddress,
    CreateSavedAddressRequest,
    CreateSavedAddressResponse,
    DeleteSavedAddressRequest,
    DeleteSavedAddressResponse,
)


async def get_saved_addresses(
    session: FTXClientSession, *, coin: Optional[str] = None
) -> list[SavedAddress]:
    """
    Get the list of all saved addresses from the FTX API
    """
    request = GetSavedAddressesRequest(coin=coin)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetSavedAddressesResponse(**data).data()


async def create_saved_address(session: FTXClientSession) -> SavedAddress:
    """
    Create a new saved address from the FTX API
    """
    request = CreateSavedAddressRequest()
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateSavedAddressResponse(**data).data()


async def delete_saved_address(session: FTXClientSession, *, id: str) -> str:
    """
    Delete a saved address from the FTX API
    """
    request = DeleteSavedAddressRequest(saved_address_id=id)
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return DeleteSavedAddressResponse(**data).data()
