# Source: https://www.helius.dev/docs/api-reference/rpc/http/gettransaction

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getTransaction
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getTransaction",
  "params": [
    "2nBhEBYYvfaAe16UMNqRHre4YNSskvuYgx3M6E4JP1oDYvZEJHvoPzyUidNgNX5r9sTyN1J9UxtbCXy2rqYcuyuv",

      "commitment": "finalized"




```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "slot": 430,
    "transaction": {
      "message": {
        "accountKeys": [
          "3UVYmECPPMZSCqWKfENfuoTv51fTDTWicX9xmBD2euKe"

        "header": {
          "numReadonlySignedAccounts": 0,
          "numReadonlyUnsignedAccounts": 3,
          "numRequiredSignatures": 1

        "instructions": [

            "accounts": [


            "data": "37u9WtQpcm6ULa3WRQHmj49EPs4if7o9f1jSRVZpm2dvihR9C8jY4NqEwXUbLwx15HBSNcP1",
            "programIdIndex": 4


        "recentBlockhash": "mfcyqEXB3DnHXki6KjjmZck6YjmZLvpAByy2fj4nh6B"

      "signatures": [
        "2nBhEBYYvfaAe16UMNqRHre4YNSskvuYgx3M6E4JP1oDYvZEJHvoPzyUidNgNX5r9sTyN1J9UxtbCXy2rqYcuyuv"


    "meta": {
      "err": null,
      "fee": 5000,
      "innerInstructions": [





```

## Request Parameters
transaction
string
required
Solana transaction signature as a base-58 encoded string for lookup.
transaction
string
required
Encoding format for the returned Solana transaction data.
  * `json`
  * `jsonParsed`
  * `base64`
  * `base58`


commitment
string
Blockchain commitment level for transaction finality verification.
  * `confirmed`
  * `finalized`


maxSupportedTransactionVersion
number
Maximum Solana transaction version to return in responses (for versioned transaction support).
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
The JSON-RPC protocol version.
Available options: 
`2.0`
Example:
`"2.0"`
id
string
default:1
A unique identifier for the request.
Example:
`"1"`
method
enum<string>
default:getTransaction
The name of the RPC method to invoke.
Available options: 
`getTransaction`
Example:
`"getTransaction"`
params
(string | enum<string> | object)[]
Parameters for querying a Solana transaction by signature.
Solana transaction signature as a base-58 encoded string for lookup.
Example:
`"D13jTJYXoQBcRY9AfT5xRtsew7ENgCkNs6mwwwAcUCp4ZZCEM7YwZ7en4tVsoDa7Gu75Jjj2FgLXNUz8Zmgedff"`
#### Response
application/json
Successfully retrieved the detailed Solana transaction data.
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
object
Complete Solana transaction details including execution data.
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/rpc/http/gettokensupply)[ getTransactionCountReturns the current Transaction count from the ledger. Next ](https://www.helius.dev/docs/api-reference/rpc/http/gettransactioncount)
getTransaction
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getTransaction",
  "params": [
    "2nBhEBYYvfaAe16UMNqRHre4YNSskvuYgx3M6E4JP1oDYvZEJHvoPzyUidNgNX5r9sTyN1J9UxtbCXy2rqYcuyuv",

      "commitment": "finalized"




```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "slot": 430,
    "transaction": {
      "message": {
        "accountKeys": [
          "3UVYmECPPMZSCqWKfENfuoTv51fTDTWicX9xmBD2euKe"

        "header": {
          "numReadonlySignedAccounts": 0,
          "numReadonlyUnsignedAccounts": 3,
          "numRequiredSignatures": 1

        "instructions": [

            "accounts": [


            "data": "37u9WtQpcm6ULa3WRQHmj49EPs4if7o9f1jSRVZpm2dvihR9C8jY4NqEwXUbLwx15HBSNcP1",
            "programIdIndex": 4


        "recentBlockhash": "mfcyqEXB3DnHXki6KjjmZck6YjmZLvpAByy2fj4nh6B"

      "signatures": [
        "2nBhEBYYvfaAe16UMNqRHre4YNSskvuYgx3M6E4JP1oDYvZEJHvoPzyUidNgNX5r9sTyN1J9UxtbCXy2rqYcuyuv"


    "meta": {
      "err": null,
      "fee": 5000,
      "innerInstructions": [





```

Assistant
Responses are generated using AI and may contain mistakes.
