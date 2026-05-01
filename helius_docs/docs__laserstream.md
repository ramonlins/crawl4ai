# Source: https://www.helius.dev/docs/laserstream

## What is LaserStream?
LaserStream is a next-generation streaming service **purpose-built for developers who need reliable, low-latency Solana data**. It delivers on-chain events (transactions, slots, blocks, accounts, and more) directly to your application with industry-leading reliability, performance, and flexibility. Similar to our gRPC offerings, LaserStream nodes tap directly into Solana leaders to receive shreds as they’re produced, delivering ultra-low latency data to your application. Unlike standard Solana RPC nodes, LaserStream is specifically designed for streaming use cases, offering features not available in conventional node setups:
## Historical Replay
Automatically backfill missed data from the last 24 hours by specifying a starting slot, ensuring data continuity even after disconnections.
## Multi-Node Reliability
Stream from multiple aggregated nodes simultaneously, eliminating single points of failure and ensuring maximum uptime.
## High Performance
Purpose-built for streaming with optimized connection handling, reducing latency and improving throughput compared to standard connections.
## Protocol Flexibility
Choose your preferred protocol to match your application’s needs and environment requirements.
### Plan Requirements
LaserStream Devnet is available for Developer and above [plans](https://www.helius.dev/docs/billing/plans). LaserStream Mainnet access requires a Business or Professional plan.
Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
## LaserStream vs. Shred Delivery: Quick Comparison
LaserStream delivers **processed data** with commitment-level guarantees (processed, confirmed, finalized), making it turnkey and production-ready. For the **earliest possible raw data** before any processing occurs, see [Shred Delivery](https://www.helius.dev/docs/shred-delivery) (requires custom deshredding logic). For decoded shreds that arrive **~8 ms faster than processed on average** , see [Preprocessed Transactions (Public Beta)](https://www.helius.dev/docs/laserstream/preprocessed-transactions) — available to any Professional plan subscriber at the standard LaserStream rate of 20 credits per 1 MB.  
| Feature  | LaserStream  | Shred Delivery  |  
| --- | --- | --- |  
| **Data Type**  | Processed data with commitment guarantees  | Raw, unprocessed shreds  |  
| **Latency**  | Ultra-low latency processed data  |  **Earliest possible** - before any processing  |  
| **Processing**  | Turnkey - data is processed and ready to use  |  **You must process raw data** - requires custom deshredding logic  |  
| **Best For**  | Production applications, analytics, backend services  | High-frequency trading, arbitrage (when milliseconds matter)  |  
| **Setup**  | Developer-friendly SDKs, drop-in replacement  | White glove provisioning (beta access required)  |  
Want to try Shred Delivery? [Apply for a 2-day trial](https://www.helius.dev/shreds-contact); we review every application.
## Easy Migration
LaserStream gRPC is designed as a seamless drop-in replacement for your existing gRPC setup. Simply change your endpoint and API token, and your application will work with LaserStream immediately.
### Using Existing gRPC Code
If you already use Yellowstone gRPC, migrating to LaserStream is as simple as:

```
// Before: Using standard Yellowstone gRPC
const connection = new GeyserConnection(
  "your-current-endpoint.com",
token: "your-current-token" }


// After: Using LaserStream (just change endpoint and token)
const connection = new GeyserConnection(
  "https://laserstream-mainnet-ewr.helius-rpc.com", // Choose your closest region
token: "your-helius-api-key" }


```

### Enhanced Experience with the LaserStream SDK
While LaserStream works with your existing code, we highly recommend using our [LaserStream SDK](https://github.com/helius-labs/laserstream-sdk) for enhanced capabilities:

```
// Using the dedicated LaserStream SDK
import { subscribe, CommitmentLevel, LaserstreamConfig } from 'helius-laserstream';

const config = {
  apiKey: "your-helius-api-key",
  endpoint: "https://laserstream-mainnet-ewr.helius-rpc.com" // Choose your closest region


// The SDK automatically handles:
// - Connection management
// - Reconnection with backoff
// - Historical replay after disconnects
// - Subscription management
await subscribe(config, subscriptionRequest, handleData, handleError);

```

## [LaserStream SDK is 40x Faster vs. JavaScript Yellowstone Clients Learn how we used Rust Core with zero-copy NAPI bindings to maximize JavaScript SDK performance ](https://www.helius.dev/blog/laserstream-sdks)
## Key Features
### Automatic Reconnection & Catch-up
The [LaserStream SDK](https://github.com/helius-labs/laserstream-sdk) automatically handles dropped connections, network issues, and data gaps. When a reconnection occurs, the SDK automatically:
  * Reconnects with minimal delay
  * Re-streams any data that was missed during the downtime
  * Continues streaming without intervention


### Advanced Filtering
LaserStream supports sophisticated filtering options:
  * **Account Filtering** : Include, exclude, or require specific accounts
  * **Transaction Types** : Filter by transaction status, vote transactions, etc.
  * **Commitment Levels** : Choose from processed, confirmed, or finalized
  * **Data Content** : Request specific data fields or full data


### Extreme Scalability
  * **Load Balancing** : Connections distributed across multiple nodes
  * **Auto-scaling** : Backend resources scale to match demand
  * **Efficient Routing** : Requests automatically routed to the most responsive node


## Endpoints & Regions
LaserStream is available in multiple regions worldwide for optimal performance. Choose the endpoint closest to your application’s location:
### Mainnet Endpoints  
| Region  | Location  | Endpoint  |  
| --- | --- | --- |  
| **ewr**  | Newark, NJ (near New York)  | `https://laserstream-mainnet-ewr.helius-rpc.com`  |  
| **pitt**  | Pittsburgh, US (Central)  | `https://laserstream-mainnet-pitt.helius-rpc.com`  |  
| **slc**  | Salt Lake City, US (West Coast)  | `https://laserstream-mainnet-slc.helius-rpc.com`  |  
| **lax**  | Los Angeles, US (West Coast)  | `https://laserstream-mainnet-lax.helius-rpc.com`  |  
| **lon**  | London, Europe  | `https://laserstream-mainnet-lon.helius-rpc.com`  |  
| **ams**  | Amsterdam, Europe  | `https://laserstream-mainnet-ams.helius-rpc.com`  |  
| **fra**  | Frankfurt, Europe  | `https://laserstream-mainnet-fra.helius-rpc.com`  |  
| **tyo**  | Tokyo, Asia  | `https://laserstream-mainnet-tyo.helius-rpc.com`  |  
| **sgp**  | Singapore, Asia  | `https://laserstream-mainnet-sgp.helius-rpc.com`  |  
### Devnet Endpoint  
| Network  | Location  | Endpoint  |  
| --- | --- | --- |  
| **Devnet**  | Newark, NJ (near New York)  | `https://laserstream-devnet-ewr.helius-rpc.com`  |  
**Choosing Your Network & Region**:
  * For **production applications** , use a mainnet endpoint closest to your server location. For example, if your server is in Frankfurt, use `https://laserstream-mainnet-fra.helius-rpc.com`.
  * For **development and testing** , use the devnet endpoint: `https://laserstream-devnet-ewr.helius-rpc.com`.


## Authentication & Availability
LaserStream uses your Helius API key for authentication. You can obtain your API key from the [Helius Dashboard](https://dashboard.helius.dev/). Your API key serves as both your authentication token and grants access to LaserStream’s enhanced features.
**Plan Requirements** :
  * **LaserStream Devnet** : Available for Developer ($49/month), Business ($499/month), and Professional ($999/month) plans. Pay 2 credits per 0.1 MB for all devnet usage.
  * **LaserStream Mainnet** : Available for Business ($499/month) and Professional ($999/month) plans. Pay 2 credits per 0.1 MB for all mainnet and devnet usage.

You can upgrade your plan in the [Helius Dashboard](https://dashboard.helius.dev/).
### Need High-Volume Streaming? LaserStream Plus Add-Ons
For applications consuming massive amounts of real-time data, LaserStream Plus transforms unpredictable pay-per-use costs into predictable monthly expenses with significant savings.
## Cost Transformation
**From:** Pay-per-use at 2 credits/0.1 MB **To:** Fixed monthly cost + included data allowance
## Multiple Tiers Available
**5TB to 100TB+** monthly allowances. Visit our [plans](https://www.helius.dev/docs/billing/plans) page for full pricing details.
**When to consider LaserStream Plus:**
  * Your app processes full market data streams (all DEX trades, NFT sales, etc.)
  * You’re building high-frequency trading systems
  * You need 24/7 account monitoring across thousands of wallets


## Getting Started
## [gRPC Performance-optimized streaming for backend services and high-throughput apps ](https://www.helius.dev/docs/laserstream/grpc)
For apps that need to catch up on historical data or need fault-tolerant connections:
## [24-Hour Historical Replay Learn how to implement historical replay to ensure data continuity ](https://www.helius.dev/docs/laserstream/historical-replay)
## When to Use LaserStream vs. Other Solana Streaming Options  
| Feature  | LaserStream  | Standard Solana WebSocket  | Yellowstone gRPC  |  
| --- | --- | --- | --- |  
| **Historical replay**  | ✅ Up to 216,000 slots (approx. 24 hours)  | ❌ Not available  | ❌ Limited  |  
| **Auto-reconnect**  | ✅ Built-in with SDK  | ❌ Manual implementation  | ❌ Manual implementation  |  
| **Multi-node failover**  | ✅ Automatic  | ❌ Manual implementation  | ❌ Manual implementation  |  
| **gRPC support**  | ✅ Enhanced  | ❌ Not available  | ✅ Standard  |  
| **Shredstream enabled**  | ✅ Yes  | ❌ No  | ❌ Manual  |  
## Next Steps
For more information, join the discussion on our [Discord](https://discord.com/invite/6GXdee3gBj) or [Telegram](https://t.me/helius_help).
## Attribution
LaserStream is a custom fork of [Richat](https://github.com/lamports-dev/richat) project.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/shred-delivery)[ gRPCStream real-time Solana blockchain data. Highly configurable low-latency streams with 24-hour historical replay and multi-region support. Next ](https://www.helius.dev/docs/laserstream/grpc)
On this page
  * [LaserStream vs. Shred Delivery: Quick Comparison](https://www.helius.dev/docs/laserstream#laserstream-vs-shred-delivery-quick-comparison)
  * [Using Existing gRPC Code](https://www.helius.dev/docs/laserstream#using-existing-grpc-code)
  * [Enhanced Experience with the LaserStream SDK](https://www.helius.dev/docs/laserstream#enhanced-experience-with-the-laserstream-sdk)
  * [Automatic Reconnection & Catch-up](https://www.helius.dev/docs/laserstream#automatic-reconnection-%26-catch-up)
  * [Authentication & Availability](https://www.helius.dev/docs/laserstream#authentication-%26-availability)
  * [Need High-Volume Streaming? LaserStream Plus Add-Ons](https://www.helius.dev/docs/laserstream#need-high-volume-streaming-laserstream-plus-add-ons)
  * [When to Use LaserStream vs. Other Solana Streaming Options](https://www.helius.dev/docs/laserstream#when-to-use-laserstream-vs-other-solana-streaming-options)


Assistant
Responses are generated using AI and may contain mistakes.
