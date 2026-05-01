# Source: https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data

## Using Standard WebSockets
Standard Solana WebSockets provide a simple integration and are available on all Helius plans, making it a convenient choice for developers. Standard WSS also uses Solana PubSub `logsSubscribe`, so you receive log messages only.
Standard WebSockets are now powered by LaserStream, and provide up to 200 ms faster responses compared to traditional RPC-based WebSockets.
### How it works
Connect to the [Standard WebSocket endpoint](https://www.helius.dev/docs/api-reference/endpoints), subscribe to logs mentioning the [Pump AMM program](https://orbmarkets.io/address/pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA/history), and process the incoming log data. The example below includes automatic reconnection logic with exponential backoffs.
## Requirements
  * **Node.js ≥ 18** (tested with v20)
  * **TypeScript ≥ 5** if you plan to run the `.ts` samples with `ts‑node`
  * Any **Helius plan** – works with all plan tiers
  * An **environment variable** named `HELIUS_API_KEY` that stores your API key


Install dependencies globally: `npm i -g typescript ts‑node`
## Implementation
Install Dependencies

```
npm install ws

```

Create the WebSocket Client
Create a file named `standard-ws-pump.ts` with the following code:

```
// standard-ws-pump.ts
import WebSocket from 'ws';

// Configuration
const MAX_RETRIES = 5;
const INITIAL_RETRY_DELAY = 1000; // 1 second
let retryCount = 0;
let retryTimeout: NodeJS.Timeout | null = null;
let subscriptionId: number | null = null;

// Create a WebSocket connection
let ws: WebSocket;

function connect() {
  ws = new WebSocket(`wss://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`);

  // Function to send a request to the WebSocket server
  function sendRequest(ws: WebSocket): void {
    const request = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "logsSubscribe",
      "params": [

          "mentions": ["pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"]



    console.log('Sending subscription request:', JSON.stringify(request, null, 2));
    ws.send(JSON.stringify(request));


  // Function to send a ping to the WebSocket server
  function startPing(ws: WebSocket): void {
    setInterval(() => {
      if (ws.readyState === WebSocket.OPEN) {
.ping();
        console.log('Ping sent');

    }, 30000); // Ping every 30 seconds


  // Define WebSocket event handlers
  ws.on('open', function open() {
    console.log('WebSocket is open');
    retryCount = 0; // Reset retry count on successful connection
    sendRequest(ws); // Send a request once the WebSocket is open
    startPing(ws); // Start sending pings
  });

  ws.on('message', function incoming(data: WebSocket.Data) {
    const messageStr = data.toString('utf8');
    try {
      const messageObj = JSON.parse(messageStr);

      // Handle subscription confirmation
      if (messageObj.result typeof messageObj.result === 'number') {
        subscriptionId = messageObj.result;
        console.log('Successfully subscribed with ID:', subscriptionId);
        return;


      // Handle actual log data
      if (messageObj.params messageObj.params.result) {
        const logData = messageObj.params.result;
        console.log('Received log data:', JSON.stringify(logData, null, 2));

        // Extract the transaction signature if available
 (logData.signature) {
          console.log('Transaction signature:', logData.signature);
          // You can call getTransaction with this signature to get the full transaction details

else {
        console.log('Received message:', JSON.stringify(messageObj, null, 2));

catch (e) {
      console.error('Failed to parse JSON:', e);

  });

  ws.on('error', function error(err: Error) {
    console.error('WebSocket error:', err);
  });

  ws.on('close', function close() {
    console.log('WebSocket is closed');
    if (subscriptionId) {
      console.log('Last subscription ID was:', subscriptionId);

    reconnect();
  });


function reconnect() {
  if (retryCount >= MAX_RETRIES) {
    console.error('Max retry attempts reached. Please check your connection and try again.');
    return;


  const delay = INITIAL_RETRY_DELAY * Math.pow(2, retryCount);
  console.log(`Attempting to reconnect in ${delay/1000} seconds... (Attempt ${retryCount + 1}/${MAX_RETRIES})`);

  retryTimeout = setTimeout(() => {
    retryCount++;
    connect();
  }, delay);


// Start the initial connection
connect();

// Cleanup function
process.on('SIGINT', () => {
  if (retryTimeout) {
    clearTimeout(retryTimeout);

  if (ws) {
    ws.close();

  process.exit();
});

```

Set Environment Variables
Add your Helius API key as an environment variable:

```
export HELIUS_API_KEY=your-helius-api-key

```

Replace `your-helius-api-key` with your actual Helius API key from the dashboard.If you don’t have an API key, [sign up](https://dashboard.helius.dev/signup) or have your agent create one programmatically with [the Helius CLI](https://www.helius.dev/docs/api-reference/helius-cli).
Run the Application
Execute the script to start streaming Pump AMM data:

```
npx ts-node standard-ws-pump.ts

```

You will receive log messages that mention the Pump AMM program. To fetch the full transaction, call [`getTransaction`](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction) with the signature from the log entry.
## Key benefits
  * **Universal access** - Available on all Helius plans, including free tier
  * **Lightweight** - Minimal data transfer since only logs are streamed, not full transactions
  * **Easy to implement** - Uses standard Solana RPC WebSocket protocol
  * **Low barrier to entry** - Perfect for prototyping and initial monitoring


## Getting full transaction details
Since the Standard WebSocket only provides log messages, you’ll need an additional step to get complete transaction data:

```
// Example of how to fetch a full transaction from a log entry
async function fetchFullTransaction(signature: string) {
  const response = await fetch(`https://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-id',
      method: 'getTransaction',
      params: [
        signature,

          encoding: 'jsonParsed',
          maxSupportedTransactionVersion: 0



  });

  const data = await response.json();
  return data.result;


```

## Common issues and solutions
401 Unauthorized
Verify your HELIUS_API_KEY is correct.
No logs received
Ensure the Pump AMM program address is correct and there is activity on the program.
Connection dropping
Implement more robust reconnection logic or check network stability.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/websocket/quickstart)[ OverviewMonitor Solana blockchain events with real-time webhooks. Get instant notifications for NFT sales, token transfers, and transactions sent to your endpoints. Next ](https://www.helius.dev/docs/webhooks)
On this page
  * [Using Standard WebSockets](https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data#using-standard-websockets)
  * [Getting full transaction details](https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data#getting-full-transaction-details)
  * [Common issues and solutions](https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data#common-issues-and-solutions)


Assistant
Responses are generated using AI and may contain mistakes.
