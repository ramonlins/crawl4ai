# Source: https://www.helius.dev/docs/api-reference/das/getsignaturesforasset

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getSignaturesForAsset
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getSignaturesForAsset",
  "params": {
    "id": "FNt6A9Mfnqbwc1tY7uwAguKQ1JcpBrxmhczDgbdJy5AC"



```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 3,
    "limit": 1000,
    "items": [

        "5nLi8m72bU6PBcz4Xrk23P6KTGy9ufF92kZiQXjTv9ELgkUxrNaiCGhMF4vh6RAcisw9DEQWJt9ogM3G2uCuwwV7",
        "MintToCollectionV1"


        "323Ag4J69gagBt3neUvajNauMydiXZTmXYSfdK5swWcK1iwCUypcXv45UFcy5PTt136G9gtQ45oyPJRs1f2zFZ3v",
        "Transfer"


        "3TbybyYRtNjVMhhahTNbd4bbpiEacZn2qkwtH7ByL7tCHmwi2g4YapPidSRGs1gjaseKbs7RjNmUKWmU6xbf3wUT",
        "Transfer"



  "id": "text"

```

## Request Parameters
id
string
required
The unique identifier (mint address) of the Solana digital asset to retrieve transaction history for.
page
number
required
The page number for paginating through the Solana asset’s transaction history.
limit
number
The maximum number of Solana transaction signatures to return per request.
before
string
The cursor for paginating backwards through the signatures.
after
string
The cursor for paginating forwards through the signatures.
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
default:getSignaturesForAsset
required
The name of the DAS method to invoke.
Available options: 
`getSignaturesForAsset`
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
`"text"`
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getnfteditions)[ getTokenAccountsRetrieve all SPL token accounts owned by a wallet address including token balances, mint addresses, and account metadata with pagination Next ](https://www.helius.dev/docs/api-reference/das/gettokenaccounts)
getSignaturesForAsset
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getSignaturesForAsset",
  "params": {
    "id": "FNt6A9Mfnqbwc1tY7uwAguKQ1JcpBrxmhczDgbdJy5AC"



```


```

  "jsonrpc": "2.0",
  "result": {
    "last_indexed_slot": 365750752,
    "total": 3,
    "limit": 1000,
    "items": [

        "5nLi8m72bU6PBcz4Xrk23P6KTGy9ufF92kZiQXjTv9ELgkUxrNaiCGhMF4vh6RAcisw9DEQWJt9ogM3G2uCuwwV7",
        "MintToCollectionV1"


        "323Ag4J69gagBt3neUvajNauMydiXZTmXYSfdK5swWcK1iwCUypcXv45UFcy5PTt136G9gtQ45oyPJRs1f2zFZ3v",
        "Transfer"


        "3TbybyYRtNjVMhhahTNbd4bbpiEacZn2qkwtH7ByL7tCHmwi2g4YapPidSRGs1gjaseKbs7RjNmUKWmU6xbf3wUT",
        "Transfer"



  "id": "text"

```

Assistant
Responses are generated using AI and may contain mistakes.
