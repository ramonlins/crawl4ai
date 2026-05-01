# Source: https://www.helius.dev/docs/api-reference/das/getassetsbycreator

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetsByCreator
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByCreator",
  "params": {
    "creatorAddress": "D3XrkNZz6wx6cofot7Zohsf2KSsu2ArngNk8VqU9cTY3",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showInscription": false




```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 1,
    "limit": 1,
    "page": 1,
    "items": [

        "interface": "Custom",
        "id": "JEH7cJxAKdprFG5AvdsY2c4ZqojxLBjFmw19zADV6oK5",
        "content": {},
        "authorities": [


        "compression": {},
        "grouping": [


        "royalty": {},
        "creators": [


        "ownership": {}




```

## Request Parameters
creatorAddress
string
required
The Solana wallet address of the creator to retrieve all digital assets for.
page
number
The page of results to return.
limit
number
The maximum number of assets to return.
sortBy
object
The sorting options for the response.
sortBy.sortBy
string
The criteria by which the retrieved Solana assets will be sorted in the response.
  * `created`
  * `recent_action`
  * `updated`
  * `none`


sortBy.sortDirection
string
The direction by which the retrieved Solana assets will be sorted in the response.
  * `asc`
  * `desc`


before
string
The cursor for paginating backwards through the assets.
after
string
The cursor for paginating forwards through the assets.
options
object
The display options for the response.
options.showUnverifiedCollections
boolean
default:"false"
Displays grouping information for unverified collections instead of skipping them.
options.showCollectionMetadata
boolean
default:"false"
Displays metadata for the collection.
options.showGrandTotal
boolean
default:"false"
Shows the total number of assets that matched the query. This will make the request slower.
options.showInscription
boolean
default:"false"
Displays inscription details of Solana assets with on-chain inscriptions.
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
default:getAssetsByCreator
required
The name of the DAS method to invoke.
Available options: 
`getAssetsByCreator`
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
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getassetsbyauthority)[ getAssetsByGroupRetrieve all Solana NFTs and compressed NFTs in a specific collection or group with flexible grouping keys and pagination support Next ](https://www.helius.dev/docs/api-reference/das/getassetsbygroup)
getAssetsByCreator
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByCreator",
  "params": {
    "creatorAddress": "D3XrkNZz6wx6cofot7Zohsf2KSsu2ArngNk8VqU9cTY3",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showInscription": false




```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 1,
    "limit": 1,
    "page": 1,
    "items": [

        "interface": "Custom",
        "id": "JEH7cJxAKdprFG5AvdsY2c4ZqojxLBjFmw19zADV6oK5",
        "content": {},
        "authorities": [


        "compression": {},
        "grouping": [


        "royalty": {},
        "creators": [


        "ownership": {}




```

Assistant
Responses are generated using AI and may contain mistakes.
