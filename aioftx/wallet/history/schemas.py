from typing import Optional

from pydantic import BaseModel

from aioftx.utils.schemas import PaginatedRequest, PaginatedResponse


class HistoryItem(BaseModel):
    coin: str
    confirmations: int
    confirmed_time: str
    fee: int
    id: int
    sent_time: str
    size: float
    status: str
    time: str
    txid: str
    notes: Optional[str]


class GetDepositHistoryRequest(PaginatedRequest):
    path = "/wallet/deposits"


class GetDepositHistoryResponse(PaginatedResponse[HistoryItem]):
    pass


class GetWithdrawalHistoryRequest(PaginatedRequest):
    path = "/wallet/withdrawals"


class GetWithdrawalHistoryResponse(PaginatedResponse[HistoryItem]):
    pass
