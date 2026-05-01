# Source: https://www.helius.dev/docs/wallet-api/history

**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
## Overview
The Transaction History endpoint retrieves the complete transaction history for a Solana wallet using the Enhanced Transactions API. Returns human-readable, parsed transactions with balance changes for each transaction. **Pagination is manual** - the API returns up to 100 transactions per request. Returns transactions in reverse chronological order (newest first). **Associated Token Accounts (ATAs):** The `tokenAccounts` parameter controls whether transactions involving token accounts owned by the wallet are included:
  * `balanceChanged` (recommended): Includes transactions that changed token account balances, filtering spam
  * `none`: Only direct wallet interactions
  * `all`: All token account transactions including spam


**Limitation for Legacy Transactions** : The `tokenAccounts` filter relies on the `owner` field in token balance metadata, which was not available before slot 111,491,819 (~December 2022). Transactions involving token accounts active before this slot may be missing. See the [getTransactionsForAddress tutorial](https://www.helius.dev/docs/rpc/gettransactionsforaddress#workaround-historical-token-account-discovery) for a workaround.
**Pagination:** Use the `before` parameter with `pagination.nextCursor` to fetch the next page. The response includes `pagination.hasMore` to indicate if more results are available. Each request makes a single API call and costs 100 credits.
## [API Reference View detailed API documentation for transaction history ](https://www.helius.dev/docs/api-reference/wallet-api/history)
## When to Use This
Use the Transaction History API when you need to:
  * **Display Transaction Feed** : Show users their complete transaction history
  * **Calculate P &L**: Track gains and losses across all transactions
  * **Tax & Accounting**: Generate complete transaction reports for tax filing
  * **Portfolio Analytics** : Analyze trading patterns and activity
  * **Audit Trails** : Maintain complete records of wallet activity
  * **Balance Reconstruction** : Rebuild current balances from historical data


## Quickstart
### Basic History Query
Get the most recent transactions with balance changes:
  * JavaScript
  * Python
  * cURL



```
const getTransactionHistory = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY`;

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);


  const data = await response.json();

  console.log(`Found ${data.data.length} transactions`);

  // Display recent transactions
  data.data.forEach(tx => {
    const date = new Date(tx.timestamp * 1000).toLocaleString();
    const status = tx.error ? 'Failed' : 'Success';

    console.log(`\n${status} - ${date}`);
    console.log(`Signature: ${tx.signature.slice(0, 20)}...`);
    console.log(`Fee: ${tx.fee} SOL`);

    // Show balance changes
    tx.balanceChanges.forEach(change => {
      const sign = change.amount 0 ? '+' : '';
      console.log(`  ${sign}${change.amount} ${change.mint === 'SOL' ? 'SOL' : change.mint.slice(0, 8)}...`);
    });
  });

  return data;


