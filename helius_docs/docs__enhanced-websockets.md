# Source: https://www.helius.dev/docs/enhanced-websockets

## What are Enhanced Websockets?
Enhanced WebSockets enable real-time monitoring of Solana activity with advanced filtering compared to [standard WebSocket APIs](https://www.helius.dev/docs/rpc/websocket). Enhanced WebSockets are built on the same high-performance infrastructure as [LaserStream](https://www.helius.dev/docs/laserstream), our next-gen gRPC streaming service built for speed, simplicity, and fault-tolerance. Enhanced WSS are ideal for applications requiring low-latency notifications of transaction confirmations, account state changes, or program interactions without having to manage dedicated nodes and gRPC connections.
### Supported Methods
Enhanced WSS support two subscription methods:
  * [`transactionSubscribe`](https://www.helius.dev/docs/enhanced-websockets/transaction-subscribe)


### Enhanced WSS Availability
Enhanced WSS are available on Developer, Business, and Professional [plans](https://www.helius.dev/docs/billing/plans).
### Enhanced WSS Metering
All Enhanced WSS usage is metered at **2 credits per 0.1 MB** of streamed data.
### Enhanced WSS Data Add-ons
For high-volume data streaming on Professional plans, [**Data Add-Ons**](https://www.helius.dev/docs/billing/plans#data-add-ons) provide monthly data allowances (5TB-100TB) at predictable costs. Data add-ons can be applied to LaserStream and Enhanced WSS.
## Enhanced WSS Endpoints
Enhanced WSS are now supported on the same [endpoints](https://www.helius.dev/docs/api-reference/endpoints) as Standard WSS to provide a unified entrypoint for all requests: **Mainnet:** `wss://mainnet.helius-rpc.com/?api-key=<API_KEY>` **Devnet:** `wss://devnet.helius-rpc.com/?api-key=<API_KEY>`
### Gatekeeper (Beta)
To test our fastest WSS offering, try the new Gatekeeper (Beta) endpoint: `wss://beta.helius-rpc.com/?api-key=<API_KEY>`
#### Will the old Enhanced WSS endpoints continue to be supported?
Yes. Use the **same unified WebSocket URLs** as Standard WSS (`wss://mainnet.helius-rpc.com` and `wss://devnet.helius-rpc.com`) for Enhanced WebSockets.
## Troubleshooting
WebSockets have a 10-minute inactivity timer. To keep the WebSocket connection alive, we recommended that you implement [health checks](https://www.helius.dev/docs/faqs/websockets#why-are-my-enhanced-websockets-connections-disconnecting) and that pings be sent every minute.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/grpc/stream-pump-amm-data)[ Transaction SubscribeStream real-time Solana transaction updates with `transactionSubscribe`. Monitor blockchain activity, filter by accounts, and receive instant notifications. Next ](https://www.helius.dev/docs/enhanced-websockets/transaction-subscribe)
On this page
  * [What are Enhanced Websockets?](https://www.helius.dev/docs/enhanced-websockets#what-are-enhanced-websockets)
  * [Enhanced WSS Availability](https://www.helius.dev/docs/enhanced-websockets#enhanced-wss-availability)
  * [Enhanced WSS Metering](https://www.helius.dev/docs/enhanced-websockets#enhanced-wss-metering)
  * [Enhanced WSS Data Add-ons](https://www.helius.dev/docs/enhanced-websockets#enhanced-wss-data-add-ons)
  * [Will the old Enhanced WSS endpoints continue to be supported?](https://www.helius.dev/docs/enhanced-websockets#will-the-old-enhanced-wss-endpoints-continue-to-be-supported)


Assistant
Responses are generated using AI and may contain mistakes.
