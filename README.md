# Asyncio FTX Python API

Requires Python `>3.9,<=3.11`

## Usage

```
# Create Session
from aioftx.api.session import FTXClientSession
session = FTXClientSession(api_key=<INSERT_API_KEY>, api_secret=<INSERT_API_SECRET>)

# Make request using helpers
from aioftx.api.wallet import get_balances
balances = await get_balances(session)

# (OR) Make request using schemas
from aioftx.api.wallet.schemas import GetBalancesRequest, GetBalancesResponse
balances = await session.make_request(GetBalancesRequest(), response_cls=GetBalancesResponse)
```

## Todo

[] Staking API

[] OTC Quotes API

[] Spot Margin API

[] NFT API

[] Latency Stats API
