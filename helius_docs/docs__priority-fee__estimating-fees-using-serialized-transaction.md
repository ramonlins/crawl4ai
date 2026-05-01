# Source: https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction

**Most Accurate Method** : Get the highest precision priority fee estimates by analyzing your exact transaction. Recommended for production applications where accuracy matters most.
## Overview
Serialized transactions provide the most accurate fee estimates because the API can analyze the exact accounts and operations that will be performed in your transaction.
## Why Use Serialized Transactions
  * **Highest accuracy** - Analyzes exact operations
  * **Detailed analysis** - Instruction-specific patterns
  * **Realistic estimates** - Reflects actual transaction
  * **Production-ready** - Built for critical applications


## Best For
  * Production applications
  * Complex transactions
  * Critical operations
  * Maximum accuracy needed


## Advantages Over Account Keys
  * Accuracy Benefits
  * Real-World Benefits


## Instruction-Specific Analysis
The API can analyze specific operations and their historical fee patterns, not just account activity.
## Transaction Size Awareness
Considers the actual size and complexity of your transaction for more accurate estimates.
## Read-Only Account Handling
Better analysis of both writable and read-only accounts in their transaction context.
### DeFi Trading
More accurate estimates for complex swap operations
### NFT Minting
Better estimates for mint transactions with specific metadata
### Multi-instruction Transactions
Accurate fees for complex multi-step operations
### Program Interactions
Better estimates for specific program calls
## Implementation Guide
Build Your Transaction
Create your transaction with all instructions (except priority fee)
Serialize the Transaction
Convert your transaction to a serialized format
Get Fee Estimate
Call the Priority Fee API with your serialized transaction
Apply Priority Fee
Add the priority fee instruction and send your transaction
### Quick Start Example
JavaScript
Python

```
import { 
  Connection, 
  PublicKey, 
  Transaction, 
  SystemProgram, 
  ComputeBudgetProgram
} from "@solana/web3.js";
import bs58 from "bs58";

const connection = new Connection("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY");

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
const priorityFee = await getPriorityFeeEstimate(connection, serializedTx, "Medium");

// 4. Add priority fee and send
transaction.instructions = []; // Reset
transaction.add(ComputeBudgetProgram.setComputeUnitPrice({ microLamports: priorityFee }));
transaction.add(transferIx);
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.sign(senderKeypair);

```

## Core Implementation Function
Here’s a reusable function for getting priority fee estimates from serialized transactions:

```
async function getPriorityFeeEstimate(connection, serializedTransaction, priorityLevel = "Medium") {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        transaction: serializedTransaction,
        options: { 
          priorityLevel: priorityLevel,
          recommended: true



  });

  const result = await response.json();

  if (result.error) {
    throw new Error(`Fee estimation failed: ${JSON.stringify(result.error)}`);


  return result.result.priorityFeeEstimate;


```

## Complete Implementation Examples
  * Simple Transfer
  * Token Transfer
  * Complex Multi-Instruction


Expand to see complete example

```
const { 
  Connection, 
  PublicKey, 
  Transaction, 
  SystemProgram, 
  ComputeBudgetProgram, 
  sendAndConfirmTransaction,
  Keypair
} = require("@solana/web3.js");
const bs58 = require("bs58");

// Initialize connection and accounts
const connection = new Connection("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY");
const senderKeypair = Keypair.fromSecretKey(bs58.decode("YOUR_PRIVATE_KEY"));
const receiverPublicKey = new PublicKey("RECIPIENT_PUBLIC_KEY");

async function sendTransactionWithPriorityFee(amount, priorityLevel = "Medium") {
  // 1. Create transaction with transfer instruction
  const transaction = new Transaction();
  const transferIx = SystemProgram.transfer({
    fromPubkey: senderKeypair.publicKey,
    toPubkey: receiverPublicKey,
    lamports: amount,
  });
  transaction.add(transferIx);

  // 2. Set required fields for serialization
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.feePayer = senderKeypair.publicKey;

  // 3. Serialize the transaction
  const serializedTransaction = bs58.encode(transaction.serialize());

  // 4. Get priority fee estimate
  const priorityFee = await getPriorityFeeEstimate(connection, serializedTransaction, priorityLevel);
  console.log(`Estimated ${priorityLevel} priority fee: ${priorityFee} micro-lamports`);

  // 5. Reset transaction and add priority fee instruction first
  transaction.instructions = [];

  // Add priority fee instruction
  const priorityFeeIx = ComputeBudgetProgram.setComputeUnitPrice({
    microLamports: priorityFee
  });
  transaction.add(priorityFeeIx);

  // Re-add the original transfer instruction
  transaction.add(transferIx);

  // 6. Update blockhash and sign
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.sign(senderKeypair);

  // 7. Send the transaction
  try {
    const signature = await sendAndConfirmTransaction(
      connection,
      transaction,
senderKeypair],
maxRetries: 0 } // Set to 0 for staked connection usage

    console.log(`Transaction successful with signature: ${signature}`);
    return signature;
catch (error) {
    console.error("Error sending transaction:", error);
    throw error;



// Usage
sendTransactionWithPriorityFee(1000000, "High"); // Send 0.001 SOL with high priority

```

