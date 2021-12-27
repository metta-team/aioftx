import hmac
import time
from types import SimpleNamespace
from typing import Any, Iterable, Mapping, Optional, Type, TypeVar, Union

from aiohttp import ClientSession
from aiohttp.client import ClientResponse, ClientTimeout
from aiohttp.client_reqrep import Fingerprint
from aiohttp.helpers import BasicAuth, sentinel
from aiohttp.typedefs import LooseCookies, LooseHeaders, StrOrURL

from ..utils.schemas import HTTPMethod, Request, Response

try:
    from ssl import SSLContext
except ImportError:  # pragma: no cover
    SSLContext = object  # type: ignore[misc,assignment]

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

    async def _request(  # type: ignore
        self,
        method: str,
        str_or_url: StrOrURL,
        *,
        params: Optional[Mapping[str, str]] = None,
        data: Any = None,
        json: Any = None,
        cookies: Optional[LooseCookies] = None,
        headers: Optional[LooseHeaders] = None,
        skip_auto_headers: Optional[Iterable[str]] = None,
        auth: Optional[BasicAuth] = None,
        allow_redirects: bool = True,
        max_redirects: int = 10,
        compress: Optional[str] = None,
        chunked: Optional[bool] = None,
        expect100: bool = False,
        raise_for_status: Optional[bool] = None,
        read_until_eof: bool = True,
        proxy: Optional[StrOrURL] = None,
        proxy_auth: Optional[BasicAuth] = None,
        timeout: Union[ClientTimeout, object] = sentinel,
        verify_ssl: Optional[bool] = None,
        fingerprint: Optional[bytes] = None,
        ssl_context: Optional[SSLContext] = None,
        ssl: Optional[Union[SSLContext, bool, Fingerprint]] = None,
        proxy_headers: Optional[LooseHeaders] = None,
        trace_request_ctx: Optional[SimpleNamespace] = None,
        read_bufsize: Optional[int] = None,
    ) -> ClientResponse:
        """Sign & make request."""

        ts = int(time.time() * 1000)
        signature_payload = f"{ts}{method}{str_or_url}".encode()
        signature = hmac.new(
            self.api_secret.encode(), signature_payload, "sha256"
        ).hexdigest()

        return await super()._request(
            method,
            str_or_url,
            params=params,
            data=data,
            json=json,
            cookies=cookies,
            headers={"FTX_TS": str(ts), "FTX-SIGN": signature, **self.headers},
            skip_auto_headers=skip_auto_headers,
            auth=auth,
            allow_redirects=allow_redirects,
            max_redirects=max_redirects,
            compress=compress,
            chunked=chunked,
            expect100=expect100,
            raise_for_status=raise_for_status,
            read_until_eof=read_until_eof,
            proxy=proxy,
            proxy_auth=proxy_auth,
            timeout=timeout,
            verify_ssl=verify_ssl,
            fingerprint=fingerprint,
            ssl_context=ssl_context,
            ssl=ssl,
            proxy_headers=proxy_headers,
            trace_request_ctx=trace_request_ctx,
            read_bufsize=read_bufsize,
        )

    async def make_request(
        self,
        request: Request,
        *,
        response_cls: Optional[Type[Response[DataType]]] = None,
    ) -> DataType:
        """Make request and parse response if response_cls is provided."""

        if request.http_method == HTTPMethod.GET:
            async with self.get(request.url) as resp:
                json_response = await resp.json()
        elif request.http_method == HTTPMethod.POST:
            async with self.post(request.url, data=request.json()) as resp:
                json_response = await resp.json()
        elif request.http_method == HTTPMethod.PUT:
            async with self.put(request.url, data=request.json()) as resp:
                json_response = await resp.json()
        elif request.http_method == HTTPMethod.DELETE:
            async with self.delete(request.url) as resp:
                json_response = await resp.json()
        else:
            raise ValueError(f"Unsupported HTTP method: {request.http_method}")

        if response_cls:
            return response_cls(**json_response).data()
        else:
            return json_response
