# Source: https://www.helius.dev/docs/api-reference/das/gettokenaccounts

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getTokenAccounts
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getTokenAccounts",
  "params": {
    "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"



```


```

  "last_indexed_slot": 365750752,
  "total": 2,
  "limit": 100,
  "cursor": "<string>",
  "token_accounts": [

      "address": "<string>",
      "mint": "<string>",
      "owner": "<string>",
      "amount": 123,
      "delegated_amount": 123,
      "frozen": true,
      "burnt": "<unknown>"



```

## Request Parameters
mint
string
The mint address key.
owner
string
The owner address key.
page
number
The page of results to return.
limit
number
The maximum number of assets to return.
cursor
string
The cursor used for pagination.
before
string
Returns results before the specified cursor.
after
string
Returns results after the specified cursor.
options
object
options.showZeroBalance
boolean
If true, show accounts with empty token balances.
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
default:getTokenAccounts
required
The name of the method to invoke.
Available options: 
`getTokenAccounts`
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
The number of results found for the request.
Example:
limit
integer
The maximum number of results requested.
Example:
`100`
cursor
string
The cursor used for pagination.
token_accounts
object[]
An array of token accounts.
Show child attributes
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getsignaturesforasset)[ searchAssetsSearch and filter Solana NFTs, compressed NFTs, and tokens using flexible criteria including ownership, creators, collections, and custom attributes Next ](https://www.helius.dev/docs/api-reference/das/searchassets)
getTokenAccounts
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getTokenAccounts",
  "params": {
    "owner": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"



```


```

  "last_indexed_slot": 365750752,
  "total": 2,
  "limit": 100,
  "cursor": "<string>",
  "token_accounts": [

      "address": "<string>",
      "mint": "<string>",
      "owner": "<string>",
      "amount": 123,
      "delegated_amount": 123,
      "frozen": true,
      "burnt": "<unknown>"



```

Assistant
Responses are generated using AI and may contain mistakes.
