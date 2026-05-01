# Source: https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys

**Advanced Method** : Get priority fee estimates using account keys for specialized use cases like pre-transaction analysis, batch operations, and account pattern research.
## Overview
The account keys method provides a simpler alternative to transaction serialization when you need quick fee estimates or want to estimate fees before constructing the complete transaction.
## Advanced Use Cases
  * Pre-transaction analysis
  * Batch account operations
  * Market research and patterns
  * Specialized architectures


## Trade-offs
  * Less accurate than serialized transactions
  * No instruction-specific analysis
  * Best for account-level patterns


**Recommendation** : For most applications, use the [serialized transaction method](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction) instead. This account keys method is for specialized use cases where you need account-level analysis or pre-transaction planning.
## When to Use Account Keys
  * Ideal Use Cases
  * Specialized Scenarios


## Pre-transaction Planning
Get fee estimates before constructing complete transactions
## Simplified Integration
When your architecture makes transaction serialization difficult
## Quick Market Analysis
Analyze fee patterns for specific accounts without building transactions
## Multi-account Analysis
Understand fee patterns across multiple accounts independently
**Research & Analysis**: When studying fee patterns across different accounts and programs**Batch Operations** : When analyzing fee patterns across many accounts simultaneously**Pre-planning** : For cost estimation before building complex transaction workflows**Custom Architectures** : When system constraints prevent transaction serialization
## Quick Start
Identify Accounts
Determine which accounts will be involved in your transaction
Call the API
Make a request with the account keys and desired priority level
Apply the Fee
Use the estimate to set priority fee in your transaction
### Basic Example
JavaScript
Python

```
import { ComputeBudgetProgram } from "@solana/web3.js";

// 1. Identify accounts involved in your transaction
const accountKeys = [
  "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", // Token program
  "YOUR_WALLET_ADDRESS"// Your wallet
  "RECIPIENT_ADDRESS"                             // Recipient


// 2. Get priority fee estimate
const priorityFee = await getPriorityFeeEstimate(connection, accountKeys, "Medium");

// 3. Add to your transaction
const priorityFeeIx = ComputeBudgetProgram.setComputeUnitPrice({
  microLamports: priorityFee
});
transaction.add(priorityFeeIx);

```

## Implementation Guide
### Core Function
Here’s a reusable function for getting priority fee estimates:

```
async function getPriorityFeeEstimate(connection, accountKeys, priorityLevel = "Medium") {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        accountKeys: accountKeys,
        options: { 
          priorityLevel: priorityLevel,
          recommended: true



  });

  const result = await response.json();

  if (result.error) {
    throw new Error(`Fee estimation failed: ${JSON.stringify(result.error)}`);


  return result.result.priorityFeeEstimate;


```

### Complete Example with Multiple Priority Levels
Expand to see full implementation

```
const { 
  Connection, 
  PublicKey, 
  Transaction, 
  ComputeBudgetProgram
} = require("@solana/web3.js");

// Initialize connection
const connection = new Connection("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY");

async function analyzeAccountPriorityFees() {
  // Define accounts involved in your transaction
  const accountKeys = [
    "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", // Token program
    "YOUR_WALLET_ADDRESS"// Your wallet
    "TOKEN_ACCOUNT_ADDRESS"// Token account
    "RECIPIENT_ADDRESS"                             // Recipient


  try {
    // Get estimates for different priority levels
    const [lowFee, mediumFee, highFee, veryHighFee] = await Promise.all([
      getPriorityFeeEstimate(connection, accountKeys, "Low"),
      getPriorityFeeEstimate(connection, accountKeys, "Medium"), 
      getPriorityFeeEstimate(connection, accountKeys, "High"),
      getPriorityFeeEstimate(connection, accountKeys, "VeryHigh")
    ]);

    console.log("Priority Fee Estimates:");
    console.log(`Low:      ${lowFee} micro-lamports`);
    console.log(`Medium:   ${mediumFee} micro-lamports`);
    console.log(`High:     ${highFee} micro-lamports`);
    console.log(`VeryHigh: ${veryHighFee} micro-lamports`);

    // Get all levels at once for comparison
    const allLevels = await getAllPriorityLevels(connection, accountKeys);
    console.log("\nAll priority levels:", allLevels);

    return {
      low: lowFee,
      medium: mediumFee,
      high: highFee,
      veryHigh: veryHighFee,
      allLevels

catch (error) {
    console.error("Error getting priority fees:", error);
    throw error;



// Helper function to get all priority levels
async function getAllPriorityLevels(connection, accountKeys) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        accountKeys: accountKeys,
        options: { 
          includeAllPriorityFeeLevels: true



  });

  const result = await response.json();

  if (result.error) {
    throw new Error(`Fee estimation failed: ${JSON.stringify(result.error)}`);


  return result.result.priorityFeeLevels;


// Run the analysis
analyzeAccountPriorityFees();

```

