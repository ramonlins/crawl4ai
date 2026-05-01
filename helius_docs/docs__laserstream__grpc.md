# Source: https://www.helius.dev/docs/laserstream/grpc

## Overview
LaserStream’s gRPC offering builds on a Yellowstone-based interface and enhances it with features like historical replay, multi-node failover, and a fully managed environment. LaserStream uses the open source gRPC protocol, ensuring no vendor lock-in and maximum compatibility with existing gRPC implementations. You can connect either directly with `@yellowstone-grpc` or use the performance-optimized **[Helius LaserStream SDK](https://www.helius.dev/docs/laserstream/clients)** for added benefits including higher throughput, automatic reconnects, subscription management, error handling, and more.
## [LaserStream SDK is 40x Faster vs. JavaScript Yellowstone Clients Learn how we used Rust Core with zero-copy NAPI bindings to maximize JavaScript SDK performance ](https://www.helius.dev/blog/laserstream-sdks)
**Performance Notice** : If you experience any lag or performance issues with your LaserStream connection, please refer to the [Troubleshooting section](https://www.helius.dev/docs/laserstream/grpc#troubleshooting-%2F-faq) for common causes and solutions.
**No Compression** : To minimize latency, LaserStream does not compress gRPC response messages. Setting `Accept-Encoding` with gzip or zstd will have no effect — responses are always returned uncompressed.
## Endpoints & Regions
LaserStream is available in multiple regions worldwide. Choose the endpoint closest to your application for optimal performance:
### Mainnet LaserStream Endpoints  
| Region  | Location  | Endpoint  |  
| --- | --- | --- |  
| **ewr**  | Newark, NJ (near New York)  | `https://laserstream-mainnet-ewr.helius-rpc.com`  |  
| **pitt**  | Pittsburgh, US (Central)  | `https://laserstream-mainnet-pitt.helius-rpc.com`  |  
| **slc**  | Salt Lake City, US (West Coast)  | `https://laserstream-mainnet-slc.helius-rpc.com`  |  
| **lax**  | Los Angeles, US (West Coast)  | `https://laserstream-mainnet-lax.helius-rpc.com`  |  
| **lon**  | London, Europe  | `https://laserstream-mainnet-lon.helius-rpc.com`  |  
| **ams**  | Amsterdam, Europe  | `https://laserstream-mainnet-ams.helius-rpc.com`  |  
| **fra**  | Frankfurt, Europe  | `https://laserstream-mainnet-fra.helius-rpc.com`  |  
| **tyo**  | Tokyo, Asia  | `https://laserstream-mainnet-tyo.helius-rpc.com`  |  
| **sgp**  | Singapore, Asia  | `https://laserstream-mainnet-sgp.helius-rpc.com`  |  
### Devnet LaserStream Endpoint  
| Network  | Location  | Endpoint  |  
| --- | --- | --- |  
| **Devnet**  | Newark, NJ (near New York)  | `https://laserstream-devnet-ewr.helius-rpc.com`  |  
**Network & Region Selection**:
  * For **production apps** , pick the mainnet endpoint nearest your server for best performance (e.g., if deploying in Europe, use Amsterdam (`ams`) or Frankfurt (`fra`))
  * For **testing** , use: `https://laserstream-devnet-ewr.helius-rpc.com`.


## Quickstart
Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
Create a New Project

```
mkdir laserstream-grpc-demo
cd laserstream-grpc-demo
npm init -y

```

Install Dependencies

```
npm install helius-laserstream
npm install --save-dev typescript ts-node
npx tsc --init

```

Obtain Your API Key
Generate a key from the [Helius Dashboard](https://dashboard.helius.dev/).This key will serve as your authentication token for LaserStream.
**Plan Requirements** : LaserStream devnet requires a Developer or higher [plan](https://www.helius.dev/docs/billing/plans). LaserStream mainnet requires a Business or Professional plan.
Create a Subscription Script
Create **`index.ts`**with the following:

```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
  const subscriptionRequest: SubscribeRequest = {
    transactions: {
      "token-filter": { // user-defined label for this filter
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
    // Optionally, you can replay missed data by specifying a fromSlot:
    // fromSlot: '224339000'
    // Note: Currently, you can only replay data from up to 216000 slots in the past (24 hours).


// Replace the values below with your actual LaserStream API key and endpoint
const config: LaserstreamConfig = {
  apiKey: 'YOUR_API_KEY', // Replace with your key from https://dashboard.helius.dev/
  endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


  await subscribe(config, subscriptionRequest, async (data) => {

    console.log(data);

  }, async (error) => {
    console.error(error);
  });


main().catch(console.error);

```

Replace Your API Key and Choose Your Region
In `index.ts`, update the `config` object with:
  1. Your actual API key from the [Helius Dashboard](https://dashboard.helius.dev/)
  2. The LaserStream endpoint closest to your server location



```
const config: LaserstreamConfig = {
  apiKey: 'YOUR_ACTUAL_API_KEY', // Replace with your key from Helius Dashboard
  endpoint: 'https://laserstream-mainnet-fra.helius-rpc.com', // Example: Frankfurt mainnet
  // For devnet: endpoint: 'https://laserstream-devnet-ewr.helius-rpc.com'


```

**Network & Region Selection Examples:**
  * **For Production (Mainnet)** : 
    * Europe: Use `fra` (Frankfurt), `ams` (Amsterdam), or `lon` (London)
    * US East: Use `ewr` (New York)
    * US West: Use `slc` (Salt Lake City) or `lax` (Los Angeles)
    * Asia: Use `tyo` (Tokyo) or `sgp` (Singapore)
  * **For Development (Devnet)** : 
    * Use `https://laserstream-devnet-ewr.helius-rpc.com`


Run and View Results

```
npx ts-node index.ts

```

Whenever a `confirmed` token transaction involves `TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA`, you’ll see the data in your console.
## Subscribe Request
In the subscribe request, you need to include the following general parameters:
**Historical Replay:** You can optionally include a `fromSlot: string` field in the main `SubscribeRequest` object to replay data from a specific slot onwards. Currently, replay is supported for up to 216,000 slots (24 hours) in the past.

```
const subscriptionRequest: SubscribeRequest = {
  commitment: CommitmentLevel.CONFIRMED,
  accountsDataSlice: [],
  transactions: {},
  accounts: {},
  slots: {},
  blocks: {},
  blocksMeta: {},
  entry: {},


```

Next, you’ll need to specify the filters for the data you want to subscribe to, such as accounts, blocks, slots, or transactions.
Slots
Define filters for slot updates. The key you use (e.g., `mySlotLabel`) is a **user-defined label** for this specific filter configuration, allowing you to potentially define multiple named configurations if needed (though typically one is sufficient).

```
slots: {
  // mySlotLabel is a user-defined name for this slot update filter configuration
  mySlotLabel: {
    // filterByCommitment: true => Only broadcast slot updates at the specified subscribeRequest commitment
    filterByCommitment: true
    // interslotUpdates: true allows receiving updates for changes occurring within a slot, not just new slots.
    interslotUpdates: true



```

Accounts
Define filters for account data updates. The key you use (e.g., `tokenAccounts`) is a **user-defined label** for this specific filter configuration.If all fields are empty, all accounts are broadcasted. Otherwise:
  * Fields operate as a logical **AND**.
  * Values within arrays act as a logical **OR** (except within `filters`, which operate as a logical **AND**).



```
accounts: {
  // tokenAccounts is a user-defined label for this account filter configuration
  tokenAccounts: {
    // Matches any of these public keys (logical OR)
    account: ["9SHQTA66Ekh7ZgMnKWsjxXk6DwXku8przs45E8bcEe38"],
    // Matches owners that are any of these public keys
    owner: ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"],
    // Filters - all must match (AND logic)
    filters: [
dataSize: 165 },

        memcmp: {
          offset: 0,
          data: { base58: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" }






```

Transaction
Define filters for transaction updates. The key you use (e.g., `myTxSubscription`) is a **user-defined label** for this specific filter configuration.If all fields are left empty, all transactions are broadcasted. Otherwise:
  * Fields operate as a logical **AND**.
  * Values within arrays are treated as a logical **OR** (except for `accountRequired`, where all must match).



```
transactions: {
  // myTxSubscription is a user-defined label for this transaction filter configuration
  myTxSubscription: {
    vote: false,
    failed: false,
    signature: "",
    // Transaction must include at least one of these public keys (OR)
    accountInclude: ["86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"],
    // Exclude if it matches any of these
    accountExclude: [],
    // Require all accounts in this array (AND)
    accountRequired: []



```

Block
Define filters for block updates. The key you use (e.g., `myBlockLabel`) is a **user-defined label** for this specific filter configuration.

```
blocks: {
  // myBlockLabel is a user-defined label for this block filter configuration
  myBlockLabel: {
    // Only broadcast blocks referencing these accounts
    accountInclude: ["86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY"],
    includeTransactions: true,
    includeAccounts: false,
    includeEntries: false



```

Blocks Meta
This functions similarly to Blocks but excludes transactions, accounts, and entries. The key you use (e.g., `blockmetadata`) is a **user-defined label** for this subscription. Currently, no filters are available for block metadata—all messages are broadcasted by default.

```
blocksMeta: {
  blockmetadata: {}


```

Entries
Subscribe to ledger entries. The key you use (e.g., `entrySubscribe`) is a **user-defined label** for this subscription. Currently, there are no filters available for entries; all entries are broadcasted.

```
entry: {
  entrySubscribe: {}


```

## Code Examples (LaserStream SDK)
  * Slot Updates
  * Account Updates
  * Transaction Updates
  * Blocks
  * Block Metadata
  * Entries



```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        transactions: {},
        commitment: CommitmentLevel.CONFIRMED,
        accounts: {},
        slots: {
            slot: { filterByCommitment: true },

        transactionsStatus: {},
        blocks: {},
        blocksMeta: {},
        entry: {},
        accountsDataSlice: [],


    const config: LaserstreamConfig = {
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        accounts: {
            "usdc-account": { // user-defined label for this filter
                account: ["EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"], // USDC mint account
                owner: [],
                filters: []


        accountsDataSlice: [],
        commitment: CommitmentLevel.CONFIRMED,
        slots: {},
        transactions: {},
        transactionsStatus: {},
        blocks: {},
        blocksMeta: {},
        entry: {}


    const config: LaserstreamConfig = {
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        transactions: {
            "token-filter": { // user-defined label for this filter
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
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        entry: {},
        accounts: {},
        accountsDataSlice: [],
        slots: {},
        blocks: {
            blocks: {
                accountInclude: []


        blocksMeta: {},
        transactions: {},
        transactionsStatus: {},
        commitment: CommitmentLevel.CONFIRMED,


    const config: LaserstreamConfig = {
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        entry: {},
        accounts: {},
        accountsDataSlice: [],
        slots: {},
        blocks: {},
        blocksMeta: {
            blockmetadata: {}

        transactions: {},
        transactionsStatus: {},
        commitment: CommitmentLevel.CONFIRMED,


    const config: LaserstreamConfig = {
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```


```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream'

async function main() {
    const subscriptionRequest: SubscribeRequest = {
        entry: {
            entrySubscribe: {}  // Subscribe to all entries

        accounts: {},
        accountsDataSlice: [],
        slots: {},
        blocks: {},
        blocksMeta: {},
        transactions: {},
        transactionsStatus: {},
        commitment: CommitmentLevel.CONFIRMED,


    const config: LaserstreamConfig = {
        apiKey: 'YOUR_API_KEY', // Replace with your key
        endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


    await subscribe(config, subscriptionRequest, async (data) => {
        console.log(data);
    }, async (error) => {
        console.error(error);
    });


main().catch(console.error);

```

## SDK Options
We provide official SDKs for multiple programming languages:
  * **TypeScript** : [LaserStream TypeScript SDK](https://github.com/helius-labs/laserstream-sdk)
  * **Rust** : [LaserStream Rust SDK](https://github.com/helius-labs/laserstream-sdk/tree/main/rust)
  * **Go** : [LaserStream Go SDK](https://github.com/helius-labs/laserstream-sdk/tree/main/go)

For other languages or custom implementations, you can use the [Yellowstone gRPC proto files](https://github.com/rpcpool/yellowstone-grpc/tree/v6.0.0%2Bsolana.2.2.12/yellowstone-grpc-proto/proto) directly to generate gRPC clients for your preferred language.
## Troubleshooting / FAQ
Q: I'm experiencing lag or slow performance with my LaserStream connection. What could be causing this?
**A:** Performance issues with LaserStream connections are typically caused by:
  * **Javascript Client Slowness** : The JavaScript client may lag behind when processing too many messages or consuming too much bandwidth. Consider filtering your subscriptions more narrowly to reduce message volume, switch to the [LaserStream JavaScript SDK](https://www.helius.dev/docs/laserstream/clients), or try using another language.
  * **Limited local bandwidth** : Heavy subscriptions can overwhelm clients with limited network bandwidth. Monitor your network usage and consider upgrading your connection or reducing subscription scope.
  * **Geographic distance** : Long network routes increase latency and packet loss. Use the [endpoint closest to your server](https://www.helius.dev/docs/laserstream/grpc#mainnet-endpoints). For high-latency connections, increase your network read buffer sizes (can improve bandwidth by 5x+):

```
sudo sysctl -w net.core.rmem_max=67108864 net.ipv4.tcp_rmem="4096 87380 67108864"

```

To persist across reboots, add to `/etc/sysctl.conf`:

```
net.core.rmem_max=67108864
net.ipv4.tcp_rmem=4096 87380 67108864

```

Increase the HTTP/2 stream window size to 64MB to prevent flow control bottlenecks:

```
// Rust (tonic)
Channel::from_static("https://laserstream-mainnet-ewr.helius-rpc.com")
initial_stream_window_size(1024 * 1024 * 64)  // 64MB window
connect()
await?;

```

  * **Client-side processing bottlenecks** : Ensure your message processing logic is optimized and doesn’t block the main thread for extended periods.

**Debugging Client Lag** : To help you debug client, we built a tool to test for the max bandwidth from your node to a Laserstream gRPC server. To use it run:

```
cargo install helius-laserstream-bandwidth
helius-laserstream-bandwidth --laserstream-url $LASERSTREAM_URL --api-key $API_KEY

```

The output returns the max network capacity between your server and the Laserstream server. At a minimum, you need 10MB/s to subscribe to all transaction data and 80MB/s to subscribe to all account data. We recommend having at least 2x the required capacity for optimal performance.
Q: I'm getting connection errors. What should I check?
**A:** Verify your API key and endpoint are correct and that your network allows outbound gRPC connections to the specified endpoint. Check the [Helius status page](https://helius.statuspage.io/) for any ongoing incidents.
Q: Why aren't my filters working as expected?
**A:** Double-check the logical operators (AND/OR) described in the filter sections. Ensure public keys are correct. Review the commitment level specified in your request.
Q: Can I subscribe to multiple types of data (e.g., accounts and transactions) in one request?
**A:** Yes, you can define filter configurations under multiple keys (e.g., `accounts`, `transactions`) within the same `SubscribeRequest` object.
Q: Does LaserStream support consumer groups?
**A:** We don’t implement consumer groups. Instead, LaserStream delivers the same outcomes teams want: resume, replay, and multi-node reliability without a coordination layer (and the latency/overhead that comes with it). We believe consumer groups are not needed for most workloads and they add latency and operational overhead. As an example a single LaserStream gRPC connection can emit up to 10× Solana’s transaction + account data, and most clients subscribe to a small, filtered slice. Using consumer groups in this case burns performance headroom and introduces another point of failure.
Q: Why am I only receiving Pong responses with no account or slot data?
**A:** Including a `ping` field in your initial `SubscribeRequest` causes LaserStream to silently ignore all subscription filters — only a Pong is returned with zero account, transaction, or slot data. To fix this, remove `ping` from the initial subscribe request and instead send pings separately via the stream’s sink after the subscription is established. This keeps the connection alive without interfering with your filters.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/laserstream)[ Historical ReplayRecover from disconnections and backfill missing Solana blockchain data with LaserStream's historical replay feature. Never miss a transaction again. Next ](https://www.helius.dev/docs/laserstream/historical-replay)
On this page
  * [Mainnet LaserStream Endpoints](https://www.helius.dev/docs/laserstream/grpc#mainnet-laserstream-endpoints)
  * [Devnet LaserStream Endpoint](https://www.helius.dev/docs/laserstream/grpc#devnet-laserstream-endpoint)
  * [Code Examples (LaserStream SDK)](https://www.helius.dev/docs/laserstream/grpc#code-examples-laserstream-sdk)


Assistant
Responses are generated using AI and may contain mistakes.
