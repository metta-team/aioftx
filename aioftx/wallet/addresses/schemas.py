from typing import Optional

from pydantic import BaseModel, Field

from aioftx.http import HTTPMethod, PaginatedResponse, Request, Response


class SavedAddress(BaseModel):
    address: str
    coin: str
    fiat: bool
    id: int
    is_prime_trust: bool
    last_used_at: str
    name: str
    tag: Optional[str]
    whitelisted: bool
    whitelisted_after: str


class GetSavedAddressesRequest(Request):
    path = "/wallet/saved_addresses"
    coin: Optional[str]

    @property
    def url(self) -> str:
        if self.coin:
            return self.path + f"?coin={self.coin}"
        return self.path


class GetSavedAddressesResponse(PaginatedResponse[SavedAddress]):
    pass


class CreateSavedAddressRequest(Request):
    http_method = HTTPMethod.POST
    path = "/wallet/saved_addresses"


class CreateSavedAddressResponse(Response[SavedAddress]):
    pass


class DeleteSavedAddressRequest(Request):
    http_method = HTTPMethod.POST
    path = "/wallet/saved_addresses/{saved_address_id}"
    saved_address_id: int = Field(..., path=True)


class DeleteSavedAddressResponse(Response[str]):
    pass
