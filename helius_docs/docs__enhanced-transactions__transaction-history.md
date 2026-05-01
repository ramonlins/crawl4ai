# Source: https://www.helius.dev/docs/enhanced-transactions/transaction-history

**Deprecated** : The Enhanced Transactions API is deprecated and no longer receiving new parser types or feature work. For transaction history, use the Helius-native [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress) RPC method, which powers this endpoint under the hood and supports server-side filtering and token account lookups.
## Overview
The Enhanced Transactions API transforms complex Solana transactions into human-readable data. Instead of dealing with raw instruction data and account lists, you get structured information about:
  * What happened in the transaction (transfers, swaps, NFT activities)
  * Which accounts were involved
  * How much SOL or tokens were transferred
  * Associated metadata (e.g. token mint addresses, token names, token symbols, etc.)

Under the hood, the API is powered by the [getTransactionsForAddress](https://www.helius.dev/docs/rpc/gettransactionsforaddress) RPC method.
## [API Reference View detailed API documentation for transaction history ](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactionsbyaddress)
## Associated Token Accounts
On Solana, your wallet doesn’t actually hold tokens directly. Instead, your wallet owns token accounts, and those token accounts hold your tokens. When someone sends you USDC, it goes to your USDC token account instead of your main wallet address.
This method is unique because it allows you to query **complete token history**. You can query for a wallet’s full history, including associated token addresses (ATAs). Native RPC methods such as getSignaturesForAddress do not include ATAs. The `token-accounts` filter gives you control over this behavior:
  * **`none`**(default): Only returns transactions that directly reference the wallet address. Use this when you only care about direct wallet interactions.
  * **`balanceChanged`**(recommended): Returns transactions that reference the wallet address OR modify the balance of a token account owned by the wallet. This filters out spam and unrelated operations like fee collections or delegations, giving you a clean view of meaningful wallet activity.
  * **`all`**: Returns all transactions that reference the wallet address or any token account owned by the wallet.


**Limitation for Legacy Transactions** : The `token-accounts` filter relies on the `owner` field in token balance metadata, which was not available before slot 111,491,819 (~December 2022). Transactions involving token accounts active before this slot may be missing from `balanceChanged` and `all` results. See the [getTransactionsForAddress tutorial](https://www.helius.dev/docs/rpc/gettransactionsforaddress#workaround-historical-token-account-discovery) for a workaround with full code example.
## Network Support  
| Network  | Supported  | Retention Period  |  
| --- | --- | --- |  
| Mainnet  | Yes  | Unlimited  |  
| Devnet  | Yes  | 2 weeks  |  
| Testnet  | No  | N/A  |  
## Quickstart
Retrieve transaction history for any Solana address:
  * JavaScript
  * Python



```
const fetchWalletTransactions = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"; // Replace with target wallet
  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("Wallet transactions:", transactions);


fetchWalletTransactions();

```


```
import requests

def fetch_wallet_transactions():
    wallet_address = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"  # Replace with target wallet
    url = f"https://api-mainnet.helius-rpc.com/v0/addresses/{wallet_address}/transactions?api-key=YOUR_API_KEY"

    response = requests.get(url)
    transactions = response.json()
    print("Wallet transactions:", transactions)

fetch_wallet_transactions()

```

### Filter by Transaction Type
Get only specific transaction types, such as NFT sales, token transfers, or swaps:
  * NFT Sales
  * Token Transfers
  * Swaps



```
const fetchNftSales = async () => {
  const tokenAddress = "GjUG1BATg5V4bdAr1csKys1XK9fmrbntgb1iV7rAkn94"; // NFT mint address
  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${tokenAddress}/transactions?api-key=YOUR_API_KEY&type=NFT_SALE`;

  const response = await fetch(url);
  const nftSales = await response.json();
  console.log("NFT sale transactions:", nftSales);


```


```
const fetchTokenTransfers = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"; // Wallet address
  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&type=TRANSFER`;

  const response = await fetch(url);
  const transfers = await response.json();
  console.log("Transfer transactions:", transfers);


```


```
const fetchSwapTransactions = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"; // Wallet address
  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&type=SWAP`;

  const response = await fetch(url);
  const swaps = await response.json();
  console.log("Swap transactions:", swaps);


```

[See all available types](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactionsbyaddress).
### Pagination
For high-volume addresses, implement pagination to fetch all transactions:

```
const fetchAllTransactions = async () => {
  const walletAddress = "2k5AXX4guW9XwRQ1AKCpAuUqgWDpQpwFfpVFh3hnm2Ha"; // Replace with target wallet
  const baseUrl = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY`;
  let url = baseUrl;
  let lastSignature = null;
  let allTransactions = [];

  while (true) {
    if (lastSignature) {
      url = baseUrl + `&before-signature=${lastSignature}`;


    const response = await fetch(url);

    // Check response status
    if (!response.ok) {
      console.error(`API error: ${response.status}`);
      break;


    const transactions = await response.json();

    if (transactions transactions.length 0) {
      console.log(`Fetched batch of ${transactions.length} transactions`);
      allTransactions = [...allTransactions, ...transactions];
      lastSignature = transactions[transactions.length - 1].signature;
else {
      console.log(`Finished! Total transactions: ${allTransactions.length}`);
      break;



  return allTransactions;


```

## API Reference  
| Parameter  | Description  | Default  | Example  |  
| --- | --- | --- | --- |  
| `limit`  | Number of transactions to return (1-100)  | 10  | `&limit=25`  |  
| `before-signature`  | Fetch transactions before this signature (use with `sort-order=desc`)  | -  | `&before-signature=sig123...`  |  
| `after-signature`  | Fetch transactions after this signature (use with `sort-order=asc`)  | -  | `&after-signature=sig456...`  |  
| `type`  | Filter by transaction type  | -  | `&type=NFT_SALE`  |  
| `sort-order`  | Sort order for results  | `desc`  | `&sort-order=asc`  |  
| `token-accounts`  | Filter transactions for related token accounts  | `none`  | `&token-accounts=balanceChanged`  |  
| `commitment`  | Commitment level  | `finalized`  | `&commitment=confirmed`  |  
### Time-Based Filtering  
| Parameter  | Description  | Example  |  
| --- | --- | --- |  
| `gt-time`  | Transactions after this Unix timestamp  | `&gt-time=1656442333`  |  
| `gte-time`  | Transactions at or after this Unix timestamp  | `&gte-time=1656442333`  |  
| `lt-time`  | Transactions before this Unix timestamp  | `&lt-time=1656442333`  |  
| `lte-time`  | Transactions at or before this Unix timestamp  | `&lte-time=1656442333`  |  
### Slot-Based Filtering  
| Parameter  | Description  | Example  |  
| --- | --- | --- |  
| `gt-slot`  | Transactions after this slot  | `&gt-slot=148277128`  |  
| `gte-slot`  | Transactions at or after this slot  | `&gte-slot=148277128`  |  
| `lt-slot`  | Transactions before this slot  | `&lt-slot=148277128`  |  
| `lte-slot`  | Transactions at or before this slot  | `&lte-slot=148277128`  |  
**Filtering Tips** :
  * Time parameters use Unix timestamps (seconds since epoch)
  * Slot parameters use Solana slot numbers
  * You cannot combine time-based and slot-based filters in the same request
  * Use `sort-order=asc` for ascending (oldest first) or `sort-order=desc` for descending (newest first)


## Advanced Filtering Examples
### Filter by Time Range
Get transactions within a specific time window:
  * Last 24 Hours
  * Specific Date Range



```
const fetchRecentTransactions = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";
  const now = Math.floor(Date.now() / 1000);
  const oneDayAgo = now - (24 * 60 * 60);

  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&gte-time=${oneDayAgo}&lte-time=${now}`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("Transactions from last 24 hours:", transactions);


```


```
const fetchTransactionsByDateRange = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";

  // January 1, 2024 to January 31, 2024
  const startTime = Math.floor(new Date('2024-01-01').getTime() / 1000);
  const endTime = Math.floor(new Date('2024-01-31').getTime() / 1000);

  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&gte-time=${startTime}&lte-time=${endTime}`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("Transactions in January 2024:", transactions);


```

### Filter by Slot Range
Get transactions within a specific slot range:

```
const fetchTransactionsBySlotRange = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";
  const startSlot = 148000000;
  const endSlot = 148100000;

  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&gte-slot=${startSlot}&lte-slot=${endSlot}`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log(`Transactions between slots ${startSlot} and ${endSlot}:`, transactions);


```

### Change Sort Order
Get transactions in ascending order (oldest first):

```
const fetchOldestTransactions = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";
  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&sort-order=asc&limit=10`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("10 oldest transactions:", transactions);


```

### Include Transfers for Related Token Accounts
Query for a wallet’s full history, including associated token addresses (ATAs):

```
const fetchTransactionsWithATA = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";

  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&token-accounts=balanceChanged&sort-order=desc&limit=50`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("Most recent transactions (including ATA transfers)", transactions);


```

### Combine Multiple Filters
Combine type filtering with time range and custom sort order:

```
const fetchFilteredTransactionsAdvanced = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";

  // Get NFT sales from the last 7 days, oldest first
  const now = Math.floor(Date.now() / 1000);
  const sevenDaysAgo = now - (7 * 24 * 60 * 60);

  const url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&type=NFT_SALE&gte-time=${sevenDaysAgo}&sort-order=asc&limit=50`;

  const response = await fetch(url);
  const transactions = await response.json();
  console.log("NFT sales from last 7 days (oldest first):", transactions);


```

### Pagination with Time Filters
Paginate through results with time filtering:

```
const fetchAllTransactionsInTimeRange = async () => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";
  const startTime = Math.floor(new Date('2024-01-01').getTime() / 1000);
  const endTime = Math.floor(new Date('2024-01-31').getTime() / 1000);

  let beforeSignature = null;
  let allTransactions = [];

  while (true) {
    let url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&gte-time=${startTime}&lte-time=${endTime}&limit=100`;

    if (beforeSignature) {
      url += `&before-signature=${beforeSignature}`;


    const response = await fetch(url);
    const transactions = await response.json();

    if (!Array.isArray(transactions) || transactions.length === 0) {
      break;


    allTransactions = [...allTransactions, ...transactions];
    beforeSignature = transactions[transactions.length - 1].signature;

    console.log(`Fetched ${transactions.length} transactions, total: ${allTransactions.length}`);


  console.log(`Total transactions in time range: ${allTransactions.length}`);
  return allTransactions;


```

**Performance Tips** :
  * Use time or slot filters to reduce the search space when you know the approximate time period
  * Combine with `limit` parameter to control page size
  * Use `sort-order=asc` when you want to process transactions chronologically
  * Time-based filters are more intuitive for date ranges, while slot-based filters are useful for blockchain-specific queries


## Type Filtering Considerations
**Runtime Type Filtering** :Type filtering happens at runtime, meaning the API searches through transactions sequentially until it finds at least 50 matching items. If the API cannot find any transactions matching your filter within the search period, it will return an error with instructions to continue searching.
When using type filters, you may encounter a situation where no matching transactions are found within the current search window. In this case, the API returns an error response like:

```

  "error": "Failed to find events within the search period. To continue search, query the API again with the `before-signature` parameter set to 2UKbsu95YzxGjUGYRg2znozmmVADVgmnhHqzDxq8Xfb3V5bf2NHUkaXGPrUpQnRFVHVKbawdQXtm4xJt9njMDHvg."


```

To continue the search, you need to use the signature provided in the error message with the appropriate parameter (`before-signature` for descending, `after-signature` for ascending) in your next request. Here’s how to handle this:

```
const fetchFilteredTransactions = async (sortOrder = 'desc') => {
  const walletAddress = "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K";
  const transactionType = "NFT_SALE";
  let continuationSignature = null;
  let allFilteredTransactions = [];
  let maxRetries = 10; // Prevent infinite loops
  let retryCount = 0;

  // Determine which parameter to use based on sort order
  const continuationParam = sortOrder === 'asc' ? 'after-signature' : 'before-signature';

  while (retryCount maxRetries) {
    // Build URL with optional continuation parameter
    let url = `https://api-mainnet.helius-rpc.com/v0/addresses/${walletAddress}/transactions?api-key=YOUR_API_KEY&type=${transactionType}&sort-order=${sortOrder}`;

    if (continuationSignature) {
      url += `&${continuationParam}=${continuationSignature}`;


    try {
      const response = await fetch(url);
      const data = await response.json();

      // Check if we received an error about search period
      if (data.error data.error.includes("Failed to find events within the search period")) {
        // Extract the signature from the error message
        const signatureMatch = data.error.match(/parameter set to ([A-Za-z0-9]+)/);

 (signatureMatch signatureMatch[1]) {
          console.log(`No results in this period. Continuing search from: ${signatureMatch[1]}`);
          continuationSignature = signatureMatch[1];
          retryCount++;
          continue; // Continue searching with new signature
else {
          console.log("No more transactions to search");
          break;



      // Check if we received transactions
      if (Array.isArray(data)  data.length 0) {
        console.log(`Found ${data.length} ${transactionType} transactions`);
        allFilteredTransactions = [...allFilteredTransactions, ...data];

        // Set continuation signature for next page
        continuationSignature = data[data.length - 1].signature;
        retryCount = 0; // Reset retry count since we found results
else {
        console.log("No more transactions found");
        break;


catch (error) {
      console.error("Error fetching transactions:", error);
      break;



  console.log(`Total ${transactionType} transactions found: ${allFilteredTransactions.length}`);
  return allFilteredTransactions;


// Usage examples:
// Descending order (newest first) - uses 'before-signature' parameter
fetchFilteredTransactions('desc');

// Ascending order (oldest first) - uses 'after-signature' parameter
fetchFilteredTransactions('asc');

```

**Key Points** :
  * The API searches through up to 50 transactions at a time when using type filters
  * If no matches are found, use the signature from the error message to continue searching
  * Use `before-signature` parameter when searching in descending order (default, newest first)
  * **Use`after-signature` parameter when searching in ascending order (oldest first)** - this is required for chronological searches
  * Implement a maximum retry limit to prevent infinite loops
  * This behavior is expected and allows you to search through an address’s entire history for specific transaction types


## Questions?
For frequently asked questions about Enhanced Transactions including usage, authentication, rate limits, and troubleshooting, visit our comprehensive [Enhanced Transactions FAQ](https://www.helius.dev/docs/faqs/enhanced-transactions).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-transactions/parse-transactions)[ OverviewQuery Solana wallet data with the Wallet API. Get balances, transaction history, transfers, identity information, and funding sources in a single request. Next ](https://www.helius.dev/docs/wallet-api/overview)
On this page
  * [Associated Token Accounts](https://www.helius.dev/docs/enhanced-transactions/transaction-history#associated-token-accounts)
  * [Filter by Transaction Type](https://www.helius.dev/docs/enhanced-transactions/transaction-history#filter-by-transaction-type)
  * [Advanced Filtering Examples](https://www.helius.dev/docs/enhanced-transactions/transaction-history#advanced-filtering-examples)
  * [Include Transfers for Related Token Accounts](https://www.helius.dev/docs/enhanced-transactions/transaction-history#include-transfers-for-related-token-accounts)
  * [Combine Multiple Filters](https://www.helius.dev/docs/enhanced-transactions/transaction-history#combine-multiple-filters)
  * [Pagination with Time Filters](https://www.helius.dev/docs/enhanced-transactions/transaction-history#pagination-with-time-filters)
  * [Type Filtering Considerations](https://www.helius.dev/docs/enhanced-transactions/transaction-history#type-filtering-considerations)


Assistant
Responses are generated using AI and may contain mistakes.
