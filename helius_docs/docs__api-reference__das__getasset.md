# Source: https://www.helius.dev/docs/api-reference/das/getasset

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAsset
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAsset",
  "params": {
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showFungible": false,
      "showInscription": false




```


```

  "jsonrpc": "2.0",
  "id": "test",
  "result": {
    "last_indexed_slot": 365749093,
    "interface": "ProgrammableNFT",
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "content": {
      "$schema": "https://schema.metaplex.com/nft1.0.json",
      "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/8420.json",
      "files": [

          "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "mime": "image/png"


          "uri": "https://arweave.net/qJ5B6fx5hEt4P7XbicbJQRyTcbyLaV-OQNA1KjzdqOQ/0.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://arweave.net/qJ5B6fx5hEt4P7XbicbJQRyTcbyLaV-OQNA1KjzdqOQ/0.png",
          "mime": "image/png"


      "metadata": {
        "attributes": [

            "value": "Male",
            "trait_type": "Gender"


            "value": "King",
            "trait_type": "Type"


            "value": "Royal",
            "trait_type": "Expression"


            "value": "Mad Crown",
            "trait_type": "Hat"


            "value": "Madness",
            "trait_type": "Eyes"


            "value": "Mad Armor",
            "trait_type": "Clothing"


            "value": "Royal Rug",
            "trait_type": "Background"


        "description": "Fock it.",
        "name": "Mad Lads #8420",
        "symbol": "MAD",
        "token_standard": "ProgrammableNonFungible"

      "links": {
        "image": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
        "external_url": "https://madlads.com"


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


        "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
        "share": 100,
        "verified": true


    "ownership": {
      "frozen": true,
      "delegated": false,
      "delegate": null,
      "ownership_model": "single",
      "owner": "4zdNGgAtFsW1cQgHqkiWyRsxaAgxrSRRynnuunxzjxue"

    "supply": {
      "print_max_supply": 0,
      "print_current_supply": 0,
      "edition_nonce": 254

    "mutable": true,
    "burnt": false,
    "token_info": {
      "supply": 1,
      "decimals": 0,
      "token_program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
      "mint_authority": "TdMA45ZnakQCBt5XUvm7ib2htKuTWdcgGKu1eUGrDyJ",
      "freeze_authority": "TdMA45ZnakQCBt5XUvm7ib2htKuTWdcgGKu1eUGrDyJ"



```

## Price Data Caching
Price data returned by getAsset is cached and may not be fresh. The price information has a 600-second cache, meaning the data can be up to 600 seconds old.
Price data is available for the top 10k tokens by 24h volume and can be found in the `token_info.price_info` section of the response. For applications requiring real-time pricing, consider implementing additional validation.
## Request Parameters
id
string
The unique identifier of the Solana NFT or digital asset to retrieve. This is typically the mint address of the NFT or token.
options
object
Display and formatting options for the asset data response.
options.showUnverifiedCollections
boolean
default:"false"
Displays grouping information for unverified collections instead of skipping them.
options.showCollectionMetadata
boolean
default:"false"
Displays metadata for the collection.
options.showFungible
boolean
default:"false"
Displays fungible tokens held by the owner.
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
The JSON-RPC protocol version.
Available options: 
`2.0`
id
string
default:1
required
A unique identifier for the request.
Example:
`"1"`
method
enum<string>
default:getAsset
required
The name of the RPC method to invoke.
Available options: 
`getAsset`
params
object
required
Show child attributes
#### Response
application/json
Successful response
jsonrpc
enum<string>
The version of the JSON-RPC protocol.
Available options: 
`2.0`
id
string
The ID used to identify the request.
result
object
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das)[ getAssetBatchRetrieve detailed information for up to 1,000 Solana NFTs, compressed NFTs, or tokens in a single efficient batch request Next ](https://www.helius.dev/docs/api-reference/das/getassetbatch)
getAsset
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAsset",
  "params": {
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showFungible": false,
      "showInscription": false




```


```

  "jsonrpc": "2.0",
  "id": "test",
  "result": {
    "last_indexed_slot": 365749093,
    "interface": "ProgrammableNFT",
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "content": {
      "$schema": "https://schema.metaplex.com/nft1.0.json",
      "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/8420.json",
      "files": [

          "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "mime": "image/png"


          "uri": "https://arweave.net/qJ5B6fx5hEt4P7XbicbJQRyTcbyLaV-OQNA1KjzdqOQ/0.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://arweave.net/qJ5B6fx5hEt4P7XbicbJQRyTcbyLaV-OQNA1KjzdqOQ/0.png",
          "mime": "image/png"


      "metadata": {
        "attributes": [

            "value": "Male",
            "trait_type": "Gender"


            "value": "King",
            "trait_type": "Type"


            "value": "Royal",
            "trait_type": "Expression"


            "value": "Mad Crown",
            "trait_type": "Hat"


            "value": "Madness",
            "trait_type": "Eyes"


            "value": "Mad Armor",
            "trait_type": "Clothing"


            "value": "Royal Rug",
            "trait_type": "Background"


        "description": "Fock it.",
        "name": "Mad Lads #8420",
        "symbol": "MAD",
        "token_standard": "ProgrammableNonFungible"

      "links": {
        "image": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
        "external_url": "https://madlads.com"


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


        "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",
        "share": 100,
        "verified": true


    "ownership": {
      "frozen": true,
      "delegated": false,
      "delegate": null,
      "ownership_model": "single",
      "owner": "4zdNGgAtFsW1cQgHqkiWyRsxaAgxrSRRynnuunxzjxue"

    "supply": {
      "print_max_supply": 0,
      "print_current_supply": 0,
      "edition_nonce": 254

    "mutable": true,
    "burnt": false,
    "token_info": {
      "supply": 1,
      "decimals": 0,
      "token_program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
      "mint_authority": "TdMA45ZnakQCBt5XUvm7ib2htKuTWdcgGKu1eUGrDyJ",
      "freeze_authority": "TdMA45ZnakQCBt5XUvm7ib2htKuTWdcgGKu1eUGrDyJ"



```

Assistant
Responses are generated using AI and may contain mistakes.
