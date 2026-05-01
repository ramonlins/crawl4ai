# Source: https://www.helius.dev/docs/faqs/websockets

## Billing and Rate Limits
How many credits does WebSocket events consume?
Opening a new WebSocket connection costs 1 credit. All WebSocket streaming data (Standard and Enhanced) is metered at 2 credits per 0.1 MB. Standard WSS metering activates on April 12, 2026 after a 30-day grace period.
How much faster are Enhanced Websockets vs. normal WebSockets?
Enhanced WebSockets are, on average, 1.5x - 2x faster than standard WebSockets. They provide faster response times through optimized infrastructure and direct access to Helius’s streaming backend, making them ideal for high-performance applications requiring low-latency data.
## Disconnects and Retries
Why are my Enhanced WebSockets connections disconnecting?
Enhanced WebSockets have a 10-minute inactivity timer that disconnects idle connections. To prevent disconnections:
  1. **Implement health checks** : Send pings every minute to keep connections alive
  2. **Add reconnection logic** : Automatically reconnect when disconnections occur
  3. **Use proper connection management** : Follow the patterns shown in our [Enhanced WebSockets documentation](https://www.helius.dev/docs/enhanced-websockets/transaction-subscribe)

Implement reconnection and ping logic as shown in our documentation, then add your application logic on top of this foundation.
## Using WebSockets
What endpoints should I use for WebSockets?
Standard and Enhanced WebSockets now use the same endpoints for Solana Mainnet and Devnet respectively: `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY` and `wss://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`. For the fastest Solana WebSockets, try the new [Gatekeeper (Beta)](https://www.helius.dev/docs/gatekeeper/overview) WebSockets endpoint: `wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY`.
Will the original Enhanced WebSockets endpoints continue to be supported?
Yes. Enhanced WebSockets use the same [unified WebSockets endpoints](https://www.helius.dev/docs/api-reference/endpoints#solana-websocket-endpoints) as Standard WebSockets (`wss://mainnet.helius-rpc.com` and `wss://devnet.helius-rpc.com`).
What is the difference between Standard and Enhanced WebSockets?
Historically, Standard WebSockets were served via RPCs and supported all standard Solana subscription methods (e.g., accounts, programs, logs, etc.). while Enhanced WebSockets were served via Geyser and only supported `accountSubscribe` and `transactionSubscribe`. Today, Standard WSS and Enhanced WSS are both powered by LaserStream, and can be used from the same API endpoint. We recommend all developers use the [unified WSS endpoint](https://www.helius.dev/docs/api-reference/endpoints) for simplicity.
What is the maximum number of active WebSocket connections?
On the Free plan, you can make 5 simultaneous WebSocket connections. On the Developer plan, 150 connections are possible. On Business, you can make 250 connections, and on Professional, up to 1,000 WebSocket connections.
Why is my client not receiving some WebSocket updates?
The client needs to keep up with the rate of incoming messages from the WebSocket server.Common causes of your client missing WebSocket updates include: insufficient network bandwidth, too slow client-side processing (e.g. a too slow programming language), or processing logic that blocks the main thread.
Can I subscribe to multiple accounts using the same WebSocket connection?
Yes, you can create multiple subscriptions to `accountSubscribe` using the same WebSocket connection.
How do I subscribe to full transactions using WebSockets?
**For Enhanced WebSockets** , set `transactionDetails: "full"` in your subscription options:

```
const subscriptionRequest = {
  jsonrpc: "2.0",
  id: 1,
  method: "transactionSubscribe",
  params: [

      accountInclude: ["YOUR_ACCOUNT_ADDRESS"],
      failed: false,
      vote: false


      commitment: "confirmed",
      encoding: "jsonParsed",
      transactionDetails: "full",  // Full transaction details
      maxSupportedTransactionVersion: 0




```

**For Standard WebSockets** , use `logsSubscribe` or `signatureSubscribe` methods depending on your monitoring needs. See our [WebSocket guide](https://www.helius.dev/docs/rpc/websocket) for detailed examples of each subscription type.
## Need More Help?
## [Contact Support Get help from our team through Discord, chat, or email support. ](https://www.helius.dev/docs/support/contact-support)
## [Status Page Check real-time service availability and performance information. ](https://www.helius.dev/docs/support/status-page)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/faqs/error-codes)[ LaserStream FAQsGet answers to the most common questions about LaserStream including purchasing, usage, troubleshooting, and subscription management Next ](https://www.helius.dev/docs/faqs/laserstream)
On this page
  * [Billing and Rate Limits](https://www.helius.dev/docs/faqs/websockets#billing-and-rate-limits)
  * [Disconnects and Retries](https://www.helius.dev/docs/faqs/websockets#disconnects-and-retries)


Assistant
Responses are generated using AI and may contain mistakes.
