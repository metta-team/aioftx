from typing import Optional

from aioftx.aioftx.session import FTXClientSession

from .schemas import (
    CreateQuoteRequestRequest,
    CreateQuoteRequestResponse,
    DeleteQuoteRequestRequest,
    DeleteQuoteRequestResponse,
    GetMyQuoteRequestsRequest,
    GetMyQuoteRequestsResponse,
    GetQuoteRequestsRequest,
    GetQuoteRequestsResponse,
    MyQuoteRequest,
    OptionType,
    QuoteRequest,
)


async def get_quote_requests(
    session: FTXClientSession,
) -> list[QuoteRequest]:
    """
    Get the quote requests from the FTX API
    """
    request = GetQuoteRequestsRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetQuoteRequestsResponse(**data).data()


async def get_my_quote_requests(
    session: FTXClientSession,
) -> list[MyQuoteRequest]:
    """
    Get the quote requests from the FTX API
    """
    request = GetMyQuoteRequestsRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetMyQuoteRequestsResponse(**data).data()


async def create_quote_request(
    session: FTXClientSession,
    *,
    underlying: str,
    type: OptionType,
    strike: float,
    expiry: int,
    side: str,
    size: float,
    limit_price: Optional[float] = None,
    hide_limit_price: bool = True,
    request_expiry: Optional[int] = None,
    counterparty_id: Optional[int] = None,
) -> QuoteRequest:
    """
    Create a quote request
    """
    request = CreateQuoteRequestRequest(
        underlying=underlying,
        type=type,
        strike=strike,
        expiry=expiry,
        side=side,
        size=size,
        limit_price=limit_price,
        hide_limit_price=hide_limit_price,
        request_expiry=request_expiry,
        counterparty_id=counterparty_id,
    )
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateQuoteRequestResponse(**data).data()


async def delete_quote_request(
    session: FTXClientSession,
    *,
    id: int,
) -> QuoteRequest:
    """
    Delete a quote request
    """
    request = DeleteQuoteRequestRequest(request_id=id)
    async with session.delete(request.url) as resp:
        data = await resp.json()
        return DeleteQuoteRequestResponse(**data).data()
