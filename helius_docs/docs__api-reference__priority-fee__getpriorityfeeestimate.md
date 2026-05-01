# Source: https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
cURL
transactionExample

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getPriorityFeeEstimate",
  "params": [

      "transaction": "LxzhDW7TapzziJVHEGPh1QjmZB6kjNqmvuJ9gmihBGEkzw2N8ospDq32UZdVmKWzRZqKuyvhp7xmLvsmmHa3MfxVKpYoLV9cPkw5isHnHgDUwLSMsDaZ4dLEULexXAvuV9k6fLD2LMhFKM6gqH6j69GQLAm1g4e3z5ZVZN6pmJdSmZ4PqKcwNn4sS7E3Abp1hV59uBJB9i4jEdEAh28rZ8WCeNizzEmrJZFhatFFFGSDsk23jDPEjbkMcoRWXKf1WthFScC2S6Wz284Dtjqp7kW8eybV3DpmN9DtBbcfFNQPtUwmiBZCKszdYym5AjJvRHiUKUdMwFpC3toPnMvTmKZ9iHQtzZRkg5xBufRtUN5eVYJfdw2DxzH6RfqhC2rAjfSbfJA4wmaq9f5eUe2iEjmqvne6r85PPcHBJzyqkVtAyUFtTc9DfU8UiM9rFhQ2UB71M6m5UCsC6EwowMw5k8iF8rL7iPCLdubVdy8S58DPLNG4E4rdosev1T63YdRWSgEwBZh7iX4zGBA9AKAm3B9itCSxLSL46Y6uZgVku9UXsMcWWz3URoa6hRbo55CYPLhrVeqjqX5DsXpaG6QkngbEaESQUnkakE1AFkYXmNXEd2m3sLRTYB2o5UTkwkJS2u5sJHyYqAvXr3vFZr7qAYFLD3LwS5tsdb45ZQVQwsbnNddMHgkpmSqLHS6Fv1epxqHbzpRCU1tgMsriApVWC3pj2LLD41HxkV8aKvkVyHgJFACUtbvRBZAasHf1F71Gz3qZNTdh3efWsZJRXnfxKPbATU7NTMaMUL8JjknfoVwp3/SsAUIMHFzjQMQmoiQMSL1q+S+r9dLR55BgaWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG3fbh12Whk9nL4UbO63msHLSF7V9bN5E6jPWFfv8AqQECAwABDAIAAAAEAAAAAAAA"




```

singleEstimateResponse

```

  "jsonrpc": "2.0",
  "result": {
    "priorityFeeEstimate": 120000

  "id": "1"

```

## Request Parameters
transaction
string
Base58 or Base64 encoded Solana transaction for which to estimate optimal priority fees. The API will analyze the specific instructions and accounts in this transaction to provide accurate fee estimates based on current network conditions and computational complexity.
accountKeys
array
Array of Solana account public keys to estimate priority fees for (alternative to providing a transaction)
options
object
Advanced options for customizing Solana priority fee estimation based on network conditions
options.transactionEncoding
string
Encoding format of the provided Solana transaction
  * `Base58`
  * `Base64`


options.priorityLevel
string
Specific priority level to estimate fees for based on current Solana network congestion
  * `Min`
  * `Low`
  * `Medium`
  * `High`
  * `VeryHigh`
  * `UnsafeMax`


options.includeAllPriorityFeeLevels
boolean
When true, returns comprehensive estimates for all priority levels from minimum to maximum
options.lookbackSlots
number
Number of recent Solana blockchain slots to analyze for accurate fee estimation (1-150)
options.includeVote
boolean
When true, includes vote transactions in the fee calculation for more comprehensive analysis
options.recommended
boolean
When true, returns the recommended optimal fee based on current Solana network conditions
options.evaluateEmptySlotAsZero
boolean
When true, slots with no transactions are counted as zero-fee slots in the calculation
#### Authorizations
api-key
string
query
required
Your Helius API key. You can get one for free in the [dashboard](https://dashboard.helius.dev/api-keys).
#### Body
application/json
jsonrpc
enum<string>
default:2.0
JSON-RPC version identifier for the Solana RPC API request, must be "2.0"
Available options: 
`2.0`
id
string
default:1
Client-generated identifier for the request
method
enum<string>
default:getPriorityFeeEstimate
The RPC method name
Available options: 
`getPriorityFeeEstimate`
params
object[]
Parameters for the method call
Show child attributes
#### Response
application/json
Successfully retrieved Solana priority fee estimates
jsonrpc
enum<string>
JSON-RPC version identifier
Available options: 
`2.0`
id
string
Client-generated identifier matching the request
result
object
Result object containing comprehensive Solana priority fee estimates
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/searchassets)[ OverviewComplete API reference for Helius Enhanced Transactions endpoints. Parse transactions into human-readable formats including NFT sales, swaps, and transfers. Next ](https://www.helius.dev/docs/api-reference/enhanced-transactions/overview)
cURL
transactionExample

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getPriorityFeeEstimate",
  "params": [

      "transaction": "LxzhDW7TapzziJVHEGPh1QjmZB6kjNqmvuJ9gmihBGEkzw2N8ospDq32UZdVmKWzRZqKuyvhp7xmLvsmmHa3MfxVKpYoLV9cPkw5isHnHgDUwLSMsDaZ4dLEULexXAvuV9k6fLD2LMhFKM6gqH6j69GQLAm1g4e3z5ZVZN6pmJdSmZ4PqKcwNn4sS7E3Abp1hV59uBJB9i4jEdEAh28rZ8WCeNizzEmrJZFhatFFFGSDsk23jDPEjbkMcoRWXKf1WthFScC2S6Wz284Dtjqp7kW8eybV3DpmN9DtBbcfFNQPtUwmiBZCKszdYym5AjJvRHiUKUdMwFpC3toPnMvTmKZ9iHQtzZRkg5xBufRtUN5eVYJfdw2DxzH6RfqhC2rAjfSbfJA4wmaq9f5eUe2iEjmqvne6r85PPcHBJzyqkVtAyUFtTc9DfU8UiM9rFhQ2UB71M6m5UCsC6EwowMw5k8iF8rL7iPCLdubVdy8S58DPLNG4E4rdosev1T63YdRWSgEwBZh7iX4zGBA9AKAm3B9itCSxLSL46Y6uZgVku9UXsMcWWz3URoa6hRbo55CYPLhrVeqjqX5DsXpaG6QkngbEaESQUnkakE1AFkYXmNXEd2m3sLRTYB2o5UTkwkJS2u5sJHyYqAvXr3vFZr7qAYFLD3LwS5tsdb45ZQVQwsbnNddMHgkpmSqLHS6Fv1epxqHbzpRCU1tgMsriApVWC3pj2LLD41HxkV8aKvkVyHgJFACUtbvRBZAasHf1F71Gz3qZNTdh3efWsZJRXnfxKPbATU7NTMaMUL8JjknfoVwp3/SsAUIMHFzjQMQmoiQMSL1q+S+r9dLR55BgaWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG3fbh12Whk9nL4UbO63msHLSF7V9bN5E6jPWFfv8AqQECAwABDAIAAAAEAAAAAAAA"




```

singleEstimateResponse

```

  "jsonrpc": "2.0",
  "result": {
    "priorityFeeEstimate": 120000

  "id": "1"

```

Assistant
Responses are generated using AI and may contain mistakes.
