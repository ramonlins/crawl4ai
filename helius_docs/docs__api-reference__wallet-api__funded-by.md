# Source: https://www.helius.dev/docs/api-reference/wallet-api/funded-by

GET
/
v1
/
wallet
/
{wallet}
/
funded-by
Try it
Get wallet funding source
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/funded-by?api-key='
```


```

  "funder": "2ojv9BAiHUrvsm9gxDe7fJSzbNZSJcxZvf8dqmWGHG8S",
  "mint": "So11111111111111111111111111111111111111112",
  "symbol": "SOL",
  "amount": 0.05,
  "amountRaw": "50000000",
  "decimals": 9,
  "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
  "timestamp": 1704067200,
  "date": "2024-01-01T00:00:00.000Z",
  "slot": 250000000,
  "explorerUrl": "https://orbmarkets.io/tx/5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
  "funderName": "Coinbase 2",
  "funderType": "exchange"

```

## Request Parameters
wallet
string
required
Solana wallet address (base58 encoded)
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
#### Response
application/json
Funding source identified
funder
string
required
Address that originally funded this wallet
Example:
`"2ojv9BAiHUrvsm9gxDe7fJSzbNZSJcxZvf8dqmWGHG8S"`
mint
string
required
Token mint address (So11111111111111111111111111111111111111112 for SOL)
Example:
`"So11111111111111111111111111111111111111112"`
symbol
string
required
Token symbol
Example:
`"SOL"`
amount
number
required
Initial funding amount (human-readable, in SOL)
Example:
`0.05`
amountRaw
string
required
Raw funding amount in smallest unit (lamports for SOL)
Example:
`"50000000"`
decimals
integer
required
Token decimals
Example:
signature
string
required
Transaction signature of the funding transfer
Example:
`"5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"`
timestamp
integer
required
Unix timestamp in seconds
Example:
`1704067200`
date
string<date-time>
required
Human-readable UTC date in ISO 8601 format
Example:
`"2024-01-01T00:00:00.000Z"`
slot
integer
required
Slot number
Example:
`250000000`
explorerUrl
string
required
Solana Explorer URL for the transaction
Example:
`"https://orbmarkets.io/tx/5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"`
funderName
string | null
Name of the funder if it's a known entity
Example:
`"Coinbase 2"`
funderType
string | null
Type of the funder entity
Example:
`"exchange"`
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/wallet-api/transfers)[ OverviewComplete API reference for ZK compression endpoints. Query compressed accounts, balances, token holders, proofs, and transaction signatures on Solana. Next ](https://www.helius.dev/docs/api-reference/zk-compression)
Get wallet funding source
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/funded-by?api-key='
```


```

  "funder": "2ojv9BAiHUrvsm9gxDe7fJSzbNZSJcxZvf8dqmWGHG8S",
  "mint": "So11111111111111111111111111111111111111112",
  "symbol": "SOL",
  "amount": 0.05,
  "amountRaw": "50000000",
  "decimals": 9,
  "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
  "timestamp": 1704067200,
  "date": "2024-01-01T00:00:00.000Z",
  "slot": 250000000,
  "explorerUrl": "https://orbmarkets.io/tx/5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
  "funderName": "Coinbase 2",
  "funderType": "exchange"

```

Assistant
Responses are generated using AI and may contain mistakes.
