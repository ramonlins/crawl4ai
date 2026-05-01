# Source: https://www.helius.dev/docs/enhanced-transactions

**Deprecated** : The Enhanced Transactions API is deprecated and no longer receiving new parser types or feature work. Existing endpoints continue to operate; new integrations should use [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress) for history and [`getTransaction`](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction) for single-transaction lookups.
## [Parse Transaction(s) Parse transactions into human-readable data ](https://www.helius.dev/docs/enhanced-transactions/parse-transactions)
## [Transaction History Get historical transaction data for any address ](https://www.helius.dev/docs/enhanced-transactions/transaction-history)
**Quick Reference** :
  * `/v0/transactions` - Parse individual or multiple transaction signatures
  * `/v0/addresses/{address}/transactions` - Get transaction history for an address
  * Filter by transaction type using the `type` parameter (e.g., `NFT_SALE`, `SWAP`, `TRANSFER`)
  * View all available type filters in the [API Reference](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactionsbyaddress)


## Overview
The Enhanced Transactions API transforms complex Solana transactions into human-readable data.
## Key Features
## Human-Readable Data
Get clear descriptions of transaction activities instead of raw blockchain data
## Type Filtering
Filter transactions by type: NFT sales, swaps, transfers, and more. [See all types](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactionsbyaddress).
## Pagination Support
Efficiently fetch large transaction histories with built-in pagination
## Detailed Metadata
Access timestamps, fees, signatures, and account information
## What You Get
The Enhanced Transactions API provides:
  * **Structured Data** : Transaction details organized in a clean, accessible format
  * **Event Summaries** : High-level summaries of what happened in each transaction
  * **Account Information** : Details about all accounts involved
  * **Transfer Details** : Clear information about SOL and token movements
  * **Timestamps** : When transactions were processed
  * **Fee Information** : Transaction fees and fee payer details


## Use Cases
The Enhanced Transactions API is ideal for:
  * **Wallet Applications** : Display transaction history to users
  * **Portfolio Trackers** : Track asset movements across accounts
  * **Analytics Platforms** : Analyze on-chain activity
  * **NFT Marketplaces** : Monitor NFT sales and listings
  * **DeFi Applications** : Track swaps and transfers (for supported protocols)


## Getting Started
Get Your API Key
Sign up at [dashboard.helius.dev](https://dashboard.helius.dev) to get your API key.
Choose Your Endpoint
Select either the parse transactions or transaction history endpoint based on your needs.
Make Your First Request
Start with a simple request to parse a transaction or fetch transaction history.
Check out our [Parse Transactions](https://www.helius.dev/docs/enhanced-transactions/parse-transactions) and [Transaction History](https://www.helius.dev/docs/enhanced-transactions/transaction-history) guides for code examples.
## Questions?
For frequently asked questions about Enhanced Transactions including usage, authentication, rate limits, and troubleshooting, visit our comprehensive [Enhanced Transactions FAQ](https://www.helius.dev/docs/faqs/enhanced-transactions).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/how-to-index-solana-data)[ Parse TransactionsParse transactions into human-readable data. Next ](https://www.helius.dev/docs/enhanced-transactions/parse-transactions)
On this page


Assistant
Responses are generated using AI and may contain mistakes.
