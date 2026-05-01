# Source: https://www.helius.dev/docs/sending-transactions/optimizing-transactions

There are two primary methods for sending transactions on Solana:
  1. Using [staked connections](https://www.helius.dev/staked-connections) (default)
  2. Using specialized landing services like [Sender](https://www.helius.dev/sender) (recommended)

This article covers transaction optimization best practices for using staked connections, which is the default method for all Helius paid plans. Staked connections are most appropriate for use cases where latency is not critical to your business (e.g., payments, wallets, social apps, etc.) If you’re an advanced trader (e.g., HFT, MEV searcher, arbitrager, token sniper, etc.) looking for a specialized, ultra-low-latency transaction landing service, read our [Sender tutorial](https://www.helius.dev/docs/sending-transactions/sender).
## Summary
Helius’ staked connections guarantee 100% transaction delivery with minimal confirmation times. To optimize your transaction landing rates with staked connections, we recommend the following best practices:
  * Use commitment “confirmed” to fetch the [latest blockhash](https://www.helius.dev/docs/rpc/guides/getlatestblockhash)
  * Add [priority fees](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#setting-the-right-priority-fee) and calculate them dynamically
  * Optimize compute unit (CU) usage
  * Set `maxRetries` to 0 and implement robust retry logic
  * Send with `skipPreflight` set to `true` (optional)


Want to go deeper? We cover all fundamentals in this [blog post](https://www.helius.dev/blog/how-to-land-transactions-on-solana).
## Recommended Optimizations for Traders
For latency-sensitive trading use cases, we recommend [using Sender](https://www.helius.dev/docs/sending-transactions/sender). However, if you’re using staked connections and want to optimize your setup for the lowest latencies possible, we recommend the following optimizations (in addition to applying the best practices mentioned above):
  * Your client server (the machine you use to send transactions from) should be located in Eastern US or Western Europe.
  * Choose FRA or PIT if you want to co-locate with Helius transaction-sending servers.
  * Avoid sending from regions far from the validator network (e.g., LATAM, South Africa).
  * Warm the Helius regional caches to minimize tail latency.
  * Only one warming thread is required per region - any more will have zero benefit.
  * Send a [`getHealth`](https://www.helius.dev/docs/rpc/guides/gethealth) RPC call every second using the same endpoint and API key you use for sending transactions.

These benefits will only be noticeable to experienced traders. For general app developers, we recommend following the guidelines in the Sending Smart Transactions section below.
Get onchain transaction data as fast as possible with [Shred Delivery](https://www.helius.dev/docs/shred-delivery). [Apply for a 2-day trial](https://www.helius.dev/shreds-contact); we review every application.
## Sending Smart Transactions
Both the Helius [Node.js](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#node-js-sdk) and [Rust](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#rust-sdk) SDKs can send smart transactions. This new method builds and sends an optimized transaction while handling its confirmation status. Users can configure the transaction’s send options, such as whether the transaction should skip preflight checks. At the most basic level, users must supply their keypair and the instructions they wish to execute, and we handle the rest. We:
  * Fetch the latest blockhash
  * Build the initial transaction
  * Simulate the initial transaction to fetch the compute units (CUs) consumed
  * Set the CU limit to the CUs consumed in the previous step, with some margin
  * Get the Helius recommended priority fee via our [Priority Fee API](https://www.helius.dev/docs/priority-fee-api)
  * Set the priority fee (microlamports per CU) as the Helius recommended fee
  * Add a small buffer fee in case the recommended fee changes in the next few seconds
  * Build and send the optimized transaction
  * Return the transaction signature if successful


Requiring the recommended value (or higher) for our staked connections ensures that Helius sends high-quality transactions and that we won’t be rate-limited by validators.
This method is the easiest way to build, send, and land a transaction on Solana. By using the Helius recommended fee, transactions sent by Helius users on one of our [standard paid plans](https://www.helius.dev/docs/billing/plans) will be routed through our staked connections, guaranteeing nearly 100% transaction delivery and minimal latency.
### Node.js SDK
The `sendSmartTransaction` method is available in our [Helius Node.js SDK](https://www.helius.dev/docs/sdks) for [versions >= 1.3.2](https://www.npmjs.com/package/helius-sdk). To update to a more recent version of the SDK, run `npm update helius-sdk`. This example transfers SOL to an account of your choice. It uses `sendSmartTransaction` to send an optimized transaction that does not skip preflight checks:

```
import { Helius } from "helius-sdk";
import {
  Keypair,
  SystemProgram,
  LAMPORTS_PER_SOL,
  TransactionInstruction,
} from "@solana/web3.js";

const helius = new Helius("YOUR_API_KEY");
const fromKeypair = /* Your keypair goes here */;
const fromPubkey = fromKeypair.publicKey;
const toPubkey = /* The person we're sending 0.5 SOL to */;

const instructions: TransactionInstruction[] = [
  SystemProgram.transfer({
    fromPubkey: fromPubkey,
    toPubkey: toPubkey,
    lamports: 0.5 * LAMPORTS_PER_SOL, 
  }),


const transactionSignature = await helius.rpc.sendSmartTransaction(instructions, [fromKeypair]);
console.log(`Successful transfer: ${transactionSignature}`);

```

### Rust SDK
The `send_smart_transaction` method is available in our [Rust SDK](https://www.helius.dev/docs/sdks) for [versions >= 0.1.5](https://crates.io/crates/helius). To update to a more recent version of the SDK, run `cargo update helius`. The following example transfers 0.01 SOL to an account of your choice. It leverages `send_smart_transaction` to send an optimized transaction that skips preflight checks and retries twice, if necessary:

```
use helius::types::*;
use helius::Helius;
use solana_sdk::{
    pubkey::Pubkey,
    signature::Keypair,
    system_instruction


#[tokio::main]
async fn main() {
    let api_key:str = "YOUR_API_KEY";
    let cluster: Cluster = Cluster::MainnetBeta;
    let helius: Helius = Helius::new(api_key, cluster).unwrap();

    let from_keypair: Keypair = /* Your keypair goes here */;
    let from_pubkey: Pubkey = from_keypair.pubkey();
    let to_pubkey: Pubkey = /* The person we're sending 0.01 SOL to */;

    // Create a simple instruction (transfer 0.01 SOL from from_pubkey to to_pubkey)
    let transfer_amount = 100_000; // 0.01 SOL in lamports
    let instruction = system_instruction::transfer(from_pubkey, to_pubkey, transfer_amount);

    // Create the SmartTransactionConfig
    let config = SmartTransactionConfig {
        instructions,
        signers: vec![from_keypair],
        send_options: RpcSendTransactionConfig {
            skip_preflight: true,
            preflight_commitment: None,
            encoding: None,
            max_retries: Some(2),
            min_context_slot: None,

        lookup_tables: None,


    // Send the optimized transaction
    match helius.send_smart_transaction(config).await {
(signature) => {
            println!("Transaction sent successfully: {}", signature);

        Err(e) => {
            eprintln!("Failed to send transaction: {:?}", e);




```

## Sending Transactions Without the SDK
We recommend sending smart transactions with one of our SDKs, but the same functionality can be achieved without using one. Both the Node.js SDK and Rust SDK are open-source, so the underlying code for the send smart transaction functionality can be viewed anytime.
### Prepare and Build the Initial Transaction
First, prepare and build the initial transaction. This includes creating a new transaction with a set of instructions, adding the recent blockhash, and assigning a fee payer. For versioned transactions, create a `TransactionMessage` and compile it with lookup tables if any are present. Then, create a new versioned transaction and sign it — this is necessary for the next step when we simulate the transaction, as the transaction must be signed. For example, if we wanted to prepare a versioned transaction:

```
// Prepare your instructions and set them to an instructions variable
// The payerKey is the public key that will be paying for this transaction
// Prepare your lookup tables and set them to a lookupTables variable
let recentBlockhash = (await this.connection.getLatestBlockhash()).blockhash;
const v0Message = new TransactionMessage({
    instructions: instructions,
    payerKey: pubKey,
    recentBlockhash: recentBlockhash,
}).compileToV0Message(lookupTables);
versionedTransaction = new VersionedTransaction(v0Message);
versionedTransaction.sign([fromKeypair]);

```

### Optimize the Transaction’s Compute Unit (CU) Usage
To [optimize the transaction’s compute unit (CU) usage](https://www.helius.dev/blog/optimizing-solana-programs), we can use the `simulateTransaction` RPC method to simulate the transaction. [Simulating the transaction](https://www.helius.dev/docs/api-reference/rpc/http/simulatetransaction) will return the amount of CUs used, so we can use this value to set our compute limit accordingly. It’s recommended to use a test transaction with the desired instructions first, plus an instruction that sets the compute limit to 1.4m CUs. This is done to ensure the transaction simulation succeeds. For example:

```
const testInstructions = [
    ComputeBudgetProgram.setComputeUnitLimit({ units: 1_400_000 }),
    ...instructions,


const testTransaction = new VersionedTransaction(
    new TransactionMessage({
        instructions: testInstructions,
        payerKey: payer,
        recentBlockhash: (await this.connection.getLatestBlockhash()).blockhash,
    }).compileToV0Message(lookupTables)


const rpcResponse = await this.connection.simulateTransaction(testTransaction, {
    replaceRecentBlockhash: true,
    sigVerify: false,
});

const unitsConsumed = rpcResponse.value.unitsConsumed;

```

It is also recommended to add a bit of margin to ensure the transaction executes without any issues. We can do so by setting the following:

```
let customersCU = Math.ceil(unitsConsumed * 1.1);

```

Then, create an instruction that sets the compute unit limit to this value and add it to your array of instructions:

```
const computeUnitIx = ComputeBudgetProgram.setComputeUnitLimit({
    units: customersCU
});
instructions.push(computeUnitIx);

```

### Serialize and Encode the Transaction
This is relatively straightforward. First, to serialize the transaction, both Transaction and VersionedTransaction types have a `.serialize()` method. Then use the [bs58 package](https://www.npmjs.com/package/bs58) to encode the transaction. Your code should look something like `bs58.encode(txt.serialize());`
### Setting the Right Priority Fee
First, use the [Priority Fee API](https://www.helius.dev/docs/priority-fee-api) to get the priority fee estimate. We want to pass in our transaction and get the Helius recommended fee via the recommended parameter:

```
const response = await fetch(HeliusURL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        jsonrpc: "2.0",
        id: "1",
        method: "getPriorityFeeEstimate",
        params: [

                transaction: bs58.encode(versionedTransaction), // Pass the serialized transaction in
                options: { recommended: true },


    }),
});

const data = await response.json();
const priorityFeeRecommendation = data.result.priorityFeeEstimate;

```

Then, create an instruction that sets the compute unit price to this value, and add that instruction to your previous instructions:

```
const computeBudgetIx = ComputeBudgetProgram.setComputeUnitPrice({
    microLamports: priorityFeeRecommendation,
});

instructions.push(computeBudgetIx);

```

### Build and Send the Optimized Transaction
This step is almost a repeat of the first step. However, the array of initial instructions has been altered to add two instructions to set the compute unit limit and price optimally. Now, send the transaction. It doesn’t matter if you send with or without preflight checks or change any other send options — the transaction will be routed through our staked connections for all paid plans.
### Polling the Transaction’s Status and Rebroadcasting
While staked connections will forward a transaction directly to the leader, it is still possible for the transaction to be dropped in the [Banking Stage](https://www.helius.dev/blog/solana-virtual-machine#the-banking-stage). It is recommended that users employ their own rebroadcasting logic rather than rely on the RPC to retry the transaction for them.
The [`sendTransaction` RPC method](https://www.helius.dev/docs/api-reference/rpc/http/sendtransaction) has a `maxRetries` parameter that can be set to override the RPC’s default retry logic, giving developers more control over the retry process. It is a common pattern to fetch the current blockhash via [`getLatestBlockhash`](https://www.helius.dev/docs/rpc/guides/getlatestblockhash), store the `lastValidBlockHeight`, and retry the transaction until the blockhash expires. It is crucial to only re-sign a transaction when the blockhash is no longer valid, or else it is possible for both transactions to be accepted by the network. Once a transaction is sent, it is important to poll its confirmation status to see whether the network has processed and confirmed it before retrying. Use the [`getSignatureStatuses` RPC method](https://www.helius.dev/docs/rpc/guides/getsignaturestatuses) to check a list of transactions’ confirmation status. The @solana/web3.js SDK also has a `getSignatureStatuses` method on its `Connection` class to fetch the current status of multiple signatures.
### How sendSmartTransaction Handles Polling and Rebroadcasting
The `sendSmartTransaction` method has a timeout period of 60 seconds. Since a blockhash is valid for 150 slots, and assuming perfect 400ms slots, we can reasonably assume a transaction’s blockhash will be invalid after one minute. The method sends the transaction and polls its signature using this timeout period:

```
try {
   // Create a smart transaction
   const transaction = await this.createSmartTransaction(instructions, signers, lookupTables, sendOptions);

   const timeout = 60000;
   const startTime = Date.now();
   let txtSig;

   while (Date.now() - startTime timeout) {
     try {
       txtSig = await this.connection.sendRawTransaction(transaction.serialize(), {
         skipPreflight: sendOptions.skipPreflight,
         ...sendOptions,
       });

       return await this.pollTransactionConfirmation(txtSig);
catch (error) {
       continue;


} catch (error) {
   throw new Error(`Error sending smart transaction: ${error}`);


```

`txtSig` is set to the signature of the transaction that was just sent. The method then uses the `pollTransactionConfirmation()` method to poll the transaction’s confirmation status. This method checks a transaction’s status every five seconds for a maximum of three times. If the transaction is not confirmed during this time, an error is returned:

```
async pollTransactionConfirmation(txtSig: TransactionSignature): PromiseTransactionSignature {
    // 15 second timeout
    const timeout = 15000;
    // 5 second retry interval
    const interval = 5000;
    let elapsed = 0;

    return new PromiseTransactionSignature>((resolve, reject) => {
      const intervalId = setInterval(async () => {
        elapsed += interval;

 (elapsed >= timeout) {
          clearInterval(intervalId);
          reject(new Error(`Transaction ${txtSig}'s confirmation timed out`));


        const status = await this.connection.getSignatureStatuses([txtSig]);

 (status?.value[0]?.confirmationStatus === "confirmed") {
          clearInterval(intervalId);
          resolve(txtSig);

      }, interval);
   });


```

Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/sending-transactions/backrun-rebates)[ OverviewEstimate optimal priority fees for Solana transactions. Real-time fee analysis with six priority levels to ensure fast confirmation and cost efficiency. Next ](https://www.helius.dev/docs/priority-fee-api)
On this page
  * [Recommended Optimizations for Traders](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#recommended-optimizations-for-traders)
  * [Sending Smart Transactions](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#sending-smart-transactions)
  * [Sending Transactions Without the SDK](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#sending-transactions-without-the-sdk)
  * [Prepare and Build the Initial Transaction](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#prepare-and-build-the-initial-transaction)
  * [Optimize the Transaction’s Compute Unit (CU) Usage](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#optimize-the-transaction%E2%80%99s-compute-unit-cu-usage)
  * [Serialize and Encode the Transaction](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#serialize-and-encode-the-transaction)
  * [Setting the Right Priority Fee](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#setting-the-right-priority-fee)
  * [Build and Send the Optimized Transaction](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#build-and-send-the-optimized-transaction)
  * [Polling the Transaction’s Status and Rebroadcasting](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#polling-the-transaction%E2%80%99s-status-and-rebroadcasting)
  * [How sendSmartTransaction Handles Polling and Rebroadcasting](https://www.helius.dev/docs/sending-transactions/optimizing-transactions#how-sendsmarttransaction-handles-polling-and-rebroadcasting)


Assistant
Responses are generated using AI and may contain mistakes.