## Account Types & Strategies
  * Program Accounts
  * User Wallets
  * Token Accounts


High-volume program accounts typically show higher priority fees due to competition.

```
// Popular program accounts
const programAccounts = [
  "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", // Token program
  "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL", // Associated token program
  "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"  // Metaplex program


const programFees = await getPriorityFeeEstimate(connection, programAccounts, "Medium");
console.log(`Program account fees: ${programFees} micro-lamports`);

```

**Expected behavior** : Higher fees due to high transaction volume and competition.
Active user wallets may have different fee patterns based on their activity.

```
// Active user wallets
const userWallets = [
  "USER_WALLET_1", // Active trader
  "USER_WALLET_2"  // Regular user


const walletFees = await getPriorityFeeEstimate(connection, userWallets, "Medium");
console.log(`User wallet fees: ${walletFees} micro-lamports`);

```

**Pro tip** : Include both sender and recipient wallets for more accurate estimates.
Specific token accounts can show varying patterns based on token popularity.

```
// Popular token accounts
const tokenAccounts = [
  "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", // USDC mint
  "So11111111111111111111111111111111111111112",  // SOL mint
  "YOUR_TOKEN_ACCOUNT"                            // Your specific token account


const tokenFees = await getPriorityFeeEstimate(connection, tokenAccounts, "Medium");

```

## Advanced Configuration Options
Empty Slot Evaluation
The `evaluateEmptySlotAsZero` option is particularly useful for account-based estimates:

```
async function compareEmptySlotHandling(accountKeys) {
  const withEmptyAsZero = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        accountKeys: accountKeys,
        options: { 
          priorityLevel: "Medium",
          evaluateEmptySlotAsZero: true // Default: true



  });

  const withoutEmptyAsZero = await fetch(connection.rpcEndpoint, {
    method: "POST", 
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate", 
      params: [{
        accountKeys: accountKeys,
        options: {
          priorityLevel: "Medium",
          evaluateEmptySlotAsZero: false



  });

  const result1 = await withEmptyAsZero.json();
  const result2 = await withoutEmptyAsZero.json();

  console.log(`With empty as zero: ${result1.result.priorityFeeEstimate}`);
  console.log(`Without empty as zero: ${result2.result.priorityFeeEstimate}`);


```

When `true` (default), slots with no transactions are treated as zero fees rather than excluded. This provides more balanced estimates for accounts with sparse activity.
Include Details
Request detailed information about each account’s fee patterns:

```
async function getDetailedFeeEstimate(connection, accountKeys) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        accountKeys: accountKeys,
        options: { 
          includeDetails: true,
          priorityLevel: "Medium"



  });

  const result = await response.json();
  console.log("Detailed fee analysis:", result.result);
  return result.result;


```

This returns additional information about how fees were calculated for each account.
Custom Lookback Period
Adjust the number of slots analyzed for fee estimation:

```
async function getCustomLookbackEstimate(accountKeys, lookbackSlots = 50) {
  const response = await fetch(connection.rpcEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getPriorityFeeEstimate",
      params: [{
        accountKeys: accountKeys,
        options: { 
          priorityLevel: "Medium",
          lookbackSlots: lookbackSlots  // 1-150, default is 150



  });

  const result = await response.json();
  return result.result.priorityFeeEstimate;


// Compare different lookback periods
const shortTerm = await getCustomLookbackEstimate(accountKeys, 50);   // Recent trends
const longTerm = await getCustomLookbackEstimate(accountKeys, 150);   // Historical average

console.log(`Short-term estimate: ${shortTerm} micro-lamports`);
console.log(`Long-term estimate: ${longTerm} micro-lamports`);

```

