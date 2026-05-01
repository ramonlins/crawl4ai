# Source: https://www.helius.dev/docs/api-reference/wallet-api/identity

GET
/
v1
/
wallet
/
{wallet}
/
identity
Try it
Get wallet identity
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/identity?api-key='
```


```

  "address": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
  "type": "exchange",
  "name": "Binance 1",
  "category": "Centralized Exchange",
  "tags": [
    "Centralized Exchange"

  "domainNames": [
    "toly.sol",
    "kash.superteam"


```

## Request Parameters
wallet
string
required
Solana wallet address (base58 encoded) or SNS/ANS domain name (e.g. `toly.sol`, `miester.bonk`). Domain resolution is mainnet-only. Any non-`.sol` domain is treated as an ANS custom TLD — there is no fixed TLD whitelist.
#### Authorizations
ApiKeyQuery ApiKeyHeaderApiKeyQueryApiKeyHeader
api-key
string
query
required
API key passed as query parameter
#### Path Parameters
wallet
string
required
Solana wallet address (base58 encoded) or SNS/ANS domain name (e.g. `toly.sol`, `miester.bonk`). Domain resolution is mainnet-only. Any non-`.sol` domain is treated as an ANS custom TLD — there is no fixed TLD whitelist.
#### Response
application/json
Identity information found
address
string
required
Solana wallet address
Example:
`"HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664"`
type
string
required
Type of entity
Example:
`"exchange"`
name
string
required
Display name
Example:
`"Binance 1"`
category
string
required
Category classification
Example:
`"Centralized Exchange"`
tags
string[]
required
Additional classification tags
Example:

```
["Centralized Exchange"]
```

domainNames
string[]
All on-chain domain names owned by this address, including SNS (.sol) and ANS custom TLDs (.bonk, .wen, etc.). The favorite .sol domain is first if set; remaining domains are sorted alphabetically. Omitted if the wallet owns no domains.
Example:

```
["toly.sol", "kash.superteam"]
```

Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/wallet-api)[ balancesRetrieve token balances and SOL holdings for a Solana wallet address. Next ](https://www.helius.dev/docs/api-reference/wallet-api/balances)
Get wallet identity
cURL

```
curl --request GET \
  --url 'https://api.helius.xyz/v1/wallet/{wallet}/identity?api-key='
```


```

  "address": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
  "type": "exchange",
  "name": "Binance 1",
  "category": "Centralized Exchange",
  "tags": [
    "Centralized Exchange"

  "domainNames": [
    "toly.sol",
    "kash.superteam"


```

Assistant
Responses are generated using AI and may contain mistakes.
