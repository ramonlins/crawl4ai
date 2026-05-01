# Source: https://www.helius.dev/docs/rpc/websocket

## What are Solana WebSockets and why use them?
WebSockets provide a persistent, real-time connection between your application and the Solana blockchain. Unlike traditional HTTP requests where you repeatedly ask “has anything changed?”, WebSockets let the blockchain notify you instantly when something happens.
## Real-Time Updates
Get instantly notified when Solana accounts change, transactions occur, or when new blocks are produced
## Efficient Resource Usage
One persistent connection instead of polling hundreds of HTTP requests
## Low Latency
Sub-second response times for time-critical trading and monitoring apps
## Powered by LaserStream
Up to 200 ms faster than standard RPC-based WSS
## Core Concepts
### Subscription Types
Account Subscriptions
Monitor changes to specific accounts like wallet balances, token accounts, or program data.**Use cases:**
  * Wallet balance tracking
  * Token account monitoring
  * Smart contract state changes
  * NFT ownership updates


Program Subscriptions
Watch all accounts owned by a specific program for any changes.**Use cases:**
  * DEX trade monitoring
  * DeFi protocol tracking
  * NFT marketplace activity
  * Gaming asset changes


Transaction Subscriptions
Get notified when specific transactions are confirmed or when transactions mention certain accounts.**Use cases:**
  * Payment confirmations
  * Transaction status tracking
  * Multi-signature approvals
  * Contract execution monitoring


Slot Subscriptions
Monitor blockchain progression and finality at the slot level.**Use cases:**
  * Block explorer applications
  * Network health monitoring
  * Consensus tracking
  * Performance analytics


### Commitment Levels
Understanding commitment levels is crucial for reliable applications:
  * Processed
  * Confirmed
  * Finalized


**Fastest** - Transaction processed by a validator but not confirmed
  * Latency: ~400ms
  * Risk: Can be dropped or reordered
  * Use for: Real-time UI updates (with caution)


**Balanced** - Majority of cluster has voted on the slot
  * Latency: ~2-3 seconds
  * Risk: Low chance of being dropped
  * Use for: Most applications


**Safest** - Supermajority of cluster has voted on the slot
  * Latency: ~15-30 seconds
  * Risk: Extremely unlikely to be dropped
  * Use for: Financial applications, high-value transactions


