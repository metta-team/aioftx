from pydantic import BaseModel, Field

from aioftx.utils.schemas import HTTPMethod, Response


class RegisterSignetDepositRequest(BaseModel):
    http_method = HTTPMethod.POST
    path = "/signet/deposits/{signet_link_id}"
    signet_link_id: int = Field(..., path=True)  # Unique ID of the Signet link
    size: float  # Amount of deposit


class RegisterSignetDepositResponse(Response[str]):
    pass


class RegisterSignetWithdrawalRequest(BaseModel):
    http_method = HTTPMethod.POST
    path = "/signet/deposits/{signet_link_id}"
    signet_link_id: int = Field(..., path=True)  # Unique ID of the Signet link
    size: float  # Amount of deposit


class RegisterSignetWithdrawalResponse(Response[str]):
    pass
