# Source: https://www.helius.dev/docs/api-reference/enhanced-websockets/transactionsubscribe

## Endpoints
Enhanced WebSockets are available on mainnet and devnet:
  * **Mainnet** `wss://mainnet.helius-rpc.com/?api-key=<api-key>`
  * **Devnet** `wss://devnet.helius-rpc.com/?api-key=<api-key>`


WebSockets have a 10-minute inactivity timer; implementing health checks and sending pings every minute is heavily recommended to keep the WebSocket connection alive.
## Authorizations
api-key
string
required
Your Helius API key. You can get one for free in the [dashboard](https://dashboard.helius.dev/api-keys).
## Body
params
array
required
Hide TransactionSubscribeFilter
vote
boolean
Include or exclude vote-related transactions.
failed
boolean
Include or exclude transactions that failed.
signature
string
Filter updates to a specific transaction by its signature.
accountInclude
string[]
List of accounts to receive transaction updates for. A transaction must include **at least one** of these accounts. Supports up to 50,000 addresses.
accountExclude
string[]
List of accounts to exclude from transaction updates. Supports up to 50,000 addresses.
accountRequired
string[]
List of accounts that **must all** be included in a transaction for it to match. Supports up to 50,000 addresses.
Show TransactionSubscribeOptions
commitment
string
Commitment level for fetching data. Can be `processed`, `confirmed`, or `finalized`.
encoding
string
Encoding format for the returned data. Can be `base58`, `base64`, or `jsonParsed`.
transactionDetails
string
Level of detail for the returned transaction data. Can be `full`, `signatures`, `accounts`, or `none`.
showRewards
boolean
Whether to include reward data in the updates.
maxSupportedTransactionVersion
integer
The highest transaction version to receive updates for. Set to `0` to get both legacy and versioned transactions.
Required when `transactionDetails` is set to `"accounts"` or `"full"`.
## Response
result
integer
Subscription id (needed to unsubscribe)
## Managing Subscriptions
### Subscription IDs
When `transactionSubscribe` succeeds, the server returns a subscription ID in the `result` field. This is the same number that appears in `params.subscription` on every notification from that subscription:
Subscribe Response
Notification

```

  "jsonrpc": "2.0",
  "result": 4743323479349712,
  "id": 420


```

Store the subscription ID from the response. You need it to unsubscribe.
### Unsubscribing
To stop receiving notifications, call `transactionUnsubscribe` with the subscription ID. Each `transactionSubscribe` call on the same connection creates a separate subscription with its own ID, so make sure to unsubscribe before resubscribing to avoid receiving duplicate notifications.
Request
Response

```

  "jsonrpc": "2.0",
  "id": 421,
  "method": "transactionUnsubscribe",
  "params": [4743323479349712]


```

A few in-flight messages may still arrive briefly after calling `transactionUnsubscribe`. This is expected behavior.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/laserstream/grpc/ping)[ OverviewComplete API reference for Helius webhook endpoints. Create, update, delete, and manage webhooks for real-time Solana transaction and account notifications. Next ](https://www.helius.dev/docs/api-reference/webhooks)
Request
Code Example

```

  "jsonrpc": "2.0",
  "id": 420,
  "method": "transactionSubscribe",
  "params": [

      "accountInclude": ["675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"]


      "commitment": "processed",
      "encoding": "jsonParsed",
      "transactionDetails": "full",
      "showRewards": true,
      "maxSupportedTransactionVersion": 0




```

Response
Notification

```

  "jsonrpc": "2.0",
  "result": 4743323479349712,
  "id": 420


```

Assistant
Responses are generated using AI and may contain mistakes.