Expand to see complete example

```
const { 
  Connection, 
  PublicKey, 
  Transaction, 
  ComputeBudgetProgram,
  sendAndConfirmTransaction,
  Keypair
} = require("@solana/web3.js");
const { 
  createTransferInstruction,
  getAssociatedTokenAddress,
  TOKEN_PROGRAM_ID,
  ASSOCIATED_TOKEN_PROGRAM_ID
} = require("@solana/spl-token");
const bs58 = require("bs58");

async function sendTokenWithPriorityFee(
  connection,
  senderKeypair,
  recipientPublicKey,
  mintAddress,
  amount,
  priorityLevel = "Medium"
) {
  // 1. Get token account addresses
  const senderTokenAccount = await getAssociatedTokenAddress(
    mintAddress,
    senderKeypair.publicKey


  const recipientTokenAccount = await getAssociatedTokenAddress(
    mintAddress,
    recipientPublicKey


  // 2. Create transaction with token transfer instruction
  const transaction = new Transaction();
  const transferIx = createTransferInstruction(
    senderTokenAccount,
    recipientTokenAccount,
    senderKeypair.publicKey,
    amount,
    [],
    TOKEN_PROGRAM_ID

  transaction.add(transferIx);

  // 3. Set required fields and serialize
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.feePayer = senderKeypair.publicKey;
  const serializedTransaction = bs58.encode(transaction.serialize());

  // 4. Get priority fee estimate
  const priorityFee = await getPriorityFeeEstimate(connection, serializedTransaction, priorityLevel);
  console.log(`Token transfer priority fee: ${priorityFee} micro-lamports`);

  // 5. Reset and rebuild transaction with priority fee
  transaction.instructions = [];

  // Add priority fee instruction first
  const priorityFeeIx = ComputeBudgetProgram.setComputeUnitPrice({
    microLamports: priorityFee
  });
  transaction.add(priorityFeeIx);

  // Re-add the transfer instruction
  transaction.add(transferIx);

  // 6. Update blockhash and send
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.sign(senderKeypair);

  const signature = await sendAndConfirmTransaction(
    connection,
    transaction,
senderKeypair],
maxRetries: 0 }


  return signature;


```

Expand to see complete example

```
async function complexTransactionWithPriorityFee(connection, keypair) {
  // 1. Build complex transaction with multiple instructions
  const transaction = new Transaction();

  // Add multiple instructions
  const createAccountIx = SystemProgram.createAccount({
    fromPubkey: keypair.publicKey,
    newAccountPubkey: newAccountKeypair.publicKey,
    lamports: await connection.getMinimumBalanceForRentExemption(165),
    space: 165,
    programId: TOKEN_PROGRAM_ID,
  });

  const initializeAccountIx = createInitializeAccountInstruction(
    newAccountKeypair.publicKey,
    mintAddress,
    keypair.publicKey,
    TOKEN_PROGRAM_ID


  const transferIx = SystemProgram.transfer({
    fromPubkey: keypair.publicKey,
    toPubkey: recipientPublicKey,
    lamports: 1000000,
  });

  transaction.add(createAccountIx);
  transaction.add(initializeAccountIx);
  transaction.add(transferIx);

  // 2. Set required fields and serialize
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.feePayer = keypair.publicKey;
  const serializedTransaction = bs58.encode(transaction.serialize());

  // 3. Get priority fee estimate for complex transaction
  const priorityFee = await getPriorityFeeEstimate(connection, serializedTransaction, "High");
  console.log(`Complex transaction priority fee: ${priorityFee} micro-lamports`);

  // 4. Rebuild transaction with priority fee
  transaction.instructions = [];

  // Add priority fee instruction first
  const priorityFeeIx = ComputeBudgetProgram.setComputeUnitPrice({
    microLamports: priorityFee
  });
  transaction.add(priorityFeeIx);

  // Optional: Set compute unit limit for complex transactions
  const computeLimitIx = ComputeBudgetProgram.setComputeUnitLimit({
    units: 400000 // Adjust based on your transaction complexity
  });
  transaction.add(computeLimitIx);

  // Re-add all original instructions
  transaction.add(createAccountIx);
  transaction.add(initializeAccountIx);
  transaction.add(transferIx);

  // 5. Update blockhash and send
  transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
  transaction.sign(keypair, newAccountKeypair);

  const signature = await sendAndConfirmTransaction(
    connection,
    transaction,
keypair, newAccountKeypair],
maxRetries: 0 }


  return signature;


```

