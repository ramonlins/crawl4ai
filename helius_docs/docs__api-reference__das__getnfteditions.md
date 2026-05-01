# Source: https://www.helius.dev/docs/api-reference/das/getnfteditions

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getNftEditions
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getNftEditions",
  "params": {
    "mint": "Ey2Qb8kLctbchQsMnhZs5DjY32To2QtPuXNwWvk4NosL"



```


```

  "last_indexed_slot": 365750752,
  "total": 1,
  "limit": 1,
  "page": 1,
  "master_edition_address": "8SHfqzJYABeGfiG1apwiEYt6TvfGQiL1pdwEjvTKsyiZ",
  "supply": 61,
  "max_supply": 69,
  "editions": [

      "mint": "GJvFDcBWf6aDncd1TBzx2ou1rgLFYaMBdbYLBa9oTAEw",
      "edition_address": "<string>",
      "edition": 123,
      "burnt": "<unknown>"



```

## Request Parameters
mint
string
required
The mint address of the Solana master edition NFT to retrieve all editions for.
page
number
The page number for paginating through the Solana NFT edition results.
limit
number
The maximum number of Solana NFT editions to return in a single request.
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
default:getNftEditions
required
The name of the DAS method to invoke.
Available options: 
`getNftEditions`
params
object
required
Show child attributes
#### Response
application/json
Successful response
last_indexed_slot
integer
All data up to and including this slot is guaranteed to have been indexed.
Example:
`365750752`
total
integer
The total number of limited edition Solana NFTs minted from this master edition.
Example:
limit
integer
The maximum number of NFT editions requested.
Example:
page
integer
The current page of results.
Example:
master_edition_address
string
The Solana blockchain address of the master edition NFT that controls the print editions.
Example:
`"8SHfqzJYABeGfiG1apwiEYt6TvfGQiL1pdwEjvTKsyiZ"`
supply
integer
Current supply of minted Solana NFT editions from this master edition.
Example:
max_supply
integer
Maximum possible supply of Solana NFT editions that can be minted from this master.
Example:
editions
object[]
An array of individual Solana NFT editions minted from this master edition.
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getassetsbyowner)[ getSignaturesForAssetRetrieve all historical transaction signatures for a Solana NFT or compressed NFT including transfers, sales, and state changes with pagination Next ](https://www.helius.dev/docs/api-reference/das/getsignaturesforasset)
getNftEditions
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getNftEditions",
  "params": {
    "mint": "Ey2Qb8kLctbchQsMnhZs5DjY32To2QtPuXNwWvk4NosL"



```


```

  "last_indexed_slot": 365750752,
  "total": 1,
  "limit": 1,
  "page": 1,
  "master_edition_address": "8SHfqzJYABeGfiG1apwiEYt6TvfGQiL1pdwEjvTKsyiZ",
  "supply": 61,
  "max_supply": 69,
  "editions": [

      "mint": "GJvFDcBWf6aDncd1TBzx2ou1rgLFYaMBdbYLBa9oTAEw",
      "edition_address": "<string>",
      "edition": 123,
      "burnt": "<unknown>"



```

Assistant
Responses are generated using AI and may contain mistakes.
