# Source: https://www.helius.dev/docs/staking/how-to-stake-with-helius-programmatically

**Zero-Commission Validator** : Stake with the Helius validator and keep 100% of your staking rewards with our 0% commission rate.
## Quick Overview
The Helius SDK provides simple methods to handle the complete SOL staking lifecycle programmatically. Perfect for building staking interfaces, DeFi protocols, or automated staking strategies.
## Create & Delegate
Set up new stake accounts and delegate to validators in one transaction
## Monitor & Manage
Track rewards, check status, and manage existing stake accounts
## Withdraw & Redeem
Deactivate stakes and withdraw SOL after cooldown periods
## Installation & Setup
yarn
pnpm

```
npm install helius-sdk @solana/web3.js bs58

```

Setup

```
import { Helius } from 'helius-sdk';
import { Keypair, Transaction } from '@solana/web3.js';
import bs58 from 'bs58';

// Initialize Helius client
const helius = new Helius('YOUR_API_KEY');

// Your wallet keypair (load from your secure storage)
const payer = Keypair.fromSecretKey(/* your secret key */);

```

## Staking Basics
How Solana Staking Works
**Stake Account** : A special account that locks SOL and delegates it to a validator. Each stake account points to exactly one validator.**Rewards** : Validators earn rewards for securing the network. These rewards are distributed to all stake accounts delegated to that validator.**Lifecycle** : Create → Delegate → Earn Rewards → Deactivate → Withdraw
Why Choose Helius Validator
  * **0% Commission** : Keep 100% of your staking rewards
  * **High Performance** : Reliable block production and minimal downtime
  * **Easy Integration** : Optimized for the Helius SDK with built-in helpers


Timing & Epochs
  * **Activation** : Stakes become active at the start of the next epoch (~2 days)
  * **Deactivation** : Takes effect at the end of the current epoch
  * **Cooldown** : Deactivated stakes can be withdrawn immediately after epoch end


## Getting Started
  * Quick Start
  * Complete Example


Stake SOL in just 3 lines of code:

```
// 1. Create the staking transaction
const { serializedTx, stakeAccountPubkey } =
  await helius.rpc.createStakeTransaction(payer.publicKey, 1.5);

// 2. Sign and send
const tx = Transaction.from(bs58.decode(serializedTx));
tx.partialSign(payer);
const signature = await helius.connection.sendRawTransaction(tx.serialize());

console.log(`Staked! Transaction: ${signature}`);
console.log(`Stake Account: ${stakeAccountPubkey}`);

```

The SDK automatically handles rent calculation and stake account creation. The `1.5` parameter is the amount in SOL you want to stake.
Full staking implementation with error handling:

```
async function stakeSOL(amountInSol: number) {
  try {
    // Create staking transaction
    const { serializedTx, stakeAccountPubkey } =
      await helius.rpc.createStakeTransaction(payer.publicKey, amountInSol);

    // Deserialize and sign transaction
    const transaction = Transaction.from(bs58.decode(serializedTx));
    transaction.partialSign(payer);

    // Send transaction
    const signature = await helius.connection.sendRawTransaction(
      transaction.serialize(),

        skipPreflight: false,
        preflightCommitment: 'confirmed'



    // Wait for confirmation
    await helius.connection.confirmTransaction(signature, 'confirmed');

    return {
      signature,
      stakeAccount: stakeAccountPubkey,
      amount: amountInSol


catch (error) {
    console.error('Staking failed:', error);
    throw error;



// Usage
const result = await stakeSOL(2.5);
console.log(`Successfully staked ${result.amount} SOL`);

```

## SDK Methods Reference
createStakeTransaction(owner, amount)
Creates a complete staking transaction that can be signed and sent.**Parameters:**
  * `owner` (PublicKey): The wallet that will own the stake account
  * `amount` (number): Amount of SOL to stake

**Returns:**

```

  serializedTx: string// Base58 encoded transaction
  stakeAccountPubkey: string   // New stake account address


```

**Example:**

```
const result = await helius.rpc.createStakeTransaction(
  payer.publicKey, 
  1.5  // 1.5 SOL


```

getStakeInstructions(owner, amount)
Returns just the instructions for staking (useful for custom transaction building).**Returns:**