## Advanced Configuration Options
Include All Priority Levels
Get estimates for all priority levels at once:

```
async function getAllPriorityLevels(connection, serializedTransaction) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        transaction: serializedTransaction,
        options: { 
          includeAllPriorityFeeLevels: true



  });

  const result = await response.json();
  return result.result.priorityFeeLevels;


// Usage
const allLevels = await getAllPriorityLevels(connection, serializedTransaction);
console.log("All priority levels:", allLevels);

Output:

  "min": 0,
  "low": 1000, 
  "medium": 5000,
  "high": 15000,
  "veryHigh": 50000,
  "unsafeMax": 100000



```

Include Detailed Analysis
Request detailed information about the fee calculation:

```
async function getDetailedFeeAnalysis(connection, serializedTransaction) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        transaction: serializedTransaction,
        options: { 
          includeDetails: true,
          priorityLevel: "Medium"



  });

  const result = await response.json();
  console.log("Detailed analysis:", result.result);
  return result.result;


```

This provides insights into how the fee was calculated, including per-account analysis.
Custom Lookback Period
Adjust the number of slots analyzed:

```
async function getCustomLookbackEstimate(connection, serializedTransaction, lookbackSlots = 50) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        transaction: serializedTransaction,
        options: { 
          priorityLevel: "Medium",
          lookbackSlots: lookbackSlots  // 1-150, default is 150



  });

  const result = await response.json();
  return result.result.priorityFeeEstimate;


// Compare different lookback periods
const recentEstimate = await getCustomLookbackEstimate(connection, serializedTx, 30);
const longerEstimate = await getCustomLookbackEstimate(connection, serializedTx, 100);

console.log(`Recent (30 slots): ${recentEstimate} micro-lamports`);
console.log(`Longer (100 slots): ${longerEstimate} micro-lamports`);

```

## Best Practices
## Transaction Serialization
**Always serialize your actual transaction** , not a simplified version

```
// ✅ Good - serialize actual transaction
const transaction = new Transaction();
transaction.add(actualInstruction1);
transaction.add(actualInstruction2);
const serialized = bs58.encode(transaction.serialize());

```

## Instruction Order
**Include all instructions except the priority fee** in your estimation transaction

```
// ✅ Good - all business logic included
transaction.add(createAccountIx);
transaction.add(initializeIx);
transaction.add(transferIx);

// ❌ Don't include priority fee in estimation

```

## Error Handling Strategies
  * Robust Error Handling
  * Simple Error Handling



```
class SerializedTransactionFeeEstimator {
  constructor(connection) {
    this.connection = connection;
    this.fallbackFee = 10000; // 10k micro-lamports


  async getEstimate(serializedTransaction, priorityLevel = "Medium") {
    try {
      // Primary attempt with serialized transaction
      return await this.getPrimaryEstimate(serializedTransaction, priorityLevel);
catch (error) {
      console.warn("Serialized transaction estimate failed:", error.message);

      // Fallback to account-based estimation
      try {
        return await this.getFallbackEstimate(serializedTransaction, priorityLevel);
catch (fallbackError) {
        console.warn("Fallback estimate failed:", fallbackError.message);
        return this.getFallbackFee(priorityLevel);




  async getPrimaryEstimate(serializedTransaction, priorityLevel) {
    const response = await fetch(this.connection.rpcEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jsonrpc: "2.0",
        id: "1",
        method: "getPriorityFeeEstimate",
        params: [{
          transaction: serializedTransaction,
          options: { 
            priorityLevel: priorityLevel,
            recommended: true



    });

    const result = await response.json();
    if (result.error) {
      throw new Error(result.error.message);


    return result.result.priorityFeeEstimate;


  async getFallbackEstimate(serializedTransaction, priorityLevel) {
    // Extract account keys from transaction and use account-based estimation
    const transaction = Transaction.from(bs58.decode(serializedTransaction));
    const accountKeys = transaction.instructions
flatMap(ix => [ix.programId, ...ix.keys.map(k => k.pubkey)])
map(key => key.toString());

    const uniqueAccountKeys = [...new Set(accountKeys)];

    // Use account-based estimation as fallback
    const response = await fetch(this.connection.rpcEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jsonrpc: "2.0",
        id: "1",
        method: "getPriorityFeeEstimate",
        params: [{
          accountKeys: uniqueAccountKeys,
          options: { 
            priorityLevel: priorityLevel,
            recommended: true



    });

    const result = await response.json();
    if (result.error) {
      throw new Error(result.error.message);


    return result.result.priorityFeeEstimate;


  getFallbackFee(priorityLevel) {
    const fallbacks = {
      "Low": 1000,
      "Medium": 5000,
      "High": 15000,
      "VeryHigh": 50000


    return fallbacks[priorityLevel] || 5000;



// Usage
const estimator = new SerializedTransactionFeeEstimator(connection);
const fee = await estimator.getEstimate(serializedTransaction, "High");

```


