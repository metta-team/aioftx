import hmac
import time
from typing import Any, Optional, Type, TypeVar

from aiohttp import ClientSession
from aiohttp.client import _RequestContextManager  # type: ignore
from aiohttp.typedefs import StrOrURL

from ..utils.schemas import HTTPMethod, Request, Response

DataType = TypeVar("DataType")
ResponseType = Response[DataType]


class FTXClientSession(ClientSession):
    def __init__(
        self,
        *,
        api_key: str,
        api_secret: str,
        base_url: str = "https://api.ftx.com/",
        **kwargs,  # type: ignore
    ) -> None:
        self.api_secret = api_secret

        super().__init__(
            base_url=base_url,
            headers={
                "FTX-KEY": api_key,
            },
            **kwargs,
        )

    async def make_request(
        self,
        request: Request,
        *,
        response_cls: Optional[Type[Response[DataType]]] = None,
    ) -> DataType:
        json_response = None
        if request.http_method == HTTPMethod.GET:
            async with self.get(request.url) as resp:
                json_response = await resp.json()
        elif request.http_method == HTTPMethod.POST:
            async with self.get(request.url, data=request.json()) as resp:
                json_response = await resp.json()

        if json_response is None:
            raise Exception("Request failed")

        if response_cls:
            return response_cls(**json_response).data()
        else:
            return json_response

    def get(
        self, url: StrOrURL, *, allow_redirects: bool = True, **kwargs: Any
    ) -> _RequestContextManager:
        """Perform HTTP GET request."""
        ts = int(time.time() * 1000)
        signature_payload = f"{ts}GET{url}".encode()
        signature = hmac.new(
            self.api_secret.encode(), signature_payload, "sha256"
        ).hexdigest()

        return super().get(
            url,
            allow_redirects=allow_redirects,
            headers={"FTX_TS": ts, "FTX-SIGN": signature, **self.headers},
            **kwargs,
        )

    def post(
        self, url: StrOrURL, *, data: Any = None, **kwargs: Any
    ) -> _RequestContextManager:
        """Perform HTTP POST request."""
        ts = int(time.time() * 1000)
        signature_payload = f"{ts}POST{url}".encode()
        signature = hmac.new(
            self.api_secret.encode(), signature_payload, "sha256"
        ).hexdigest()

        return super().post(
            url,
            data=data,
            headers={"FTX_TS": ts, "FTX-SIGN": signature, **self.headers},
            **kwargs,
        )

    def put(
        self, url: StrOrURL, *, data: Any = None, **kwargs: Any
    ) -> _RequestContextManager:
        """Perform HTTP PUT request."""
        ts = int(time.time() * 1000)
        signature_payload = f"{ts}PUT{url}".encode()
        signature = hmac.new(
            self.api_secret.encode(), signature_payload, "sha256"
        ).hexdigest()

        return super().put(
            url,
            data=data,
            headers={"FTX_TS": ts, "FTX-SIGN": signature, **self.headers},
            **kwargs,
        )

    def delete(self, url: StrOrURL, **kwargs: Any) -> _RequestContextManager:
        """Perform HTTP DELETE request."""
        ts = int(time.time() * 1000)
        signature_payload = f"{ts}DELETE{url}".encode()
        signature = hmac.new(
            self.api_secret.encode(), signature_payload, "sha256"
        ).hexdigest()

        return super().delete(
            url,
            headers={"FTX_TS": ts, "FTX-SIGN": signature, **self.headers},
            **kwargs,
        )
