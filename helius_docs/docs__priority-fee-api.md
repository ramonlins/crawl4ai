# Source: https://www.helius.dev/docs/priority-fee-api

**Save money, improve performance** : Get precise priority fee estimates based on real-time network conditions. Pay only what you need for the speed you want.
## What Are Priority Fees?
On Solana, priority fees allow your transactions to jump ahead in the validator queue during network congestion. Think of them as express lanes for your transactions.
## Base Fees vs Priority Fees
**Base fees** are fixed costs for transaction processing**Priority fees** are optional payments for faster processing
## How They Work
You set a price per compute unit - higher prices get processed first during network congestion
## Why Use Priority Fees
Priority fees are now a standard part of Solana transactions, helping ensure reliable confirmation times and optimal network performance.
## Reliable Confirmation
Ensure your transactions confirm quickly and reliably, even during varying network conditions
## Competitive Edge
Stay competitive in time-sensitive operations like trading, minting, and DeFi interactions
## User Experience
Provide consistent, fast transaction processing for better user experience
## Network Efficiency
Help optimize network resource allocation and overall performance
## Priority Levels Explained
Our API provides six priority levels based on recent network activity:
**Lowest observed fee** - Based on minimum fees seen in recent slots**Best for** : Non-urgent transactions when cost optimization is priority**Note** : May result in slower confirmation times
**25th percentile** - Budget-friendly option with reasonable confirmation times**Best for** : Standard operations where speed isn’t critical**Note** : Good balance of cost and reliability
Medium (Recommended)
**50th percentile** - Median fee providing reliable confirmation times**Best for** : Most applications and general use cases**Note** : Recommended starting point for most developers
High
**75th percentile** - Higher fees for faster processing**Best for** : Time-sensitive operations and competitive scenarios**Note** : Prioritized processing during network activity
VeryHigh
**95th percentile** - Premium fees for maximum speed**Best for** : Critical operations, MEV strategies, urgent transactions**Note** : Fast confirmation even during high network activity
UnsafeMax
**Maximum observed** - Highest fees seen in recent slots**Best for** : Emergency situations only**Warning** : Often unnecessarily high - use with caution
**Cost Calculation** : Total priority fee = Price per compute unit × Compute units consumedA typical transaction uses 200,000-400,000 compute units. At current Medium level (~40,000 microlamports per unit), that’s 0.000008-0.000016 SOL in priority fees. Always check current network conditions for accurate estimates.
## Implementation Methods
## [Serialized Transaction (Recommended) **Primary Method** - Analyzes your exact transaction for maximum accuracy**Best for** : Most applications and production use cases**Benefits** :
  * Instruction-specific analysis
  * Highest accuracy
  * Production-ready
  * Considers transaction complexity

](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction)
## [Account Keys (Advanced) **Specialized Use Cases** - Estimates based on account patterns**Best for** : Pre-transaction analysis, batch operations, specialized architectures**Benefits** :
  * Account-level pattern analysis
  * Useful for planning and research
  * Batch account analysis

](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys)
## Quick Start Example
JavaScript
Python
cURL

```
import { Transaction, SystemProgram, ComputeBudgetProgram } from "@solana/web3.js";
import bs58 from "bs58";

// 1. Build your transaction (without priority fee)
const transaction = new Transaction();
const transferIx = SystemProgram.transfer({
  fromPubkey: senderKeypair.publicKey,
  toPubkey: recipientPublicKey,
  lamports: 1000000, // 0.001 SOL
});
transaction.add(transferIx);

// 2. Set required fields and serialize
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.feePayer = senderKeypair.publicKey;
const serializedTx = bs58.encode(transaction.serialize());

// 3. Get priority fee estimate
const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    jsonrpc: "2.0",
    id: "1",
    method: "getPriorityFeeEstimate",
    params: [{
      transaction: serializedTx,
      options: { 
        priorityLevel: "Medium",
        recommended: true



});

const result = await response.json();
const priorityFee = result.result.priorityFeeEstimate;

// 4. Add priority fee and send
transaction.instructions = []; // Reset
transaction.add(ComputeBudgetProgram.setComputeUnitPrice({ microLamports: priorityFee }));
transaction.add(transferIx);
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.sign(senderKeypair);

```

## API Reference
## [getPriorityFeeEstimate Complete API documentation with all parameters and response formats ](https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate)
## Real-Time Network Monitoring
**Pro tip** : Monitor network conditions to optimize your priority fee strategy. During normal conditions, use lower priority levels. During congestion, consider higher levels for time-sensitive operations.You can check current network conditions using Solana explorers or the `getRecentPerformanceSamples` RPC method.
## Support & Resources
## [Discord Community Get help from the community and Helius team ](https://discord.com/invite/6GXdee3gBj)
## [Direct Support Priority fee questions and optimization assistance ](https://www.helius.dev/docs/support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/sending-transactions/optimizing-transactions)[ Using Serialized TransactionGet the most accurate Solana priority fee estimates using serialized transactions with the Helius Priority Fee API. Perfect for production applications. Next ](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction)
On this page
  * [What Are Priority Fees?](https://www.helius.dev/docs/priority-fee-api#what-are-priority-fees)
  * [Priority Levels Explained](https://www.helius.dev/docs/priority-fee-api#priority-levels-explained)
  * [Real-Time Network Monitoring](https://www.helius.dev/docs/priority-fee-api#real-time-network-monitoring)


Assistant
Responses are generated using AI and may contain mistakes.
