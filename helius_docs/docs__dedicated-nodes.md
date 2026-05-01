# Source: https://www.helius.dev/docs/dedicated-nodes

## Considering streaming data?
[LaserStream](https://www.helius.dev/docs/laserstream) is our recommended solution for most streaming use cases. It offers enhanced reliability, [historical replay (24 hours)](https://www.helius.dev/docs/laserstream/historical-replay), auto-reconnection, and multi-node failover without infrastructure management. [Compare LaserStream vs Dedicated Nodes](https://www.helius.dev/docs/laserstream/laserstream-vs-dedicated-nodes) to choose the right solution for your needs.
Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
## What are Dedicated Nodes?
**Dedicated nodes are specifically designed for gRPC streaming applications** and should be combined with a shared plan for comprehensive Solana development needs:
  * **gRPC Streaming** : Real-time blockchain data streaming with ultra-low latency
  * **Data Monitoring** : Account, transaction, and block updates via Yellowstone Geyser
  * **Trading Applications** : High-frequency data feeds for algorithmic trading
  * **Analytics** : Real-time blockchain analytics and monitoring


## Node Options
  * AMD EPYC 7443p
  * AMD EPYC 7543p (Best for resource-intensive RPC calls)
  * AMD EPYC 9254 (Best for resource-intensive RPC calls)


## Access Includes
  * **gRPC streaming** via [Yellowstone Geyser Plugin](https://www.helius.dev/docs/grpc) (primary use case)
  * Standard RPC and WebSocket methods (basic functionality only)
  * Premium support
  * Node clients — Agave (recommended) or Jito Labs


## Limitations
**Important** : Dedicated nodes have specific limitations and are not suitable as standalone solutions:
  * **[`sendTransaction`](https://www.helius.dev/docs/api-reference/rpc/http/sendtransaction)Poor Landing Rates** : While supported, not optimized - most transactions will not land
  * **No Archival Data** : Historical data access is not available
  * **[`getProgramAccounts`](https://www.helius.dev/docs/api-reference/rpc/http/getprogramaccounts)Performance Risk** : While supported, heavy usage can impact node performance or cause node failure
  * **No Platform Features** : APIs, webhooks, and staked connections require a shared plan

**Recommendation** : Use dedicated nodes for gRPC streaming in combination with a shared paid plan for comprehensive functionality.
## Dedicated Fleets
If your team needs a cluster of multiple Dedicated Nodes [contact our sales team](https://www.helius.dev/contact). We’ll review your requirements and help you with a custom solution.
## Ready to Get Started?
To learn how to order a dedicated node, see [How to Order](https://www.helius.dev/docs/dedicated-nodes/getting-started).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/funded-by)[ Getting StartedComplete guide to setting up your Solana dedicated node with gRPC streaming, Yellowstone plugin, and optimal configuration for blockchain data. Next ](https://www.helius.dev/docs/dedicated-nodes/getting-started)
On this page
  * [Considering streaming data?](https://www.helius.dev/docs/dedicated-nodes#considering-streaming-data)
  * [What are Dedicated Nodes?](https://www.helius.dev/docs/dedicated-nodes#what-are-dedicated-nodes)


Assistant
Responses are generated using AI and may contain mistakes.
