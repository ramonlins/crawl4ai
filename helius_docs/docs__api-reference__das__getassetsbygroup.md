# Source: https://www.helius.dev/docs/api-reference/das/getassetsbygroup

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetsByGroup
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByGroup",
  "params": {
    "groupKey": "collection",
    "groupValue": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w",
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

        "interface": "ProgrammableNFT",
        "id": "JEGruwYE13mhX2wi2MGrPmeLiVyZtbBptmVy9vG3pXRC",
        "authorities": "<array>",
        "compression": {},
        "grouping": "<array>",
        "royalty": {},
        "creators": "<array>",
        "ownership": {},
        "supply": {},
        "mutable": true,
        "burnt": false




```

## Request Parameters
groupKey
string
required
The Solana group classification type to search by (e.g., ‘collection’, ‘community’, ‘creator’, etc.).
groupValue
string
required
The Solana collection address or group identifier to retrieve all matching NFTs for.
page
number
The page number for paginating through the Solana collection results.
limit
number
The maximum number of Solana NFTs to return per request from this collection.
sortBy
object
The sorting options for the response.
sortBy.sortBy
string
The criteria by which the retrieved Solana NFTs in the collection will be sorted.
  * `created`
  * `recent_action`
  * `updated`
  * `none`


sortBy.sortDirection
string
The direction by which the retrieved Solana NFTs in the collection will be sorted.
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
Displays inscription details for Solana NFTs with on-chain inscriptions in the collection.
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
default:getAssetsByGroup
required
The name of the DAS method to invoke.
Available options: 
`getAssetsByGroup`
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
[Previous](https://www.helius.dev/docs/api-reference/das/getassetsbycreator)[ getAssetsByOwnerRetrieve all Solana NFTs, compressed NFTs, and fungible tokens owned by a specific wallet address with sorting and pagination options Next ](https://www.helius.dev/docs/api-reference/das/getassetsbyowner)
getAssetsByGroup
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByGroup",
  "params": {
    "groupKey": "collection",
    "groupValue": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w",
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

        "interface": "ProgrammableNFT",
        "id": "JEGruwYE13mhX2wi2MGrPmeLiVyZtbBptmVy9vG3pXRC",
        "authorities": "<array>",
        "compression": {},
        "grouping": "<array>",
        "royalty": {},
        "creators": "<array>",
        "ownership": {},
        "supply": {},
        "mutable": true,
        "burnt": false




```

Assistant
Responses are generated using AI and may contain mistakes.
