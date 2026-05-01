# Source: https://www.helius.dev/docs/api-reference/das/getassetproof

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
getAssetProof
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetProof",
  "params": {
    "id": "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss"



```


```

  "last_indexed_slot": 365750752,
  "root": "2o6Y6EiY3WXhoaEpei2pHmHLYnHDcEQVhgD89GrGHDBH",
  "proof": [

      "EmJXiXEAhEN3FfNQtBa5hwR8LC5kHvdLsaGCoERosZjK",
      "7NEfhcNPAwbw3L87fjsPqTz2fQdd1CjoLE138SD58FDQ",
      "6dM3VyeQoYkRFZ74G53EwvUPbQC6LsMZge6c7S1Ds4ks",
      "A9AACJ5m7UtaVz4HxzhDxGjYaY88rc2XPoFvnoTvgYBj",
      "2VG5cKeBZdqozwhHGGzs13b9tzy9TXt9kPfN8MzSJ1Sm",
      "3E1uFze4pi6BnTZXMsQbeh3jQCeDi966Zax9aMbYgg2D",
      "Bx9PdctdWCeC1WfU6dwP49idsXCYhqyxbRLyLwwGhr61",
      "HSbJ8quT4vuXFgf5FnjzeUuFfAtLKsq6W1Frj8y1qrif",
      "GJMLzL4F4hY9yFHY1EY6XRmW4wpuNGeBZTiv7vM2mYra",
      "FYPtEiqmRx6JprHQvWeEWEuVp3WA7DPRCE4VbhFRVuAj",
      "6MJKrpnK1GbYsnEzwMRWStNGkTjAZF23NhzTQSQVXsD3",
      "HjnrJn5vBUUzpCxzjjM9ZnCPuXei2cXKJjX468B9yWD7",
      "4YCF1CSyTXm1Yi9W9JeYevawupkomdgy2dLxEBHL9euq",
      "E3oMtCuPEauftdZLX8EZ8YX7BbFzpBCVRYEiLxwPJLY2"


  "node_index": 16384,
  "leaf": "6YdZXw49M97mfFTwgQb6kxM2c6eqZkHSaW9XhhoZXtzv",
  "tree_id": "2kuTFCcjbV22wvUmtmgsFR7cas7eZUzAu96jzJUvUcb7",
  "burnt": "<unknown>"

```

## Request Parameters
id
string
required
The unique identifier (mint address) of the compressed Solana NFT to retrieve the merkle proof for.
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
default:getAssetProof
required
The name of the DAS method to invoke.
Available options: 
`getAssetProof`
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
root
string
The root hash of the Solana state compression merkle tree that contains this compressed NFT.
Example:
`"2o6Y6EiY3WXhoaEpei2pHmHLYnHDcEQVhgD89GrGHDBH"`
proof
string[]
The array of merkle proof hashes needed to cryptographically verify this Solana compressed NFT exists in the tree.
node_index
integer
The position index of this compressed NFT in the Solana merkle tree structure.
Example:
`16384`
leaf
string
The leaf hash representing this compressed NFT's data in the Solana merkle tree.
Example:
`"6YdZXw49M97mfFTwgQb6kxM2c6eqZkHSaW9XhhoZXtzv"`
tree_id
string
The unique identifier of the Solana merkle tree where this compressed NFT is stored.
Example:
`"2kuTFCcjbV22wvUmtmgsFR7cas7eZUzAu96jzJUvUcb7"`
burnt
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/das/getassetbatch)[ getAssetProofBatchRetrieve Merkle proofs for multiple compressed Solana NFTs in a single batch request for efficient verification and on-chain operations Next ](https://www.helius.dev/docs/api-reference/das/getassetproofbatch)
getAssetProof
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "getAssetProof",
  "params": {
    "id": "Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss"



```


```

  "last_indexed_slot": 365750752,
  "root": "2o6Y6EiY3WXhoaEpei2pHmHLYnHDcEQVhgD89GrGHDBH",
  "proof": [

      "EmJXiXEAhEN3FfNQtBa5hwR8LC5kHvdLsaGCoERosZjK",
      "7NEfhcNPAwbw3L87fjsPqTz2fQdd1CjoLE138SD58FDQ",
      "6dM3VyeQoYkRFZ74G53EwvUPbQC6LsMZge6c7S1Ds4ks",
      "A9AACJ5m7UtaVz4HxzhDxGjYaY88rc2XPoFvnoTvgYBj",
      "2VG5cKeBZdqozwhHGGzs13b9tzy9TXt9kPfN8MzSJ1Sm",
      "3E1uFze4pi6BnTZXMsQbeh3jQCeDi966Zax9aMbYgg2D",
      "Bx9PdctdWCeC1WfU6dwP49idsXCYhqyxbRLyLwwGhr61",
      "HSbJ8quT4vuXFgf5FnjzeUuFfAtLKsq6W1Frj8y1qrif",
      "GJMLzL4F4hY9yFHY1EY6XRmW4wpuNGeBZTiv7vM2mYra",
      "FYPtEiqmRx6JprHQvWeEWEuVp3WA7DPRCE4VbhFRVuAj",
      "6MJKrpnK1GbYsnEzwMRWStNGkTjAZF23NhzTQSQVXsD3",
      "HjnrJn5vBUUzpCxzjjM9ZnCPuXei2cXKJjX468B9yWD7",
      "4YCF1CSyTXm1Yi9W9JeYevawupkomdgy2dLxEBHL9euq",
      "E3oMtCuPEauftdZLX8EZ8YX7BbFzpBCVRYEiLxwPJLY2"


  "node_index": 16384,
  "leaf": "6YdZXw49M97mfFTwgQb6kxM2c6eqZkHSaW9XhhoZXtzv",
  "tree_id": "2kuTFCcjbV22wvUmtmgsFR7cas7eZUzAu96jzJUvUcb7",
  "burnt": "<unknown>"

```

Assistant
Responses are generated using AI and may contain mistakes.
