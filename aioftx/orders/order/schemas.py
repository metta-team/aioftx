from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, validator

from aioftx.shared.schemas import Side
from aioftx.utils.schemas import (HTTPMethod, PaginatedRequest,
                                  PaginatedResponse, Request, Response)


class OrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"


class OrderStatus(str, Enum):
    NEW = "new"
    OPEN = "open"
    CLOSED = "closed"


class Order(BaseModel):
    avg_fill_price: float
    client_id: Optional[str]
    created_at: str
    filled_size: float
    future: str
    id: int
    ioc: bool
    market: str
    post_only: bool
    price: float
    reduce_only: bool
    remaining_size: float
    side: Side
    size: float
    status: OrderStatus
    type: OrderType


""" Order Status """


class GetOrderStatusRequest(Request):
    path = "/orders/{order_id}"

    order_id: int


class GetOrderStatusResponse(Response[Order]):
    pass


""" Open Orders """


class GetOpenOrdersRequest(Request):
    path = "/orders"
    market: str


class GetOpenOrdersResponse(PaginatedResponse[Order]):
    pass


""" History """


class GetOrderHistoryRequest(PaginatedRequest):
    path = "/orders/history"
    market: Optional[str]
    side: Optional[str]
    order_type: Optional[str]


class GetOrderHistoryResponse(PaginatedResponse[Order]):
    pass


""" Orders """


class CreateOrderRequest(Request):
    http_method = HTTPMethod.POST
    path = "/orders"

    market: str
    side: Side
    size: float
    price: float
    type: OrderType
    reduce_only: bool
    ioc: bool
    post_only: bool
    client_id: Optional[str]
    reject_on_price_band: Optional[bool]
    reject_after_ts: Optional[int]


class CreateOrderResponse(Response[Order]):
    pass


class ModifyOrderRequest(Request):
    http_method = HTTPMethod.POST
    path = "/orders/{id}/modify"

    order_id: int = Field(..., path=True)
    price: Optional[float]
    size: Optional[float]
    client_id: Optional[str]

    @validator("price", "size")
    def check_payload(cls, v: tuple[Optional[float], Optional[float]]):
        if v[0] is None and v[1] is None:
            raise ValueError("Either price or size must be specified")
        return v


class ModifyOrderResponse(Response[Order]):
    pass


class ModifyOrderByClientIdRequest(Request):
    http_method = HTTPMethod.POST
    path = "/orders/by_client_id/{client_id}/modify"

    client_id: int = Field(..., path=True)
    price: float
    size: float

    @validator("price", "size")
    def check_payload(cls, v: tuple[Optional[float], Optional[float]]):
        if v[0] is None and v[1] is None:
            raise ValueError("Either price or size must be specified")
        return v


class ModifyOrderByClientIdResponse(Response[Order]):
    pass


class CancelOrderRequest(Request):
    http_method = HTTPMethod.DELETE
    path = "/orders/{order_id}"

    order_id: int = Field(..., path=True)


class CancelOrderResponse(Response[str]):
    pass


class CancelAllOrdersRequest(Request):
    http_method = HTTPMethod.DELETE
    path = "/orders"

    market: Optional[str]
    side: Optional[str]
    conditional_orders_only: Optional[bool]
    limit_orders_only: Optional[bool]


class CancelAllOrdersResponse(Response[str]):
    pass
