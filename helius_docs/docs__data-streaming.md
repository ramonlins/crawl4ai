# Source: https://www.helius.dev/docs/data-streaming

## What is data streaming on Solana?
Data streaming allows applications to receive real-time updates from the Solana blockchain as events occur on-chain. Instead of repeatedly polling for updates, streaming establishes persistent connections that push data to your application instantly when transactions are processed, accounts change, or blocks are produced. This is essential for applications that require up-to-the-second data such as:
  * **Trading applications** monitoring price changes and liquidations
  * **DeFi protocols** tracking user interactions and state changes
  * **NFT marketplaces** detecting sales, listings, and transfers
  * **Analytics platforms** collecting comprehensive blockchain metrics
  * **Wallets** showing real-time balance and transaction updates


## Why choose Helius for data streaming?
## Ultra-Low Latency
Direct connections to Solana leaders ensure sub-second data delivery
## Enterprise Reliability
Multi-node redundancy and automatic failover for 99.9% uptime
## 24-Hour Historical Replay
Never miss data with automatic backfill capabilities
## Global Infrastructure
Endpoints in multiple regions for optimal performance worldwide
## Helius Streaming Solutions
We offer multiple streaming options to match your app’s specific needs, from simple WebSocket connections to ultra-low latency raw data streaming for HFTs.
### Shred Delivery (Beta)
[Shred Delivery](https://www.helius.dev/docs/shred-delivery) is a specialized, ultra-low latency feed of raw Solana shreds delivered via UDP. Requires deshredding capabilities.
#### Key Features
  * Earliest Access: Raw shreds delivered as they’re produced by the network
  * Unprocessed Data: Raw format allows for custom processing tailored to your trading strategies
  * Validator Advantage: Helius is a [top validator](https://www.helius.dev/validator) by stake and receives shreds faster than validators with less stake and non-staked RPC nodes
  * White Glove Provisioning: Managed access with dedicated engineering support
  * Beta Access Only: Currently limited to qualified teams and HFTs


#### Best For
Raw shreds are ideal for latency-critical strategies where milliseconds determine profitability such as:
  * High-frequency trading desks
  * Arbitrage traders
  * Liquidation systems
  * MEV searchers


Interested in trying Shred Delivery? [Apply for a 2-day trial](https://www.helius.dev/shreds-contact); we review every application.
### LaserStream (Developer+ Devnet, Business+ Mainnet)
LaserStream provides ultra low-latency data streaming via gRPC, and includes advanced features such as historical replay, automatic reconnects, and multi-node reliability.
#### Key Features
  * Turnkey: Get faster gRPC streams without the headaches of managing hardware or upgrades
  * 24-Hour Historical Replay: Automatically backfill up to 24 hours of missed data
  * Auto-Reconnection: Built-in connection management with intelligent retry logic
  * Global Endpoints: Available in [9 regions](https://www.helius.dev/docs/laserstream#mainnet-endpoints) worldwide for optimal latency
  * Drop-in Replacement: Compatible with existing Yellowstone gRPC implementations


#### Preprocessed Transactions (Public Beta)
In addition to streaming processed, confirmed, and finalized data, LaserStream can also serve [preprocessed transactions](https://www.helius.dev/docs/laserstream/preprocessed-transactions), or decoded shreds. Instead of waiting for full transaction processing, LaserStream decodes transactions directly from shreds as they arrive at the validator, delivering transaction data **~8 ms faster on average than the processed commitment level**. Preprocessed transactions are available to any **Professional plan or higher** subscriber, metered at the standard LaserStream rate of **20 credits per 1 MB**.
#### Best For
  * Backend services
  * High-throughput applications
  * Mission-critical systems requiring guaranteed data delivery


Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
### Enhanced WebSockets
[Enhanced WSS](https://www.helius.dev/docs/enhanced-websockets) are performance-optimized WebSockets [powered by the same infrastructure](https://www.helius.dev/blog/introducing-next-generation-enhanced-websockets) that powers LaserStream. Enhanced WSS include advanced filtering, and account and transaction subscriptions.
#### Key Features
  * Faster Response Times: Optimized for lower latency than standard WebSockets
  * Enhanced Filtering: Advanced subscription options for precise data targeting
  * Account & Transaction Subscriptions: Monitor specific accounts or transaction patterns
  * Next-gen Infrastructure: Powered by the same high-performance streaming backend thats used by LaserStream


#### Best For
Real-time frontend apps, moderate-volume backends, custom filtering requirements
### Standard WebSockets
Standard [Solana WebSocket API](https://www.helius.dev/docs/rpc/websocket) enhanced with Helius infrastructure reliability.
#### Key Features
  * Full Compatibility: Works with any Solana WebSocket client library
  * Standard Methods: All supported Solana subscription types (accounts, programs, logs, signatures, slots)
  * Multiple Networks: Available on mainnet and devnet
  * Helius Reliability: Enhanced uptime and performance over standard RPC nodes


#### Best For
Existing applications, standard use cases, broad compatibility requirements
### Webhooks
Event-driven, server-to-server [webhook](https://www.helius.dev/docs/webhooks) notifications for on-chain activities delivered to your endpoints.
#### Key Features
  * Parsed Event Data: Human-readable transaction data for sales, swaps, and more
  * Multiple Types: Enhanced, raw, and Discord webhook options
  * Transaction Filtering: Subscribe to specific event types and addresses
  * Reliable Delivery: Automatic retries and delivery confirmations


#### Best For
Event-driven architectures, notifications, integrations with external services
## Getting Started
Choose Your Solution
Select the streaming method that best fits your app requirements and infra.
Get Your API Key
Sign up at [dashboard.helius.dev](https://dashboard.helius.dev) and obtain your API key.
Follow the Quickstart
Each solution has dedicated quickstart guides and code examples.
Monitor & Scale
Use the Helius dashboard to monitor usage and scale your plan as needed.
## [Data Streaming Quickstart Get up and running with your first streaming connection in minutes ](https://www.helius.dev/docs/data-streaming/quickstart)
## Support & Community
## [Documentation Comprehensive API references and guides for all streaming methods ](https://www.helius.dev/docs/api-reference)
## [Discord Community Join thousands of developers building on Solana with Helius ](https://discord.com/invite/6GXdee3gBj)
## [Enterprise Support Priority support channels for business and professional customers ](https://www.helius.dev/docs/support)
Ready to start streaming Solana data? Choose your preferred method above and dive into the documentation!
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/guides/requestairdrop)[ QuickstartGet your first real-time Solana data stream running in under 5 minutes. LaserStream, Enhanced WebSockets, and Webhooks setup guide. Next ](https://www.helius.dev/docs/data-streaming/quickstart)
On this page
  * [What is data streaming on Solana?](https://www.helius.dev/docs/data-streaming#what-is-data-streaming-on-solana)
  * [Why choose Helius for data streaming?](https://www.helius.dev/docs/data-streaming#why-choose-helius-for-data-streaming)
  * [Helius Streaming Solutions](https://www.helius.dev/docs/data-streaming#helius-streaming-solutions)
  * [Shred Delivery (Beta)](https://www.helius.dev/docs/data-streaming#shred-delivery-beta)
  * [LaserStream (Developer+ Devnet, Business+ Mainnet)](https://www.helius.dev/docs/data-streaming#laserstream-developer%2B-devnet-business%2B-mainnet)
  * [Preprocessed Transactions (Public Beta)](https://www.helius.dev/docs/data-streaming#preprocessed-transactions-public-beta)


Assistant
Responses are generated using AI and may contain mistakes.
