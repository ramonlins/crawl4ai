# Source: https://www.helius.dev/docs/wallet-api/transfers

**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
## Overview
The Token Transfers endpoint retrieves all token transfer activity for a Solana wallet, including detailed sender/recipient information. Unlike the full transaction history, this endpoint focuses specifically on transfers, making it ideal for payment tracking and transfer monitoring.
## [API Reference View detailed API documentation for token transfers ](https://www.helius.dev/docs/api-reference/wallet-api/transfers)
## When to Use This
Use the Token Transfers API when you need to:
  * **Track Payments** : Monitor incoming payments for payment processors
  * **Build Transfer Feed** : Display a simple “sent/received” activity feed
  * **Monitor Specific Tokens** : Track transfers of a specific token (e.g., USDC payments)
  * **Identify Counterparties** : See who sent or received tokens
  * **Generate Receipts** : Create payment receipts with sender/recipient details
  * **Detect Suspicious Activity** : Monitor unusual transfer patterns


## Quickstart
### Basic Transfers Query
Get recent incoming and outgoing transfers:
  * JavaScript
  * Python
  * cURL



```
const getWalletTransfers = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/transfers?api-key=YOUR_API_KEY`;

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);


  const data = await response.json();

  console.log(`Found ${data.data.length} transfers`);

  // Display recent transfers
  data.data.forEach(transfer => {
    const date = new Date(transfer.timestamp * 1000).toLocaleString();
    const direction = transfer.direction === 'in' ? 'Received' : 'Sent';
    const counterparty = transfer.counterparty.slice(0, 8) + '...';

    console.log(`\n${direction} - ${date}`);
    console.log(`Amount: ${transfer.amount} ${transfer.symbol || transfer.mint.slice(0, 8) + '...'}`);
    console.log(`${transfer.direction === 'in' ? 'From' : 'To'}: ${counterparty}`);
    console.log(`Signature: ${transfer.signature.slice(0, 20)}...`);
  });

  return data;


