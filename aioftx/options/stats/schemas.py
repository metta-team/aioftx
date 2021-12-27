import datetime

from aioftx.http import PaginatedRequest, PaginatedResponse
from pydantic import BaseModel, Field

""" Option Volume """


class OptionVolume(BaseModel):
    contracts: float
    underlying_total: float


class Get24hrOptionVolumeRequest(PaginatedRequest):
    path = "/options/24hr_options_volumes"


class Get24hrOptionVolumeResponse(PaginatedResponse[OptionVolume]):
    pass


class OptionHistoricalVolume(BaseModel):
    num_contracts: float
    start_time: datetime.datetime
    end_time: datetime.datetime


class GetOptionHistoricalVolumeRequest(PaginatedRequest):
    path = "/options/historical_volumes/{symbol}"

    symbol: str = Field(..., path=True)


class GetOptionalHistoricalVolumeResponse(PaginatedResponse[OptionHistoricalVolume]):
    pass


""" Option Interest """


class OptionOpenInterest(BaseModel):
    open_interest: float


class GetOptionOpenInterestRequest(PaginatedRequest):
    path = "/options/open_interest/{symbol}"

    symbol: str = Field(..., path=True)


class GetOptionOpenInterestResponse(PaginatedResponse[OptionOpenInterest]):
    pass


class OptionHistoricalOpenInterest(BaseModel):
    num_contracts: float
    time: datetime.datetime


class GetOptionHistoricalOpenInterestRequest(PaginatedRequest):
    path = "/options/historical_open_interest/{symbol}"

    symbol: str = Field(..., path=True)


class GetOptionHistoricalOpenInterestResponse(
    PaginatedResponse[OptionHistoricalOpenInterest]
):
    pass