```
async function safeGetPriorityFeeEstimate(connection, serializedTransaction, priorityLevel = "Medium") {
  try {
    return await getPriorityFeeEstimate(connection, serializedTransaction, priorityLevel);
catch (error) {
    console.warn(`Priority fee estimation failed: ${error.message}`);

    // Extract account keys and fall back to account-based estimation
    try {
      const transaction = Transaction.from(bs58.decode(serializedTransaction));
      const accountKeys = transaction.instructions
flatMap(ix => [ix.programId, ...ix.keys.map(k => k.pubkey)])
map(key => key.toString());

      const uniqueAccountKeys = [...new Set(accountKeys)];
      return await getAccountBasedEstimate(connection, uniqueAccountKeys, priorityLevel);
catch (fallbackError) {
      console.warn(`Fallback estimation failed: ${fallbackError.message}`);

      // Return reasonable fallback based on priority level
      const fallbacks = {
        "Low": 1000,
        "Medium": 5000,
        "High": 15000,
        "VeryHigh": 50000


      return fallbacks[priorityLevel] || 5000;




```

## Common Issues & Solutions
Transaction Serialization Errors
**Problem** : Error serializing incomplete transactions**Solution** : Always set required fields before serialization:

```
// ✅ Always set these fields
transaction.recentBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.feePayer = keypair.publicKey;

// Then serialize
const serialized = bs58.encode(transaction.serialize());

```

Stale Blockhash Issues
**Problem** : Using stale blockhash causes transaction failures**Solution** : Always get fresh blockhash before final send:

```
// Get estimate with temporary blockhash
const tempBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.recentBlockhash = tempBlockhash;
const serialized = bs58.encode(transaction.serialize());

const priorityFee = await getPriorityFeeEstimate(connection, serialized, "Medium");

// Reset and rebuild with fresh blockhash
transaction.instructions = [];
transaction.add(ComputeBudgetProgram.setComputeUnitPrice({ microLamports: priorityFee }));
transaction.add(originalInstruction);

// Get FRESH blockhash before sending
const freshBlockhash = (await connection.getLatestBlockhash()).blockhash;
transaction.recentBlockhash = freshBlockhash;

```

Large Transaction Errors
**Problem** : Transaction too large for serialization**Solution** : Use versioned transactions or break into multiple transactions:

```
import { VersionedTransaction, TransactionMessage } from "@solana/web3.js";

// For large transactions, use versioned transactions
const messageV0 = new TransactionMessage({
  payerKey: keypair.publicKey,
  recentBlockhash: (await connection.getLatestBlockhash()).blockhash,
  instructions: [instruction1, instruction2, instruction3] // Many instructions
}).compileToV0Message();

const versionedTransaction = new VersionedTransaction(messageV0);
const serialized = bs58.encode(versionedTransaction.serialize());

```

## When to Use vs Account Keys
## Use Serialized Transactions
**Production applications**
  * Maximum accuracy required
  * Complex multi-instruction transactions
  * Critical operations
  * Performance-sensitive applications

**Development scenarios**
  * Final integration testing
  * Performance optimization
  * Production deployment


## Use Account Keys
**Development & prototyping**
  * Quick estimates during development
  * Simple transactions
  * Pre-transaction planning
  * Architecture constraints preventing serialization

**Analysis scenarios**
  * Account-level fee pattern analysis
  * Batch account analysis
  * Quick market research


## Related Resources
## [Account Keys Method Advanced method using account keys for specialized use cases ](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys)
## [API Reference Complete API documentation and parameters ](https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/priority-fee-api)[ Using Account KeysEstimate Solana priority fees using account keys with the Helius Priority Fee API. Quick fee estimates for pre-transaction analysis and batch operations. Next ](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys)
On this page
  * [Advantages Over Account Keys](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#advantages-over-account-keys)
  * [Core Implementation Function](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#core-implementation-function)
  * [Complete Implementation Examples](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#complete-implementation-examples)
  * [Advanced Configuration Options](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#advanced-configuration-options)
  * [Error Handling Strategies](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#error-handling-strategies)
  * [Common Issues & Solutions](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#common-issues-%26-solutions)
  * [When to Use vs Account Keys](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction#when-to-use-vs-account-keys)


Assistant
Responses are generated using AI and may contain mistakes.
