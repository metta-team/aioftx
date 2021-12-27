from enum import Enum

from pydantic import BaseModel


class OptionType(str, Enum):
    CALL = "call"
    PUT = "put"


class OptionStatus(str, Enum):
    OPEN = "open"


class Option(BaseModel):
    underlying: str
    type: OptionType
    strike: float
    expiry: str
