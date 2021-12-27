from typing import Optional

from aioftx.aioftx.session import FTXClientSession
from aioftx.shared.schemas import Side

from ..order.schemas import OrderType
from .schemas import (CancelTriggerOrderRequest, CancelTriggerOrderResponse,
                      CreateTriggerOrderRequest, CreateTriggerOrderResponse,
                      GetOpenTriggerOrdersRequest,
                      GetOpenTriggerOrdersResponse,
                      GetTriggerOrderHistoryRequest,
                      GetTriggerOrderHistoryResponse,
                      GetTriggerOrderTriggersRequest,
                      GetTriggerOrderTriggersResponse,
                      ModifyTriggerOrderRequest, ModifyTriggerOrderResponse,
                      Trigger, TriggerOrder, TriggerType)


async def get_open_trigger_orders(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
    type: Optional[TriggerType] = None,
) -> list[TriggerOrder]:
    """
    Get all open orders from the FTX API
    """
    request = GetOpenTriggerOrdersRequest(market=market, type=type)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOpenTriggerOrdersResponse(**data).data()


async def get_trigger_order_triggers(
    session: FTXClientSession,
    *,
    order_id: int,
) -> list[Trigger]:
    """
    Get a specific order from the FTX API
    """
    request = GetTriggerOrderTriggersRequest(order_id=order_id)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetTriggerOrderTriggersResponse(**data).data()


async def get_trigger_order_history(
    session: FTXClientSession,
    *,
    market: Optional[str] = None,
    side: Optional[Side] = None,
    type: Optional[TriggerType] = None,
    order_type: Optional[OrderType] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> list[TriggerOrder]:
    """
    Get trigger order history from the FTX API
    """
    request = GetTriggerOrderHistoryRequest(
        market=market,
        side=side,
        type=type,
        order_type=order_type,
        start_time=start_time,
        end_time=end_time,
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetTriggerOrderHistoryResponse(**data).data()


async def create_trigger_order(
    session: FTXClientSession,
    *,
    market: str,
    side: Side,
    type: TriggerType,
    trigger_price: Optional[float] = None,
    order_price: Optional[float] = None,
    trail_value: Optional[float] = None,
    reduce_only: Optional[bool] = None,
    retry_until_filled: Optional[bool] = None,
) -> TriggerOrder:
    """
    Create a trigger order on the FTX API
    """
    request = CreateTriggerOrderRequest(
        market=market,
        side=side,
        type=type,
        trigger_price=trigger_price,
        order_price=order_price,
        trail_value=trail_value,
        reduce_only=reduce_only,
        retry_until_filled=retry_until_filled,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateTriggerOrderResponse(**data).data()


async def modify_trigger_order(
    session: FTXClientSession,
    *,
    order_id: int,
    size: float,
    trigger_price: Optional[float] = None,
    order_price: Optional[float] = None,
    trail_value: Optional[float] = None,
) -> TriggerOrder:
    """
    Modify a trigger order on the FTX API
    """
    request = ModifyTriggerOrderRequest(
        order_id=order_id,
        trigger_price=trigger_price,
        order_price=order_price,
        trail_value=trail_value,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return ModifyTriggerOrderResponse(**data).data()


async def cancel_trigger_order(
    session: FTXClientSession,
    *,
    order_id: int,
) -> str:
    """
    Cancel a trigger order on the FTX API
    """
    request = CancelTriggerOrderRequest(order_id=order_id)
    async with session.post(request.url) as resp:
        data = await resp.json()
        return CancelTriggerOrderResponse(**data).data()
