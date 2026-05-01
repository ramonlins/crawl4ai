# Source: https://www.helius.dev/docs/faqs/enhanced-transactions

[Skip to main content](https://www.helius.dev/docs/faqs/enhanced-transactions#content-area)
New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
Search...
Ctrl K


##### FAQs Overview


##### Account & Billing


##### Infrastructure & Nodes


##### Real-time Data Streaming


##### Transaction & Fee APIs


##### Data APIs


  * English


New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
English
Search...
Ctrl KAsk AI
Search...
Navigation
Transaction & Fee APIs
Enhanced Transactions FAQs
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
##  Using Enhanced Transactions
What is the Enhanced Transactions API?
The [Enhanced Transactions API](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions) provides parsed transaction data in a human-readable format. It allows you to parse individual or multiple transactions, or fetch the complete historical transaction history for a specific address, transforming complex raw blockchain data into structured, readable information.
What types of transactions can be parsed with the Enhanced Transactions API?
The [Enhanced Transactions API](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions) parses a wide range of transaction types including NFT sales/mints, token swaps, SPL token transfers, DeFi operations, and more. We’re actively expanding parser coverage. See the [transaction types documentation](https://www.helius.dev/docs/webhooks/transaction-types) for the full list of supported types.
How do I authenticate Enhanced Transaction API requests?
Add your Helius API key as the `?api-key=YOUR_API_KEY` query parameter to all [Enhanced Transactions API](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions) requests.
What is the type for this transaction?
Transaction types are returned in the `type` field of the API response (e.g., `NFT_SALE`, `SWAP`, `TRANSFER`). You can also filter by transaction type using the `type` parameter in your API requests. See our [transaction types documentation](https://www.helius.dev/docs/webhooks/transaction-types) for all available types.
Is the Enhanced Transactions API still being actively developed?
No. The Enhanced Transactions API is deprecated and no longer receiving new parser types or feature work. Existing endpoints continue to operate, but new integrations should use [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress) for history and [`getTransaction`](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction) for single-transaction lookups.
##  Rate Limits
What are the rate limits for Enhanced Transactions?
[Enhanced Transactions API](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions) usage follows Helius’s standard rate-limiting and pricing policies. See the [Rate limits](https://www.helius.dev/docs/billing/rate-limits) page for specific limits based on your plan.
##  Troubleshooting Enhanced Transactions
Why don't I get all transactions for the Enhanced Transaction History call?
The [Enhanced Transactions API](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions) returns parsed transactions for supported types. If a transaction type isn’t yet supported, it may not appear in results. Check your pagination parameters and ensure you’re using the correct address format. Large transaction histories may require multiple paginated requests.
##  Need More Help?
## [Contact Support Get help from our team through Discord, chat, or email support. ](https://www.helius.dev/docs/support/contact-support)
## [Status Page Check real-time service availability and performance information. ](https://www.helius.dev/docs/support/status-page)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/faqs/sender)[ DAS API FAQsGet answers to the most common questions about Digital Asset Standard API including asset data, price information, and troubleshooting Next ](https://www.helius.dev/docs/faqs/das-api)
Ctrl+I
On this page
  * [Using Enhanced Transactions](https://www.helius.dev/docs/faqs/enhanced-transactions#using-enhanced-transactions)
  * [Troubleshooting Enhanced Transactions](https://www.helius.dev/docs/faqs/enhanced-transactions#troubleshooting-enhanced-transactions)


Assistant
Responses are generated using AI and may contain mistakes.