```

  instructions: TransactionInstruction[],
  stakeAccount: Keypair


```

**Example:**

```
const { instructions } = await helius.rpc.getStakeInstructions(
  payer.publicKey, 
  1.5


// Use with Smart Transactions
const signature = await helius.rpc.sendSmartTransaction(
  instructions, 
  [payer]


```

getHeliusStakeAccounts(wallet)
Retrieves all stake accounts delegated to the Helius validator for a wallet.**Example:**

```
const accounts = await helius.rpc.getHeliusStakeAccounts(
  payer.publicKey.toBase58()


accounts.forEach(account => {
  const delegation = account.account.data.parsed.info.stake.delegation;
  console.log(`Account: ${account.pubkey}`);
  console.log(`Stake: ${delegation.stake / LAMPORTS_PER_SOL} SOL`);
});

```

createUnstakeTransaction(owner, stakeAccount)
Creates a transaction to deactivate (begin unstaking) a stake account.**Example:**

```
const tx = await helius.rpc.createUnstakeTransaction(
  payer.publicKey,
  stakeAccountPubkey


const transaction = Transaction.from(bs58.decode(tx));
transaction.partialSign(payer);
await helius.connection.sendRawTransaction(transaction.serialize());

```

getWithdrawableAmount(stakeAccount, includeRent?)
Check how much SOL can be withdrawn from a deactivated stake account.**Parameters:**
  * `includeRent` (boolean): Whether to include rent-exempt amount

**Example:**

```
const available = await helius.rpc.getWithdrawableAmount(stakeAccountPubkey);
const total = await helius.rpc.getWithdrawableAmount(stakeAccountPubkey, true);

console.log(`Available now: ${available / LAMPORTS_PER_SOL} SOL`);
console.log(`Total balance: ${total / LAMPORTS_PER_SOL} SOL`);

```

createWithdrawTransaction(owner, stakeAccount, destination, amount)
Creates a transaction to withdraw SOL from a deactivated stake account.**Example:**

```
const tx = await helius.rpc.createWithdrawTransaction(
  payer.publicKey,
  stakeAccountPubkey,
  destinationPubkey,
  withdrawAmount  // in lamports


```

## Complete Staking Workflow
Create and Delegate

```
// Stake 2 SOL to Helius validator
const { serializedTx, stakeAccountPubkey } =
  await helius.rpc.createStakeTransaction(payer.publicKey, 2.0);

const tx = Transaction.from(bs58.decode(serializedTx));
tx.partialSign(payer);

const signature = await helius.connection.sendRawTransaction(tx.serialize());
console.log(`Stake created: ${stakeAccountPubkey}`);

```

Monitor Your Stakes

```
// Get all your Helius stake accounts
const accounts = await helius.rpc.getHeliusStakeAccounts(
  payer.publicKey.toBase58()


console.log(`You have ${accounts.length} active stake accounts`);

accounts.forEach((account, index) => {
  const info = account.account.data.parsed.info;
  const delegation = info.stake.delegation;

  console.log(`Stake ${index + 1}:`);
  console.log(`  Amount: ${delegation.stake / LAMPORTS_PER_SOL} SOL`);
  console.log(`  Activated: Epoch ${delegation.activationEpoch}`);
  console.log(`  Status: ${info.meta.lockup.unixTimestamp === 0 ? 'Active' : 'Locked'}`);
});

```

Deactivate (Start Unstaking)

```
// Begin the unstaking process
const unstakeTx = await helius.rpc.createUnstakeTransaction(
  payer.publicKey,
  stakeAccountPubkey


const tx = Transaction.from(bs58.decode(unstakeTx));
tx.partialSign(payer);

await helius.connection.sendRawTransaction(tx.serialize());
console.log('Deactivation started. Will be withdrawable next epoch.');

```

Withdraw SOL

```
// Check withdrawable amount
const withdrawable = await helius.rpc.getWithdrawableAmount(
  stakeAccountPubkey, 
  true  // include rent


if (withdrawable 0) {
  // Create withdrawal instruction
  const withdrawInstruction = helius.rpc.getWithdrawInstruction(
    payer.publicKey,
    stakeAccountPubkey,
    payer.publicKey,  // withdraw to same wallet
    withdrawable


  // Send using Smart Transactions for better reliability
  const signature = await helius.rpc.sendSmartTransaction(
withdrawInstruction], 
payer]


  console.log(`Withdrawn ${withdrawable / LAMPORTS_PER_SOL} SOL`);


```

