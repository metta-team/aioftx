from aioftx.session import FTXClientSession

from .schemas import (
    Get24hrOptionVolumeRequest,
    Get24hrOptionVolumeResponse,
    GetOptionalHistoricalVolumeResponse,
    GetOptionHistoricalOpenInterestRequest,
    GetOptionHistoricalOpenInterestResponse,
    GetOptionHistoricalVolumeRequest,
    GetOptionOpenInterestRequest,
    GetOptionOpenInterestResponse,
    OptionHistoricalOpenInterest,
    OptionHistoricalVolume,
    OptionOpenInterest,
    OptionVolume,
)


async def get_24hr_option_volume(session: FTXClientSession) -> list[OptionVolume]:
    """
    Get the 24hr option volume from the FTX API
    """
    request = Get24hrOptionVolumeRequest()
    async with session.get(request.url) as resp:
        data = await resp.json()
        return Get24hrOptionVolumeResponse(**data).data()


async def get_option_historical_volume(
    session: FTXClientSession,
    *,
    symbol: str,
    start_time: int,
    end_time: str,
) -> list[OptionHistoricalVolume]:
    """
    Get the option historical volume from the FTX API
    """
    request = GetOptionHistoricalVolumeRequest(
        symbol=symbol, start_time=start_time, end_time=end_time
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOptionalHistoricalVolumeResponse(**data).data()


async def get_option_open_interest(
    session: FTXClientSession, *, symbol: str, start_time: int, end_time: str
) -> list[OptionOpenInterest]:
    """
    Get the option open interest from the FTX API
    """
    request = GetOptionOpenInterestRequest(
        symbol=symbol, start_time=start_time, end_time=end_time
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOptionOpenInterestResponse(**data).data()


async def get_option_historical_open_interest(
    session: FTXClientSession, *, symbol: str, start_time: int, end_time: str
) -> list[OptionHistoricalOpenInterest]:
    """
    Get the option historical open interest from the FTX API
    """
    request = GetOptionHistoricalOpenInterestRequest(
        symbol=symbol, start_time=start_time, end_time=end_time
    )
    async with session.get(request.url) as resp:
        data = await resp.json()
        return GetOptionHistoricalOpenInterestResponse(**data).data()
