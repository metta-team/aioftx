# FTX Python API

## Usage

```
from ftx.api.session import FTXClientSession
from ftx.api.wallet import get_balances
from ftx.api.wallet.schemas import GetBalancesRequest, GetBalancesResponse

session = FTXClientSession(api_key=<INSERT_API_KEY>, api_secret=<INSERT_API_SECRET>)

balances = await get_balances(session)

# or
balances = session.make_request(GetBalancesRequest(), response_cls=GetBalancesResponse())


```
