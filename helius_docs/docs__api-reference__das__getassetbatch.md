# Source: https://www.helius.dev/docs/api-reference/das/getassetbatch

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetBatch
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetBatch",
  "params": {
    "ids": [
      "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk"

    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showFungible": false,
      "showInscription": false




```


```


    "interface": "ProgrammableNFT",
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "content": {
      "last_indexed_slot": 365750752,
      "$schema": "https://schema.metaplex.com/nft1.0.json",
      "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/8420.json",
      "files": [

          "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "mime": "image/png"


      "metadata": {
        "attributes": [

            "value": "Male",
            "trait_type": "Gender"


            "value": "King",
            "trait_type": "Type"


        "description": "Fock it.",
        "name": "Mad Lads #8420",
        "symbol": "MAD"


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

    "token_info": {
      "symbol": "<string>",
      "supply": 123,
      "decimals": 123,
      "token_program": "<string>",
      "price_info": {
        "price_per_token": 123,
        "currency": "<string>"

      "mint_authority": "<string>",
      "freeze_authority": "<string>"

    "inscription": {
      "order": 123,
      "size": 123,
      "contentType": "<string>",
      "encoding": "<string>",
      "validationHash": "<string>",
      "inscriptionDataAccount": "<string>",
      "authority": "<string>"

    "spl20": {}


```

## Request Parameters
ids
array
required
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
default:getAssetBatch
required
The name of the DAS method to invoke.
Available options: 
`getAssetBatch`
params
object
required
Show child attributes
Example:

```
{  "ids": [    "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk"  ]}
```

#### Response
application/json
Successful response
interface
enum<string>
The interface of the asset.
Available options: 
`V1_NFT`, 
`V1_PRINT`, 
`LEGACY_NFT`, 
`V2_NFT`, 
`FungibleAsset`, 
`FungibleToken`, 
`Custom`, 
`Identity`, 
`Executable`, 
`ProgrammableNFT`
Example:
`"ProgrammableNFT"`
id
string
The ID of the asset.
Example:
`"F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk"`
content
object
The content of the asset.
Show child attributes
authorities
object[]
Example:

```
[  {    "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",    "scopes": ["full"]  }]
```

compression
object
Example:

```
{  "eligible": false,  "compressed": false,  "data_hash": "",  "creator_hash": "",  "asset_hash": "",  "tree": "",  "seq": 0,  "leaf_id": 0}
```

grouping
object[]
Example:

```
[  {    "group_key": "collection",    "group_value": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w"  }]
```

royalty
object
Example:

```
{  "royalty_model": "creators",  "target": null,  "percent": 0.042,  "basis_points": 420,  "primary_sale_happened": true,  "locked": false}
```

creators
object[]
Example:

```
[  {    "address": "5XvhfmRjwXkGp3jHGmaKpqeerNYjkuZZBYLVQYdeVcRv",    "share": 0,    "verified": true  },  {    "address": "2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW",    "share": 100,    "verified": true  }]
```

ownership
object
Example:

```
{  "frozen": true,  "delegated": false,  "delegate": null,  "ownership_model": "single",  "owner": "4zdNGgAtFsW1cQgHqkiWyRsxaAgxrSRRynnuunxzjxue"}
```

supply
object
Example:

```
{  "print_max_supply": 0,  "print_current_supply": 0,  "edition_nonce": 254}
```

token_info
object
Details about the specific token.
Show child attributes
inscription
object
Show child attributes
spl20
object
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getasset)[ getAssetProofRetrieve the Merkle proof for a compressed Solana NFT required for verification and on-chain operations like transfers and burns Next ](https://www.helius.dev/docs/api-reference/das/getassetproof)
getAssetBatch
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetBatch",
  "params": {
    "ids": [
      "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk"

    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showFungible": false,
      "showInscription": false




```


```


    "interface": "ProgrammableNFT",
    "id": "F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk",
    "content": {
      "last_indexed_slot": 365750752,
      "$schema": "https://schema.metaplex.com/nft1.0.json",
      "json_uri": "https://madlads.s3.us-west-2.amazonaws.com/json/8420.json",
      "files": [

          "uri": "https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "cdn_uri": "https://cdn.helius-rpc.com/cdn-cgi/image//https://madlads.s3.us-west-2.amazonaws.com/images/8420.png",
          "mime": "image/png"


      "metadata": {
        "attributes": [

            "value": "Male",
            "trait_type": "Gender"


            "value": "King",
            "trait_type": "Type"


        "description": "Fock it.",
        "name": "Mad Lads #8420",
        "symbol": "MAD"


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

    "token_info": {
      "symbol": "<string>",
      "supply": 123,
      "decimals": 123,
      "token_program": "<string>",
      "price_info": {
        "price_per_token": 123,
        "currency": "<string>"

      "mint_authority": "<string>",
      "freeze_authority": "<string>"

    "inscription": {
      "order": 123,
      "size": 123,
      "contentType": "<string>",
      "encoding": "<string>",
      "validationHash": "<string>",
      "inscriptionDataAccount": "<string>",
      "authority": "<string>"

    "spl20": {}


```

Assistant
Responses are generated using AI and may contain mistakes.
