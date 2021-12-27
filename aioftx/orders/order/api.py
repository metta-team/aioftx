from typing import Optional

from aioftx.session import FTXClientSession
from aioftx.types import Side

from .schemas import (
    CancelAllOrdersRequest,
    CancelAllOrdersResponse,
    CancelOrderRequest,
    CancelOrderResponse,
    CreateOrderRequest,
    CreateOrderResponse,
    GetOpenOrdersRequest,
    GetOpenOrdersResponse,
    GetOrderHistoryRequest,
    GetOrderHistoryResponse,
    GetOrderStatusRequest,
    GetOrderStatusResponse,
    ModifyOrderByClientIdRequest,
    ModifyOrderByClientIdResponse,
    ModifyOrderRequest,
    ModifyOrderResponse,
    Order,
)


async def get_order_status(
    session: FTXClientSession,
    *,
    order_id: int,
) -> Order:
    """
    Get a specific order from the FTX API
    """
    request = GetOrderStatusRequest(
        order_id=order_id,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOrderStatusResponse(**data).data()


async def get_open_orders(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
) -> list[Order]:
    """
    Get all open orders from the FTX API
    """
    request = GetOpenOrdersRequest(
        market=market,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOpenOrdersResponse(**data).data()


async def get_order_history(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
    side: Optional[str] = None,
    order_type: Optional[str] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[Order]:
    """
    Get all order history from the FTX API
    """
    request = GetOrderHistoryRequest(
        market=market,
        side=side,
        order_type=order_type,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOrderHistoryResponse(**data).data()


async def create_order(
    session: FTXClientSession,
    *,
    market: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float,
    reduce_only: bool,
    client_id: Optional[str] = None,
    reject_on_price_band: Optional[bool] = None,
    reject_after_ts: Optional[int] = None,
) -> Order:
    """
    Create an order on the FTX API
    """
    request = CreateOrderRequest(
        market=market,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
        reduce_only=reduce_only,
        client_id=client_id,
        reject_on_price_band=reject_on_price_band,
        reject_after_ts=reject_after_ts,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateOrderResponse(**data).data()


async def modify_order(
    session: FTXClientSession,
    *,
    order_id: int,
    price: Optional[float] = None,
    size: Optional[float] = None,
    client_id: Optional[str] = None,
) -> Order:
    """
    Modify an order on the FTX API
    """
    request = ModifyOrderRequest(
        order_id=order_id, price=price, size=size, client_id=client_id
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return ModifyOrderResponse(**data).data()


async def modify_order_by_client_id(
    session: FTXClientSession,
    *,
    client_id: int,
    price: Optional[float] = None,
    size: Optional[float] = None,
) -> Order:
    """
    Modify an order on the FTX API
    """
    request = ModifyOrderByClientIdRequest(
        client_id=client_id,
        price=price,
        size=size,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return ModifyOrderByClientIdResponse(**data).data()


async def cancel_order(
    session: FTXClientSession,
    *,
    order_id: int,
) -> str:
    """
    Cancel an order on the FTX API
    """
    request = CancelOrderRequest(
        order_id=order_id,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CancelOrderResponse(**data).data()


async def cancel_all_orders(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
    side: Optional[Side] = None,
    conditional_orders_only: Optional[bool] = None,
    limit_orders_only: Optional[bool] = None,
) -> str:
    """
    Cancel all orders on the FTX API
    """
    request = CancelAllOrdersRequest(
        market=market,
        side=side,
        conditional_orders_only=conditional_orders_only,
        limit_orders_only=limit_orders_only,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CancelAllOrdersResponse(**data).data()
