# Source: https://www.helius.dev/docs/api-reference/wallet-api/balances

[Skip to main content](https://www.helius.dev/docs/api-reference/wallet-api/balances#content-area)
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
Get Wallet Balances
GET
/
v1
/
wallet
/
{wallet}
/
balances
Try it
Get wallet balances
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/balances?page=1&limit=100&showNative=true&api-key='
```


```

  "balances": [

      "mint": "So11111111111111111111111111111111111111112",
      "balance": 1.5,
      "decimals": 9,
      "tokenProgram": "spl-token",
      "symbol": "SOL",
      "name": "Solana",
      "pricePerToken": 145.32,
      "usdValue": 217.98,
      "logoUri": "https://example.com/sol-logo.png"


  "totalUsdValue": 217.98,
  "pagination": {
    "page": 1,
    "limit": 100,
    "hasMore": true

  "nfts": [

      "mint": "7Xq8wXyXVqfBPPqVJjPDwG9zN5wCVxBYZ6z7vPYBzr6F",
      "compressed": false,
      "name": "Degen Ape",
      "imageUri": "https://example.com/nft.png",
      "collectionName": "Degen Ape Academy",
      "collectionAddress": "DegN1dXmU2uYa4n7U9qTh7YNYpK4u8L9qXx7XqYqJfGH"



```

> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
##  Request Parameters
wallet
string
required
Solana wallet address (base58 encoded)
page
number
default:"1"
Page number for pagination (1-indexed)
limit
number
default:"100"
Maximum number of tokens per page
showZeroBalance
boolean
default:"false"
Include tokens with zero balance
showNative
boolean
default:"true"
Include native SOL in results
showNfts
boolean
default:"false"
Include NFTs in results (max 100, first page only)
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
page
integer
default:1
Page number for pagination (1-indexed)
Required range: `x >= 1`
limit
integer
default:100
Maximum number of tokens per page
Required range: `1 <= x <= 100`
showZeroBalance
boolean
default:false
Include tokens with zero balance
showNative
boolean
default:true
Include native SOL in results
showNfts
boolean
default:false
Include NFTs in results (max 100, first page only)
#### Response
application/json
Wallet balances retrieved successfully
balances
object[]
required
Array of token balances for the current page, including native SOL. When showNative=true, SOL appears as the first element with mint address So11111111111111111111111111111111111111112. Other tokens are sorted by USD value (descending).
Show child attributes
totalUsdValue
number
required
Total USD value of balances on this page (not total portfolio value)
Example:
`217.98`
pagination
object
required
Pagination metadata. Users must manually request additional pages using the page parameter.
Show child attributes
nfts
object[]
Array of NFT holdings (only included if showNfts=true, max 100, first page only)
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/wallet-api/identity)[ historyRetrieve the full transaction history for a Solana wallet with pagination. Next ](https://www.helius.dev/docs/api-reference/wallet-api/history)
Ctrl+I
Get wallet balances
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/balances?page=1&limit=100&showNative=true&api-key='
```


```

  "balances": [

      "mint": "So11111111111111111111111111111111111111112",
      "balance": 1.5,
      "decimals": 9,
      "tokenProgram": "spl-token",
      "symbol": "SOL",
      "name": "Solana",
      "pricePerToken": 145.32,
      "usdValue": 217.98,
      "logoUri": "https://example.com/sol-logo.png"


  "totalUsdValue": 217.98,
  "pagination": {
    "page": 1,
    "limit": 100,
    "hasMore": true

  "nfts": [

      "mint": "7Xq8wXyXVqfBPPqVJjPDwG9zN5wCVxBYZ6z7vPYBzr6F",
      "compressed": false,
      "name": "Degen Ape",
      "imageUri": "https://example.com/nft.png",
      "collectionName": "Degen Ape Academy",
      "collectionAddress": "DegN1dXmU2uYa4n7U9qTh7YNYpK4u8L9qXx7XqYqJfGH"



```

Assistant
Responses are generated using AI and may contain mistakes.
