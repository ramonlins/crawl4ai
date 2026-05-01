# Source: https://www.helius.dev/docs/api-reference/wallet-api/history

[Skip to main content](https://www.helius.dev/docs/api-reference/wallet-api/history#content-area)
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
Get Wallet History
GET
/
v1
/
wallet
/
{wallet}
/
history
Try it
Get transaction history
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/history?limit=100&tokenAccounts=balanceChanged&api-key='
```


```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "slot": 250000000,
      "fee": 0.000005,
      "feePayer": "GQUtvPx89ZNCwmvQqFmH59bJcU8fW8siETpaxod7Aydz",
      "balanceChanges": [

          "mint": "So11111111111111111111111111111111111111112",
          "amount": -0.05,
          "decimals": 9


      "timestamp": 1704067200,
      "error": null


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
default:"100"
Maximum number of transactions per request
before
string
Fetch transactions before this signature (use `pagination.nextCursor` from previous response)
after
string
Fetch transactions after this signature (for ascending order pagination)
type
string
Filter by transaction type. Available types: SWAP, TRANSFER, NFT_SALE, NFT_BID, NFT_LISTING, NFT_MINT, NFT_CANCEL_LISTING, TOKEN_MINT, BURN, COMPRESSED_NFT_MINT, COMPRESSED_NFT_TRANSFER, COMPRESSED_NFT_BURN, CREATE_STORE, WHITELIST_CREATOR, ADD_TO_WHITELIST, REMOVE_FROM_WHITELIST, AUCTION_MANAGER_CLAIM_BID, EMPTY_PAYMENT_ACCOUNT, UPDATE_PRIMARY_SALE_METADATA, ADD_TOKEN_TO_VAULT, ACTIVATE_VAULT, INIT_VAULT, INIT_BANK, INIT_STAKE, MERGE_STAKE, SPLIT_STAKE, CREATE_AUCTION_MANAGER, START_AUCTION, CREATE_AUCTION_MANAGER_V2, UPDATE_EXTERNAL_PRICE_ACCOUNT, EXECUTE_TRANSACTION
  * `SWAP`
  * `TRANSFER`
  * `NFT_SALE`
  * `NFT_BID`
  * `NFT_LISTING`
  * `NFT_MINT`
  * `NFT_CANCEL_LISTING`
  * `TOKEN_MINT`
  * `BURN`
  * `COMPRESSED_NFT_MINT`
  * `COMPRESSED_NFT_TRANSFER`
  * `COMPRESSED_NFT_BURN`
  * `CREATE_STORE`
  * `WHITELIST_CREATOR`
  * `ADD_TO_WHITELIST`
  * `REMOVE_FROM_WHITELIST`
  * `AUCTION_MANAGER_CLAIM_BID`
  * `EMPTY_PAYMENT_ACCOUNT`
  * `UPDATE_PRIMARY_SALE_METADATA`
  * `ADD_TOKEN_TO_VAULT`
  * `ACTIVATE_VAULT`
  * `INIT_VAULT`
  * `INIT_BANK`
  * `INIT_STAKE`
  * `MERGE_STAKE`
  * `SPLIT_STAKE`
  * `CREATE_AUCTION_MANAGER`
  * `START_AUCTION`
  * `CREATE_AUCTION_MANAGER_V2`
  * `UPDATE_EXTERNAL_PRICE_ACCOUNT`
  * `EXECUTE_TRANSACTION`


tokenAccounts
string
default:"balanceChanged"
Filter transactions involving token accounts owned by the wallet.
  * `balanceChanged` (recommended): Includes transactions that changed token balances, filters spam
  * `none`: Only transactions directly referencing the wallet
  * `all`: All transactions including token accounts (may include spam) 
    * `none`
    * `balanceChanged`
    * `all`


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
default:100
Maximum number of transactions per request
Required range: `1 <= x <= 100`
before
string
Fetch transactions before this signature (use `pagination.nextCursor` from previous response)
after
string
Fetch transactions after this signature (for ascending order pagination)
type
enum<string>
Filter by transaction type. Available types: SWAP, TRANSFER, NFT_SALE, NFT_BID, NFT_LISTING, NFT_MINT, NFT_CANCEL_LISTING, TOKEN_MINT, BURN, COMPRESSED_NFT_MINT, COMPRESSED_NFT_TRANSFER, COMPRESSED_NFT_BURN, CREATE_STORE, WHITELIST_CREATOR, ADD_TO_WHITELIST, REMOVE_FROM_WHITELIST, AUCTION_MANAGER_CLAIM_BID, EMPTY_PAYMENT_ACCOUNT, UPDATE_PRIMARY_SALE_METADATA, ADD_TOKEN_TO_VAULT, ACTIVATE_VAULT, INIT_VAULT, INIT_BANK, INIT_STAKE, MERGE_STAKE, SPLIT_STAKE, CREATE_AUCTION_MANAGER, START_AUCTION, CREATE_AUCTION_MANAGER_V2, UPDATE_EXTERNAL_PRICE_ACCOUNT, EXECUTE_TRANSACTION
Available options: 
`SWAP`, 
`TRANSFER`, 
`NFT_SALE`, 
`NFT_BID`, 
`NFT_LISTING`, 
`NFT_MINT`, 
`NFT_CANCEL_LISTING`, 
`TOKEN_MINT`, 
`BURN`, 
`COMPRESSED_NFT_MINT`, 
`COMPRESSED_NFT_TRANSFER`, 
`COMPRESSED_NFT_BURN`, 
`CREATE_STORE`, 
`WHITELIST_CREATOR`, 
`ADD_TO_WHITELIST`, 
`REMOVE_FROM_WHITELIST`, 
`AUCTION_MANAGER_CLAIM_BID`, 
`EMPTY_PAYMENT_ACCOUNT`, 
`UPDATE_PRIMARY_SALE_METADATA`, 
`ADD_TOKEN_TO_VAULT`, 
`ACTIVATE_VAULT`, 
`INIT_VAULT`, 
`INIT_BANK`, 
`INIT_STAKE`, 
`MERGE_STAKE`, 
`SPLIT_STAKE`, 
`CREATE_AUCTION_MANAGER`, 
`START_AUCTION`, 
`CREATE_AUCTION_MANAGER_V2`, 
`UPDATE_EXTERNAL_PRICE_ACCOUNT`, 
`EXECUTE_TRANSACTION`
tokenAccounts
enum<string>
default:balanceChanged
Filter transactions involving token accounts owned by the wallet.
  * `balanceChanged` (recommended): Includes transactions that changed token balances, filters spam
  * `none`: Only transactions directly referencing the wallet
  * `all`: All transactions including token accounts (may include spam)


Available options: 
`none`, 
`balanceChanged`, 
`all`
#### Response
application/json
Transaction history retrieved successfully
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
[Previous](https://www.helius.dev/docs/api-reference/wallet-api/balances)[ transfersRetrieve all token and SOL transfers for a Solana wallet address with pagination. Next ](https://www.helius.dev/docs/api-reference/wallet-api/transfers)
Ctrl+I
Get transaction history
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/history?limit=100&tokenAccounts=balanceChanged&api-key='
```


```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "slot": 250000000,
      "fee": 0.000005,
      "feePayer": "GQUtvPx89ZNCwmvQqFmH59bJcU8fW8siETpaxod7Aydz",
      "balanceChanges": [

          "mint": "So11111111111111111111111111111111111111112",
          "amount": -0.05,
          "decimals": 9


      "timestamp": 1704067200,
      "error": null


  "pagination": {
    "hasMore": true,
    "nextCursor": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"


```

Assistant
Responses are generated using AI and may contain mistakes.