**Smaller lookback** : More recent, potentially volatile data**Larger lookback** : More stable, historical context
## Best Practices for Account Selection
## Include Writable Accounts
**Priority** : Focus on accounts that will be modified

```
const writableAccounts = [
  "YOUR_WALLET"// Paying fees
  "TOKEN_ACCOUNT"// Being modified  
  "RECIPIENT_ACCOUNT"   // Receiving tokens


```

## Add Key Programs
**Context** : Include relevant program accounts

```
const programAccounts = [
  "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", // Token program
  "CUSTOM_PROGRAM_ID"                           // Your program


```

## Error Handling & Fallbacks
Robust Implementation
Simple Error Handling

```
class AccountBasedFeeEstimator {
  constructor(connection) {
    this.connection = connection;
    this.fallbackFee = 10000; // 10k micro-lamports fallback


  async getEstimate(accountKeys, priorityLevel = "Medium") {
    try {
      // Primary attempt
      const estimate = await this.getPrimaryEstimate(accountKeys, priorityLevel);
      return estimate;
catch (error) {
      console.warn("Primary estimate failed:", error.message);

      // Fallback to different configuration
      try {
        return await this.getFallbackEstimate(accountKeys, priorityLevel);
catch (fallbackError) {
        console.warn("Fallback estimate failed:", fallbackError.message);
        return this.fallbackFee;




  async getPrimaryEstimate(accountKeys, priorityLevel) {
    const response = await fetch(this.connection.rpcEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jsonrpc: "2.0",
        id: "1",
        method: "getPriorityFeeEstimate",
        params: [{
          accountKeys: accountKeys,
          options: { 
            priorityLevel: priorityLevel,
            recommended: true



    });

    const result = await response.json();
    if (result.error) {
      throw new Error(result.error.message);


    return result.result.priorityFeeEstimate;


  async getFallbackEstimate(accountKeys, priorityLevel) {
    // Try with fewer accounts or different settings
    const coreAccounts = accountKeys.slice(0, 3); // Take first 3 accounts

    const response = await fetch(this.connection.rpcEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jsonrpc: "2.0",
        id: "1",
        method: "getPriorityFeeEstimate",
        params: [{
          accountKeys: coreAccounts,
          options: { 
            priorityLevel: "Medium", // Use medium as fallback
            evaluateEmptySlotAsZero: true



    });

    const result = await response.json();
    if (result.error) {
      throw new Error(result.error.message);


    return result.result.priorityFeeEstimate;



// Usage
const estimator = new AccountBasedFeeEstimator(connection);
const fee = await estimator.getEstimate(accountKeys, "High");

```

## Limitations & Considerations
**Account-based method limitations:**
  1. **Less accurate for read-only accounts** - The algorithm focuses on writable accounts
  2. **No instruction-specific analysis** - Can’t consider specific operations
  3. **Account activity dependency** - Less accurate for inactive accounts
  4. **No transaction size consideration** - Doesn’t account for transaction complexity


**When to upgrade to serialized transactions:**
  * Production applications requiring highest accuracy
  * Complex transactions with multiple instructions
  * When instruction-specific fee patterns matter
  * Performance-critical applications


## Related Resources
## [Serialized Transactions More accurate method using full transaction serialization ](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction)
## [API Reference Complete API documentation and parameters ](https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/priority-fee/estimating-fees-using-serialized-transaction)[ OverviewComprehensive Solana blockchain data APIs and tools for querying, indexing, and retrieving on-chain information. DAS API, Enhanced Transactions, and more. Next ](https://www.helius.dev/docs/getting-data)
On this page
  * [When to Use Account Keys](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#when-to-use-account-keys)
  * [Complete Example with Multiple Priority Levels](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#complete-example-with-multiple-priority-levels)
  * [Account Types & Strategies](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#account-types-%26-strategies)
  * [Advanced Configuration Options](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#advanced-configuration-options)
  * [Best Practices for Account Selection](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#best-practices-for-account-selection)
  * [Error Handling & Fallbacks](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#error-handling-%26-fallbacks)
  * [Limitations & Considerations](https://www.helius.dev/docs/priority-fee/estimating-fees-using-account-keys#limitations-%26-considerations)


Assistant
Responses are generated using AI and may contain mistakes.