**Want to learn more about commitment levels?** Read our comprehensive blog post: [Understanding Solana Commitment Levels](https://www.helius.dev/blog/solana-commitment-levels)
## Available WebSocket Methods
The examples in this guide cover the most commonly used WebSocket methods, but Solana’s WebSocket API offers many more subscription types for specialized use cases.
## [Complete API Reference **Explore all 18+ WebSocket methods**. Each method includes detailed parameters, response formats, and examples. ](https://www.helius.dev/docs/api-reference/rpc/websocket-methods)
## How to Implement Reconnection Logic
WebSocket connections can disconnect for various reasons - network issues, server maintenance, or temporary outages. Production applications **must** implement reconnection logic to ensure reliability.
### Why Disconnections Happen
Network Issues
  * Internet connectivity problems
  * WiFi handoffs on mobile devices
  * Corporate firewall timeouts
  * ISP routing changes


Server-Side Events
  * Planned maintenance windows
  * Load balancer restarts
  * RPC node updates
  * Temporary overload protection


Client-Side Issues
  * Browser tab backgrounding
  * Mobile app suspension
  * Computer sleep/hibernation
  * Process crashes or restarts


### Detecting Disconnections
  * JavaScript/Browser
  * Node.js



```
class ConnectionMonitor {
  constructor(ws) {
    this.ws = ws;
    this.pingInterval = null;
    this.lastPong = Date.now();
    this.isConnected = false;

    this.setupEventListeners();
    this.startPingMonitoring();


  setupEventListeners() {
    this.ws.onopen = () => {
      console.log('Connected');
      this.isConnected = true;
      this.lastPong = Date.now();


    this.ws.onclose = (event) => {
      console.log('Disconnected:', event.code, event.reason);
      this.isConnected = false;
      this.stopPingMonitoring();


    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.isConnected = false;


    // Listen for pong responses (server acknowledgment)
    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.method === 'pong') {
        this.lastPong = Date.now();

      // Handle other messages...



  startPingMonitoring() {
    this.pingInterval = setInterval(() => {
      if (this.isConnected) {
        // Send ping to check connection health
        this.ws.send(JSON.stringify({
          jsonrpc: '2.0',
          method: 'ping',
          id: Date.now()
        }));

        // Check if we received a pong recently
        const timeSinceLastPong = Date.now() - this.lastPong;
 (timeSinceLastPong 30000) { // 30 seconds timeout
          console.warn('No pong received, connection may be stale');
          this.ws.close();


    }, 10000); // Ping every 10 seconds


  stopPingMonitoring() {
    if (this.pingInterval) {
      clearInterval(this.pingInterval);
      this.pingInterval = null;




```


```
const WebSocket = require('ws');

class NodeConnectionMonitor {
  constructor(url) {
    this.url = url;
    this.ws = null;
    this.pingInterval = null;
    this.isAlive = false;


  connect() {
    this.ws = new WebSocket(this.url);

    this.ws.on('open', () => {
      console.log('Connected');
      this.isAlive = true;
      this.startHeartbeat();
    });

    this.ws.on('close', () => {
      console.log('Disconnected');
      this.isAlive = false;
      this.stopHeartbeat();
    });

    this.ws.on('error', (error) => {
      console.error('WebSocket error:', error);
      this.isAlive = false;
    });

    // Built-in ping/pong handling
    this.ws.on('pong', () => {
      this.isAlive = true;
    });


  startHeartbeat() {
    this.pingInterval = setInterval(() => {
      if (!this.isAlive) {
        console.log('Connection lost, terminating');
        return this.ws.terminate();


      this.isAlive = false;
      this.ws.ping();
    }, 30000); // Ping every 30 seconds


  stopHeartbeat() {
    if (this.pingInterval) {
      clearInterval(this.pingInterval);
      this.pingInterval = null;




```

### Reconnection Strategies
  * Exponential Backoff
  * Circuit Breaker Pattern



```
class ExponentialBackoffReconnector {
  constructor(url, maxRetries = 10) {
    this.url = url;
    this.maxRetries = maxRetries;
    this.retryCount = 0;
    this.baseDelay = 1000; // Start with 1 second
    this.maxDelay = 30000; // Cap at 30 seconds
    this.ws = null;
    this.subscriptions = new Map();
    this.isReconnecting = false;


  connect() {
    if (this.isReconnecting) return;

    try {
      this.ws = new WebSocket(this.url);
      this.setupEventHandlers();
catch (error) {
      console.error('Failed to create WebSocket:', error);
      this.scheduleReconnect();



  setupEventHandlers() {
    this.ws.onopen = () => {
      console.log('Connected successfully');
      this.retryCount = 0; // Reset retry count on successful connection
      this.isReconnecting = false;
      this.resubscribeAll(); // Restore subscriptions


    this.ws.onclose = (event) => {
      console.log('Connection closed:', event.code);
      if (!this.isReconnecting) {
        this.scheduleReconnect();



    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);



  scheduleReconnect() {
    if (this.retryCount >= this.maxRetries) {
      console.error('Max retry attempts reached. Giving up.');
      return;


    this.isReconnecting = true;
    this.retryCount++;

    // Calculate delay with exponential backoff + jitter
    const delay = Math.min(
      this.baseDelay * Math.pow(2, this.retryCount - 1),
      this.maxDelay


    // Add jitter to prevent thundering herd
    const jitteredDelay = delay + (Math.random() * 1000);

    console.log(`Reconnecting in ${jitteredDelay}ms (attempt ${this.retryCount}/${this.maxRetries})`);

    setTimeout(() => {
      this.connect();
    }, jitteredDelay);


  subscribe(method, params, callback) {
    const id = this.generateId();
    this.subscriptions.set(id, { method, params, callback });

    if (this.ws this.ws.readyState === WebSocket.OPEN) {
      this.sendSubscription(id, method, params);


    return id;


  resubscribeAll() {
    console.log(`Restoring ${this.subscriptions.size} subscriptions`);
    for (const [id, sub] of this.subscriptions) {
      this.sendSubscription(id, sub.method, sub.params);



  sendSubscription(id, method, params) {
    this.ws.send(JSON.stringify({
      jsonrpc: '2.0',
      id: id,
      method: method,
      params: params
    }));


  generateId() {
    return Date.now() + Math.random();



```


```
class CircuitBreakerWebSocket {
  constructor(url, options = {}) {
    this.url = url;
    this.failureThreshold = options.failureThreshold || 5;
    this.recoveryTimeout = options.recoveryTimeout || 60000;
    this.checkInterval = options.checkInterval || 10000;

    this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
    this.failureCount = 0;
    this.lastFailureTime = null;
    this.ws = null;
    this.subscriptions = new Map();


  connect() {
    if (this.state === 'OPEN') {
      if (Date.now() - this.lastFailureTime this.recoveryTimeout) {
        console.log('Circuit breaker moving to HALF_OPEN state');
        this.state = 'HALF_OPEN';
else {
        console.log('Circuit breaker is OPEN, connection blocked');
        return false;



    try {
      this.ws = new WebSocket(this.url);
      this.setupEventHandlers();
      return true;
catch (error) {
      this.recordFailure();
      return false;



  setupEventHandlers() {
    this.ws.onopen = () => {
      console.log('Connected - Circuit breaker CLOSED');
      this.state = 'CLOSED';
      this.failureCount = 0;
      this.resubscribeAll();


    this.ws.onclose = () => {
      this.recordFailure();


    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.recordFailure();



  recordFailure() {
    this.failureCount++;
    this.lastFailureTime = Date.now();

    console.log(`Failure recorded: ${this.failureCount}/${this.failureThreshold}`);

    if (this.failureCount >= this.failureThreshold) {
      console.log('Circuit breaker opened due to repeated failures');
      this.state = 'OPEN';



  startHealthCheck() {
    setInterval(() => {
      if (this.state === 'OPEN' ||
this.ws this.ws.readyState !== WebSocket.OPEN)) {
        this.connect();

    }, this.checkInterval);



```

### Testing Reconnection Logic
  * Network Simulation
  * Automated Testing



```
// Test disconnection scenarios
class NetworkSimulator {
  constructor(wsManager) {
    this.wsManager = wsManager;


  // Simulate network outage
  simulateNetworkOutage(duration = 5000) {
    console.log('Simulating network outage...');

    // Force close the connection
    if (this.wsManager.ws) {
      this.wsManager.ws.close(1006, 'Network outage simulation');


    // Block reconnection temporarily
    const originalConnect = this.wsManager.connect.bind(this.wsManager);
    this.wsManager.connect = () => {
      console.log('Connection blocked during outage simulation');


    // Restore connection after duration
    setTimeout(() => {
      console.log('Network restored');
      this.wsManager.connect = originalConnect;
      this.wsManager.connect();
    }, duration);


  // Simulate intermittent connectivity
  simulateIntermittentConnectivity() {
    setInterval(() => {
      if (Math.random()  0.1) { // 10% chance every 10 seconds
        console.log('Simulating connection drop...');
        this.wsManager.ws?.close(1006, 'Intermittent connectivity');

    }, 10000);



// Usage
const simulator = new NetworkSimulator(wsManager);
simulator.simulateNetworkOutage(10000); // 10 second outage

```


```
// Jest test example
describe('WebSocket Reconnection', () => {
  let wsManager;

  beforeEach(() => {
    wsManager = new ProductionWebSocketManager({
      endpoint: 'ws://localhost:8080',
      apiKey: 'test-key'
    });
  });

  test('should reconnect after connection loss', async () => {
    const reconnectPromise = new Promise((resolve) => {
      wsManager.on('connected', resolve);
    });

    await wsManager.connect();

    // Simulate connection loss
    wsManager.ws.close(1006, 'Test disconnection');

    // Wait for reconnection
    await reconnectPromise;

    expect(wsManager.connectionState).toBe('CONNECTED');
    expect(wsManager.metrics.reconnections).toBeGreaterThan(0);
  });

  test('should restore subscriptions after reconnection', async () => {
    await wsManager.connect();

    const messages = [];
    const subscriptionId = wsManager.subscribe(
      'accountSubscribe',
'test-account', {}],
data) => messages.push(data)


    // Verify subscription exists
    expect(wsManager.subscriptions.has(subscriptionId)).toBe(true);

    // Simulate disconnection and reconnection
    wsManager.ws.close(1006, 'Test disconnection');

    await new Promise(resolve => wsManager.on('connected', resolve));

    // Verify subscription was restored
    const subscription = wsManager.subscriptions.get(subscriptionId);
    expect(subscription.pending).toBe(true); // Should be re-subscribing
  });
});

```

**Critical for Production** : Implementing proper reconnection logic is not optional for production applications. WebSocket connections will disconnect - plan for it, test it, and monitor it in production.
## Troubleshooting
Connection Failed
**Symptoms** : WebSocket fails to connect initially**Solutions** :
  * Verify your API key is correct and has sufficient credits
  * Check the endpoint URL format: `wss://mainnet.helius-rpc.com?api-key=YOUR_KEY`
  * Ensure your firewall allows WebSocket connections on port 443
  * Test with a simple ping first to verify basic connectivity


Frequent Disconnections
**Symptoms** : Connection drops every few minutes**Solutions** :
  * Implement proper ping/pong heartbeat (shown in reconnection examples above)
  * Check your network stability and corporate firewall settings
  * Monitor your subscription count - too many can cause instability
  * Verify you’re handling the connection lifecycle properly


Missing Messages
**Symptoms** : Not receiving expected subscription updates**Solutions** :
  * Verify your subscription is confirmed (check the response)
  * Ensure the account/program you’re monitoring has actual activity
  * Monitor your connection state - missed messages often indicate disconnections


High Latency
**Symptoms** : Slow message delivery, delays in updates**Solutions** :
  * Use “confirmed” instead of “finalized” commitment
  * Reduce the number of active subscriptions
  * Optimize your message processing logic
  * Consider using multiple connections to distribute load
  * Check your network connection quality


Memory Leaks
**Symptoms** : Application memory usage grows over time**Solutions** :
  * Implement proper subscription cleanup
  * Remove event listeners when components unmount
  * Clear message logs periodically
  * Monitor subscription count and enforce limits
  * Use weak references for callback functions where possible


## Migration from Standard RPC
If you’re currently using HTTP polling, here’s how to migrate to WebSockets:

```
// Old approach - HTTP polling
class HTTPAccountMonitor {
  constructor(connection, accountAddress) {
    this.connection = connection;
    this.accountAddress = accountAddress;
    this.interval = null;
    this.lastKnownBalance = null;


  start() {
    this.interval = setInterval(async () => {
      try {
        const accountInfo = await this.connection.getAccountInfo(
          new PublicKey(this.accountAddress)


        const currentBalance = accountInfo?.lamports || 0;

 (this.lastKnownBalance !== currentBalance) {
          console.log(`Balance changed: ${currentBalance}`);
          this.lastKnownBalance = currentBalance;

catch (error) {
        console.error('Failed to fetch account info:', error);

    }, 2000); // Poll every 2 seconds


  stop() {
    if (this.interval) {
      clearInterval(this.interval);
      this.interval = null;




// New approach - WebSocket subscription
class WebSocketAccountMonitor {
  constructor(wsManager, accountAddress) {
    this.wsManager = wsManager;
    this.accountAddress = accountAddress;
    this.subscriptionId = null;


  start() {
    this.subscriptionId = this.wsManager.subscribe(
      'accountSubscribe',

        this.accountAddress,
encoding: 'jsonParsed', commitment: 'confirmed' }

data) => {
        const currentBalance = data.value.lamports;
        console.log(`Balance changed: ${currentBalance}`);

        // Handle the change immediately - no polling delay!




  stop() {
    if (this.subscriptionId) {
      this.wsManager.unsubscribe(this.subscriptionId);
      this.subscriptionId = null;




```

## Enhanced Capabilities
For apps requiring even more advanced features, consider using [LaserStream gRPC](https://www.helius.dev/docs/laserstream):
## 24-Hour Historical Replay
Catch up on missed data when your app was offline
## Multi-Node Aggregation
Better reliability via data from multiple validators
## Higher Throughput
Handle more subscriptions and higher message rates
## Enterprise Features
Advanced monitoring, analytics, and data pipelines
## Get Started
Ready to Get Started? Check out our [WebSocket Quickstart Guide](https://www.helius.dev/docs/rpc/websocket/quickstart) for practical examples and a step-by-step implementation.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-websockets/stream-pump-amm-data)[ QuickstartStart using Solana WebSockets in minutes with this step-by-step guide covering account monitoring, transaction tracking, and building real-time apps. Next ](https://www.helius.dev/docs/rpc/websocket/quickstart)
On this page
  * [What are Solana WebSockets and why use them?](https://www.helius.dev/docs/rpc/websocket#what-are-solana-websockets-and-why-use-them)
  * [Available WebSocket Methods](https://www.helius.dev/docs/rpc/websocket#available-websocket-methods)
  * [How to Implement Reconnection Logic](https://www.helius.dev/docs/rpc/websocket#how-to-implement-reconnection-logic)
  * [Why Disconnections Happen](https://www.helius.dev/docs/rpc/websocket#why-disconnections-happen)
  * [Detecting Disconnections](https://www.helius.dev/docs/rpc/websocket#detecting-disconnections)
  * [Reconnection Strategies](https://www.helius.dev/docs/rpc/websocket#reconnection-strategies)
  * [Testing Reconnection Logic](https://www.helius.dev/docs/rpc/websocket#testing-reconnection-logic)
  * [Migration from Standard RPC](https://www.helius.dev/docs/rpc/websocket#migration-from-standard-rpc)


Assistant
Responses are generated using AI and may contain mistakes.