getTransactionHistory("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
import requests
from datetime import datetime

def get_transaction_history(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/history"
    headers = {"X-Api-Key": "YOUR_API_KEY"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    print(f"Found {len(data['data'])} transactions")

    # Display recent transactions
    for tx in data['data']:
        date = datetime.fromtimestamp(tx['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        status = 'Failed' if tx.get('error') else 'Success'

        print(f"\n{status} - {date}")
        print(f"Signature: {tx['signature'][:20]}...")
        print(f"Fee: {tx['fee']} SOL")

        # Show balance changes
        for change in tx['balanceChanges']:
            sign = '+' if change['amount']  0 else ''
            mint_display = 'SOL' if change['mint'] == 'SOL' else change['mint'][:8] + '...'
            print(f"  {sign}{change['amount']} {mint_display}")

    return data

get_transaction_history("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```


```
curl "https://api.helius.xyz/v1/wallet/86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY/history?api-key=YOUR_API_KEY"

```

### Pagination for Complete History
Fetch all transactions using pagination with the `before` parameter:
  * JavaScript
  * Python



```
const getAllTransactionHistory = async (address) => {
  let allTransactions = [];
  let before = null;


    const url = before
 `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY&before=${before}`
 `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY`;

    const response = await fetch(url);
    const data = await response.json();

    allTransactions = allTransactions.concat(data.data);
    before = data.pagination.hasMore ? data.pagination.nextCursor : null;

    console.log(`Fetched ${allTransactions.length} transactions so far...`);

while (before);

  console.log(`\nTotal transactions: ${allTransactions.length}`);
  return allTransactions;


getAllTransactionHistory("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
def get_all_transaction_history(address: str):
    all_transactions = []
    before = None

    while True:
        url = f"https://api.helius.xyz/v1/wallet/{address}/history"
        params = {"api-key": "YOUR_API_KEY"}

 before:
            params["before"] = before

        response = requests.get(url, params=params, headers={"X-Api-Key": "YOUR_API_KEY"})
        response.raise_for_status()

        data = response.json()
        all_transactions.extend(data['data'])

        print(f"Fetched {len(all_transactions)} transactions so far...")

 not data['pagination']['hasMore']:
            break

        before = data['pagination']['nextCursor']

    print(f"\nTotal transactions: {len(all_transactions)}")
    return all_transactions

get_all_transaction_history("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```

## Query Parameters  
| Parameter  | Type  | Default  | Description  |  
| --- | --- | --- | --- |  
| `limit`  | integer  | 100  | Maximum number of transactions per request (1-100)  |  
| `before`  | string  | -  | Fetch transactions before this signature (use `pagination.nextCursor` from previous response)  |  
| `after`  | string  | -  | Fetch transactions after this signature (for ascending order pagination)  |  
| `type`  | string  | -  | Filter by transaction type (e.g., SWAP, TRANSFER, NFT_SALE, TOKEN_MINT)  |  
| `tokenAccounts`  | string  | balanceChanged  | Filter transactions involving token accounts: `none`, `balanceChanged` (recommended), or `all`  |  
### Available Transaction Types
The `type` parameter supports filtering by these transaction types: `SWAP`, `TRANSFER`, `NFT_SALE`, `NFT_BID`, `NFT_LISTING`, `NFT_MINT`, `NFT_CANCEL_LISTING`, `TOKEN_MINT`, `BURN`, `COMPRESSED_NFT_MINT`, `COMPRESSED_NFT_TRANSFER`, `COMPRESSED_NFT_BURN`, `CREATE_STORE`, `WHITELIST_CREATOR`, `ADD_TO_WHITELIST`, `REMOVE_FROM_WHITELIST`, `AUCTION_MANAGER_CLAIM_BID`, `EMPTY_PAYMENT_ACCOUNT`, `UPDATE_PRIMARY_SALE_METADATA`, `ADD_TOKEN_TO_VAULT`, `ACTIVATE_VAULT`, `INIT_VAULT`, `INIT_BANK`, `INIT_STAKE`, `MERGE_STAKE`, `SPLIT_STAKE`, `CREATE_AUCTION_MANAGER`, `START_AUCTION`, `CREATE_AUCTION_MANAGER_V2`, `UPDATE_EXTERNAL_PRICE_ACCOUNT`, `EXECUTE_TRANSACTION`
### Filter Examples
  * Filter by Type
  * Token Accounts Filter
  * Combined Filters



```
// Get only SWAP transactions
const url = `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY&type=SWAP`;

```


```
// Exclude spam by only including transactions that changed token balances
const url = `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY&tokenAccounts=balanceChanged`;

// Only show direct wallet interactions
const url = `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY&tokenAccounts=none`;

```


```
// Get only NFT sales that changed balances
const url = `https://api.helius.xyz/v1/wallet/${address}/history?api-key=YOUR_API_KEY&type=NFT_SALE&tokenAccounts=balanceChanged`;

```

## Response Format

```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "timestamp": 1704067200,
      "slot": 250000000,
      "fee": 0.000005,
      "feePayer": "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
      "error": null,
      "balanceChanges": [

          "mint": "So11111111111111111111111111111111111111112",
          "amount": -0.05,
          "decimals": 9


          "mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
          "amount": 50.0,
          "decimals": 6




  "pagination": {
    "hasMore": true,
    "nextCursor": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"



```

The `timestamp` field may be `null` for very recent transactions that haven’t been fully processed yet.
## Use Cases
### Calculate Total Trading Volume
Sum all transfers to get trading volume:

```
const calculateTradingVolume = async (address, tokenMint) => {
  const transactions = await getAllTransactionHistory(address);

  let totalVolume = 0;

  transactions.forEach(tx => {
    tx.balanceChanges.forEach(change => {
      if (change.mint === tokenMint) {
        totalVolume += Math.abs(change.amount);

    });
  });

  console.log(`Total ${tokenMint} volume: ${totalVolume}`);
  return totalVolume;


// Example: Calculate total USDC volume
calculateTradingVolume(
  "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
  "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" // USDC


```

### Generate Tax Report
Create a transaction report for tax filing:

```
const generateTaxReport = async (address, year) => {
  const transactions = await getAllTransactionHistory(address);

  const startDate = new Date(`${year}-01-01`).getTime() / 1000;
  // Set to end of December 31st (23:59:59.999) to include all transactions from that day
  const endDate = new Date(`${year}-12-31T23:59:59.999Z`).getTime() / 1000;

  const taxableTransactions = transactions
filter(tx => tx.timestamp >= startDate tx.timestamp <= endDate)
map(tx => ({
      date: new Date(tx.timestamp * 1000).toISOString(),
      signature: tx.signature,
      fee: tx.fee,
      balanceChanges: tx.balanceChanges,
      explorerUrl: `https://orbmarkets.io/tx/${tx.signature}`
    }));

  console.log(`Found ${taxableTransactions.length} transactions in ${year}`);

  // Export as JSON
  const report = {
    address,
    year,
    transactionCount: taxableTransactions.length,
    transactions: taxableTransactions


  console.log(JSON.stringify(report, null, 2));
  return report;


generateTaxReport("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY", 2024);

```

### Track Failed Transactions
Find all failed transactions to understand errors:

```
const getFailedTransactions = async (address) => {
  const data = await getTransactionHistory(address);

  const failed = data.data.filter(tx => tx.error !== null);

  console.log(`Found ${failed.length} failed transactions`);

  failed.forEach(tx => {
    const date = new Date(tx.timestamp * 1000).toLocaleString();
    console.log(`\n${date}`);
    console.log(`Signature: ${tx.signature}`);
    console.log(`Error: ${tx.error}`);
    console.log(`Fee Paid: ${tx.fee} SOL`);
  });

  return failed;


```

### Reconstruct Historical Balance
Calculate what the balance was at a specific point in time:

```
const getHistoricalBalance = async (address, targetTimestamp) => {
  const transactions = await getAllTransactionHistory(address);

  // Filter to transactions before target date
  const relevantTxs = transactions.filter(tx => tx.timestamp <= targetTimestamp);

  // Sum all balance changes
  const balances = {};

  relevantTxs.forEach(tx => {
    tx.balanceChanges.forEach(change => {
      if (!balances[change.mint]) {
        balances[change.mint] = 0;

      balances[change.mint] += change.amount;
    });
  });

  console.log(`Historical balances as of ${new Date(targetTimestamp * 1000).toLocaleString()}:`);
  Object.entries(balances).forEach(([mint, balance]) => {
    console.log(`${mint}: ${balance}`);
  });

  return balances;


// Example: Get balances on Jan 1, 2024
getHistoricalBalance(
  "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
  new Date("2024-01-01").getTime() / 1000


```

### Analyze Transaction Fees
Calculate total fees paid:

```
const analyzeFees = async (address) => {
  const transactions = await getAllTransactionHistory(address);

  const totalFees = transactions.reduce((sum, tx) => sum + tx.fee, 0);
  const avgFee = totalFees / transactions.length;

  const successfulTxs = transactions.filter(tx => !tx.error);
  const failedTxs = transactions.filter(tx => tx.error);

  const wastedFees = failedTxs.reduce((sum, tx) => sum + tx.fee, 0);

  console.log(`Total Transactions: ${transactions.length}`);
  console.log(`Successful: ${successfulTxs.length}`);
  console.log(`Failed: ${failedTxs.length}`);
  console.log(`Total Fees Paid: ${totalFees.toFixed(6)} SOL`);
  console.log(`Average Fee: ${avgFee.toFixed(6)} SOL`);
  console.log(`Wasted on Failed Txs: ${wastedFees.toFixed(6)} SOL`);

  return {
    totalFees,
    avgFee,
    wastedFees,
    successRate: (successfulTxs.length / transactions.length) * 100



```

## Understanding Balance Changes
Each transaction includes an array of `balanceChanges` showing how the wallet’s holdings changed:
  * **Positive amount** (`+`): Tokens received
  * **Negative amount** (`-`): Tokens sent or spent
  * **`mint`field** : Token mint address (or `"SOL"` for native SOL)
  * **`decimals`field** : Number of decimals for the token


All `amount` values in `balanceChanges` are **human-readable** — already divided by `decimals`. For example, `-0.05` means −0.05 SOL, not −0.05 lamports. This endpoint does not include a raw `amountRaw` field.
### Example Balance Changes

```
// Swap: Sold 0.05 SOL, received 5 USDC

  "balanceChanges": [
"mint": "SOL", "amount": -0.05, "decimals": 9 },
"mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "amount": 5.0, "decimals": 6 }



// Simple transfer: Sent 10 USDC

  "balanceChanges": [
"mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "amount": -10.0, "decimals": 6 }



```

## Best Practices
Use Pagination for Complete History
Always implement pagination when fetching complete transaction history. Some wallets have hundreds of thousands of transactions.
Cache Historical Data
Historical transactions never change. Cache them locally and only fetch new transactions.
Handle Failed Transactions
Check the `error` field to distinguish between successful and failed transactions. Failed transactions still incur fees.
Use Timestamps for Date Filtering
Timestamps are in Unix seconds. Convert to local dates for display and filtering.
## Common Errors  
| Error Code  | Description  | Solution  |  
| --- | --- | --- |  
| 400  | Invalid wallet address format  | Verify the address is a valid base58 Solana address  |  
| 401  | Missing or invalid API key  | Check your API key is included in the request  |  
| 429  | Rate limit exceeded  | Reduce request frequency or upgrade your plan  |  
## Need Help?
## [API Reference View detailed API specs with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api/history)
## [Contact Support Get help from our team ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/balances)[ Wallet TransfersTrack all incoming and outgoing token transfers for any Solana wallet. See sender/recipient information, amounts, and timestamps for complete transfer history. Next ](https://www.helius.dev/docs/wallet-api/transfers)
On this page
  * [Pagination for Complete History](https://www.helius.dev/docs/wallet-api/history#pagination-for-complete-history)
  * [Available Transaction Types](https://www.helius.dev/docs/wallet-api/history#available-transaction-types)
  * [Calculate Total Trading Volume](https://www.helius.dev/docs/wallet-api/history#calculate-total-trading-volume)
  * [Track Failed Transactions](https://www.helius.dev/docs/wallet-api/history#track-failed-transactions)
  * [Reconstruct Historical Balance](https://www.helius.dev/docs/wallet-api/history#reconstruct-historical-balance)
  * [Analyze Transaction Fees](https://www.helius.dev/docs/wallet-api/history#analyze-transaction-fees)
  * [Understanding Balance Changes](https://www.helius.dev/docs/wallet-api/history#understanding-balance-changes)
  * [Example Balance Changes](https://www.helius.dev/docs/wallet-api/history#example-balance-changes)


Assistant
Responses are generated using AI and may contain mistakes.