## Advanced Patterns
  * Browser Integration
  * Batch Operations
  * Smart Transactions


For browser applications using wallet adapters:

```
// Get instructions instead of full transaction
const { instructions, stakeAccount } = await helius.rpc.getStakeInstructions(
  wallet.publicKey,
  stakeAmount


// Let the wallet handle transaction building and signing
const transaction = new Transaction().add(...instructions);

// Sign with wallet adapter
const signature = await wallet.sendTransaction(transaction, connection);

console.log(`Stake account: ${stakeAccount.publicKey.toBase58()}`);

```

Stake for multiple wallets efficiently:

```
async function batchStake(wallets: Keypair[], amount: number) {
  const promises = wallets.map(async (wallet) => {
    try {
      const { serializedTx, stakeAccountPubkey } =
        await helius.rpc.createStakeTransaction(wallet.publicKey, amount);

      const tx = Transaction.from(bs58.decode(serializedTx));
      tx.partialSign(wallet);

      return helius.connection.sendRawTransaction(tx.serialize());
catch (error) {
      console.error(`Failed to stake for ${wallet.publicKey.toBase58()}:`, error);
      return null;

  });

  const results = await Promise.allSettled(promises);
  const successful = results.filter(r => r.status === 'fulfilled').length;

  console.log(`Successfully staked for ${successful}/${wallets.length} wallets`);


```

Use Smart Transactions for better reliability and optimization:

```
// Get individual instructions
const { instructions } = await helius.rpc.getStakeInstructions(
  payer.publicKey,
  2.5


// Send with Smart Transaction features:
// - Automatic priority fee optimization
// - Retry logic with backoff
// - Better error handling
const signature = await helius.rpc.sendSmartTransaction(
  instructions,
  [payer],

    skipPreflight: false,
    maxRetries: 3



console.log(`Smart transaction sent: ${signature}`);

```

## Important Notes
**Epoch Timing** : Solana epochs last ~2 days. Stakes activate at the next epoch start, and deactivation takes effect at the current epoch end.
**Rent Considerations** : Stake accounts need rent-exempt reserves (~0.00228 SOL). Withdrawing the full balance closes the account.
**Hardware Wallets** : Users will see two signature prompts - one for the stake account (pre-signed) and one for the fee payer. Design your UX accordingly.
## Quick Reference
Need a quick reminder? Here are the essential methods:

```
// Stake SOL
await helius.rpc.createStakeTransaction(owner, amountInSol);

// Check your stakes  
await helius.rpc.getHeliusStakeAccounts(ownerAddress);

// Start unstaking
await helius.rpc.createUnstakeTransaction(owner, stakeAccount);

// Check withdrawable amount
await helius.rpc.getWithdrawableAmount(stakeAccount, includeRent);

// Withdraw SOL
helius.rpc.getWithdrawInstruction(owner, stakeAccount, destination, amount);

```

## Next Steps
## [Helius SDK Documentation Complete SDK reference with all available methods ](https://github.com/helius-labs/helius-sdk)
## [Smart Transactions Optimize your transactions with priority fees and retry logic ](https://www.helius.dev/docs/sending-transactions/optimizing-transactions)
## [Join Discord Get help from our developer community ](https://discord.com/invite/6GXdee3gBj)
## [Validator Dashboard Monitor Helius validator performance and rewards ](https://www.validators.app/validators/EKgWgpJY5BtX7TeJfhKbqcJT7gzLKFFtj7cjX1XY6CxA)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/airship/getting-started)[ Additional CreditsSet up Helius autoscaling and prepaid credits to ensure uninterrupted Solana API service. Automatic credit purchases, cost management, and seamless scaling. Next ](https://www.helius.dev/docs/billing/autoscaling)
On this page
  * [Complete Staking Workflow](https://www.helius.dev/docs/staking/how-to-stake-with-helius-programmatically#complete-staking-workflow)


Assistant
Responses are generated using AI and may contain mistakes.
