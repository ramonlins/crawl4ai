# Source: https://www.helius.dev/docs/api-reference/das/getassetproofbatch

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetProofBatch
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetProofBatch",
  "params": {
    "ids": [
      "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss"




```


```

  "jsonrpc": "2.0",
  "result": {
    "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss": {
      "last_indexed_slot": 365750752,
      "root": "2o6Y6EiY3WXhoaEpei2pHmHLYnHDcEQVhgD89GrGHDBH",
      "proof": [
        "EmJXiXEAhEN3FfNQtBa5hwR8LC5kHvdLsaGCoERosZjK",
        "7NEfhcNPAwbw3L87fjsPqTz2fQdd1CjoLE138SD58FDQ"

      "node_index": 16384,
      "leaf": "6YdZXw49M97mfFTwgQb6kxM2c6eqZkHSaW9XhhoZXtzv",
      "tree_id": "2kuTFCcjbV22wvUmtmgsFR7cas7eZUzAu96jzJUvUcb7",
      "burnt": "<unknown>"


  "id": "my-id"

```

## Request Parameters
ids
array
required
#### Authorizations
api-key
string
query
required
Your Helius API key. You can get one for free in the [dashboard](https://dashboard.helius.dev/api-keys).
#### Query Parameters
api-key
string
required
Your Helius API key required for authenticating batch requests to the Solana compression API.
Example:
`"string"`
#### Body
application/json
jsonrpc
enum<string>
default:2.0
required
The version of the JSON-RPC protocol.
Available options: 
`2.0`
id
string
default:1
required
An ID to identify the request.
method
enum<string>
default:getAssetProofBatch
required
The name of the DAS method to invoke.
Available options: 
`getAssetProofBatch`
params
object
required
Show child attributes
#### Response
application/json
Successful response
jsonrpc
string
Example:
`"2.0"`
result
object
Show child attributes
id
string
Example:
`"my-id"`
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getassetproof)[ getAssetsByAuthorityRetrieve all Solana NFTs, compressed NFTs, and tokens controlled by a specific authority address with pagination support Next ](https://www.helius.dev/docs/api-reference/das/getassetsbyauthority)
getAssetProofBatch
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetProofBatch",
  "params": {
    "ids": [
      "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss"




```


```

  "jsonrpc": "2.0",
  "result": {
    "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss": {
      "last_indexed_slot": 365750752,
      "root": "2o6Y6EiY3WXhoaEpei2pHmHLYnHDcEQVhgD89GrGHDBH",
      "proof": [
        "EmJXiXEAhEN3FfNQtBa5hwR8LC5kHvdLsaGCoERosZjK",
        "7NEfhcNPAwbw3L87fjsPqTz2fQdd1CjoLE138SD58FDQ"

      "node_index": 16384,
      "leaf": "6YdZXw49M97mfFTwgQb6kxM2c6eqZkHSaW9XhhoZXtzv",
      "tree_id": "2kuTFCcjbV22wvUmtmgsFR7cas7eZUzAu96jzJUvUcb7",
      "burnt": "<unknown>"


  "id": "my-id"

```

Assistant
Responses are generated using AI and may contain mistakes.
