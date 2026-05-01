# Source: https://www.helius.dev/docs/enhanced-websockets/stream-pump-amm-data

[Skip to main content](https://www.helius.dev/docs/enhanced-websockets/stream-pump-amm-data#content-area)
New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
Search...
Ctrl K


##### Get Started


##### Solana RPC Nodes
  * Gatekeeper (Beta)
  * RPC Method Guides


##### Data Streaming & Event Listening
  * Shred Delivery
  * LaserStream
  * Yellowstone gRPC
  * Enhanced Websockets
  * Standard Websockets
  * Webhooks


##### How to Send Transactions
  * Helius Sender (For Traders)
  * Priority Fee API


##### Getting Data
  * [getTransactionsForAddress 🔥](https://www.helius.dev/docs/rpc/gettransactionsforaddress)
  * Digital Asset Standard (DAS)
  * Indexing & Historical Data
  * Enhanced Transactions API
  * Wallet API (Beta)


##### Dedicated Nodes


##### Compression
  * [What is ZK Compression on Solana?](https://www.helius.dev/docs/zk-compression/introduction)
  * Helius AirShip


##### Staking
  * [Programmatic Solana Staking with Helius SDK](https://www.helius.dev/docs/staking/how-to-stake-with-helius-programmatically)


##### Billing


##### Using Orb


##### Resources


  * English


New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
English
Search...
Ctrl KAsk AI
Search...
Navigation
Enhanced Websockets
How to Stream Pump AMM Data
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Enhanced WebSockets provide fast JSON streams with decoded accounts and transactions. No custom network stack is required. Enhanced WebSockets are available on Developer plans and higher.
##  How it Works
  * Connect to the [Enhanced WebSocket endpoint](https://www.helius.dev/docs/api-reference/endpoints)
  * Subscribe to [Pump AMM program](https://orbmarkets.io/address/pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA/history) and listen for transactions
  * The code example retries five times with an exponential back‑off


##  Requirements
  * **Node.js ≥ 18** (tested with v20)
  * **TypeScript ≥ 5** if you plan to run the `.ts` samples with `ts‑node`
  * A **Helius Business Plan or higher**
  * An **environment variable** named `HELIUS_API_KEY` that stores your API key


Install dependencies globally: `npm i -g typescript ts‑node`
##  Implementation
Install Dependencies

```
npm install ws

```

Create the WebSocket Client
Create a file named `enhanced-ws-pump.ts` with the following code:

```
// enhanced-ws-pump.ts
import WebSocket from 'ws';

// Configuration for reconnection
const MAX_RETRIES = 5;
const INITIAL_RETRY_DELAY = 1000; // 1 second
let retryCount = 0;
let retryDelay = INITIAL_RETRY_DELAY;

// Function to create a new WebSocket connection
function createWebSocket() {
  return new WebSocket(`wss://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`);


// Function to send a request to the WebSocket server
function sendRequest(ws: WebSocket) {
  const request = {
    jsonrpc: "2.0",
    id: 420,
    method: "transactionSubscribe",
    params: [

        accountInclude: ["pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"]


        commitment: "processed",
        encoding: "jsonParsed",
        transactionDetails: "full",
        maxSupportedTransactionVersion: 0



  ws.send(JSON.stringify(request));


// Function to send a ping to the WebSocket server
function startPing(ws: WebSocket) {
  return setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.ping();
      console.log('Ping sent');

  }, 30000); // Ping every 30 seconds


// Function to handle reconnection
function reconnect() {
  if (retryCount >= MAX_RETRIES) {
    console.error('Maximum retry attempts reached.');
    return;


  console.log(`Attempting to reconnect in ${retryDelay/1000} seconds... (Attempt ${retryCount + 1}/${MAX_RETRIES})`);

  setTimeout(() => {
    retryCount++;
    retryDelay *= 2; // Exponential backoff
    initializeWebSocket();
  }, retryDelay);


// Function to initialize WebSocket with all event handlers
function initializeWebSocket() {
  const ws = createWebSocket();
  let pingInterval: NodeJS.Timeout;

  ws.on('open', function open() {
    console.log('WebSocket is open');
    retryCount = 0; // Reset retry count on successful connection
    retryDelay = INITIAL_RETRY_DELAY; // Reset retry delay
    sendRequest(ws);
    pingInterval = startPing(ws);
  });

  ws.on('message', function incoming(data: WebSocket.Data) {
    const messageStr = data.toString('utf8');
    try {
      const messageObj = JSON.parse(messageStr);

      // Check if it's a subscription confirmation
      if (messageObj.result !== undefined) {
        console.log('Subscription confirmed:', messageObj);
        return;


      // Check if it's transaction data
      if (messageObj.params messageObj.params.result) {
        const transaction = messageObj.params.result;
        console.log('Received transaction:', JSON.stringify(transaction, null, 2));

catch (e) {
      console.error('Failed to parse JSON:', e);

  });

  ws.on('error', function error(err: Error) {
    console.error('WebSocket error:', err);
  });

  ws.on('close', function close() {
    console.log('WebSocket is closed');
    if (pingInterval) {
      clearInterval(pingInterval);

    reconnect();
  });


// Start the WebSocket connection
initializeWebSocket();

// Handle program termination
process.on('SIGINT', () => {
  console.log('Shutting down...');
  process.exit(0);
});

```

Set Environment Variables
Add your Helius API key as an environment variable:

```
export HELIUS_API_KEY=your-helius-api-key

```

Replace `your-helius-api-key` with your actual Helius API key from the dashboard.If you don’t have an API key, [sign up](https://dashboard.helius.dev/signup) for an account, or have your agent create one programmatically with the [Helius CLI](https://www.helius.dev/docs/agents/cli).
Run the Application
Execute the script to start streaming Pump AMM data:

```
npx ts-node enhanced-ws-pump.ts

```

You will see parsed Pump AMM transactions in your terminal. The client retries automatically when the socket closes.
##  Key benefits
  * **Browser-compatible** - WSS works in both Node.js and browser environments
  * **Rich data** - fully parsed transaction objects with decoded instructions and accounts
  * **Simple implementation** - No special libraries required (just a standard WSS client)
  * **Auto-reconnect** - Built-in retry logic ensures a stable connection


##  Common issues and solutions
401 Unauthorized
Verify your HELIUS_API_KEY is correct.
No logs received
Ensure the [Pump AMM program address](https://orbmarkets.io/address/pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA/history) is correct and there is activity.
Connection dropping
Implement more robust reconnection logic or check network stability.
##  Next steps
Create a UI Dashboard
Build a web interface to visualize incoming Pump AMM transactions in real-time using React or Vue.js.
Implement Database Storage
Store transaction data in a database like MongoDB or PostgreSQL for historical analysis:

```
import { MongoClient } from 'mongodb';

// Setup MongoDB connection
async function setupDatabase() {
  const client = new MongoClient('mongodb://localhost:27017');
  await client.connect();
  return client.db('pump-amm').collection('transactions');


// Then in your message handler:
ws.on('message', async function incoming(data: WebSocket.Data) {
  const messageStr = data.toString('utf8');
  try {
    const messageObj = JSON.parse(messageStr);

    if (messageObj.params messageObj.params.result) {
      const transaction = messageObj.params.result;

      // Store in database
      const collection = await setupDatabase();
      await collection.insertOne({
        timestamp: new Date(),
        transaction: transaction
      });

      console.log('Transaction stored in database');

catch (e) {
    console.error('Failed to process message:', e);

});

```

Set Up Alerting System
Configure alerts for high-value transactions or specific patterns using a service like Discord webhooks:

```
import axios from 'axios';

// Send alert to Discord webhook
async function sendAlert(message: string) {
  await axios.post('YOUR_DISCORD_WEBHOOK_URL', {
    content: message
  });


// Then in your message handler:
if (messageObj.params messageObj.params.result) {
  const transaction = messageObj.params.result;

  // Example: Check for transactions above a certain value
  const isHighValue = checkIfHighValueTransaction(transaction);

  if (isHighValue) {
    sendAlert(`High-value transaction detected: ${transaction.signature}`);



```

Implement Heartbeat Monitoring
Add a more robust heartbeat system to ensure continuous connectivity:

```
// Enhanced heartbeat system
function setupHeartbeat(ws: WebSocket) {
  let lastPongTime = Date.now();

  // Send ping regularly
  const pingInterval = setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.ping();

  }, 30000);

  // Track pong responses
  ws.on('pong', () => {
    lastPongTime = Date.now();
  });

  // Check connection health
  const healthCheck = setInterval(() => {
    const now = Date.now();
    if (now - lastPongTime 90000) {  // No pong for 90 seconds
      console.warn('Connection seems unresponsive, reconnecting...');
      ws.terminate();
      clearInterval(pingInterval);
      clearInterval(healthCheck);

  }, 30000);

  return { pingInterval, healthCheck };


```

Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-websockets/account-subscribe)[ OverviewStream real-time Solana blockchain data with WebSockets, now powered by LaserStream for up to 200 ms faster responses vs. standard Agave RPC-based WebSockets. Next ](https://www.helius.dev/docs/rpc/websocket)
Ctrl+I
On this page
  * [Common issues and solutions](https://www.helius.dev/docs/enhanced-websockets/stream-pump-amm-data#common-issues-and-solutions)


Assistant
Responses are generated using AI and may contain mistakes.
