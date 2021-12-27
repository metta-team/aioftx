from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from aioftx.types import Side
from aio.http import (
    HTTPMethod,
    PaginatedRequest,
    PaginatedResponse,
    Request,
    Response,
)

from ..order.schemas import OrderType


class TriggerType(str, Enum):
    STOP = "stop"
    TRAILING_STOP = "trailing_stop"
    TAKE_PROFIT = "take_profit"


class TriggerOrderStatus(str, Enum):
    OPEN = "open"
    CANCELLED = "cancelled"
    TRIGGERED = "triggered"


class TriggerOrder(BaseModel):
    id: int
    created_at: str
    error: Optional[str]
    future: str
    market: str
    reduce_only: bool
    side: Side
    size: float
    status: TriggerOrderStatus
    trail_start: Optional[str]
    trail_value: Optional[str]
    trigger_price: float
    triggered_at: Optional[str]
    type: TriggerType
    order_type: OrderType
    filled_size: float
    avg_fill_price: Optional[float]
    retry_until_filled: bool
    order_id: Optional[int]
    order_price: Optional[float]


class GetOpenTriggerOrdersRequest(Request):
    path = "/conditional_orders"
    market: Optional[str]
    type: Optional[TriggerType]


class GetOpenTriggerOrdersResponse(PaginatedResponse[TriggerOrder]):
    pass


""" Trigger """


class Trigger(BaseModel):
    time: str
    order_size: Optional[float]
    filled_size: Optional[float]
    order_id: Optional[int]
    error: Optional[str]


class GetTriggerOrderTriggersRequest(Request):
    path = "/conditional_orders/{conditional_order_id}/triggers"
    order_id: int = Field(..., path=True)


class GetTriggerOrderTriggersResponse(PaginatedResponse[Trigger]):
    pass


""" History """


class GetTriggerOrderHistoryRequest(PaginatedRequest):
    path = "/conditional_orders/history"
    market: Optional[str]
    side: Optional[Side]
    type: Optional[TriggerType]
    order_type: Optional[OrderType]


class GetTriggerOrderHistoryResponse(PaginatedResponse[TriggerOrder]):
    has_more_data: bool


""" Trigger Order """


class CreateTriggerOrderRequest(Request):
    http_method = HTTPMethod.POST
    path = "/conditional_orders"

    market: str
    side: Side
    size: float
    type: TriggerType
    trigger_price: Optional[float]  # for use with stop or take_profie
    order_price: Optional[float]  # for use with stop or take_profie
    trail_value: Optional[
        float
    ]  # for use with trailing_stop. negative for sell, positive for buy.
    reduce_only: Optional[bool]
    retry_until_filled: Optional[bool]


class CreateTriggerOrderResponse(Response[TriggerOrder]):
    pass


class ModifyTriggerOrderRequest(Request):
    http_method = HTTPMethod.POST
    path = "/conditional_orders/{order_id}/modify"

    order_id: int = Field(..., path=True)
    size: float
    trigger_price: Optional[float]
    order_price: Optional[float]
    trail_value: Optional[float]


class ModifyTriggerOrderResponse(Response[TriggerOrder]):
    pass


class CancelTriggerOrderRequest(Request):
    http_method = HTTPMethod.DELETE
    path = "/conditional_orders/{order_id}"

    order_id: int = Field(..., path=True)


class CancelTriggerOrderResponse(Response[str]):
    pass
