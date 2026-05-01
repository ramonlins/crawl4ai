# Source: https://www.helius.dev/docs/rpc/overview

Helius offers a globally distributed Solana JSON-RPC service — a fleet of bare-metal nodes across 11 regions with automatic routing to the nearest edge, built for low-latency production workloads.
## [Start Building Now Get your RPC endpoint and make your first request ](https://www.helius.dev/docs/rpc/overview#getting-your-rpc-url)
## [Browse RPC Methods Explore practical guides for all Solana RPC methods ](https://www.helius.dev/docs/rpc/guides/overview)
## Global Solana RPC Coverage
Access our RPC node fleet across the following regions with automatic routing to the nearest node:
  * Pittsburgh (PIT)
  * Newark (EWR)
  * Salt Lake City (SLC)
  * Los Angeles (LAX)
  * Vancouver (VAN)
  * Dublin (DUB)
  * London (LON)
  * Amsterdam (AMS)
  * Frankfurt (FRA)
  * Singapore (SGP)
  * Tokyo (TYO)


**New: Try Gatekeeper (Beta)** - Our high-performance edge gateway delivers significantly lower latency. Simply replace `mainnet.helius-rpc.com` with `beta.helius-rpc.com` in your code. [Learn more →](https://www.helius.dev/docs/gatekeeper/overview)
## Why Developers Choose Helius RPC
## 99.99% Uptime
Enterprise-grade reliability with automatic failover and multi-node redundancy
## <100ms Latency
Global infrastructure optimized for speed with multiple regions worldwide
## 24/7 Support
Expert engineering support and active Discord community
## What are RPCs?
RPCs gives your application high-performance access to Solana data and transaction submission. With 99.99% uptime and sub-100ms global latency, Helius routes requests across nodes in 11 regions worldwide. Beyond standard Solana RPC methods, every plan includes the DAS API for NFT queries, priority fee estimation, and enhanced transaction parsing — no extra infrastructure required.
## Getting Your RPC URL
Go to Dashboard
Navigate to [dashboard.helius.dev](https://dashboard.helius.dev) and sign up or log in
Create a Plan
Choose a plan that fits your needs - free tier available to get started
Go to RPCs Section
Navigate to the RPCs section in your dashboard
Copy Your Endpoint
Copy your RPC endpoint URL for the network you want to use (mainnet or devnet)
## Test Your Connection
Choose your preferred language to test your RPC connection:
  * JavaScript/TypeScript
  * Python
  * Rust
  * cURL



```
import { Connection } from '@solana/web3.js';

// Your Helius RPC URL from dashboard
const rpcUrl = 'YOUR_HELIUS_RPC_URL';
const connection = new Connection(rpcUrl);

// Test the connection
const testConnection = async () => {
  try {
    const version = await connection.getVersion();
    const slot = await connection.getSlot();

    console.log('Connection successful!');
    console.log(`Solana version: ${version['solana-core']}`);
    console.log(`Current slot: ${slot}`);
catch (error) {
    console.error('Connection failed:', error);



testConnection();

```


```
from solana.rpc.api import Client

# Your Helius RPC URL from dashboard
rpc_url = 'YOUR_HELIUS_RPC_URL'
client = Client(rpc_url)

# Test the connection
try:
    version = client.get_version()
    slot = client.get_slot()

    print('Connection successful!')
    print(f'Solana version: {version.value}')
    print(f'Current slot: {slot.value}')
except Exception as e:
    print(f'Connection failed: {e}')

```


```
use solana_client::rpc_client::RpcClient;
use solana_sdk::commitment_config::CommitmentConfig;

#[tokio::main]
async fn main() -> Result<(), Boxdyn std::error::Error>> {
    // Your Helius RPC URL from dashboard
    let rpc_url = "YOUR_HELIUS_RPC_URL";

    let client = RpcClient::new_with_commitment(
        rpc_url.to_string(),
        CommitmentConfig::confirmed(),


    // Test the connection
    match client.get_version() {
(version) => {
            println!("Connection successful!");
            println!("Solana version: {:?}", version.solana_core);

            let slot = client.get_slot()?;
            println!("Current slot: {}", slot);

        Err(err) => println!("Connection failed: {}", err),


    Ok(())


```


```
curl -X POST "YOUR_HELIUS_RPC_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getVersion"
  }' | jq

```

## Choose Your RPC Solution
### Regular RPC Nodes (Recommended)
## Best for 99% of Applications
**Superior performance, reliability, and features at cost-effective pricing**
  * **Superior Performance** : Multi-node redundancy with optimized infrastructure
  * **Maximum Reliability** : No single points of failure, automatic failover
  * **Complete API Coverage** : All Solana RPC methods plus enhanced APIs
  * **Global Infrastructure** : Multiple regions for optimal latency
  * **Enhanced Features** : DAS API, Priority Fee API, Enhanced Transactions included
  * **Starting at $0** : Generous free tier, pay only for what you use


### Dedicated RPC Nodes (Limited Use Cases)
## Only for Unlimited Credits/Rate Limits
**Consider only if you specifically need unlimited credits and rate limits****When to Consider:**
  * Require unlimited credits
  * Require unlimited rate limits

**Important Trade-offs:**
  * Performance risk: Can become slow under high load
  * Higher cost: $2,300+/month plus requires shared plan
  * Limited features: Missing advanced APIs


## [Learn More About Dedicated Nodes Explore dedicated options (only if you need unlimited credits/rates) ](https://www.helius.dev/docs/dedicated-nodes)
## Use Case Recommendations
  * DeFi Applications
  * NFT Marketplaces
  * Wallets & Explorers
  * Analytics Platforms


**Real-time Trading & AMM Data**
  * Monitor account changes for price updates
  * Track swap transactions and liquidity changes
  * Submit time-sensitive arbitrage transactions

**Recommended:** Regular RPC Plan
**Collection Monitoring & Sales Tracking**
  * Query NFT metadata and ownership
  * Monitor marketplace program accounts
  * Track sales and listing events

**Recommended:** Regular RPC Plan
**Account Management & Transaction History**
  * Fetch account balances and token holdings
  * Display transaction history with parsed data
  * Submit user transactions reliably

**Recommended:** Regular RPC Plan
**Data Collection & Processing**
  * Bulk account and transaction queries
  * Historical data analysis
  * Real-time blockchain monitoring

**Recommended:** Regular RPC Plan
## What’s Next?
## [Optimize Performance Learn advanced techniques to maximize RPC performance and minimize costs ](https://www.helius.dev/docs/rpc/optimization-techniques)
## [Real-time Data Set up streams for live blockchain events ](https://www.helius.dev/docs/data-streaming)
## Get Started
You now have everything needed to start building on Solana with Helius RPC. Check out our [complete API reference](https://www.helius.dev/docs/api-reference) for detailed method documentation, or join our [Discord community](https://discord.gg/aXjCcEDN) to connect with other developers and get support from our team.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/billing/rate-limits)[ OverviewHelius's high-performance edge gateway purpose-built for Solana Next ](https://www.helius.dev/docs/gatekeeper/overview)
On this page
  * [Global Solana RPC Coverage](https://www.helius.dev/docs/rpc/overview#global-solana-rpc-coverage)
  * [Why Developers Choose Helius RPC](https://www.helius.dev/docs/rpc/overview#why-developers-choose-helius-rpc)
  * [Choose Your RPC Solution](https://www.helius.dev/docs/rpc/overview#choose-your-rpc-solution)
  * [Regular RPC Nodes (Recommended)](https://www.helius.dev/docs/rpc/overview#regular-rpc-nodes-recommended)
  * [Dedicated RPC Nodes (Limited Use Cases)](https://www.helius.dev/docs/rpc/overview#dedicated-rpc-nodes-limited-use-cases)
  * [Use Case Recommendations](https://www.helius.dev/docs/rpc/overview#use-case-recommendations)


Assistant
Responses are generated using AI and may contain mistakes.
