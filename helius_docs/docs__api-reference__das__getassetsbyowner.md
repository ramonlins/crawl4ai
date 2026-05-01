# Source: https://www.helius.dev/docs/api-reference/das/getassetsbyowner

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetsByOwner
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByOwner",
  "params": {
    "ownerAddress": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showFungible": false,
      "showNativeBalance": false,
      "showInscription": false,
      "showZeroBalance": false




```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 1,
    "limit": 1,
    "page": 1,
    "items": [

        "interface": "V1_NFT",
        "id": "JCfTS6dmJZY4NXhjMwHqayGGHUwxp59pzcYhZrYqMBce",
        "content": {
          "$schema": "https://schema.metaplex.com/nft1.0.json",
          "json_uri": "https://www.hi-hi.vip/json/5000wif.json",
          "files": [

              "uri": "https://img.hi-hi.vip/json/img/5000wif.png",
              "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://img.hi-hi.vip/json/img/5000wif.png",
              "mime": "image/png"



        "authorities": [

            "address": "2iVwwSHr7hGR6wxNuQM8ArQYnX6Mzy2yeFnhBGgQetRw",
            "scopes": [
              "full"



        "compression": {
          "eligible": false,
          "compressed": true,
          "data_hash": "7zquDVS1VKu9HDh4WS4ray5ozLThiK6xrnFNhJtusj65",
          "creator_hash": "6v7GeYRiVML5mG1kJqi6eujN9sPB3ziCZJF4Vartj1qd",
          "asset_hash": "8gQZkgZ1L91qkNPtsiRGkRzpNcEfhBABEQr1D3wquB8H",
          "tree": "BZNn9zX1MysbSvqyGZ33Seb8bvimaiE9fxmLKwX2Euae",
          "seq": 251133,
          "leaf_id": 250758

        "grouping": [

            "group_key": "collection",
            "group_value": "723Vxwr6aYZHNqc8dVQVwchDHUR3cEwZA8zkejdYWKaS"


        "royalty": {
          "royalty_model": "creators",
          "target": null,
          "percent": 0,
          "basis_points": 0,
          "primary_sale_happened": false,
          "locked": false

        "creators": [

            "address": "GVKwqsEC5YQZX4hG7Fdy6m7cJUi4DA3ezYx1CC9wkj34",
            "share": 100,
            "verified": true


        "ownership": {
          "frozen": false,
          "delegated": true,
          "delegate": "GVKwqsEC5YQZX4hG7Fdy6m7cJUi4DA3ezYx1CC9wkj34",
          "ownership_model": "single",
          "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"

        "supply": {
          "print_max_supply": 0,
          "print_current_supply": 0,
          "edition_nonce": 0

        "mutable": true,
        "burnt": false



  "id": "text"

```

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
Example:
`"1"`
method
enum<string>
default:getAssetsByOwner
required
The name of the DAS method to invoke.
Available options: 
`getAssetsByOwner`
params
object
required
Parameters for querying Solana digital assets by owner address with filtering and pagination options.
  * Option 1
  * Option 2


Show child attributes
#### Response
application/json
Successfully retrieved Solana digital assets owned by the specified wallet address
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
`"text"`
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getassetsbygroup)[ getNftEditionsRetrieve all editions and prints of a Solana NFT master edition including edition numbers and metadata with pagination support Next ](https://www.helius.dev/docs/api-reference/das/getnfteditions)
getAssetsByOwner
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetsByOwner",
  "params": {
    "ownerAddress": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showFungible": false,
      "showNativeBalance": false,
      "showInscription": false,
      "showZeroBalance": false




```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 1,
    "limit": 1,
    "page": 1,
    "items": [

        "interface": "V1_NFT",
        "id": "JCfTS6dmJZY4NXhjMwHqayGGHUwxp59pzcYhZrYqMBce",
        "content": {
          "$schema": "https://schema.metaplex.com/nft1.0.json",
          "json_uri": "https://www.hi-hi.vip/json/5000wif.json",
          "files": [

              "uri": "https://img.hi-hi.vip/json/img/5000wif.png",
              "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://img.hi-hi.vip/json/img/5000wif.png",
              "mime": "image/png"



        "authorities": [

            "address": "2iVwwSHr7hGR6wxNuQM8ArQYnX6Mzy2yeFnhBGgQetRw",
            "scopes": [
              "full"



        "compression": {
          "eligible": false,
          "compressed": true,
          "data_hash": "7zquDVS1VKu9HDh4WS4ray5ozLThiK6xrnFNhJtusj65",
          "creator_hash": "6v7GeYRiVML5mG1kJqi6eujN9sPB3ziCZJF4Vartj1qd",
          "asset_hash": "8gQZkgZ1L91qkNPtsiRGkRzpNcEfhBABEQr1D3wquB8H",
          "tree": "BZNn9zX1MysbSvqyGZ33Seb8bvimaiE9fxmLKwX2Euae",
          "seq": 251133,
          "leaf_id": 250758

        "grouping": [

            "group_key": "collection",
            "group_value": "723Vxwr6aYZHNqc8dVQVwchDHUR3cEwZA8zkejdYWKaS"


        "royalty": {
          "royalty_model": "creators",
          "target": null,
          "percent": 0,
          "basis_points": 0,
          "primary_sale_happened": false,
          "locked": false

        "creators": [

            "address": "GVKwqsEC5YQZX4hG7Fdy6m7cJUi4DA3ezYx1CC9wkj34",
            "share": 100,
            "verified": true


        "ownership": {
          "frozen": false,
          "delegated": true,
          "delegate": "GVKwqsEC5YQZX4hG7Fdy6m7cJUi4DA3ezYx1CC9wkj34",
          "ownership_model": "single",
          "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"

        "supply": {
          "print_max_supply": 0,
          "print_current_supply": 0,
          "edition_nonce": 0

        "mutable": true,
        "burnt": false



  "id": "text"

```

Assistant
Responses are generated using AI and may contain mistakes.
