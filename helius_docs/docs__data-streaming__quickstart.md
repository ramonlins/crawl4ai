# Source: https://www.helius.dev/docs/data-streaming/quickstart

## Quick Setup
Get streaming Solana data in minutes with working code examples. Choose your approach based on your needs:  
| Method  | Best For  | Plan Required  | Latency  |  
| --- | --- | --- | --- |  
| **LaserStream gRPC**  | Mission-critical, backend services  | Developer+ (Devnet), Business+ (Mainnet)  | **Fastest**  |  
| **Enhanced WSS**  | Advanced filtering, high-performance apps  | Developer, Business, Professional  | **Fast**  |  
| **Standard WSS**  | Most applications, existing Solana code  | Free+  | **Good**  |  
| **Webhooks**  | Server notifications, event-driven apps  | Free+  | **Variable**  |  
Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
## Option 1: Standard WebSockets
Perfect for most use cases and compatible with existing Solana WebSocket code.

```
const WebSocket = require('ws');

const ws = new WebSocket('wss://mainnet.helius-rpc.com?api-key=YOUR_API_KEY');

ws.on('open', () => {
  console.log('Connected to Helius');

  // Subscribe to account changes
  ws.send(JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "accountSubscribe",
    params: [
      "9PejEmViKHgUkVFWN57cNEZnFS4Qo6SzsLj5UPAXfDTF", // Replace with your account
encoding: "jsonParsed", commitment: "confirmed" }

  }));
});

ws.on('message', (data) => {
  const message = JSON.parse(data);
  if (message.method === 'accountNotification') {
    console.log('Account updated:', message.params.result.value);

});

```

**Replace`YOUR_API_KEY`** with your key from [dashboard.helius.dev](https://dashboard.helius.dev)
## [Standard WebSockets Guide Complete reference with all subscription methods and examples ](https://www.helius.dev/docs/rpc/websocket)
## Option 2: Enhanced WebSockets
For applications needing advanced filtering and faster performance.

```
const WebSocket = require('ws');

const ws = new WebSocket('wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY');

ws.on('open', () => {
  console.log('Enhanced WebSocket connected');

  // Subscribe to transactions involving specific accounts
  ws.send(JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "transactionSubscribe",
    params: [

        accountInclude: ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"],
        vote: false,
        failed: false


        commitment: "confirmed",
        encoding: "jsonParsed",
        transactionDetails: "full"


  }));

  // Keep connection alive
  setInterval(() => ws.ping(), 30000);
});

ws.on('message', (data) => {
  const message = JSON.parse(data);
  console.log('Transaction:', message);
});

```

## [Enhanced WebSockets Guide Learn advanced filtering and subscription options ](https://www.helius.dev/docs/enhanced-websockets)
## Option 3: LaserStream gRPC
Most reliable option with [24-hour historical replay](https://www.helius.dev/docs/laserstream/historical-replay) and multi-node failover.

```
npm install helius-laserstream

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream';

async function main() {
  const subscriptionRequest: SubscribeRequest = {
    transactions: {
      client: {
        accountInclude: ['TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'],
        accountExclude: [],
        accountRequired: [],
        vote: false,
        failed: false


    commitment: CommitmentLevel.CONFIRMED,
    accounts: {},
    slots: {},
    transactionsStatus: {},
    blocks: {},
    blocksMeta: {},
    entry: {},
    accountsDataSlice: [],


  const config: LaserstreamConfig = {
    apiKey: 'YOUR_API_KEY',
    endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com',


  await subscribe(config, subscriptionRequest, async (data) => {
    console.log(data);
  }, async (error) => {
    console.error(error);
  });


main().catch(console.error);

```

## [LaserStream Guide Complete LaserStream documentation with historical replay ](https://www.helius.dev/docs/laserstream)
## [LaserStream Trial Apply for a 2-day LaserStream trial before upgrading your plan ](https://www.helius.dev/laserstream-contact)
## Option 4: Webhooks
For server-side applications that need event notifications.

```
# Create a webhook
curl -X POST "https://api-mainnet.helius-rpc.com/v0/webhooks" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookURL": "https://your-server.com/webhook",
    "transactionTypes": ["Any"],
    "accountAddresses": ["YOUR_ACCOUNT_ADDRESS"],
    "webhookType": "enhanced"


```


```
// Handle webhook events (Express.js example)
app.post('/webhook', (req, res) => {
  req.body.forEach(event => {
    console.log('Blockchain event:', event);
  });
  res.status(200).send('OK');
});

```

## [Webhooks Guide Complete webhook setup and event handling ](https://www.helius.dev/docs/webhooks)
## Common Use Cases
**Monitor Token Transfers**

```
// Subscribe to Token Program activity
method: "programSubscribe",
params: ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", {...}]

```

**Track NFT Sales**

```
// Subscribe to Magic Eden program
method: "programSubscribe", 
params: ["M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K", {...}]

```

**Watch Wallet Activity**

```
// Monitor specific wallet
method: "accountSubscribe",
params: ["WALLET_ADDRESS", {...}]

```

## Next Steps
## [Streaming Overview Learn about all streaming options and when to use each ](https://www.helius.dev/docs/data-streaming)
## [API Reference Complete method documentation and parameters ](https://www.helius.dev/docs/api-reference)
**Need help?** Join our [Discord](https://discord.com/invite/6GXdee3gBj) or check [support docs](https://www.helius.dev/docs/support).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/data-streaming)[ OverviewSpecialized feed of raw Solana shreds delivered via UDP — the earliest possible on-chain signal optimized for traders and low-latency use cases. Next ](https://www.helius.dev/docs/shred-delivery)
On this page
  * [Option 1: Standard WebSockets](https://www.helius.dev/docs/data-streaming/quickstart#option-1-standard-websockets)
  * [Option 2: Enhanced WebSockets](https://www.helius.dev/docs/data-streaming/quickstart#option-2-enhanced-websockets)
  * [Option 3: LaserStream gRPC](https://www.helius.dev/docs/data-streaming/quickstart#option-3-laserstream-grpc)


Assistant
Responses are generated using AI and may contain mistakes.
