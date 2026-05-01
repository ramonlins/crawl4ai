# Source: https://www.helius.dev/docs/rpc/optimization-techniques

Optimizing RPC usage can significantly improve performance, reduce costs, and enhance user experience. This guide covers proven techniques for efficient Solana RPC interactions.
## Quick Start
## [Transaction Optimization Optimize compute units, priority fees, and transaction sending ](https://www.helius.dev/docs/rpc/optimization-techniques#transaction-optimization)
## [Data Retrieval Efficient patterns for fetching account and program data ](https://www.helius.dev/docs/rpc/optimization-techniques#data-retrieval-optimization)
## [Real-time Monitoring WebSocket subscriptions and streaming data optimization ](https://www.helius.dev/docs/rpc/optimization-techniques#real-time-monitoring)
## [Best Practices Performance guidelines and resource management ](https://www.helius.dev/docs/rpc/optimization-techniques#best-practices)
## Transaction Optimization
### Compute Unit Management
**1. Simulate to determine actual usage:**

```
const testTransaction = new VersionedTransaction(/* your transaction */);
const simulation = await connection.simulateTransaction(testTransaction, {
  replaceRecentBlockhash: true,
  sigVerify: false
});
const unitsConsumed = simulation.value.unitsConsumed;

```

**2. Set appropriate limits with margin:**

```
const computeUnitLimit = Math.ceil(unitsConsumed * 1.1);
const computeUnitIx = ComputeBudgetProgram.setComputeUnitLimit({ 
  units: computeUnitLimit
});
instructions.unshift(computeUnitIx); // Add at beginning

```

### Priority Fee Optimization
**1. Get dynamic fee estimates:**

```
const response = await fetch(`https://mainnet.helius-rpc.com/?api-key=${API_KEY}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    method: 'getPriorityFeeEstimate',
    params: [{
      accountKeys: ['11111111111111111111111111111112'], // System Program
      options: { recommended: true }


});
const { priorityFeeEstimate } = await response.json().result;

```

**2. Apply the priority fee:**

```
const priorityFeeIx = ComputeBudgetProgram.setComputeUnitPrice({ 
  microLamports: priorityFeeEstimate
});
instructions.unshift(priorityFeeIx);

```

### Transaction Sending Best Practices
  * Standard Approach
  * With Confirmation



```
// Serialize and encode
const serializedTx = transaction.serialize();
const signature = await connection.sendRawTransaction(serializedTx, {
  skipPreflight: true, // Saves ~100ms
  maxRetries: 0 // Handle retries manually
});

```


```
// Send and confirm with custom logic
const signature = await connection.sendRawTransaction(serializedTx);

// Monitor confirmation
const confirmation = await connection.confirmTransaction({
  signature,
  blockhash: latestBlockhash.blockhash,
  lastValidBlockHeight: latestBlockhash.lastValidBlockHeight
});

```

## Data Retrieval Optimization
### Enhanced Pagination Methods (V2)
**For large-scale data queries, use the new V2 methods with cursor-based pagination:**
## ⚡ Performance Boost
`getProgramAccountsV2` and `getTokenAccountsByOwnerV2` provide significant performance improvements for applications dealing with large datasets:
  * **Configurable limits** : 1-10,000 accounts per request
  * **Cursor-based pagination** : Prevents timeouts on large queries
  * **Incremental updates** : Use `changedSinceSlot` for real-time synchronization
  * **Better memory usage** : Stream data instead of loading everything at once


**Example: Efficient program account querying**

```
// ❌ Old approach - could timeout with large datasets
const allAccounts = await connection.getProgramAccounts(programId, {
  encoding: 'base64',
  filters: [{ dataSize: 165 }]
});

// ✅ New approach - paginated with better performance
let allAccounts = [];
let paginationKey = null;


  const response = await fetch(`https://mainnet.helius-rpc.com/?api-key=${API_KEY}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getProgramAccountsV2',
      params: [
        programId,

          encoding: 'base64',
          filters: [{ dataSize: 165 }],
          limit: 5000,
          ...(paginationKey { paginationKey })



  });

  const data = await response.json();
  allAccounts.push(...data.result.accounts);
  paginationKey = data.result.paginationKey;
} while (paginationKey);

```

**Incremental updates for real-time applications:**

```
// Get only accounts modified since a specific slot
const incrementalUpdate = await fetch(`https://mainnet.helius-rpc.com/?api-key=${API_KEY}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    id: '1',
    method: 'getProgramAccountsV2',
    params: [
      programId,

        encoding: 'jsonParsed',
        limit: 1000,
        changedSinceSlot: lastProcessedSlot // Only get recent changes



});

```

## Data Retrieval Optimization
### Efficient Account Queries
  * Single Account
  * Multiple Accounts
  * Program Accounts



```
// Use dataSlice to reduce payload size
const accountInfo = await connection.getAccountInfo(pubkey, {
  encoding: 'base64',
  dataSlice: { offset: 0, length: 100 }, // Only get needed data
  commitment: 'confirmed'
});

