# Source: https://www.helius.dev/docs/api-reference/endpoints

RPC (Remote Procedure Call) endpoints are your application’s gateway to Solana. These HTTPS URLs allow you to query account data, fetch transaction history, monitor program state, and interact with Solana programs. For optimized transaction sending with built-in routing and MEV protection, instead of using `sendTransaction`, see [Sender](https://www.helius.dev/docs/sending-transactions/sender).
## Solana RPC Endpoints
High-performance RPC endpoints providing full Solana API compatibility with enhanced reliability and throughput. These endpoints support [all Solana JSON-RPC methods](https://www.helius.dev/docs/api-reference/rpc/http-methods) and now **use staked connections by default** for all paid plans, providing optimal transaction landing rates:
  * **Mainnet** : `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet (Gatekeeper Beta)** : `https://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet** : `https://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`


**Want the fastest experience?** Try our [Gatekeeper (Beta)](https://www.helius.dev/docs/gatekeeper/overview) endpoint for significantly lower latency. Your API key works on both standard and beta endpoints without any changes.
## Secure RPC Endpoints
Secure RPC URLs are specifically masked and IP rate-limited at 5 TPS, making them safe to use directly from frontend applications while [protecting your API keys](https://www.helius.dev/docs/rpc/protect-your-keys):
  * **Mainnet** : `https://abc-456-fast-mainnet.helius-rpc.com`
  * **Devnet** : `https://123-xyz-fast-devnet.helius-rpc.com`


## Solana WebSockets Endpoints
Standard WebSocket endpoints provide real-time data streaming according to the Solana WebSocket protocol. These endpoints support [all standard Solana WebSocket subscription methods](https://www.helius.dev/docs/api-reference/rpc/websocket-methods) including account, program, signature, slot, and log subscriptions:
  * **Mainnet** : `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet (Gatekeeper Beta)** : `wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet** : `wss://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`


Solana WebSockets are now powered by LaserStream, reducing latency by ~200 ms compared to RPC-based WebSockets. Available on all plans. No code changes required.
### Key Features
  * **Powered by LaserStream** : uses the same infra as LaserStream to deliver data up to 200 ms faster than RPC-based WSS.
  * **Supported subscriptions** : `accountSubscribe`, `programSubscribe`, `signatureSubscribe`, `slotSubscribe`, `logsSubscribe`, and more
  * **Protocol compatibility** : Fully compatible with Solana’s WSS API
  * **Best for** : Apps that need to monitor account changes, track transactions, or get real-time updates on Solana activity


## Enhanced WebSockets Endpoints
Enhanced WebSockets, now [powered by LaserStream](https://www.helius.dev/blog/introducing-next-generation-enhanced-websockets), offer low-latency response times compared to RPC-based WebSockets and provide real-time transaction and account updates directly to your apps. To simplify the Solana developer experience, Enhanced WebSockets use the **same** URLs as Standard WebSockets:
  * **Mainnet** : `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet (Gatekeeper Beta)** : `wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet** : `wss://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`


### Key Features
  * **Available for** : Developer, Business, and Professional plans (not the same as Yellowstone Geyser, which requires a Dedicated Node)
  * **Subscription methods** : Supports `transactionSubscribe` and `accountSubscribe`
  * **Connection management** : WebSockets have a 10-minute inactivity timer; implement health checks and send pings every minute to keep connections alive


## Staked Connection Endpoints (Deprecated)
The staked endpoint (`staked.helius-rpc.com`) is deprecated. Use the regular endpoint (`mainnet.helius-rpc.com`), which uses staked connections by default for all paid plans.
  * **Cost** : 1 credit per `sendTransaction` request (reduced from 10 credits)
  * **Automatic optimization** : All transactions are sent over optimized network infrastructure (Asia, Europe, and North America)
  * **Higher landing rates** : Guaranteed access to staked connections during congestion
  * **No code changes** : Existing apps automatically benefit from staked connections


## Next Steps
## [Signup Sign up for free to generate a new API key ](https://www.helius.dev/docs/api-reference/authentication)
## [Agent Signup Use the Helius CLI to sign up agentically ](https://www.helius.dev/docs/api-reference/helius-cli)
## [Enterprise Contact sales for enterprise pricing. ](https://www.helius.dev/contact)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/authentication)[ OverviewComplete reference for all Solana JSON-RPC HTTP methods available through Helius. Account data, blocks, transactions, tokens, epochs, and system information. Next ](https://www.helius.dev/docs/api-reference/rpc/http-methods)
On this page
  * [Solana WebSockets Endpoints](https://www.helius.dev/docs/api-reference/endpoints#solana-websockets-endpoints)
  * [Enhanced WebSockets Endpoints](https://www.helius.dev/docs/api-reference/endpoints#enhanced-websockets-endpoints)
  * [Staked Connection Endpoints (Deprecated)](https://www.helius.dev/docs/api-reference/endpoints#staked-connection-endpoints-deprecated)


Assistant
Responses are generated using AI and may contain mistakes.
