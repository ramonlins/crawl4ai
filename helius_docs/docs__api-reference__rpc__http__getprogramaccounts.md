# Source: https://www.helius.dev/docs/api-reference/rpc/http/getprogramaccounts

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getProgramAccounts
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getProgramAccounts",
  "params": [
    "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T"



```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": [

      "pubkey": "CxELquR1gPP8wHe33gZ4QxqGB3sZ9RSwsJ2KshVewkFY",
      "account": {
        "lamports": 15298080,
        "owner": "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T",
        "data": [
          "2R9jLfiAQ9bgdcw6h8s44439",
          "base58"

        "executable": false,
        "rentEpoch": 28,
        "space": 42




```

**New Feature** : `getProgramAccounts` now supports the `changedSinceSlot` parameter for incremental updates. When specified, the method returns only accounts that have been modified at or after the given slot number. This is perfect for real-time indexing and data synchronization workflows.
## Request Parameters
address
string
required
The Solana program public key (address) to query accounts for, as a base-58 encoded string.
commitment
string
The commitment level for the request.
  * `confirmed`
  * `finalized`
  * `processed`


minContextSlot
number
The minimum slot that the request can be evaluated at.
withContext
boolean
Wrap the result in an RpcResponse JSON object.
encoding
string
Encoding format for the returned account data.
  * `jsonParsed`
  * `base58`
  * `base64`
  * `base64+zstd`


dataSlice
object
Request a slice of the account’s data.
dataSlice.length
number
Number of bytes to return.
dataSlice.offset
number
Byte offset from which to start reading.
changedSinceSlot
number
Only return accounts that were modified at or after this slot number. Useful for incremental updates.
filters
array
Powerful filtering system to efficiently query specific Solana account data patterns.
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
required
The JSON-RPC protocol version.
Available options: 
`2.0`
Example:
`"2.0"`
id
string
default:1
required
A unique identifier for the request.
Example:
`"1"`
method
enum<string>
default:getProgramAccounts
required
The name of the RPC method to invoke.
Available options: 
`getProgramAccounts`
Example:
`"getProgramAccounts"`
params
(string | object)[]
required
Parameters for the method.
The Solana program public key (address) to query accounts for, as a base-58 encoded string.
Example:
`"4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T"`
#### Response
application/json
Successfully retrieved program accounts.
jsonrpc
enum<string>
The JSON-RPC protocol version.
Available options: 
`2.0`
Example:
`"2.0"`
id
string
Identifier matching the request.
Example:
`"1"`
result
object[]
List of program accounts.
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/rpc/http/getmultipleaccounts)[ getProgramAccountsV2Enhanced version of getProgramAccounts with cursor-based pagination and changedSinceSlot support for efficiently querying large sets of accounts owned by specific Solana programs with incremental updates. Next ](https://www.helius.dev/docs/api-reference/rpc/http/getprogramaccountsv2)
getProgramAccounts
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getProgramAccounts",
  "params": [
    "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T"



```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": [

      "pubkey": "CxELquR1gPP8wHe33gZ4QxqGB3sZ9RSwsJ2KshVewkFY",
      "account": {
        "lamports": 15298080,
        "owner": "4Nd1mBQtrMJVYVfKf2PJy9NZUZdTAsp7D4xWLs4gDB4T",
        "data": [
          "2R9jLfiAQ9bgdcw6h8s44439",
          "base58"

        "executable": false,
        "rentEpoch": 28,
        "space": 42




```

Assistant
Responses are generated using AI and may contain mistakes.
