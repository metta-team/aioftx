from enum import Enum
from typing import Any, Generic, Optional, TypeVar, Union
from urllib.parse import urlencode

from pydantic import BaseModel

T = TypeVar("T")


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class ResponseOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class Request(BaseModel):
    http_method: HTTPMethod = HTTPMethod.GET
    path: str

    def dict(  # type: ignore
        self,
        *,
        include: Optional[set[Union[str, int]]] = None,
        exclude: Optional[set[Union[str, int]]] = None,
        by_alias: bool = False,
        skip_defaults: bool = None,  # type: ignore
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = True
    ) -> dict[str, Any]:
        if exclude is None:
            exclude = set()

        for f in self.__fields__:
            field_info = self.__fields__[f].field_info
            if "path" in field_info.extra and field_info.extra["path"] is True:  # type: ignore
                exclude.add(f)

        return super().dict(
            include=include,  # type: ignore
            exclude={"http_method", "path", *exclude},
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )

    @property
    def url(self):
        required_params: dict[str, Any] = {}
        for f in self.__fields__:
            field_info = self.__fields__[f].field_info
            if "path" in field_info.extra and field_info.extra["path"] is True:  # type: ignore
                required_params[f] = getattr(self, f)

        result = self.path.format(**required_params)

        optional_params = self.dict()
        if optional_params:
            result += "?" + urlencode(optional_params)
        return result


class PaginatedRequest(Request):
    start_time: Optional[int]
    end_time: Optional[int]

    # TODO: add validation for start_time and end_time


class Response(BaseModel, Generic[T]):
    success: bool
    result: Optional[T]

    def data(self) -> T:
        if not self.success or self.result is None:
            raise ValueError("Response was not successful")
        return self.result


class PaginatedResponse(BaseModel, Generic[T]):
    success: bool
    result: Optional[list[T]]

    def data(self) -> list[T]:
        if not self.success or self.result is None:
            raise ValueError("Response was not successful")
        return self.result


class KeyedPaginatedResponse(BaseModel, Generic[T]):
    success: bool
    result: dict[str, list[T]]

    def data(self) -> dict[str, list[T]]:
        if not self.success or self.result is None:
            raise ValueError("Response was not successful")
        return self.result
