# Source: https://www.helius.dev/docs/rpc/websocket/quickstart

## Quick Start Guide
Get Your API Key
Obtain your Helius API key from the [dashboard](https://dashboard.helius.dev). You’ll need this for authentication. Agents can get a key using [the Helius CLI](https://www.helius.dev/docs/api-reference/helius-cli).
Choose Your Network
Select the appropriate [endpoint](https://www.helius.dev/docs/api-reference/endpoints):
  * **Mainnet** : `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet (Gatekeeper Beta)** : `wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet** : `wss://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`


Create Your First Connection

```
const ws = new WebSocket('wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY');

ws.onopen = () => {
  console.log('Connected to Solana!');


ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);


```

Subscribe to Updates

```
// Subscribe to account changes
const subscribeMessage = {
  "jsonrpc": "2.0",
  "id": 1,
  "method": "accountSubscribe",
  "params": [
    "ACCOUNT_ADDRESS_HERE",
"commitment": "confirmed" }



ws.send(JSON.stringify(subscribeMessage));

```

## Subscription Methods
### Account Monitoring
Monitor specific accounts for balance changes, data updates, or ownership transfers.
Basic Account Subscription
Token Account Monitoring

```
const ws = new WebSocket('wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY');

const subscribeToAccount = (accountAddress) => {
  const request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "accountSubscribe",
    "params": [
      accountAddress,

        "encoding": "jsonParsed",
        "commitment": "confirmed"




  ws.send(JSON.stringify(request));


ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  if (data.method === "accountNotification") {
    console.log("Account updated:", data.params.result.value);

    // Handle the account change
    const accountInfo = data.params.result.value;
    console.log(`New balance: ${accountInfo.lamports} lamports`);



// Subscribe to a wallet address
subscribeToAccount("9PejEmViKHgUkVFWN57cNEZnFS4Qo6SzsLj5UPAXfDTF");

```

### Program Activity Monitoring
Watch all accounts owned by a program - perfect for monitoring DEX trades, NFT transfers, or DeFi activity.
DEX Trade Monitoring
NFT Marketplace Monitoring

```
// Monitor Raydium AMM for all trade activity
const RAYDIUM_AMM_PROGRAM = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8";

const subscribeToProgram = (programId) => {
  const request = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "programSubscribe",
    "params": [
      programId,

        "encoding": "jsonParsed",
        "commitment": "confirmed",
        "filters": [

            "dataSize": 752 // Raydium pool account size






  ws.send(JSON.stringify(request));


ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  if (data.method === "programNotification") {
    console.log("Raydium pool updated:", data.params.result.value.pubkey);
    // Process the pool data change
    const accountData = data.params.result.value.account;
    // Parse and handle the pool state change



subscribeToProgram(RAYDIUM_AMM_PROGRAM);

```

### Transaction Monitoring
Track specific transactions or monitor transactions that mention certain accounts.
Transaction Status Tracking
Log-Based Monitoring

```
// Monitor a specific transaction signature
const trackTransaction = (signature) => {
  const request = {
    "jsonrpc": "2.0",
    "id": 5,
    "method": "signatureSubscribe",
    "params": [
      signature,

        "commitment": "confirmed"




  ws.send(JSON.stringify(request));


ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  if (data.method === "signatureNotification") {
    const result = data.params.result;

    if (result.value.err) {
      console.log("Transaction failed:", result.value.err);
else {
      console.log("Transaction confirmed successfully!");


    // Subscription automatically ends after notification



// Track a payment or swap transaction
trackTransaction("YOUR_TRANSACTION_SIGNATURE_HERE");

```

## Production-Ready Implementation
Here’s a robust WebSocket implementation with reconnection logic, error handling, and proper state management:

```
class WebSocketManager {
  constructor(endpoint) {
    this.endpoint = endpoint;
    this.ws = null;
    this.subscriptions = new Map();
    this.isConnected = false;


  async connect() {
    this.ws = new WebSocket(this.endpoint);

    this.ws.onopen = () => {
      console.log('Connected');
      this.isConnected = true;
      this.resubscribeAll();


    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      // Handle subscription confirmations
      if (data.result typeof data.result === 'number') {
        const sub = Array.from(this.subscriptions.values())
find(s => s.requestId === data.id);
 (sub) sub.subscriptionId = data.result;
        return;


      // Handle notifications
      if (data.method?.endsWith('Notification')) {
        const sub = Array.from(this.subscriptions.values())
find(s => s.subscriptionId === data.params.subscription);
 (sub?.callback) sub.callback(data.params.result);



    this.ws.onclose = () => {
      console.log('Disconnected');
      this.isConnected = false;
      // Implement reconnection logic here



  subscribe(method, params, callback) {
    const requestId = Date.now();
    const subscription = { requestId, method, params, callback, subscriptionId: null };
    this.subscriptions.set(requestId, subscription);

    if (this.isConnected) {
      this.ws.send(JSON.stringify({
        jsonrpc: '2.0',
        id: requestId,
        method,
        params
      }));


    return requestId;


  resubscribeAll() {
    for (const [id, sub] of this.subscriptions) {
      sub.subscriptionId = null;
      this.ws.send(JSON.stringify({
        jsonrpc: '2.0',

        method: sub.method,
        params: sub.params
      }));




// Usage
const wsManager = new WebSocketManager('wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY');
await wsManager.connect();

// Subscribe to account changes
wsManager.subscribe(
  'accountSubscribe',
  ['account-address-here', { commitment: 'confirmed' }],
  (data) => console.log('Account updated:', data)


```

## Explore More WebSocket Methods
The examples above cover the most commonly used subscription types, but Solana’s WebSocket API offers many more methods for specialized monitoring needs.
## [Complete WebSocket API Reference **Discover 18+ WebSocket methods** with detailed documentation, parameters, and response formats. ](https://www.helius.dev/docs/api-reference/rpc/websocket-methods)
## Real-World Use Cases
### DeFi Trading Dashboard

```
class LiquidityPoolMonitor {
  constructor(wsManager) {
    this.wsManager = wsManager;
    this.pools = new Map();


  monitorPool(poolAddress, tokenAMint, tokenBMint) {
    // Monitor the pool account itself
    const poolSubscription = this.wsManager.subscribe(
      'accountSubscribe',
poolAddress, { encoding: 'base64', commitment: 'confirmed' }],
data) => this.handlePoolUpdate(poolAddress, data)


    // Monitor token reserves
    const tokenASubscription = this.wsManager.subscribe(
      'accountSubscribe', 
tokenAMint, { encoding: 'jsonParsed', commitment: 'confirmed' }],
data) => this.handleReserveUpdate(poolAddress, 'tokenA', data)


    const tokenBSubscription = this.wsManager.subscribe(
      'accountSubscribe',
tokenBMint, { encoding: 'jsonParsed', commitment: 'confirmed' }],
data) => this.handleReserveUpdate(poolAddress, 'tokenB', data)


    this.pools.set(poolAddress, {
      poolSubscription,
      tokenASubscription, 
      tokenBSubscription,
      lastUpdate: Date.now()
    });


  handlePoolUpdate(poolAddress, data) {
    // Decode pool state and calculate price
    const poolState = this.decodePoolState(data.value.data);

    console.log(`Pool ${poolAddress} updated:`);
    console.log(`- Price: ${poolState.price}`);
    console.log(`- Liquidity: ${poolState.liquidity}`);
    console.log(`- Volume 24h: ${poolState.volume24h}`);

    // Emit price update event
    this.emitPriceUpdate(poolAddress, poolState);


  handleReserveUpdate(poolAddress, tokenType, data) {
    const tokenAmount = data.value.data.parsed.info.tokenAmount;
    console.log(`${tokenType} reserve updated: ${tokenAmount.uiAmount}`);

    // Update internal state and recalculate price
    this.updatePoolPrice(poolAddress, tokenType, tokenAmount);


  decodePoolState(data) {
    // Implement pool state decoding based on DEX
    // This is pseudo-code - actual implementation depends on the DEX
    return {
      price: 0,
      liquidity: 0,
      volume24h: 0



  emitPriceUpdate(poolAddress, poolState) {
    // Emit custom events for price updates
    window.dispatchEvent(new CustomEvent('poolPriceUpdate', {
      detail: { poolAddress, ...poolState }
    }));



// Usage
const poolMonitor = new LiquidityPoolMonitor(wsManager);
poolMonitor.monitorPool(
  'POOL_ADDRESS',
  'TOKEN_A_MINT', 
  'TOKEN_B_MINT'


```

### Portfolio Tracker

```
class PortfolioTracker {
  constructor(wsManager) {
    this.wsManager = wsManager;
    this.watchedAddresses = new Set();
    this.balances = new Map();


  addWallet(walletAddress) {
    if (this.watchedAddresses.has(walletAddress)) return;

    this.watchedAddresses.add(walletAddress);

    // Monitor SOL balance
    const solSubscription = this.wsManager.subscribe(
      'accountSubscribe',
walletAddress, { encoding: 'jsonParsed', commitment: 'confirmed' }],
data) => this.handleSolBalanceUpdate(walletAddress, data)


    // Monitor all token accounts owned by this wallet
    const tokenSubscription = this.wsManager.subscribe(
      'programSubscribe',

        'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA',

          encoding: 'jsonParsed',
          commitment: 'confirmed',
          filters: [
memcmp: { offset: 32, bytes: walletAddress } }



data) => this.handleTokenBalanceUpdate(walletAddress, data)


    console.log(`Now tracking portfolio for ${walletAddress}`);


  handleSolBalanceUpdate(walletAddress, data) {
    const lamports = data.value.lamports;
    const solBalance = lamports / 1e9;

    this.balances.set(`${walletAddress}:SOL`, solBalance);

    console.log(`${walletAddress} SOL balance: ${solBalance}`);
    this.emitBalanceUpdate(walletAddress, 'SOL', solBalance);


  handleTokenBalanceUpdate(walletAddress, data) {
    const tokenData = data.value.account.data.parsed.info;
    const tokenMint = tokenData.mint;
    const balance = parseFloat(tokenData.tokenAmount.uiAmount);

    this.balances.set(`${walletAddress}:${tokenMint}`, balance);

    console.log(`${walletAddress} token ${tokenMint} balance: ${balance}`);
    this.emitBalanceUpdate(walletAddress, tokenMint, balance);


  emitBalanceUpdate(walletAddress, asset, balance) {
    window.dispatchEvent(new CustomEvent('balanceUpdate', {
      detail: { walletAddress, asset, balance, timestamp: Date.now() }
    }));


  getPortfolioValue(walletAddress) {
    // Calculate total portfolio value in USD
    // This would integrate with price feeds
    let totalValue = 0;

    for (const [key, balance] of this.balances) {
      if (key.startsWith(walletAddress)) {
        const asset = key.split(':')[1];
        const price = this.getAssetPrice(asset); // Implement price lookup
        totalValue += balance * price;



    return totalValue;



```

### NFT Marketplace Integration

```
class NFTActivityMonitor {
  constructor(wsManager) {
    this.wsManager = wsManager;
    this.watchedCollections = new Map();


  monitorCollection(collectionAddress, options = {}) {
    const { includeListings = true, includeSales = true, includeCancellations = true } = options;

    // Monitor the collection's update authority or creator address
    const collectionSubscription = this.wsManager.subscribe(
      'logsSubscribe',

mentions: [collectionAddress] },
commitment: 'confirmed' }

data) => this.handleCollectionActivity(collectionAddress, data)


    this.watchedCollections.set(collectionAddress, {
      subscription: collectionSubscription,
      options,
      stats: {
        listings: 0,
        sales: 0,
        volume: 0

    });

    console.log(`Monitoring NFT collection: ${collectionAddress}`);


  handleCollectionActivity(collectionAddress, data) {
    const logs = data.value.logs;
    const signature = data.value.signature;

    // Parse marketplace-specific logs
    const activity = this.parseMarketplaceActivity(logs);

    if (activity) {
      console.log(`NFT Activity in ${collectionAddress}:`);
      console.log(`- Type: ${activity.type}`);
      console.log(`- Price: ${activity.price} SOL`);
      console.log(`- Signature: ${signature}`);

      // Update collection stats
      this.updateCollectionStats(collectionAddress, activity);

      // Emit activity event
      this.emitNFTActivity(collectionAddress, activity, signature);



  parseMarketplaceActivity(logs) {
    // Parse Magic Eden, OpenSea, or other marketplace logs
    for (const log of logs) {
      // Magic Eden listing
      if (log.includes('Instruction: List')) {
        const price = this.extractPriceFromLog(log);
        return { type: 'listing', price };


      // Magic Eden sale
      if (log.includes('Instruction: ExecuteSale')) {
        const price = this.extractPriceFromLog(log);
        return { type: 'sale', price };


      // Listing cancellation
      if (log.includes('Instruction: CancelBuy') || log.includes('Instruction: CancelSell')) {
        return { type: 'cancellation', price: 0 };



    return null;


  extractPriceFromLog(log) {
    // Extract price from marketplace logs - implementation depends on marketplace
    // This is pseudo-code
    const priceMatch = log.match(/price:\s*(\d+)/);
    return priceMatch ? parseInt(priceMatch[1]) / 1e9 : 0;


  updateCollectionStats(collectionAddress, activity) {
    const collection = this.watchedCollections.get(collectionAddress);
    if (!collection) return;

    switch (activity.type) {
      case 'listing':
        collection.stats.listings++;
        break;
      case 'sale':
        collection.stats.sales++;
        collection.stats.volume += activity.price;
        break;



  emitNFTActivity(collectionAddress, activity, signature) {
    window.dispatchEvent(new CustomEvent('nftActivity', {
      detail: {
        collection: collectionAddress,
        activity,
        signature,
        timestamp: Date.now()

    }));



```

### React Integration Example

```
import React, { useEffect, useState } from 'react';

function WebSocketComponent() {
  const [accountData, setAccountData] = useState(null);
  const [wsManager, setWsManager] = useState(null);

  useEffect(() => {
    // Initialize WebSocket
    const manager = new WebSocketManager('wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY');

    manager.connect().then(() => {
      // Subscribe to account changes
      manager.subscribe(
        'accountSubscribe',
'account-address-here', { commitment: 'confirmed' }],
data) => setAccountData(data)

    });

    setWsManager(manager);

    // Cleanup on unmount
    return () => {
      if (manager) manager.disconnect();

  }, []);

  return (
div
h3Account Monitor</h3
accountData ? (
div
pBalance: {accountData.value.lamports} lamports</p
pOwner: {accountData.value.owner}</p
div

pWaiting for account updates...</p

    </div



```

## Performance Optimization
  * Connection Management
  * Memory Management



```
// Use connection pooling for multiple subscriptions
class WebSocketPool {
  constructor(endpoint, maxConnections = 3) {
    this.endpoint = endpoint;
    this.connections = [];
    this.maxConnections = maxConnections;
    this.currentConnectionIndex = 0;


  async getConnection() {
    if (this.connections.length this.maxConnections) {
      const wsManager = new SolanaWebSocketManager(this.endpoint);
      await wsManager.connect();
      this.connections.push(wsManager);
      return wsManager;


    // Round-robin selection
    const connection = this.connections[this.currentConnectionIndex];
    this.currentConnectionIndex = (this.currentConnectionIndex + 1) % this.connections.length;
    return connection;



```


```
// Implement subscription cleanup and memory management
class ManagedWebSocket extends SolanaWebSocketManager {
  constructor(endpoint, options = {}) {
    super(endpoint, options);
    this.maxSubscriptions = options.maxSubscriptions || 100;
    this.subscriptionHistory = [];


  subscribe(method, params, callback) {
    // Check subscription limit
    if (this.subscriptions.size >= this.maxSubscriptions) {
      this.cleanupOldSubscriptions();


    const requestId = super.subscribe(method, params, callback);

    // Track subscription for cleanup
    this.subscriptionHistory.push({
      requestId,
      timestamp: Date.now(),
      method
    });

    return requestId;


  cleanupOldSubscriptions() {
    // Remove oldest 10% of subscriptions
    const toRemove = Math.floor(this.subscriptions.size * 0.1);
    const sortedHistory = this.subscriptionHistory
sort((a, b) => a.timestamp - b.timestamp);

    for (let i = 0; i toRemove i sortedHistory.length; i++) {
      const sub = sortedHistory[i];
      this.unsubscribe(sub.requestId);

      // Remove from history
      this.subscriptionHistory = this.subscriptionHistory
filter(s => s.requestId !== sub.requestId);




```

## Error Handling and Debugging
Robust error handling is crucial for production WebSocket applications. Implement these patterns to handle network issues, rate limits, and API errors gracefully.

```
class ErrorHandlingWebSocket extends SolanaWebSocketManager {
  constructor(endpoint, options = {}) {
    super(endpoint, options);
    this.errorCounts = new Map();
    this.maxErrorsPerMinute = options.maxErrorsPerMinute || 10;


  handleMessage(data) {
    try {
      // Handle rate limiting
      if (data.error data.error.code === 429) {
        console.warn('Rate limited, backing off...');
        this.handleRateLimit();
        return;


      // Handle subscription errors
      if (data.error data.error.code === -32602) {
        console.error('Invalid subscription parameters:', data.error.message);
        this.handleInvalidSubscription(data.id);
        return;


      // Handle network errors
      if (data.error data.error.code === -32603) {
        console.error('Internal server error:', data.error.message);
        this.handleServerError();
        return;


      super.handleMessage(data);
catch (error) {
      console.error('Error processing WebSocket message:', error);
      this.incrementErrorCount('message_processing');



  handleRateLimit() {
    // Exponential backoff for rate limiting
    const backoffDelay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), 30000);

    setTimeout(() => {
      if (this.subscriptions.size 0) {
        console.log('Retrying after rate limit...');
        this.resubscribeAll();

    }, backoffDelay);


  handleInvalidSubscription(requestId) {
    // Remove invalid subscription
    const subscription = Array.from(this.subscriptions.entries())
find(([id, sub]) => sub.requestId === requestId);

    if (subscription) {
      console.warn(`Removing invalid subscription: ${subscription[1].method}`);
      this.subscriptions.delete(subscription[0]);



  handleServerError() {
    // Log server error and potentially switch endpoints
    this.incrementErrorCount('server_error');

    if (this.getErrorCount('server_error')  5) {
      console.error('Too many server errors, consider switching endpoints');
      this.eventEmitter.dispatchEvent(new CustomEvent('tooManyServerErrors'));



  incrementErrorCount(errorType) {
    const now = Date.now();
    const errors = this.errorCounts.get(errorType) || [];

    // Add current error
    errors.push(now);

    // Remove errors older than 1 minute
    const oneMinuteAgo = now - 60000;
    const recentErrors = errors.filter(timestamp => timestamp oneMinuteAgo);

    this.errorCounts.set(errorType, recentErrors);

    // Check if we're exceeding error threshold
    if (recentErrors.length this.maxErrorsPerMinute) {
      console.error(`Too many ${errorType} errors in the last minute`);
      this.eventEmitter.dispatchEvent(new CustomEvent('errorThresholdExceeded', {
        detail: { errorType, count: recentErrors.length }
      }));



  getErrorCount(errorType) {
    const errors = this.errorCounts.get(errorType) || [];
    const oneMinuteAgo = Date.now() - 60000;
    return errors.filter(timestamp => timestamp oneMinuteAgo).length;



```

## Next Steps
## [API Reference Complete documentation for all WebSocket subscription methods ](https://www.helius.dev/docs/api-reference/rpc/websocket-methods)
## [Enhanced WebSockets Explore Helius Enhanced WebSockets with additional features and filters ](https://www.helius.dev/docs/enhanced-websockets)
## [LaserStream Upgrade to LaserStream for ultra-fast data streaming with historical replay ](https://www.helius.dev/docs/laserstream)
## [LaserStream Guide Learn how to stream real-time account updates using LaserStream ](https://www.helius.dev/docs/laserstream/guides/account-subscription)
For questions or additional support, join our [Discord community](https://discord.com/invite/6GXdee3gBj) where our team and community members are ready to help!
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/websocket)[ Stream Pump AMM DataLearn how to stream live Solana Pump AMM data using Standard WebSocket. Log-based monitoring available on all plans with automatic reconnection. Next ](https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data)
On this page
  * [Program Activity Monitoring](https://www.helius.dev/docs/rpc/websocket/quickstart#program-activity-monitoring)
  * [Transaction Monitoring](https://www.helius.dev/docs/rpc/websocket/quickstart#transaction-monitoring)
  * [Production-Ready Implementation](https://www.helius.dev/docs/rpc/websocket/quickstart#production-ready-implementation)
  * [Explore More WebSocket Methods](https://www.helius.dev/docs/rpc/websocket/quickstart#explore-more-websocket-methods)
  * [DeFi Trading Dashboard](https://www.helius.dev/docs/rpc/websocket/quickstart#defi-trading-dashboard)
  * [NFT Marketplace Integration](https://www.helius.dev/docs/rpc/websocket/quickstart#nft-marketplace-integration)
  * [React Integration Example](https://www.helius.dev/docs/rpc/websocket/quickstart#react-integration-example)
  * [Performance Optimization](https://www.helius.dev/docs/rpc/websocket/quickstart#performance-optimization)
  * [Error Handling and Debugging](https://www.helius.dev/docs/rpc/websocket/quickstart#error-handling-and-debugging)


Assistant
Responses are generated using AI and may contain mistakes.
