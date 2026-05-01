# Source: https://www.helius.dev/docs/api-reference/das/getassetsbyauthority

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetsByAuthority
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByAuthority",
  "params": {
    "authorityAddress": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
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
        "content": {
          "$schema": "https://schema.metaplex.com/nft1.0.json",
          "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/6867.json",
          "files": [

              "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/6867.png",
              "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/6867.png",
              "mime": "image/png"



        "authorities": [

            "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
            "scopes": [
              "full"



        "compression": {
          "eligible": false,
          "compressed": false,
          "data_hash": "",
          "creator_hash": "",
          "asset_hash": "",
          "tree": "",
          "seq": 0,
          "leaf_id": 0

        "grouping": [

            "group_key": "collection",
            "group_value": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w"


        "royalty": {
          "royalty_model": "creators",
          "target": null,
          "percent": 0.042,
          "basis_points": 420,
          "primary_sale_happened": true,
          "locked": false

        "creators": [

            "address": "5XvhfmRjwXkGp3jHGmaKpqeerNYjkuZZBYLVQYdeVcRv",
            "share": 0,
            "verified": true


        "ownership": {
          "frozen": true,
          "delegated": false,
          "delegate": null,
          "ownership_model": "single",
          "owner": "3F21SJs4FMpsakrxmd8GjgfQZG6BN6MVsvXcm5Yc6Jcf"

        "burnt": "<unknown>"




```

## Request Parameters
authorityAddress
string
required
The address of the owner whose assets to retrieve.
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
The criteria by which the retrieved assets will be sorted.
  * `created`
  * `recent_action`
  * `updated`
  * `none`


sortBy.sortDirection
string
The direction by which the retrieved assets will be sorted.
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
Displays inscription details of assets inscribed on-chain.
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
default:getAssetsByAuthority
required
The name of the DAS method to invoke.
Available options: 
`getAssetsByAuthority`
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
[Previous](https://www.helius.dev/docs/api-reference/das/getassetproofbatch)[ getAssetsByCreatorRetrieve all Solana NFTs and compressed NFTs created by a specific creator address with optional verified-only filtering Next ](https://www.helius.dev/docs/api-reference/das/getassetsbycreator)
getAssetsByAuthority
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByAuthority",
  "params": {
    "authorityAddress": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
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
        "content": {
          "$schema": "https://schema.metaplex.com/nft1.0.json",
          "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/6867.json",
          "files": [

              "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/6867.png",
              "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/6867.png",
              "mime": "image/png"



        "authorities": [

            "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
            "scopes": [
              "full"



        "compression": {
          "eligible": false,
          "compressed": false,
          "data_hash": "",
          "creator_hash": "",
          "asset_hash": "",
          "tree": "",
          "seq": 0,
          "leaf_id": 0

        "grouping": [

            "group_key": "collection",
            "group_value": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w"


        "royalty": {
          "royalty_model": "creators",
          "target": null,
          "percent": 0.042,
          "basis_points": 420,
          "primary_sale_happened": true,
          "locked": false

        "creators": [

            "address": "5XvhfmRjwXkGp3jHGmaKpqeerNYjkuZZBYLVQYdeVcRv",
            "share": 0,
            "verified": true


        "ownership": {
          "frozen": true,
          "delegated": false,
          "delegate": null,
          "ownership_model": "single",
          "owner": "3F21SJs4FMpsakrxmd8GjgfQZG6BN6MVsvXcm5Yc6Jcf"

        "burnt": "<unknown>"




```

Assistant
Responses are generated using AI and may contain mistakes.
