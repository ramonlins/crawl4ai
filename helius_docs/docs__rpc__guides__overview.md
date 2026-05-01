# Source: https://www.helius.dev/docs/rpc/guides/overview

## Quick Navigation
## [Current State Methods Query live blockchain data and network status ](https://www.helius.dev/docs/rpc/guides/overview#current-state-methods)
## [Historical Data (Archival) Access complete transaction and block history ](https://www.helius.dev/docs/rpc/guides/overview#historical-data-archival)
## [Transaction Submission Send and simulate transactions with fee estimation ](https://www.helius.dev/docs/rpc/guides/overview#transaction-submission)
## [Network & Cluster Info Monitor validators, epochs, and network performance ](https://www.helius.dev/docs/rpc/guides/overview#network-%26-cluster-info)
## What are RPC method guides?
These practical guides show you **how to use specific Solana RPC methods** to solve common development challenges. Each guide includes:
  * **Real-world use cases** and when to use each method
  * **Complete code examples** in multiple languages
  * **Parameter explanations** with practical tips
  * **Response structure** breakdown
  * **Developer tips** for optimization and best practices

Perfect for developers who want to understand not just _what_ each RPC method does, but _how_ to use it effectively in production applications.
**Independent Infrastructure** : Helius runs its own dedicated RPC and archival infrastructure. Unlike providers relying on shared systems, our independent architecture delivers consistent performance, faster response times, and higher reliability across all RPC methods.
## Current State Methods
Query live blockchain data including accounts, balances, current slots, and real-time network status.
### Account & Balance Queries
## [getAccountInfo Get complete account details including balance, owner, and data ](https://www.helius.dev/docs/rpc/guides/getaccountinfo)
## [getBalance Quick SOL balance lookup for any account ](https://www.helius.dev/docs/rpc/guides/getbalance)
## [getMultipleAccounts Batch query multiple accounts efficiently ](https://www.helius.dev/docs/rpc/guides/getmultipleaccounts)
## [getProgramAccounts Find all accounts owned by a specific program ](https://www.helius.dev/docs/rpc/guides/getprogramaccounts)
## [getLargestAccounts Get accounts with largest SOL balances ](https://www.helius.dev/docs/rpc/guides/getlargestaccounts)
## [getSupply Get information about current supply ](https://www.helius.dev/docs/rpc/guides/getsupply)
### Guides for Token Account Methods
## [getTokenAccountsByOwner Get all token accounts for a wallet ](https://www.helius.dev/docs/rpc/guides/gettokenaccountsbyowner)
## [getTokenAccountsByDelegate Query token accounts by delegate ](https://www.helius.dev/docs/rpc/guides/gettokenaccountsbydelegate)
## [getTokenAccountBalance Get balance of a specific token account ](https://www.helius.dev/docs/rpc/guides/gettokenaccountbalance)
## [getTokenSupply Query total supply of an SPL token ](https://www.helius.dev/docs/rpc/guides/gettokensupply)
## [getTokenLargestAccounts Find accounts with largest token holdings ](https://www.helius.dev/docs/rpc/guides/gettokenlargestaccounts)
### Guides for Current Slot & Blockhash
## [getSlot Get current slot number ](https://www.helius.dev/docs/rpc/guides/getslot)
## [getBlockHeight Get current block height of the network ](https://www.helius.dev/docs/rpc/guides/getblockheight)
## [getLatestBlockhash Get most recent blockhash for transactions ](https://www.helius.dev/docs/rpc/guides/getlatestblockhash)
## [isBlockhashValid Validate if a blockhash is still valid ](https://www.helius.dev/docs/rpc/guides/isblockhashvalid)
## [getSlotLeader Get current slot leader ](https://www.helius.dev/docs/rpc/guides/getslotleader)
## [getSlotLeaders Get slot leaders for a range of slots ](https://www.helius.dev/docs/rpc/guides/getslotleaders)
### Transaction Status & Confirmation
## [getSignatureStatuses Check confirmation status of transactions ](https://www.helius.dev/docs/rpc/guides/getsignaturestatuses)
## [getTransactionCount Get total number of transactions processed ](https://www.helius.dev/docs/rpc/guides/gettransactioncount)
## Historical Data (Archival)
Access complete transaction and block history from Solana genesis. All archival methods cost 1 credit. [Learn more about historical data →](https://www.helius.dev/docs/rpc/historical-data)
### Transaction History
## [getTransactionsForAddress Advanced transaction history with filtering, sorting, and token account support (Helius exclusive) ](https://www.helius.dev/docs/rpc/gettransactionsforaddress)
## [getTransaction Get detailed information about a specific transaction ](https://www.helius.dev/docs/rpc/guides/gettransaction)
## [getSignaturesForAddress Get transaction signatures for an account ](https://www.helius.dev/docs/rpc/guides/getsignaturesforaddress)
## [getInflationReward Calculate inflation rewards for accounts ](https://www.helius.dev/docs/rpc/guides/getinflationreward)
## Guides for Block History
Access blockchain structure, timing, and historical data.
## [getBlock Get complete block information including all transactions ](https://www.helius.dev/docs/rpc/guides/getblock)
## [getBlocks Get list of confirmed blocks in a range ](https://www.helius.dev/docs/rpc/guides/getblocks)
## [getBlocksWithLimit Get limited number of confirmed blocks ](https://www.helius.dev/docs/rpc/guides/getblockswithlimit)
## [getBlockTime Get estimated production time of a block ](https://www.helius.dev/docs/rpc/guides/getblocktime)
## Guides for Transaction Submission
Send and simulate transactions with fee estimation and optimization.
### Guides for Transaction Methods
## [requestAirdrop Request SOL airdrop on devnet/testnet ](https://www.helius.dev/docs/rpc/guides/requestairdrop)
## [getPriorityFees Get recent priority fees for optimal pricing ](https://www.helius.dev/docs/rpc/guides/getrecentprioritizationfees)
## [getFeeForMessage Calculate transaction fees before sending ](https://www.helius.dev/docs/rpc/guides/getfeeformessage)
## Guides for Network & Cluster Methods
Monitor validators, epochs, network performance, and cluster health.
### Cluster Information
## [getHealth Check RPC node health status ](https://www.helius.dev/docs/rpc/guides/gethealth)
## [getVersion Get Solana software version information ](https://www.helius.dev/docs/rpc/guides/getversion)
## [getClusterNodes Get information about cluster validators ](https://www.helius.dev/docs/rpc/guides/getclusternodes)
## [getVoteAccounts Get current and delinquent vote accounts ](https://www.helius.dev/docs/rpc/guides/getvoteaccounts)
## [getEpochInfo Get information about the current epoch ](https://www.helius.dev/docs/rpc/guides/getepochinfo)
## [getEpochSchedule Get epoch schedule information ](https://www.helius.dev/docs/rpc/guides/getepochschedule)
## [getLeaderSchedule Get leader schedule for an epoch ](https://www.helius.dev/docs/rpc/guides/getleaderschedule)
### Guides for Network Performance & Economics
## [getPerformanceSamples Get recent network performance metrics ](https://www.helius.dev/docs/rpc/guides/getrecentperformancesamples)
## [getInflationGovernor Get current inflation parameters ](https://www.helius.dev/docs/rpc/guides/getinflationgovernor)
## [getInflationRate Get current inflation rate ](https://www.helius.dev/docs/rpc/guides/getinflationrate)
## [getStakeDelegation Get minimum stake delegation amount ](https://www.helius.dev/docs/rpc/guides/getstakeminimumdelegation)
## Guides for Utility & System Methods
Helper methods for system information, validation, and advanced queries.
### Basic Utility Methods
## [getRentExemption Calculate minimum balance for rent exemption ](https://www.helius.dev/docs/rpc/guides/getminimumbalanceforrentexemption)
## [getGenesisHash Get genesis hash of the cluster ](https://www.helius.dev/docs/rpc/guides/getgenesishash)
## [getIdentity Get identity public key of the RPC node ](https://www.helius.dev/docs/rpc/guides/getidentity)
## [getFirstAvailableBlock Get slot of first available block ](https://www.helius.dev/docs/rpc/guides/getfirstavailableblock)
## [getHighestSnapshotSlot Get highest slot with a snapshot ](https://www.helius.dev/docs/rpc/guides/gethighestsnapshotslot)
## [minimumLedgerSlot Get minimum slot that node has ledger information ](https://www.helius.dev/docs/rpc/guides/minimumledgerslot)
### Guides for Advanced System Queries
## [getMaxRetransmitSlot Get maximum slot seen from retransmit stage ](https://www.helius.dev/docs/rpc/guides/getmaxretransmitslot)
## [getMaxShredInsertSlot Get maximum slot seen from shred insert ](https://www.helius.dev/docs/rpc/guides/getmaxshredinsertslot)
## Related Resources
### Additional Documentation
## [Historical Data Overview Learn about Helius’s archival infrastructure and capabilities ](https://www.helius.dev/docs/rpc/historical-data)
## [RPC Optimization Advanced techniques for optimizing RPC performance ](https://www.helius.dev/docs/rpc/optimization-techniques)
## [WebSocket Methods Explore real-time subscriptions and streaming data ](https://www.helius.dev/docs/rpc/websocket)
## [API Reference Complete technical reference for all RPC methods ](https://www.helius.dev/docs/api-reference/rpc/http-methods)
**Need help with a specific RPC method?** Each guide includes practical examples and developer tips to get you started quickly. Browse the categories above or use the search to find exactly what you need.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/optimization-techniques)[ getAccountInfoLearn getAccountInfo use cases, code examples, request parameters, response structure, and tips. Next ](https://www.helius.dev/docs/rpc/guides/getaccountinfo)
On this page
  * [What are RPC method guides?](https://www.helius.dev/docs/rpc/guides/overview#what-are-rpc-method-guides)
  * [Account & Balance Queries](https://www.helius.dev/docs/rpc/guides/overview#account-%26-balance-queries)
  * [Guides for Token Account Methods](https://www.helius.dev/docs/rpc/guides/overview#guides-for-token-account-methods)
  * [Guides for Current Slot & Blockhash](https://www.helius.dev/docs/rpc/guides/overview#guides-for-current-slot-%26-blockhash)
  * [Transaction Status & Confirmation](https://www.helius.dev/docs/rpc/guides/overview#transaction-status-%26-confirmation)
  * [Historical Data (Archival)](https://www.helius.dev/docs/rpc/guides/overview#historical-data-archival)
  * [Guides for Block History](https://www.helius.dev/docs/rpc/guides/overview#guides-for-block-history)
  * [Guides for Transaction Submission](https://www.helius.dev/docs/rpc/guides/overview#guides-for-transaction-submission)
  * [Guides for Transaction Methods](https://www.helius.dev/docs/rpc/guides/overview#guides-for-transaction-methods)
  * [Guides for Network & Cluster Methods](https://www.helius.dev/docs/rpc/guides/overview#guides-for-network-%26-cluster-methods)
  * [Guides for Network Performance & Economics](https://www.helius.dev/docs/rpc/guides/overview#guides-for-network-performance-%26-economics)
  * [Guides for Utility & System Methods](https://www.helius.dev/docs/rpc/guides/overview#guides-for-utility-%26-system-methods)
  * [Basic Utility Methods](https://www.helius.dev/docs/rpc/guides/overview#basic-utility-methods)
  * [Guides for Advanced System Queries](https://www.helius.dev/docs/rpc/guides/overview#guides-for-advanced-system-queries)
  * [Additional Documentation](https://www.helius.dev/docs/rpc/guides/overview#additional-documentation)


Assistant
Responses are generated using AI and may contain mistakes.
