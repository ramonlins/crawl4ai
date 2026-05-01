# Source: https://www.helius.dev/docs/gatekeeper/overview

Gatekeeper is Helius’s new edge gateway, now in public beta, that removes Cloudflare from the critical path. Eliminating our edge latency unlocks the true speed of our core APIs and services—response time improvements range from tens to hundreds of milliseconds. Gatekeeper acts as a single, unified entry-point for all requests (e.g., JSON-RPC, WebSockets, and Helius APIs): it terminates connections at geographically distributed edge locations, and intelligently routes requests to our backend infrastructure. For latency-critical workloads, Gatekeeper provides the shortest network path, reducing hops and shaving off milliseconds.
## Quickstart
To use Gatekeeper, replace your existing endpoint with the Gatekeeper (Beta) endpoint:
Before
After

```
const url = "https://mainnet.helius-rpc.com?api-key=YOUR_API_KEY";

```

**That’s it!** Your existing API key works without any additional changes.
## Supported Methods
Gatekeeper currently supports:
  * All standard Solana RPC endpoints
  * All Helius-specific RPC endpoints (e.g., gTFA) 
  * All Standard and Enhanced WebSockets endpoints
  * All DAS API endpoints
  * All Photon API endpoints (i.e., ZK Compression)
  * The Helius Priority Fee API
  * The Enhanced Transactions API


**Currently not supported** : LaserStream is not yet available on Gatekeeper. Continue using the dedicated [LaserStream endpoints](https://www.helius.dev/docs/laserstream#mainnet-endpoints) for gRPC connections.
## Usage Examples
JavaScript/TypeScript
Python
Rust
cURL

```
const url = `https://beta.helius-rpc.com?api-key=${YOUR_API_KEY}`;

const response = await fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    id: 1,
    method: 'getLatestBlockhash',
    params: []

});

const data = await response.json();
console.log(data);

```

## WebSocket Support
Gatekeeper supports Standard and Enhanced WebSocket connections with the same performance improvements.

```
const ws = new WebSocket(`wss://beta.helius-rpc.com?api-key=${YOUR_API_KEY}`);

ws.on('open', () => {
  ws.send(JSON.stringify({
    jsonrpc: '2.0',
    id: 1,
    method: 'transactionSubscribe',
    params: [

        accountInclude: ['YOUR_ACCOUNT_ADDRESS']


        commitment: 'confirmed',
        encoding: 'jsonParsed',
        transactionDetails: 'full',
        showRewards: true,
        maxSupportedTransactionVersion: 0


  }));
});

ws.on('message', (data) => {
  console.log('Transaction:', JSON.parse(data));
});

```

## What to Expect
During the beta period:
  * **Lower Latency** - Significantly faster response times across the board
  * **Better Performance Under Load** - Improved reliability during high-traffic periods
  * **More Consistent Response Times** - Reduced variance in latency
  * **Improved WebSocket Stability** - More reliable real-time connections
  * **Full API Compatibility** - All existing RPC methods work identically
  * **Same Pricing** - No additional cost for beta access
  * **Global Distribution** - Edge nodes across multiple continents


## Who should use Gatekeeper?
Gatekeeper is ideal for applications where performance matters:
  * **High-Frequency Applications** - Any app where latency matters
  * **Trading Bots** - Maximum speed for arbitrage opportunities
  * **DeFi Protocols** - Real-time price feeds and fast transaction submission
  * **Gaming Applications** - Low response times for smooth UX
  * **NFT Marketplaces** - Instant minting and low-latency queries


## Migration Checklist
Update Your Endpoint
Change `mainnet.helius-rpc.com` to `beta.helius-rpc.com` in your code
Test in Development
Run your test suite to verify everything works as expected
Monitor Performance
Check your metrics—you should see improved latency and more consistent response times
Deploy to Production
Once verified, deploy your changes to production
## Rollback
If you need to rollback for any reason, simply switch back to the standard endpoint:

```
const url = "https://mainnet.helius-rpc.com?api-key=YOUR_API_KEY";

```

## Limitations & Known Issues
**Beta Status** : Gatekeeper is production-ready but still being optimized. We recommend testing in development before switching production traffic.
**Not yet supported:**
  * **LaserStream** : Use the dedicated [LaserStream endpoints](https://www.helius.dev/docs/laserstream#mainnet-endpoints) for gRPC connections

**Current status:**
  * Some advanced features are still being rolled out
  * We’re continuously optimizing routing algorithms
  * Performance improvements are ongoing


## Rollout Plan
Gatekeeper is currently **opt-in** while we optimize performance and gather feedback. Timeline:
  * **Now** : Public beta available to all users
  * **Coming Weeks** : Additional optimizations and performance improvements
  * **Coming Months** : Gradual migration of all traffic to Gatekeeper as the default


## Feedback & Support
We’re actively monitoring Gatekeeper’s performance and would love your feedback:
  * **Issues or questions?** Contact support@helius.dev
  * **Join our Discord** for real-time discussion: <https://discord.com/invite/6GXdee3gBj>
  * **Report bugs** through your developer dashboard


## FAQs
Do I need a new API key?
No. Your existing API key works with Gatekeeper without any changes.
Will Gatekeeper cost extra?
No. Gatekeeper is available at no additional cost. Your existing pricing plan applies.
What endpoints are supported on Gatekeeper?
All JSON-RPC endpoints are fully supported, including standard Solana RPC methods, Helius-specific RPC endpoints (e.g., gTFA), DAS, Photon, Priority Fee API, and the Enhanced Transactions API. Standard and Enhanced WebSockets are also supported.
What endpoints are not yet supported on Gatekeeper?
LaserStream is not yet available on Gatekeeper. For gRPC connections, use the dedicated [LaserStream endpoints](https://www.helius.dev/docs/laserstream#mainnet-endpoints).
What if I encounter issues using Gatekeeper?
You can easily rollback by switching back to `mainnet.helius-rpc.com`. Contact [support](https://www.helius.dev/docs/support) if you need help.
When will Gatekeeper become the default?
We’re planning a gradual rollout over the coming months. We’ll notify all users before making any changes to the default Helius endpoints.
Can I use Gatekeeper on Solana Devnet or Testnet?
No, Gatekeeper is currently only available on Solana Mainnet. Solana Devnet and Testnet support is coming soon.
## Get Started
## [Try Gatekeeper Migrate to Gatekeeper in less than 5 minutes ](https://www.helius.dev/docs/gatekeeper/migration-guide)
## [Learn About Gatekeeper Read our blog to understand how Gatekeeper works ](https://www.helius.dev/blog/introducing-gatekeeper)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/overview)[ Migration GuideStep-by-step guide to migrate your application to Gatekeeper Next ](https://www.helius.dev/docs/gatekeeper/migration-guide)
On this page
  * [Who should use Gatekeeper?](https://www.helius.dev/docs/gatekeeper/overview#who-should-use-gatekeeper)
  * [Limitations & Known Issues](https://www.helius.dev/docs/gatekeeper/overview#limitations-%26-known-issues)


Assistant
Responses are generated using AI and may contain mistakes.