```


```
// Batch multiple account queries
const accounts = await connection.getMultipleAccountsInfo([
  pubkey1, pubkey2, pubkey3
], {
  encoding: 'base64',
  commitment: 'confirmed'
});

```


```
// Use filters to reduce data transfer
const accounts = await connection.getProgramAccounts(programId, {
  filters: [
dataSize: 165 }, // Token account size
memcmp: { offset: 0, bytes: mintAddress }}

  encoding: 'jsonParsed'
});

```

### Token Balance Lookups
❌ Inefficient
✅ Optimized

```
// Don't do this - requires N+1 RPC calls
const tokenAccounts = await connection.getTokenAccountsByOwner(owner, {
  programId: TOKEN_PROGRAM_ID
});
const balances = await Promise.all(
  tokenAccounts.value.map(acc =>
    connection.getTokenAccountBalance(acc.pubkey)


// ~500ms + (100ms * N accounts)

```

### Transaction History
❌ Inefficient
✅ Fast (Helius Exclusive)

```
// Avoid sequential transaction fetching
const signatures = await connection.getSignaturesForAddress(address, { limit: 100 });
const transactions = await Promise.all(
  signatures.map(sig => connection.getTransaction(sig.signature))

// ~1s + (200ms * 100 txs) = ~21s
// Also note: getSignaturesForAddress doesn't include token account transactions

```

## Real-time Monitoring
### Account Subscriptions
❌ Polling
✅ WebSocket

```
// Avoid polling - wastes resources
setInterval(async () => {
  const accountInfo = await connection.getAccountInfo(pubkey);
  // Process updates...
}, 1000);

```

### Program Account Monitoring

```
// Monitor specific program accounts with filters
connection.onProgramAccountChange(
  programId,
  (accountInfo, context) => {
    // Handle program account changes

  'confirmed',

    filters: [
dataSize: 1024 },
memcmp: { offset: 0, bytes: ACCOUNT_DISCRIMINATOR }}

    encoding: 'base64'



```

### Transaction Monitoring

```
// Subscribe to transaction logs for real-time monitoring
const ws = new WebSocket(`wss://mainnet.helius-rpc.com/?api-key=${API_KEY}`);

ws.on('open', () => {
  ws.send(JSON.stringify({
    jsonrpc: '2.0',
    id: 1,
    method: 'logsSubscribe',
    params: [
mentions: [programId] },
commitment: 'confirmed' }

  }));
});

ws.on('message', (data) => {
  const message = JSON.parse(data);
  if (message.params) {
    const signature = message.params.result.value.signature;
    // Process transaction signature

});

```

## Advanced Patterns
### Smart Retry Logic

```
class RetryManager {
  private backoff = new ExponentialBackoff({
    min: 100,
    max: 5000,
    factor: 2,
    jitter: 0.2
  });

  async executeWithRetryT>(operation: () => PromiseT>): PromiseT> {
    while (true) {
      try {
        return await operation();
catch (error) {
 (error.message.includes('429')) {
          // Rate limit - wait and retry
          await this.backoff.delay();
          continue;

        throw error;





```

### Memory-Efficient Processing

```
// Process large datasets in chunks
function chunkT>(array: T[], size: number): T[][] {
  return Array.from({ length: Math.ceil(array.length / size) }, (_, i) =>
    array.slice(i * size, i * size + size)



// Process program accounts in batches
const allAccounts = await connection.getProgramAccounts(programId, {
  dataSlice: { offset: 0, length: 32 }
});

const chunks = chunk(allAccounts, 100);
for (const batch of chunks) {
  const detailedAccounts = await connection.getMultipleAccountsInfo(
    batch.map(acc => acc.pubkey)

  // Process batch...


```

### Connection Pooling

```
class ConnectionPool {
  private connections: Connection[] = [];
  private currentIndex = 0;

  constructor(rpcUrls: string[]) {
    this.connections = rpcUrls.map(url => new Connection(url));


  getConnection(): Connection {
    const connection = this.connections[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.connections.length;
    return connection;



const pool = new ConnectionPool([
  'https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY',
  'https://mainnet-backup.helius-rpc.com/?api-key=YOUR_API_KEY'
]);

```

## Performance Monitoring
### Track RPC Usage

```
class RPCMonitor {
  private metrics = {
    calls: 0,
    errors: 0,
    totalLatency: 0


  async monitoredCallT>(operation: () => PromiseT>): PromiseT> {
    const start = Date.now();
    this.metrics.calls++;

    try {
      const result = await operation();
      this.metrics.totalLatency += Date.now() - start;
      return result;
catch (error) {
      this.metrics.errors++;
      throw error;



  getStats() {
    return {
      ...this.metrics,
      averageLatency: this.metrics.totalLatency / this.metrics.calls,
      errorRate: this.metrics.errors / this.metrics.calls




```

## Best Practices
### Commitment Levels
  * processed
  * confirmed
  * finalized


  * **Use for** : WebSocket subscriptions, real-time updates
  * **Latency** : ~400ms
  * **Reliability** : Good for most applications


  * **Use for** : General queries, account info
  * **Latency** : ~1s
  * **Reliability** : Recommended for most use cases


  * **Use for** : Final settlement, irreversible operations
  * **Latency** : ~32s
  * **Reliability** : Maximum certainty


### Resource Management
### Error Handling

```
// Implement robust error handling
async function robustRPCCallT>(operation: () => PromiseT>): PromiseT> {
  try {
    return await operation();
catch (error) {
    if (error.code === -32602) {
      // Invalid params - fix request
      throw new Error('Invalid RPC parameters');
else if (error.code === -32005) {
      // Node behind - retry with different node
      throw new Error('Node synchronization issue');
else if (error.message.includes('429')) {
      // Rate limit - implement backoff
      throw new Error('Rate limited');

    throw error;



```

## Common Pitfalls to Avoid
**Avoid these common mistakes:**
  * Polling instead of using WebSocket subscriptions
  * Fetching full account data when only partial data is needed
  * Not using batch operations for multiple queries
  * Ignoring rate limits and not implementing proper retry logic
  * Using `finalized` commitment when `confirmed` is sufficient
  * Not closing subscriptions, leading to memory leaks


## Related Methods
The optimization techniques in this guide reference the following WebSocket and RPC methods:
## [getSignaturesForAddress Get transaction signatures for an address ](https://www.helius.dev/docs/api-reference/rpc/http/getsignaturesforaddress)
## [getTransaction Retrieve full transaction details by signature ](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction)
## [getProgramAccounts Fetch all accounts owned by a program ](https://www.helius.dev/docs/api-reference/rpc/http/getprogramaccounts)
## [getTokenAccountsByOwner Get token accounts for a wallet ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountsbyowner)
## [getMultipleAccountsInfo Batch fetch multiple account details ](https://www.helius.dev/docs/api-reference/rpc/http/getmultipleaccounts)
## [getAccountInfo Get information about a single account ](https://www.helius.dev/docs/api-reference/rpc/http/getaccountinfo)
## [accountSubscribe Subscribe to account changes via WebSocket ](https://www.helius.dev/docs/api-reference/rpc/websocket/accountsubscribe)
## [programSubscribe Subscribe to program account changes via WebSocket ](https://www.helius.dev/docs/api-reference/rpc/websocket/programsubscribe)
## [logsSubscribe Subscribe to transaction logs via WebSocket ](https://www.helius.dev/docs/api-reference/rpc/websocket/logssubscribe)
## Summary
By implementing these optimization techniques, you can achieve:
  * **60-90% reduction** in API call volume
  * **Significantly lower latency** for real-time operations
  * **Reduced bandwidth usage** through targeted queries
  * **Better error resilience** with smart retry logic
  * **Lower operational costs** through efficient resource usage


## Next Steps
Ready to implement these optimizations? Check out our [Transaction Optimization Guide](https://www.helius.dev/docs/sending-transactions/optimizing-transactions) for transaction-specific best practices.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/devnet-sol)[ OverviewPractical guides and tutorials for effectively using Solana RPC methods. Real-world examples, code samples, and best practices for blockchain development. Next ](https://www.helius.dev/docs/rpc/guides/overview)
On this page
  * [Transaction Optimization](https://www.helius.dev/docs/rpc/optimization-techniques#transaction-optimization)
  * [Compute Unit Management](https://www.helius.dev/docs/rpc/optimization-techniques#compute-unit-management)
  * [Priority Fee Optimization](https://www.helius.dev/docs/rpc/optimization-techniques#priority-fee-optimization)
  * [Transaction Sending Best Practices](https://www.helius.dev/docs/rpc/optimization-techniques#transaction-sending-best-practices)
  * [Data Retrieval Optimization](https://www.helius.dev/docs/rpc/optimization-techniques#data-retrieval-optimization)
  * [Enhanced Pagination Methods (V2)](https://www.helius.dev/docs/rpc/optimization-techniques#enhanced-pagination-methods-v2)
  * [Data Retrieval Optimization](https://www.helius.dev/docs/rpc/optimization-techniques#data-retrieval-optimization-2)
  * [Efficient Account Queries](https://www.helius.dev/docs/rpc/optimization-techniques#efficient-account-queries)
  * [Token Balance Lookups](https://www.helius.dev/docs/rpc/optimization-techniques#token-balance-lookups)
  * [Account Subscriptions](https://www.helius.dev/docs/rpc/optimization-techniques#account-subscriptions)
  * [Program Account Monitoring](https://www.helius.dev/docs/rpc/optimization-techniques#program-account-monitoring)
  * [Transaction Monitoring](https://www.helius.dev/docs/rpc/optimization-techniques#transaction-monitoring)
  * [Memory-Efficient Processing](https://www.helius.dev/docs/rpc/optimization-techniques#memory-efficient-processing)
  * [Common Pitfalls to Avoid](https://www.helius.dev/docs/rpc/optimization-techniques#common-pitfalls-to-avoid)


Assistant
Responses are generated using AI and may contain mistakes.
