from aioftx.session import FTXClientSession

from .schemas import (
    AcceptQuoteRequest,
    AcceptQuoteResponse,
    CancelQuoteRequest,
    CancelQuoteResponse,
    CreateQuoteRequest,
    CreateQuoteResponse,
    GetMyQuotesReponse,
    GetMyQuotesRequest,
    GetQuotesRequest,
    GetQuotesResponse,
    Quote,
)


async def get_quotes_for_request(
    session: FTXClientSession,
    *,
    quote_request_id: str,
) -> Quote:
    """
    Get the quotes for a quote request from the FTX API
    """
    request = GetQuotesRequest(request_id=quote_request_id)
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetQuotesResponse(**data).data()


async def get_my_quotes(
    session: FTXClientSession,
) -> list[Quote]:
    """
    Get my quotes from the FTX API
    """
    request = GetMyQuotesRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetMyQuotesReponse(**data).data()


async def create_quote(
    session: FTXClientSession,
    *,
    quote_request_id: str,
    price: float,
) -> Quote:
    """
    Create a quote for a quote request from the FTX API
    """
    request = CreateQuoteRequest(request_id=quote_request_id, price=price)
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CreateQuoteResponse(**data).data()


async def cancel_quote(
    session: FTXClientSession,
    *,
    quote_id: str,
) -> Quote:
    """
    Cancel a quote from the FTX API
    """
    request = CancelQuoteRequest(quote_id=quote_id)
    async with session.delete(request.url, data=request.json()) as resp:
        data = await resp.json()
        return CancelQuoteResponse(**data).data()


async def accept_quote(
    session: FTXClientSession,
    *,
    quote_id: str,
) -> Quote:
    """
    Accept a quote from the FTX API
    """
    request = AcceptQuoteRequest(quote_id=quote_id)
    async with session.post(request.url, data=request.json()) as resp:
        data = await resp.json()
        return AcceptQuoteResponse(**data).data()
