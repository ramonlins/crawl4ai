# Source: https://www.helius.dev/docs/api-reference/das/searchassets

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
searchAssets
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "searchAssets",
  "params": {
    "ownerAddress": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
    "tokenType": "all",
    "limit": 50,
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showNativeBalance": false,
      "showInscription": false,
      "showZeroBalance": false




```


```

  "assets": {
    "total": 80,
    "limit": 50,
    "page": 1,
    "items": [

        "interface": "V1_NFT",
        "id": "SomeNftMintKey12345",
        "ownership": {
          "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
          "ownership_model": "single"

        "content": {
          "json_uri": "https://example.com/metadata/12345.json"




  "nativeBalance": {
    "lamports": 123,
    "price_per_sol": 123,
    "total_price": 123


```

## Request Parameters
ownerAddress
string
required
The Solana wallet address to retrieve owned digital assets for filtering search results.
tokenType
string
required
Filter for specific Solana token types including compressed NFTs (cNFTs), regular NFTs, programmable NFTs (pNFTs), or fungible SPL tokens for targeted asset discovery.
  * `fungible`
  * `nonFungible`
  * `regularNft`
  * `compressedNft`
  * `all`


page
number
The page of results to return.
authorityAddress
string
The authority address criteria for filtering Solana digital assets based on program authority, useful for finding assets controlled by specific protocols or update authorities.
limit
number
The maximum number of assets to return.
sortBy
object
The sorting options for the response.
sortBy.sortBy
string
The criteria by which the assets will be sorted.
  * `created`
  * `recent_action`
  * `updated`
  * `none`


sortBy.sortDirection
string
The sorting direction.
  * `asc`
  * `desc`


compressed
boolean
Filter for compressed Solana NFTs (cNFTs) that use state compression technology for reduced storage costs and improved scalability.
compressible
boolean
Filter for Solana assets that are eligible for compression but have not yet been compressed into the state compression format.
delegate
number
Delegate criteria for the asset search.
creatorAddress
string
Creator wallet address criteria for finding Solana NFTs created by specific artists, projects, or creators for attribution and royalty tracking.
creatorVerified
boolean
Whether a creator is verified.
grouping
array
Collection grouping array for filtering Solana NFTs by their collection membership (e.g. `["collection", "<collectionKey>"]`) to find related assets.
tree
string
Merkle tree address for filtering compressed NFTs (cNFTs) by their collection tree. This parameter is Helius-specific and not part of the official DAS specification.
supply
number
Supply criteria for the asset search.
supplyMint
string
Supply mint criteria for the asset search.
frozen
boolean
Whether an asset is frozen.
burnt
boolean
Whether an asset is burnt.
interface
string
The Solana token standard interface type to filter for specific NFT implementations including programmable NFTs, legacy NFTs, and fungible tokens.
  * `V1_NFT`
  * `V1_PRINT`
  * `LEGACY_NFT`
  * `V2_NFT`
  * `FungibleAsset`
  * `FungibleToken`
  * `Custom`
  * `Identity`
  * `Executable`
  * `ProgrammableNFT`


royaltyTargetType
string
Royalty target type criteria.
royaltyTarget
number
Royalty target criteria.
royaltyAmount
number
Royalty amount criteria.
ownerType
number
Ownership model criteria.
before
string
A cursor for paginating backward.
after
string
A cursor for paginating forward.
options
object
Advanced display options for customizing the Solana asset search response.
options.showUnverifiedCollections
boolean
default:"false"
Show unverified collections instead of skipping them.
options.showCollectionMetadata
boolean
default:"false"
Show metadata for the collection.
options.showGrandTotal
boolean
default:"false"
Show total number of matching assets (slower request).
options.showNativeBalance
boolean
default:"false"
Show the native (SOL) balance of the owner.
options.showInscription
boolean
default:"false"
Display inscription details.
options.showZeroBalance
boolean
default:"false"
Display assets with zero balance.
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
default:searchAssets
required
The name of the JSON-RPC method to invoke.
Available options: 
`searchAssets`
params
object
required
Parameters for the `searchAssets` method.
Show child attributes
#### Response
application/json
Successful response
assets
object
Show child attributes
Example:

```
{  "total": 80,  "limit": 50,  "page": 1,  "items": [      "interface": "V1_NFT",      "id": "SomeNftMintKey12345",      "ownership": {        "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",        "ownership_model": "single"      },      "content": {        "json_uri": "https://example.com/metadata/12345.json"  ]}
```

nativeBalance
object
The native SOL balance of the Solana wallet account in lamports and USD value.
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/gettokenaccounts)[ getPriorityFeeEstimateGet recommended priority fee estimates for Solana transactions to optimize for inclusion and cost based on recent network activity and account locks Next ](https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate)
searchAssets
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "searchAssets",
  "params": {
    "ownerAddress": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
    "tokenType": "all",
    "limit": 50,
    "options": {
      "showUnverifiedCollections": false,
      "showCollectionMetadata": false,
      "showGrandTotal": false,
      "showNativeBalance": false,
      "showInscription": false,
      "showZeroBalance": false




```


```

  "assets": {
    "total": 80,
    "limit": 50,
    "page": 1,
    "items": [

        "interface": "V1_NFT",
        "id": "SomeNftMintKey12345",
        "ownership": {
          "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
          "ownership_model": "single"

        "content": {
          "json_uri": "https://example.com/metadata/12345.json"




  "nativeBalance": {
    "lamports": 123,
    "price_per_sol": 123,
    "total_price": 123


```

Assistant
Responses are generated using AI and may contain mistakes.
