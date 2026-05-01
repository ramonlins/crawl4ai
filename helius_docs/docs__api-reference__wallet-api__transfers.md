# Source: https://www.helius.dev/docs/api-reference/wallet-api/transfers

[Skip to main content](https://www.helius.dev/docs/api-reference/wallet-api/transfers#content-area)
New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
Search...
Ctrl K


##### API Reference


##### Solana RPC APIs
  * HTTP Methods
  * WebSocket Methods


##### Solana APIs
  * Helius Sender
  * Digital Asset Standard (DAS)
  * Priority Fee
  * Enhanced Transactions
  * Wallet API (Beta)
    * [ identity](https://www.helius.dev/docs/api-reference/wallet-api/identity)
    * [ balances](https://www.helius.dev/docs/api-reference/wallet-api/balances)
    * [ history](https://www.helius.dev/docs/api-reference/wallet-api/history)
    * [ transfers](https://www.helius.dev/docs/api-reference/wallet-api/transfers)
    * [ funded-by](https://www.helius.dev/docs/api-reference/wallet-api/funded-by)
  * ZK Compression


##### Data Streaming APIs
  * LaserStream gRPC
  * Enhanced WebSockets


##### Event Listening APIs
  * Webhooks


##### Account Management APIs
  * Admin


##### Deprecated APIs
  * Token Metadata
  * Mint


  * English


New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
English
Search...
Ctrl KAsk AI
Search...
Navigation
Wallet API (Beta)
Get Wallet Transfers
GET
/
v1
/
wallet
/
{wallet}
/
transfers
Try it
Get token transfers
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/transfers?limit=50&api-key='
```


```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "timestamp": 1704067200,
      "direction": "in",
      "counterparty": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
      "mint": "So11111111111111111111111111111111111111112",
      "amount": 1.5,
      "amountRaw": "1500000000",
      "decimals": 9,
      "symbol": "SOL"


  "pagination": {
    "hasMore": true,
    "nextCursor": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"


```

> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
##  Request Parameters
wallet
string
required
Solana wallet address (base58 encoded)
limit
number
default:"50"
Maximum number of transfers to return
cursor
string
Pagination cursor from previous response
#### Authorizations
ApiKeyQuery ApiKeyHeaderApiKeyQueryApiKeyHeader
api-key
string
query
required
API key passed as query parameter
#### Path Parameters
wallet
string
required
Solana wallet address (base58 encoded)
Pattern: `^[1-9A-HJ-NP-Za-km-z]{32,44}$`
#### Query Parameters
limit
integer
default:50
Maximum number of transfers to return
Required range: `1 <= x <= 100`
cursor
string
Pagination cursor from previous response
#### Response
application/json
Transfer history retrieved successfully
data
object[]
required
Show child attributes
pagination
object
required
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/wallet-api/history)[ funded-byDiscover which addresses funded a Solana wallet with its initial SOL deposit. Next ](https://www.helius.dev/docs/api-reference/wallet-api/funded-by)
Ctrl+I
Get token transfers
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/transfers?limit=50&api-key='
```


```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "timestamp": 1704067200,
      "direction": "in",
      "counterparty": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
      "mint": "So11111111111111111111111111111111111111112",
      "amount": 1.5,
      "amountRaw": "1500000000",
      "decimals": 9,
      "symbol": "SOL"


  "pagination": {
    "hasMore": true,
    "nextCursor": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"


```

Assistant
Responses are generated using AI and may contain mistakes.
