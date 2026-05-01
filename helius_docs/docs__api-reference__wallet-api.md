# Source: https://www.helius.dev/docs/api-reference/wallet-api

**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
## [identity Get wallet identity by address or SNS/ANS domain ](https://www.helius.dev/docs/api-reference/wallet-api/identity)
## [balances Retrieve all token and NFT balances with USD values ](https://www.helius.dev/docs/api-reference/wallet-api/balances)
## [history Fetch transaction history with balance changes ](https://www.helius.dev/docs/api-reference/wallet-api/history)
## [transfers Get all token transfer activity with sender/recipient info ](https://www.helius.dev/docs/api-reference/wallet-api/transfers)
## [funded-by Discover the original funding source for a wallet ](https://www.helius.dev/docs/api-reference/wallet-api/funded-by)
## Authentication
All Wallet API requests require authentication via API key:

```
# Query parameter
GET https://api.helius.xyz/v1/wallet/{wallet}/balances?api-key=YOUR_API_KEY

# Header (recommended)
GET https://api.helius.xyz/v1/wallet/{wallet}/balances
X-Api-Key: YOUR_API_KEY

```

## Base URL

```
https://api.helius.xyz

```

## Quick Reference
  * `GET /v1/wallet/{wallet}/identity` - Get wallet identity by address or SNS/ANS domain
  * `POST /v1/wallet/batch-identity` - Batch identity lookup (up to 100 addresses and/or domains)
  * `GET /v1/wallet/{wallet}/balances` - Get all token and NFT balances
  * `GET /v1/wallet/{wallet}/history` - Get transaction history with balance changes
  * `GET /v1/wallet/{wallet}/transfers` - Get all token transfer activity
  * `GET /v1/wallet/{wallet}/funded-by` - Find the original funding source


Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactionsbyaddress)[ identityResolve on-chain identity information for a Solana wallet including domain names and social profiles. Next ](https://www.helius.dev/docs/api-reference/wallet-api/identity)
On this page


Assistant
Responses are generated using AI and may contain mistakes.
