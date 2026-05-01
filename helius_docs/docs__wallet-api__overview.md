# Source: https://www.helius.dev/docs/wallet-api/overview

**Beta** : The Wallet API is currently in beta. APIs and response formats may change. This is an experimental API that we’re actively improving coverage and adding new features to.
## Guides and Tutorials
## [Wallet Identity Look up wallet identities by address or SNS/ANS domain ](https://www.helius.dev/docs/wallet-api/identity)
## [Wallet Balances Get token and NFT balances with USD values ](https://www.helius.dev/docs/wallet-api/balances)
## [Wallet History Fetch complete transaction history with balance changes ](https://www.helius.dev/docs/wallet-api/history)
## [Token Transfers See all token transfers with sender/recipient info ](https://www.helius.dev/docs/wallet-api/transfers)
## [Funding Source Discover who originally funded a wallet ](https://www.helius.dev/docs/wallet-api/funded-by)
**Quick Reference** :
  * `GET /v1/wallet/{wallet}/identity` - Get wallet identity by address or SNS/ANS domain
  * `POST /v1/wallet/batch-identity` - Batch identity lookup (up to 100 addresses and/or domains)
  * `GET /v1/wallet/{wallet}/balances` - Get all token and NFT balances
  * `GET /v1/wallet/{wallet}/history` - Get transaction history with balance changes
  * `GET /v1/wallet/{wallet}/transfers` - Get all token transfer activity
  * `GET /v1/wallet/{wallet}/funded-by` - Find the original funding source
  * **Base URL** : `https://api.helius.xyz`


## What is the Wallet API?
The Wallet API provides high-performance REST endpoints for querying complete Solana wallet data — balances, transaction history, token transfers, identity resolution, and funding sources. Instead of making multiple RPC calls and parsing raw blockchain data, get structured, human-readable information with USD pricing in a single request. Ideal for wallets, portfolio trackers, explorers, and compliance tools.
## Key Features
## Complete Wallet Profiles
Get everything about a wallet: balances, history, transfers, and identity in structured format
## USD Pricing
Token balances include USD values (hourly updates via DAS) and portfolio totals
## Identity Resolution
Identify known wallets with 10,000+ labeled accounts and 2,250+ labeled programs, plus 10.7M+ categorical tags (exchanges, protocols, institutions)
## Fast & Efficient
Optimized queries return data in milliseconds, not seconds
## Pagination Support
Efficiently fetch large datasets with cursor-based pagination
## Human-Readable
Get clear, structured data instead of raw blockchain instructions
## What You Get
The Wallet API provides:
  * **Token Balances** : All SPL tokens and Token-2022 with USD values, logos, and metadata
  * **NFT Holdings** : Compressed and uncompressed NFTs with collection information
  * **Transaction History** : Complete history with balance changes for each transaction
  * **Transfer Activity** : All incoming and outgoing transfers with counterparty information
  * **Identity Data** : Names and categories for known wallets (exchanges, protocols, etc.)
  * **Funding Analysis** : Original funding source and amount for wallet attribution


## Amounts and Units
The Wallet API is a high-level abstraction over raw Solana data. All `amount` fields in responses are **human-readable** — already divided by the token’s `decimals` — so you can display them directly without any conversion.
**No lamport conversion needed.** Raw Solana RPC calls return values in lamports (the smallest unit, 10⁻⁹ SOL). The Wallet API does not — `"amount": 1.5` means 1.5 SOL, not 1.5 lamports.
Where exact arithmetic is required, some endpoints also expose `amountRaw`: the same value as a raw integer serialized as a string to avoid floating-point precision loss. The conversion formula is: `amount = parseInt(amountRaw) / 10**decimals`  
| Endpoint  | Human-readable `amount`  | Raw `amountRaw` string  |  
| --- | --- | --- |  
| **Balances**  |  `balance` field  | Not available  |  
| **Funded-by**  |  `amount` field  |  `amountRaw` field  |  
| **Transfers**  |  `amount` field  |  `amountRaw` field  |  
|  **History** (`balanceChanges`)  |  `amount` field  | Not available  |  
Use `amount` for display. Use `amountRaw` when passing values to on-chain instructions or other systems that require exact integer arithmetic.
## Use Cases
The Wallet API is ideal for:
  * **Wallet Applications** : Display portfolio balances and transaction history to users
  * **Payment Processors** : Track payment history and verify transactions for merchants
  * **Portfolio Trackers** : Show current holdings with USD values
  * **Tax & Accounting**: Generate complete transaction reports for tax filing
  * **Compliance & AML**: Monitor wallet activity and identify exchange funding sources
  * **Analytics Platforms** : Track whale wallets, smart money, and on-chain behavior
  * **Trading Bots** : Analyze wallet holdings and activity patterns
  * **DeFi Dashboards** : Display user positions across protocols


## Authentication
All Wallet API requests require an API key. You can pass it in two ways:
  * Query Parameter
  * Header



```
curl "https://api.helius.xyz/v1/wallet/{wallet}/balances?api-key=YOUR_API_KEY"

```


```
curl "https://api.helius.xyz/v1/wallet/{wallet}/balances" \
  -H "X-Api-Key: YOUR_API_KEY"

```

## Getting Started
Get Your API Key
Sign up at [dashboard.helius.dev](https://dashboard.helius.dev) to get your API key.
Choose Your Endpoint
Select the endpoint that matches your use case:
  * [**Identity**](https://www.helius.dev/docs/api-reference/wallet-api/identity): Identify known wallets (exchanges, protocols)
  * [**Balances**](https://www.helius.dev/docs/api-reference/wallet-api/balances): Get portfolio holdings with USD values
  * [**History**](https://www.helius.dev/docs/api-reference/wallet-api/history): Fetch complete transaction history
  * [**Transfers**](https://www.helius.dev/docs/api-reference/wallet-api/transfers): Track all token movements
  * [**Funding**](https://www.helius.dev/docs/api-reference/wallet-api/funded-by): Find original funding source


Make Your First Request
Start with a simple balance query:

```
curl "https://api.helius.xyz/v1/wallet/86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY/balances?api-key=YOUR_API_KEY"

```

Handle the Response
Parse the JSON response and display the data in your application.
## Need Help?
## [API Reference View detailed API documentation with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api)
## [Contact Support Get help from our team through Discord, chat, or email ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-transactions/transaction-history)[ Wallet IdentityIdentify known Solana wallets by address or SNS/ANS domain. Look up single entries or batch process up to 100 addresses and domains at once. Next ](https://www.helius.dev/docs/wallet-api/identity)
On this page
  * [What is the Wallet API?](https://www.helius.dev/docs/wallet-api/overview#what-is-the-wallet-api)


Assistant
Responses are generated using AI and may contain mistakes.
