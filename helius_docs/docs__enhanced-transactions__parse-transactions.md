# Source: https://www.helius.dev/docs/enhanced-transactions/parse-transactions

**Deprecated** : The Enhanced Transactions API is deprecated and no longer receiving new parser types or feature work. Existing endpoints continue to operate, but new integrations should use [`getTransaction`](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction) or [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress) directly.
## Overview
The Parse Transactions endpoint transforms raw transaction signatures or data into structured, human-readable information. Instead of manually decoding instruction data and account lists, you receive clear details about transfers, swaps, NFT activities, and more.
## [API Reference View detailed API documentation for parsing transactions ](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions)
## Quickstart
Parse one or more transaction signatures with a single API call:
  * JavaScript
  * Python



```
const parseTransaction = async () => {
  const url = "https://api-mainnet.helius-rpc.com/v0/transactions/?api-key=YOUR_API_KEY";

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      transactions: ["5rfFLBUp5YPr6rC2g1KBBW8LGZBcZ8Lvs7gKAdgrBjmQvFf6EKkgc5cpAQUTwGxDJbNqtLYkjV5vS5zVK4tb6JtP"],
    }),
  });

  const data = await response.json();
  console.log("Parsed transaction:", data);


parseTransaction();

```


```
import requests
import json

def parse_transaction():
    url = "https://api-mainnet.helius-rpc.com/v0/transactions/?api-key=YOUR_API_KEY"

    payload = {
        "transactions": ["5rfFLBUp5YPr6rC2g1KBBW8LGZBcZ8Lvs7gKAdgrBjmQvFf6EKkgc5cpAQUTwGxDJbNqtLYkjV5vS5zVK4tb6JtP"]


    response = requests.post(url, json=payload)
    data = response.json()
    print("Parsed transaction:", data)

parse_transaction()

```

## Response Structure
Enhanced transaction responses include structured data with human-readable descriptions:

```

  "description": "Transfer 0.1 SOL to FXvStt8aeQHMGKDgqaQ2HXWfJsXnqiKSoBEpHJahkuD",
  "type": "TRANSFER",
  "source": "SYSTEM_PROGRAM",
  "fee": 5000,
  "feePayer": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
  "signature": "5rfFLBUp5YPr6rC2g1KBBW8LGZBcZ8Lvs7gKAdgrBjmQvFf6EKkgc5cpAQUTwGxDJbNqtLYkjV5vS5zVK4tb6JtP",
  "slot": 171341028,
  "timestamp": 1674080473,
  "nativeTransfers": [

      "fromUserAccount": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
      "toUserAccount": "FXvStt8aeQHMGKDgqaQ2HXWfJsXnqiKSoBEpHJahkuD",
      "amount": 100000000


  "events": {
    "sol": {
      "from": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
      "to": "FXvStt8aeQHMGKDgqaQ2HXWfJsXnqiKSoBEpHJahkuD",
      "amount": 0.1




```

## What You Get
The parsed transaction data includes:
  * **Description** : Human-readable summary of what happened
  * **Type** : Transaction category (TRANSFER, SWAP, NFT_SALE, etc.)
  * **Source** : Program that executed the transaction
  * **Fee Information** : Transaction fees and fee payer
  * **Native Transfers** : SOL movements between accounts
  * **Token Transfers** : SPL token movements
  * **Events** : High-level event summaries
  * **Timestamps** : When the transaction was processed


## Questions?
For frequently asked questions about Enhanced Transactions including usage, authentication, rate limits, and troubleshooting, visit our comprehensive [Enhanced Transactions FAQ](https://www.helius.dev/docs/faqs/enhanced-transactions).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-transactions/overview)[ Transaction HistoryHuman-readable transaction history for any Solana address. Next ](https://www.helius.dev/docs/enhanced-transactions/transaction-history)
On this page


Assistant
Responses are generated using AI and may contain mistakes.