getWalletTransfers("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
import requests
from datetime import datetime

def get_wallet_transfers(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/transfers"
    headers = {"X-Api-Key": "YOUR_API_KEY"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    print(f"Found {len(data['data'])} transfers")

    # Display recent transfers
    for transfer in data['data']:
        date = datetime.fromtimestamp(transfer['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        direction = 'Received' if transfer['direction'] == 'in' else 'Sent'
        counterparty = transfer['counterparty'][:8] + '...'
        symbol = transfer.get('symbol') or transfer['mint'][:8] + '...'

        print(f"\n{direction} - {date}")
        print(f"Amount: {transfer['amount']} {symbol}")
        print(f"{'From' if transfer['direction'] == 'in' else 'To'}: {counterparty}")
        print(f"Signature: {transfer['signature'][:20]}...")

    return data

get_wallet_transfers("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```


```
curl "https://api.helius.xyz/v1/wallet/86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY/transfers?api-key=YOUR_API_KEY"

```

### Filter by Direction
Get only incoming or outgoing transfers:
  * Incoming Only
  * Outgoing Only



```
const getIncomingTransfers = async (address) => {
  const data = await getWalletTransfers(address);

  const incoming = data.data.filter(t => t.direction === 'in');

  console.log(`Received ${incoming.length} incoming transfers`);

  incoming.forEach(transfer => {
    console.log(`Received ${transfer.amount} ${transfer.symbol} from ${transfer.counterparty.slice(0, 8)}...`);
  });

  return incoming;


```


```
const getOutgoingTransfers = async (address) => {
  const data = await getWalletTransfers(address);

  const outgoing = data.data.filter(t => t.direction === 'out');

  console.log(`Made ${outgoing.length} outgoing transfers`);

  outgoing.forEach(transfer => {
    console.log(`Sent ${transfer.amount} ${transfer.symbol} to ${transfer.counterparty.slice(0, 8)}...`);
  });

  return outgoing;


```

## Query Parameters  
| Parameter  | Type  | Default  | Description  |  
| --- | --- | --- | --- |  
| `limit`  | integer  | 50  | Maximum number of transfers to return (1-100)  |  
| `cursor`  | string  | -  | Pagination cursor from previous response  |  
## Response Format

```

  "data": [

      "signature": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "timestamp": 1704067200,
      "direction": "in",
      "counterparty": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
      "mint": "So11111111111111111111111111111111111111112",
      "symbol": "SOL",
      "amount": 1.5,
      "amountRaw": "1500000000",
      "decimals": 9


      "signature": "4aHu2qwD8Jtj4xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE",
      "timestamp": 1704067100,
      "direction": "out",
      "counterparty": "2ojv9BAiHUrvsm9gxDe7fJSzbNZSJcxZvf8dqmWGHG8S",
      "mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
      "symbol": "USDC",
      "amount": 100.0,
      "amountRaw": "100000000",
      "decimals": 6


  "pagination": {
    "hasMore": true,
    "nextCursor": "5wHu1qwD7Jsj3xqWjdSEJmYr3Q5f5RjXqjqQJ7jqEj7jqEj7jqEj7jqEj7jqEj7jqE"



```

  * **`amount`**: Human-readable transfer amount, already divided by`decimals`. Use this for display (e.g., `1.5` SOL, `100.0` USDC).
  * **`amountRaw`**: The same amount as a raw integer string, before decimal adjustment (e.g.,`"1500000000"` for 1.5 SOL). Serialized as a string to avoid floating-point precision loss. Use this for on-chain instructions or precise arithmetic: `amount = parseInt(amountRaw) / 10**decimals`.
  * **`mint`**: Token mint address (`So11111111111111111111111111111111111111112` for native SOL).


## Understanding Direction
The `direction` field is relative to the wallet you’re querying:
  * **`in`**: Tokens**received** by the wallet (incoming payment)
  * **`out`**: Tokens**sent** by the wallet (outgoing payment)

The `counterparty` field is:
  * **For`in` transfers**: The sender (who sent tokens to this wallet)
  * **For`out` transfers**: The recipient (who received tokens from this wallet)


## Use Cases
### Track Payment History for a Merchant
Monitor incoming USDC payments:

```
const trackMerchantPayments = async (merchantWallet) => {
  const data = await getWalletTransfers(merchantWallet);

  // Filter for incoming USDC transfers
  const usdcPayments = data.data.filter(t =>
.direction === 'in'
.mint === 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v' // USDC


  console.log(`Received ${usdcPayments.length} USDC payments`);

  const totalReceived = usdcPayments.reduce((sum, t) => sum + t.amount, 0);
  console.log(`Total USDC Received: $${totalReceived.toFixed(2)}`);

  // Display each payment
  usdcPayments.forEach(payment => {
    const date = new Date(payment.timestamp * 1000).toLocaleString();
    console.log(`${date}: $${payment.amount} from ${payment.counterparty}`);
  });

  return {
    count: usdcPayments.length,
    total: totalReceived,
    payments: usdcPayments



```

### Generate Payment Receipt
Create a detailed receipt for a specific transfer:

```
const generatePaymentReceipt = async (address, signature) => {
  const data = await getWalletTransfers(address);

  const transfer = data.data.find(t => t.signature === signature);

  if (!transfer) {
    console.log('Transfer not found');
    return null;


  const receipt = {
    receiptId: transfer.signature.slice(0, 16),
    date: new Date(transfer.timestamp * 1000).toISOString(),
    type: transfer.direction === 'in' ? 'Payment Received' : 'Payment Sent',
    amount: `${transfer.amount} ${transfer.symbol || 'tokens'}`,
    from: transfer.direction === 'in' ? transfer.counterparty : address,
    to: transfer.direction === 'out' ? transfer.counterparty : address,
    transactionUrl: `https://orbmarkets.io/tx/${transfer.signature}`


  console.log('--- PAYMENT RECEIPT ---');
  Object.entries(receipt).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
  });

  return receipt;


```

### Monitor Suspicious Transfer Patterns
Detect unusual transfer activity:

```
const detectSuspiciousActivity = async (address) => {
  const data = await getWalletTransfers(address);

  const recentTransfers = data.data.filter(t => {
    const hourAgo = Date.now() / 1000 - 3600;
    return t.timestamp hourAgo;
  });

  // Check for high frequency
  if (recentTransfers.length 100) {
    console.log(`Warning: ${recentTransfers.length} transfers in the last hour`);


  // Check for large amounts
  const largeTransfers = recentTransfers.filter(t => {
    // Assuming USDC/stablecoins
    return t.amount 10000 t.decimals === 6;
  });

  if (largeTransfers.length 0) {
    console.log(`Warning: ${largeTransfers.length} large transfers (>$10k) in the last hour`);


  // Check for transfers to same address
  const counterparties = recentTransfers.map(t => t.counterparty);
  const duplicates = counterparties.filter((item, index) => counterparties.indexOf(item) !== index);

  if (duplicates.length 5) {
    console.log(`Warning: Multiple transfers to the same address`);


  return {
    recentCount: recentTransfers.length,
    largeTransfers: largeTransfers.length,
    suspiciousPatterns: duplicates.length 5



```

### Build Transfer Activity Feed
Create a user-friendly activity feed:

```
const buildTransferFeed = async (address) => {
  const data = await getWalletTransfers(address);

  const feed = data.data.map(transfer => {
    const date = new Date(transfer.timestamp * 1000);
    const timeAgo = getTimeAgo(date);

    return {
      id: transfer.signature,
      icon: transfer.direction === 'in' ? '📥' : '📤',
      title: transfer.direction === 'in' ? 'Received' : 'Sent',
      subtitle: `${transfer.amount} ${transfer.symbol || 'tokens'}`,
      description: transfer.direction === 'in'
 `from ${transfer.counterparty.slice(0, 8)}...`
 `to ${transfer.counterparty.slice(0, 8)}...`,
      timeAgo,
      explorerUrl: `https://orbmarkets.io/tx/${transfer.signature}`

  });

  return feed;


function getTimeAgo(date) {
  const seconds = Math.floor((new Date() - date) / 1000);

  if (seconds 60) return 'Just now';
  if (seconds 3600) return `${Math.floor(seconds / 60)}m ago`;
  if (seconds 86400) return `${Math.floor(seconds / 3600)}h ago`;
  return `${Math.floor(seconds / 86400)}d ago`;


```

### Reconcile Payments
Match transfers against expected payments:

```
const reconcilePayments = async (address, expectedPayments) => {
  const data = await getWalletTransfers(address);

  const recentTransfers = data.data.filter(t =>
.direction === 'in'
.mint === 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v' // USDC


  const reconciliation = expectedPayments.map(expected => {
    const match = recentTransfers.find(t =>
      Math.abs(t.amount - expected.amount)  0.01
.counterparty === expected.from


    return {
      orderId: expected.orderId,
      expectedAmount: expected.amount,
      status: match ? 'Received' : 'Pending',
      receivedAmount: match?.amount,
      signature: match?.signature,
      timestamp: match?.timestamp

  });

  console.log('Payment Reconciliation:');
  reconciliation.forEach(r => {
    console.log(`Order ${r.orderId}: ${r.status}`);
  });

  return reconciliation;


// Example usage
const expected = [
orderId: 'ORDER-001', amount: 100.00, from: 'ABC...' },
orderId: 'ORDER-002', amount: 250.50, from: 'XYZ...' }


reconcilePayments("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY", expected);

```

## Pagination
For wallets with many transfers, use pagination to fetch all results:

```
const getAllTransfers = async (address) => {
  let allTransfers = [];
  let cursor = null;


    const url = cursor
 `https://api.helius.xyz/v1/wallet/${address}/transfers?api-key=YOUR_API_KEY&cursor=${cursor}`
 `https://api.helius.xyz/v1/wallet/${address}/transfers?api-key=YOUR_API_KEY`;

    const response = await fetch(url);
    const data = await response.json();

    allTransfers = allTransfers.concat(data.data);
    cursor = data.pagination.hasMore ? data.pagination.nextCursor : null;

    console.log(`Fetched ${allTransfers.length} transfers so far...`);

while (cursor);

  console.log(`\nTotal transfers: ${allTransfers.length}`);
  return allTransfers;


```

## Best Practices
Filter Client-Side for Specific Tokens
The API returns all token transfers. Filter by `mint` address client-side to track specific tokens like USDC or SOL.
Combine with Identity API
Use the Identity API to show human-readable names for known counterparties (exchanges, protocols, etc.).
Cache Recent Transfers
Transfer data doesn’t change. Cache results and only fetch new transfers since your last query.
Use Pagination for Complete History
Implement pagination to handle wallets with thousands of transfers efficiently.
Handle Missing Symbol
Not all tokens have a `symbol` field. Fall back to displaying the mint address when `symbol` is `null`.
## Transfers vs Transaction History  
| Feature  | Transfers  | Transaction History  |  
| --- | --- | --- |  
| **Focus**  | Only token transfers  | All transaction types  |  
| **Data**  | Sender/recipient info  | Balance changes for all tokens  |  
| **Use Case**  | Payment tracking  | Complete activity log  |  
| **Performance**  | Faster, simpler  | More comprehensive  |  
Use **Transfers** when you only care about payments. Use **Transaction History** when you need complete balance change data.
## Common Errors  
| Error Code  | Description  | Solution  |  
| --- | --- | --- |  
| 400  | Invalid wallet address format  | Verify the address is a valid base58 Solana address  |  
| 401  | Missing or invalid API key  | Check your API key is included in the request  |  
| 429  | Rate limit exceeded  | Reduce request frequency or upgrade your plan  |  
## Need Help?
## [API Reference View detailed API specs with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api/transfers)
## [Contact Support Get help from our team ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/history)[ Wallet Funding SourceDiscover the original funding source of any Solana wallet by tracing its first incoming SOL transfer. Identify exchange funding, attribution, and wallet relationships. Next ](https://www.helius.dev/docs/wallet-api/funded-by)
On this page
  * [Basic Transfers Query](https://www.helius.dev/docs/wallet-api/transfers#basic-transfers-query)
  * [Understanding Direction](https://www.helius.dev/docs/wallet-api/transfers#understanding-direction)
  * [Track Payment History for a Merchant](https://www.helius.dev/docs/wallet-api/transfers#track-payment-history-for-a-merchant)
  * [Generate Payment Receipt](https://www.helius.dev/docs/wallet-api/transfers#generate-payment-receipt)
  * [Monitor Suspicious Transfer Patterns](https://www.helius.dev/docs/wallet-api/transfers#monitor-suspicious-transfer-patterns)
  * [Build Transfer Activity Feed](https://www.helius.dev/docs/wallet-api/transfers#build-transfer-activity-feed)
  * [Transfers vs Transaction History](https://www.helius.dev/docs/wallet-api/transfers#transfers-vs-transaction-history)


Assistant
Responses are generated using AI and may contain mistakes.
