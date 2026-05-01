# Source: https://www.helius.dev/docs/shred-delivery

## [Request Access Submit your application for a 2-day Shred Delivery trial ](https://www.helius.dev/shreds-contact)
## What is Helius Shred Delivery?
[Shred Delivery](https://www.helius.dev/shreds) is Helius’s **specialized delivery of raw Solana shreds via UDP** , designed to provide you with the earliest possible access to Solana’s raw transaction data. By delivering unprocessed shreds directly from the network, Shred Delivery offers a significant competitive edge for high-frequency trading (HFT), arbitrage strategies, and other latency-sensitive apps.
## Earliest Access
Receive raw Solana shreds as they are produced, providing the fastest insight into network activity.
## Unprocessed Data
Access data in its raw form, allowing for customized processing tailored to your specific trading strategies.
## Validator Advantage
Helius is the top validator by stake and receives shreds faster than validators with less stake and non-staked RPC nodes.
## White Glove Provisioning
Carefully provisioned access ensures optimal performance and dedicated support from the Helius team.
## What are shreds?
In Solana, transactions are broken down into smaller data packets called **“shreds”** to facilitate efficient and rapid propagation across the network. Each shred is a fragment of transaction data, optimized to fit within standard network packets, ensuring swift distribution and reconstruction into complete blocks by validators. This architecture is pivotal for maintaining Solana’s high throughput and low latency, and Shred Delivery taps directly into this raw data stream before any processing occurs.
## [Deep Dive: Understanding Solana Shreds Read our comprehensive blog post explaining how Solana’s shred mechanism works and why it matters for trading ](https://www.helius.dev/blog/solana-shreds)
## Shred Delivery vs. LaserStream
While both Shred Delivery and LaserStream are flagship data streaming offerings from Helius, they serve distinct purposes:
## Shred Delivery
**Earliest Possible Data**
  * Raw shreds delivered as they’re produced
  * Earliest possible on-chain signal - no processing delay
  * Requires deshredding logic
  * White glove provisioning only
  * High-frequency traders & arbitrage strategies


## LaserStream
**Turnkey Processed Data**
  * Commitment-level guarantees (processed, confirmed, finalized)
  * 24-Hour historical replay
  * Developer-friendly SDKs
  * Automatic reconnection
  * Production apps & analytics


### When to Choose Shred Delivery
Choose Shred Delivery when you need the **earliest possible access** to raw transaction data and have the technical capability to process raw shreds. Shred Delivery provides the absolute lowest latency by delivering unprocessed shreds directly from the network—but you must implement your own deshredding and processing logic.
### When to Choose LaserStream
Choose LaserStream when you need reliable, processed data with commitment guarantees, [historical replay capabilities](https://www.helius.dev/docs/laserstream/historical-replay), and developer-friendly tooling. LaserStream delivers processed transactions with commitment-level guarantees, making it ideal for production applications that need reliable data delivery without custom processing infrastructure. LaserStream also offers [Preprocessed Transactions (Public Beta)](https://www.helius.dev/docs/laserstream/preprocessed-transactions), or decoded shreds, which arrive **~8 ms faster on average than the standard`processed` commitment level** (but slower than raw, unprocessed shreds). Available to any Professional plan subscriber at the standard LaserStream rate of 20 credits per 1 MB.
## [Learn About LaserStream Learn how LaserStream works and how to start streaming data ](https://www.helius.dev/docs/laserstream)
## [LaserStream Trial Apply for a 2-day trial to compare LaserStream vs. alternative solutions before you subscribe ](https://www.helius.dev/laserstream-contact)
### Summary
Shred Delivery provides the **earliest possible on-chain signal** by delivering raw, unprocessed shreds directly from the network. However, you must implement custom deshredding logic to process this raw data. For processed data with commitment guarantees and developer-friendly tooling, see [LaserStream](https://www.helius.dev/docs/laserstream).  
| Feature  | Shred Delivery  | LaserStream  |  
| --- | --- | --- |  
| **Data Type**  | Raw, unprocessed shreds  | Processed data with commitment guarantees  |  
| **Latency**  |  **Earliest possible** - before any processing  | Ultra-low latency processed data  |  
| **Processing**  |  **You must process raw data** - requires custom deshredding logic  | Turnkey - data is processed and ready to use  |  
| **Best For**  | High-frequency trading, arbitrage (when milliseconds matter)  | Production applications, analytics, backend services  |  
| **Setup**  | White glove provisioning  | Developer-friendly SDKs, drop-in replacement  |  
## The Helius Validator Advantage
Helius is the top validator by stake weight and receives shreds faster than validators with less stake and non-staked RPC nodes. In Turbine, validators with higher stake weights receive priority in the data propagation tree, meaning block leaders send shreds to high-stake validators like Helius first. This stake-weighted propagation ensures we receive shreds at the earliest possible moment in the network’s data flow. While other providers must wait for secondary propagation or rely on unstaked infrastructure, our validator position grants direct, prioritized access to the raw transaction data as it flows through the network.
## Technical Requirements
To effectively utilize Shred Delivery, your system should have:
## Deshredding Capability
Custom logic to reconstruct complete transactions from raw shreds
## Low-Latency Infrastructure
High-performance systems optimized for microsecond-level processing
## Trading Logic Integration
Ability to act on unprocessed data with appropriate risk management
## Network Optimization
Optimized network configuration for minimal processing delays
**Technical Expertise Required** : Shred Delivery provides raw, unprocessed shreds via UDP. Your team must have the technical capability to properly handle deshredding and implement appropriate processing logic.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/data-streaming/quickstart)[ OverviewNext-generation Solana data streaming with ultra-low latency, historical replay, and multi-node reliability. Purpose-built for high-performance applications. Next ](https://www.helius.dev/docs/laserstream)
On this page
  * [What is Helius Shred Delivery?](https://www.helius.dev/docs/shred-delivery#what-is-helius-shred-delivery)
  * [Shred Delivery vs. LaserStream](https://www.helius.dev/docs/shred-delivery#shred-delivery-vs-laserstream)
  * [When to Choose Shred Delivery](https://www.helius.dev/docs/shred-delivery#when-to-choose-shred-delivery)
  * [When to Choose LaserStream](https://www.helius.dev/docs/shred-delivery#when-to-choose-laserstream)
  * [The Helius Validator Advantage](https://www.helius.dev/docs/shred-delivery#the-helius-validator-advantage)


Assistant
Responses are generated using AI and may contain mistakes.
