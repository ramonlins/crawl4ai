# Source: https://www.helius.dev/docs/laserstream/clients

[Skip to main content](https://www.helius.dev/docs/laserstream/clients#content-area)
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
LaserStream Clients
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
##  Automatic Replay on Disconnect
LaserStream clients continuously track your streaming position by slot number. If a disconnection occurs - from network issues, server maintenance, or any other cause - the client automatically reconnects and resumes streaming from your last processed slot. You never lose data, never miss transactions, and never need to write reconnection logic.
##  JavaScript/TypeScript Client
**We highly recommend switching to LaserStream SDK for JavaScript apps.** If you’re currently using Yellowstone gRPC clients, you will experience progressive stream delays and performance bottlenecks that compound over time. LaserStream client’s performance headroom ensures your app scales with the network and eliminates these issues entirely.
The [JavaScript client](https://github.com/helius-labs/laserstream-sdk/tree/main/javascript) uses native Rust bindings to achieve 1.3GB/s throughput – over 40x faster than Yellowstone gRPC JavaScript clients that max out at 30MB/s. **4x faster event detection** : Thanks to its Rust-based architecture, the LaserStream JavaScript client receives and processes events 4x faster than Yellowstone clients, giving your application a significant competitive advantage in seeing events first. On high-bandwidth subscriptions, Yellowstone clients experience progressive delays that compound over time. LaserStream maintains consistent, low-latency streaming regardless of data volume.
###  Installation
yarn
pnpm

```
npm install helius-laserstream

```

Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
###  Quick Start

```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream';

async function streamTransactions() {
  const config: LaserstreamConfig = {
    apiKey: 'YOUR_API_KEY',
    endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com',


  const request: SubscribeRequest = {
    transactions: {
      "jupiter-filter": { // user-defined label for this filter
        accountInclude: ['JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4'], // Jupiter Program
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
    accountsDataSlice: []


  // The SDK handles reconnection and replay automatically
  await subscribe(config, request, 
    async (data) => {
      console.log('New transaction:', data);

    async (error) => {
      console.error('Error:', error);




streamTransactions().catch(console.error);

```

###  Reliability Comparison  
| Feature  | LaserStream  | Yellowstone  |  
| --- | --- | --- |  
| Automatic Replay  | ✅ Built-in  | ❌ Manual implementation required  |  
| Progressive Delays  | ❌ None  | ✅ On high bandwidth  |  
| Data Loss Protection  | ✅ Automatic  | ❌ Application responsibility  |  
| Reconnection  | ✅ Seamless  | ❌ No built-in support  |  
##  Rust Client
The [Rust client](https://github.com/helius-labs/laserstream-sdk/tree/main/rust) provides zero-copy deserialization and native performance for applications requiring maximum control.
###  Installation

```
[dependencies]
helius-laserstream = "0.1"
tokio = { version = "1", features = ["full"] }

```

###  Quick Start

```
use helius_laserstream::{subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest};
use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Boxdyn std::error::Error>> {
    let config = LaserstreamConfig {
        api_key: "YOUR_API_KEY".to_string(),
        endpoint: "https://laserstream-mainnet-ewr.helius-rpc.com".to_string(),


    let request = SubscribeRequest {
        transactions: Some(TransactionsFilter {
            client: Some(TransactionFilter {
                account_include: vec!["JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4".to_string()],
                vote: false,
                failed: false,
Default::default()


        commitment: CommitmentLevel::Confirmed,
Default::default()


    let mut stream = subscribe(config, request).await?;

    while let Some(result) = stream.next().await {
        match result {
(data) => println!("New transaction: {:?}", data),
            Err(e) => eprintln!("Error: {:?}", e),



    Ok(())


```

##  Go Client
The [Go client](https://github.com/helius-labs/laserstream-sdk/tree/main/go) provides idiomatic Go interfaces.
###  Installation

```
go get github.com/helius-labs/laserstream-sdk/go

```

###  Quick Start

```
package main

import (
context"
fmt"
log"

    laserstream "github.com/helius-labs/laserstream-sdk/go"


func main() {
    config :=laserstream.Config{
        APIKey"YOUR_API_KEY",
        Endpoint: "https://laserstream-mainnet-ewr.helius-rpc.com",


    request :=laserstream.SubscribeRequest{
        Transactions: laserstream.TransactionsFilter{
            Client: laserstream.TransactionFilter{
                AccountInclude: []string{"JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4"},
                Votefalse,
                Failedfalse,


        Commitment: laserstream.CommitmentConfirmed,


    ctx := context.Background()
    stream, err := laserstream.Subscribe(ctx, config, request)
    if err != nil {
        log.Fatal(err)


    for data := range stream {
 data.Error != nil {
            log.Printf("Error: %v", data.Error)
            continue

        fmt.Printf("New transaction: %+v\n", data)



```

##  Why Migrate from Yellowstone to LaserStream
Yellowstone clients face critical limitations that will only worsen as Solana scales:
  1. **Performance Bottleneck** : Yellowstone JavaScript clients max out at 30MB/s – insufficient for high-throughput applications
  2. **Progressive Delays** : Latency compounds over time on high-bandwidth subscriptions
  3. **Manual Replay** : You must implement your own reconnection and replay logic
  4. **Data Loss Risk** : Without built-in replay, network disruptions mean missed transactions

**LaserStream solves these problems today**. With 40x better performance, automatic replay, and zero data loss guarantees, migrating to LaserStream ensures your application remains competitive as Solana evolves.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/laserstream/preprocessed-transactions)[ Delivery GuaranteesUnderstand LaserStream's delivery guarantees, including exactly-once delivery, message ordering, slot notification behavior, and fork handling. Next ](https://www.helius.dev/docs/laserstream/delivery-guarantees)
Ctrl+I
On this page
  * [Automatic Replay on Disconnect](https://www.helius.dev/docs/laserstream/clients#automatic-replay-on-disconnect)
  * [JavaScript/TypeScript Client](https://www.helius.dev/docs/laserstream/clients#javascript%2Ftypescript-client)
  * [Reliability Comparison](https://www.helius.dev/docs/laserstream/clients#reliability-comparison)
  * [Why Migrate from Yellowstone to LaserStream](https://www.helius.dev/docs/laserstream/clients#why-migrate-from-yellowstone-to-laserstream)


Assistant
Responses are generated using AI and may contain mistakes.
