# Source: https://www.helius.dev/docs/laserstream/preprocessed-transactions

[Skip to main content](https://www.helius.dev/docs/laserstream/preprocessed-transactions#content-area)
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
    * [Preprocessed Transactions (Public Beta)](https://www.helius.dev/docs/laserstream/preprocessed-transactions)
    * [LaserStream vs Dedicated Nodes](https://www.helius.dev/docs/laserstream/laserstream-vs-dedicated-nodes)
    * LaserStream Guides
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
LaserStream
Preprocessed Transactions (Public Beta)
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
**Public Beta.** Preprocessed transactions are available to any **Professional plan or higher** subscriber and are metered at **20 credits per 1 MB** (the standard LaserStream rate).On average, preprocessed transactions arrive **~8 ms faster than the processed commitment level** , at the cost of execution metadata (see [tradeoffs](https://www.helius.dev/docs/laserstream/preprocessed-transactions#what-data-is-available) below).
Preprocessed transactions are the fastest way to receive Solana transactions. Instead of waiting for full transaction processing, LaserStream decodes transactions directly from shreds as they arrive at the validator, giving you access to transaction data milliseconds earlier than standard subscriptions — roughly **8 ms ahead of the processed commitment level on average**. This guide explains when to use preprocessed transactions, what data is available, and how to implement them across all LaserStream SDKs.
##  What are preprocessed transactions?
In Solana’s architecture, transactions flow through several stages before becoming fully processed:
  1. **Shred Reception** → Validator receives transaction shreds (data fragments)
  2. **Shred Decoding** → Shreds are decoded into raw transactions ← **Preprocessed transactions available here**
  3. **Transaction Execution** → Transaction is executed by the runtime
  4. **Metadata Generation** → Pre/post balances, logs, and error information are computed
  5. **Commitment** → Transaction reaches processed/confirmed/finalized state

Standard transaction subscriptions deliver data at stage 5 - after full execution and metadata generation. Preprocessed subscriptions deliver at stage 2 - immediately after decoding shreds, before execution completes. **The tradeoff:** You receive transaction data milliseconds earlier, but without execution metadata like balance changes, logs, or error information.
Need raw Solana shreds? Try [Helius Shred Delivery](https://www.helius.dev/docs/shred-delivery) and [apply for a 2-day trial](https://www.helius.dev/shreds-contact).
##  Best-effort Delivery Guarantees
Preprocessed transaction delivery is best-effort, not guaranteed. We target 99.99% delivery rate, but some transactions may be lost during:
  * Infrastructure updates and redeployments
  * Network issues or validator connectivity problems
  * Edge cases in shred decoding or processing

For critical applications requiring guaranteed delivery, use standard [transaction subscriptions](https://www.helius.dev/docs/laserstream/guides/decoding-transaction-data) instead.
##  What data is available?
Preprocessed transactions include the complete transaction message but lack execution metadata:
###  Available Data
  * ✅ **Transaction signature** - Unique transaction identifier
  * ✅ **Account keys** - All accounts referenced by the transaction
  * ✅ **Instructions** - Complete instruction data and program calls
  * ✅ **Recent blockhash** - Transaction expiration reference
  * ✅ **Signatures** - All transaction signatures
  * ✅ **Is vote transaction** - Whether this is a vote transaction
  * ✅ **Slot number** - Which slot contained this transaction


###  Missing Data
  * ❌ **Transaction metadata** - Token balances changes, pre/post balances, transaction status
  * ❌ **Transaction errors** - We cannot determine if the transaction failed
  * ❌ **Inner instructions** - Cross-program invocations (CPIs) are not included
  * ❌ **Log messages** - Program logs are generated during execution
  * ❌ **Compute units consumed** - Execution metrics unavailable

Think of preprocessed transactions as receiving the “proposal” without the “result.” You see what the user tried to do, but not what actually happened.
##  SDK Support and Version Requirements
Preprocessed transaction subscriptions are supported across all LaserStream SDKs:
## [JavaScript/TypeScript Version **0.2.8** or later ](https://github.com/helius-labs/laserstream-sdk/tree/main/javascript)
## [Rust Version **0.1.5** or later ](https://github.com/helius-labs/laserstream-sdk/tree/main/rust)
## [Go Version **0.1.0** or later ](https://github.com/helius-labs/laserstream-sdk/tree/main/go)
##  Implementation Examples
###  JavaScript/TypeScript
The JavaScript SDK provides a dedicated `subscribePreprocessed` function with automatic reconnection:

```
import {
  subscribePreprocessed,
  CommitmentLevel,
  LaserstreamConfig,
  SubscribePreprocessedRequest,
  SubscribePreprocessedUpdate
} from 'helius-laserstream';
import bs58 from 'bs58';

async function streamPreprocessedTransactions() {
  const config: LaserstreamConfig = {
    apiKey: 'YOUR_API_KEY',
    endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com',


  const request: SubscribePreprocessedRequest = {
    transactions: {
      "jupiter-swaps": {
        vote: false,
        accountInclude: ['JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4']




  const stream = await subscribePreprocessed(
    config,
    request,
    async (update: SubscribePreprocessedUpdate) => {
      if (update.transaction) {
        const tx = update.transaction;
        const signature = bs58.encode(tx.transaction.signature);

        console.log('⚡ Preprocessed transaction received:');
        console.log(`  Signature: ${signature}`);
        console.log(`  Slot: ${tx.slot}`);
        console.log(`  Is Vote: ${tx.transaction.isVote}`);
        console.log(`  Filters: ${update.filters.join(', ')}`);
        console.log('---');


    async (error) => {
      console.error('Stream error:', error);



  console.log(`✅ Preprocessed stream started (id: ${stream.id})`);

  // Graceful shutdown
  process.on('SIGINT', () => {
    console.log('\n🛑 Shutting down stream...');
    stream.cancel();
    process.exit(0);
  });


streamPreprocessedTransactions().catch(console.error);

```

**Full example:** [preprocessed-transaction-sub.ts](https://github.com/helius-labs/laserstream-sdk/blob/main/javascript/examples/preprocessed-transaction-sub.ts)
###  Rust
The Rust SDK provides native performance:

```
use futures::StreamExt;
use helius_laserstream::{
    grpc::{SubscribePreprocessedRequest, SubscribePreprocessedRequestFilterTransactions},
    subscribe_preprocessed, LaserstreamConfig,


#[tokio::main]
async fn main() -> Result<(), Boxdyn std::error::Error>> {
    let config = LaserstreamConfig {
        endpoint: "https://laserstream-mainnet-ewr.helius-rpc.com".to_string(),
        api_key: "YOUR_API_KEY".to_string(),
Default::default()


    let mut request = SubscribePreprocessedRequest::default();
    request.transactions.insert(
        "jupiter-swaps".to_string(),
        SubscribePreprocessedRequestFilterTransactions {
            vote: Some(false),
            account_include: vec![
                "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4".to_string()

Default::default()



    let (stream, _handle) = subscribe_preprocessed(config, request);
    tokio::pin!(stream);

    println!("✅ Preprocessed stream started");

    while let Some(result) = stream.next().await {
        match result {
(update) => {
 let Some(tx) = update.transaction {
                    println!("⚡ Preprocessed transaction:");
                    println!("  Slot: {}", tx.slot);
                    println!("  Is Vote: {}", tx.transaction.is_vote);
                    println!("---");


            Err(e) => {
                eprintln!("Stream error: {:?}", e);
                break;




    Ok(())


```

**Full example:** [preprocessed_transaction_sub.rs](https://github.com/helius-labs/laserstream-sdk/blob/main/rust/examples/preprocessed_transaction_sub.rs)
###  Go
The Go SDK provides idiomatic Go interfaces:

```
package main

import (
log"
os"
os/signal"
syscall"

    laserstream "github.com/helius-labs/laserstream-sdk/go"
    pb "github.com/helius-labs/laserstream-sdk/go/proto"


func main() {
    log.SetFlags(0)

    clientConfig := laserstream.LaserstreamConfig{
        Endpoint: "https://laserstream-mainnet-ewr.helius-rpc.com",
        APIKey"YOUR_API_KEY",


    voteFilter := false
    subscriptionRequest :=pb.SubscribePreprocessedRequest{
        Transactions: map[string]*pb.SubscribePreprocessedRequestFilterTransactions{
            "jupiter-swaps": {
                Vote: voteFilter,
                AccountInclude: []string{
                    "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4",





    client := laserstream.NewPreprocessedClient(clientConfig)

    dataCallback := func(data *pb.SubscribePreprocessedUpdate) {
 data.Transaction != nil {
            log.Println("⚡ Preprocessed transaction:")
            log.Printf("  Slot: %d\n", data.Transaction.Slot)
            log.Printf("  Is Vote: %t\n", data.Transaction.Transaction.IsVote)
            log.Println("---")



    errorCallback := func(err error) {
        log.Printf("Error: %v", err)


    err := client.Subscribe(subscriptionRequest, dataCallback, errorCallback)
    if err != nil {
        log.Fatalf("Failed to subscribe: %v", err)


    log.Println("✅ Preprocessed stream started")
    log.Println("Press Ctrl+C to exit")

    sigChan := make(chan os.Signal, 1)
    signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)
    <-sigChan

    log.Println("\nShutting down...")
    client.Close()


```

**Full example:** [preprocessed-transaction-sub.go](https://github.com/helius-labs/laserstream-sdk/blob/main/go/examples/preprocessed-transaction-sub.go)
##  Subscription Structure and Filtering
###  Request Structure
The preprocessed subscription request follows a similar structure to standard subscriptions but with a focused set of filters:

```
interface SubscribePreprocessedRequest {
  transactions: {
filterName: string]: SubscribePreprocessedRequestFilterTransactions

  ping?: SubscribeRequestPing;


interface SubscribePreprocessedRequestFilterTransactions {
  vote?: boolean// Include/exclude vote transactions
  signature?: string// Filter by specific transaction signature
  accountInclude?: string[];   // Include transactions touching these accounts
  accountExclude?: string[];   // Exclude transactions touching these accounts
  accountRequired?: string[];  // Require all these accounts to be present


```

###  Response Structure
Updates arrive with the complete transaction message and basic metadata:

```
interface SubscribePreprocessedUpdate {
  filters: string// Which filters matched
  transaction?: SubscribePreprocessedTransaction; // The transaction data
  ping?: SubscribeUpdatePing// Keepalive ping
  pong?: SubscribeUpdatePong// Ping response
  createdAt: Date// When update was created


interface SubscribePreprocessedTransaction {
  transaction: SubscribePreprocessedTransactionInfo;
  slot: number// Slot containing transaction


interface SubscribePreprocessedTransactionInfo {
  signature: Uint8Array// Transaction signature
  isVote: boolean// Is this a vote transaction
  transaction: solana.storage.Transaction// Full transaction message


```

The `transaction.transaction` field contains the complete Solana transaction structure including:
  * **Message** - Account keys, instructions, recent blockhash
  * **Signatures** - All transaction signatures
  * **Address table lookups** - For versioned transactions

This is identical to the transaction structure in standard subscriptions, but without the `meta` field containing execution results.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/laserstream/historical-replay)[ ClientsHigh-performance SDKs for gRPC streaming with automatic replay and zero data loss Next ](https://www.helius.dev/docs/laserstream/clients)
Ctrl+I
On this page
  * [What are preprocessed transactions?](https://www.helius.dev/docs/laserstream/preprocessed-transactions#what-are-preprocessed-transactions)
  * [Best-effort Delivery Guarantees](https://www.helius.dev/docs/laserstream/preprocessed-transactions#best-effort-delivery-guarantees)
  * [What data is available?](https://www.helius.dev/docs/laserstream/preprocessed-transactions#what-data-is-available)
  * [SDK Support and Version Requirements](https://www.helius.dev/docs/laserstream/preprocessed-transactions#sdk-support-and-version-requirements)
  * [Implementation Examples](https://www.helius.dev/docs/laserstream/preprocessed-transactions#implementation-examples)
  * [Subscription Structure and Filtering](https://www.helius.dev/docs/laserstream/preprocessed-transactions#subscription-structure-and-filtering)


Assistant
Responses are generated using AI and may contain mistakes.
