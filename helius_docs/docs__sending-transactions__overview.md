# Source: https://www.helius.dev/docs/sending-transactions/overview

## Why is transaction sending hard on Solana?
Every interaction with Solana — trading on a DEX, minting an NFT, transferring tokens, or calling a program — requires a transaction that lands onchain. During network congestion, unoptimized transactions are frequently dropped before reaching a leader. Helius provides staked connections that route directly to leaders, priority fee optimization, and enterprise-grade redundancy to ensure your transactions confirm quickly and reliably.
## Transaction Sending Options
We offer multiple pathways for sending transactions, each designed for different needs and use cases.
## [Staked Connections Recommended for production systems. Direct routing to block leaders with priority lane access, bypassing public queues for reliable delivery. ](https://www.helius.dev/docs/sending-transactions/send-manually)
## [Sender (Ultra-Low Latency) Specialized service for high-frequency traders requiring ultra-low latency. Dual routing to validators and Jito infrastructure with global endpoints. ](https://www.helius.dev/docs/sending-transactions/sender)
## [Transaction Rebates Earn automatic SOL rebates via post-trade backruns with no additional risk of toxic MEV. One parameter addition to your sendTransaction calls. ](https://www.helius.dev/docs/sending-transactions/backrun-rebates)
## Key Concepts for Reliable Transactions
Regardless of the method you choose, understanding these concepts is key to success on Solana.
## [Optimizing Transactions Learn best practices for setting priority fees and compute units to maximize your transaction’s chances of landing quickly. ](https://www.helius.dev/docs/sending-transactions/optimizing-transactions)
## What is the difference between staked and unstaked connections?
Helius offers both staked and unstaked connections for sending transactions.
  * **Staked Connections (Recommended)** : When you send transactions through our endpoints (available on paid plans), your transactions are routed directly to the current and upcoming block leaders. This provides a priority lane, bypassing the public transaction processing queue and offering near-guaranteed delivery. Using the Helius [Priority Fee API](https://www.helius.dev/docs/priority-fee-api) ensures you pay the optimal fee required by the leader.
  * **Unstaked Connections** : On our free plan, transactions are sent through high-performance, but unstaked, RPC nodes. They are subject to the same network congestion and competition for leader processing as any other public transaction.

For any production application, using **staked connections is the single most effective way to ensure reliable transaction delivery.**
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/webhooks/transaction-types)[ How to Send TransactionsStep-by-step guide for building robust, production-grade Solana transaction sending workflows. Learn compute optimization, priority fees, and confirmation strategies. Next ](https://www.helius.dev/docs/sending-transactions/send-manually)
On this page
  * [Why is transaction sending hard on Solana?](https://www.helius.dev/docs/sending-transactions/overview#why-is-transaction-sending-hard-on-solana)
  * [Transaction Sending Options](https://www.helius.dev/docs/sending-transactions/overview#transaction-sending-options)
  * [Key Concepts for Reliable Transactions](https://www.helius.dev/docs/sending-transactions/overview#key-concepts-for-reliable-transactions)
  * [What is the difference between staked and unstaked connections?](https://www.helius.dev/docs/sending-transactions/overview#what-is-the-difference-between-staked-and-unstaked-connections)


Assistant
Responses are generated using AI and may contain mistakes.
