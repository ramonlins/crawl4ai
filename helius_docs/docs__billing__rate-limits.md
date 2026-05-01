# Source: https://www.helius.dev/docs/billing/rate-limits

## What are rate limits?
Rate limits control how many requests you can make per second. When rate limits are exceeded, you’ll receive an HTTP 429 response. For guidance on what to do when you hit a 429 or other transient failure, see [Retries and error handling](https://www.helius.dev/docs/billing/rate-limits#retries-and-error-handling) below.
## Standard Rate Limits
Your plan has two standard rate limit groups: one for RPC requests, and one for DAS API requests. Here are the base rate limits for each Helius plan:  
| Plan  | RPC Rate Limit  | DAS & Enhanced APIs  |  
| --- | --- | --- |  
| **Free**  | 10 requests/s  | 2 requests/s  |  
| **Developer**  | 50 requests/s  | 10 requests/s  |  
| **Business**  | 200 requests/s  | 50 requests/s  |  
| **Professional**  | 500 requests/s  | 100 requests/s  |  
| **Enterprise**  | Custom  | Custom  |  
### Increase Rate Limits
Teams on Professional plans can purchase an extra 100 RPS for $100/month. If you need custom rate limits ahead of launches, [contact our sales team](https://www.helius.dev/contact). If you are on Developer or Business tier, please upgrade your plan to increase your rate limits.
## Special Rate Limits
Some endpoints and specialized Helius products have special rate limits due to their computational requirements.
### Sending Transactions  
| Endpoint  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| `Sender`  | 50/sec  | 50/sec  | 50/sec  | 50/sec  |  
| `sendTransaction`  | 1/sec  | 5/sec  | 50/sec  | 100/sec  |  
| `sendBundle`  | —  | —  | 5/sec  | 5/sec  |  
| `simulateBundle`  | 10/sec  | 50/sec  | 200/sec  | 500/sec  |  
If you are on a Professional plan and need to increase your `sendTransaction` rate limits, [contact our sales team](https://www.helius.dev/contact). Professional plan users can also [request](https://www.helius.dev/contact) rate limit increases and custom tip arrangements for Sender to support higher-throughput trading apps.
### Complex RPC Calls  
| Endpoint  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| `getProgramAccounts`  | 5/sec  | 25/sec  | 50/sec  | 75/sec  |  
### Historical Data
When making batch requests for historical data methods, the following limits apply:  
| Method  | Max Batch Size  |  
| --- | --- |  
| `getTransaction`  | 100 items per request  |  
| `getTransactionsForAddress`  | No batch requests allowed  |  
| All other historical methods  | 10 items per request  |  
Exceeding batch limits will result in an error response. For `getTransactionsForAddress`, each address must be queried in a separate request.
### LaserStream  
| Resource  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| Networks  | —  | Devnet  | Devnet, Mainnet  | Devnet, Mainnet  |  
| Max Pubkeys  | —  | 10M  | 10M  | 10M  |  
| Active Connections  | —  | —  | 10  | 100  |  
### Wallet API
The [Wallet API](https://www.helius.dev/docs/api-reference/wallet-api) follows the same rate limits as DAS & Enhanced APIs. All endpoints share these limits:  
| Endpoint  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| All Wallet API Endpoints  | 2/sec  | 10/sec  | 50/sec  | 100/sec  |  
This includes identity lookups, balances, history, transfers, and funding source endpoints. Learn more in our [Wallet API documentation](https://www.helius.dev/docs/wallet-api/overview).
### WebSockets  
| Resource  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| Concurrent Connections  | 5  | 150  | 250  | 1,000  |  
| Subscriptions per Connection  | 1,000  | 1,000  | 1,000  | 1,000  |  
| WebSocket Types  | Standard  | Standard, Enhanced  | Standard, Enhanced  | Standard, Enhanced  |  
### Webhooks  
| Resource  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| Max Webhooks  | 5  | 50  | 50  | 50  |  
| Addresses per Webhook  | 100k  | 100k  | 100k  | 100k  |  
### ZK Compression  
| Service  | Free  | Developer  | Business  | Professional  |  
| --- | --- | --- | --- | --- |  
| Photon APIs  | 2/sec  | 10/sec  | 50/sec  | 100/sec  |  
| `getValidityProof`  | 1/sec  | 5/sec  | 10/sec  | 20/sec  |  
## Retries and error handling
When your application receives a `429 Too Many Requests`, `503 Service Unavailable`, or transient `5xx` response, wait a moment and retry — don’t retry immediately. Immediate retries pile up requests and make rate-limit recovery slower, not faster.
### Recommended strategy
  * Wait about **1 second** before the first retry.
  * **Double the wait** each time you retry, up to a maximum of **30 seconds**.
  * Add a small random variation of **±25%** to each wait so multiple applications don’t all retry at the same instant.
  * Give up after **5 attempts** and return the error to the code that called you.


### Which errors to retry  
| Status  | Retry?  | Reason  |  
| --- | --- | --- |  
|  `400`, `401`, `403`, `404`  | No  | Client errors — retrying will not change the outcome.  |  
| `408`  | Yes  | Request timeout.  |  
| `409`  | No  | Conflict — resolve at the caller.  |  
| `422`  | No  | Validation error.  |  
| `429`  | Yes  | Rate limit exceeded — wait and retry with backoff.  |  
|  `500`, `502`  | Yes  | Transient server error.  |  
| `503`  | Yes  | Service unavailable — wait and retry with backoff.  |  
| `504`  | Yes  | Gateway timeout.  |  
| Network error  | Yes  | Connection reset, DNS failure, or socket timeout.  |  
### Example
TypeScript
Python
Shell

```
const RETRYABLE = new Set([408, 429, 500, 502, 503, 504]);

export async function callWithRetryT>(
  request: () => PromiseResponse>,
  maxAttempts = 5,
): PromiseT> {
  let delay = 1000;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    const res = await request();
    if (res.ok) return (await res.json()) as T;

    if (!RETRYABLE.has(res.status) || attempt === maxAttempts) {
      throw new Error(`${res.status} after ${attempt} attempt(s): ${await res.text()}`);


    const jitterMs = delay * (0.75 + Math.random() * 0.5);
    await new Promise((r) => setTimeout(r, jitterMs));
    delay = Math.min(delay * 2, 30_000);

  throw new Error("unreachable");


```

### Error response shape
All Helius APIs return a structured JSON body on error. JSON-RPC endpoints (Solana RPC, DAS, Sender, Priority Fee, ZK Compression) return the standard JSON-RPC 2.0 envelope:

```

  "jsonrpc": "2.0",
  "error": { "code": -32005, "message": "Too many requests" },
  "id": "1"


```

REST endpoints (Wallet API, Admin API) return:

```

  "error": "RATE_LIMIT_EXCEEDED",
  "code": 429,
  "details": "Too many requests. Retry after 2 seconds."


```

See [Common error codes](https://www.helius.dev/docs/api-reference/common-error-codes) for the full list of error codes and what each one means.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/billing/credits)[ OverviewHigh-performance Solana RPC infrastructure with 95% faster response times. Complete guide to RPC methods, optimization, and best practices. Next ](https://www.helius.dev/docs/rpc/overview)
On this page
  * [Retries and error handling](https://www.helius.dev/docs/billing/rate-limits#retries-and-error-handling)
  * [Which errors to retry](https://www.helius.dev/docs/billing/rate-limits#which-errors-to-retry)
  * [Error response shape](https://www.helius.dev/docs/billing/rate-limits#error-response-shape)


Assistant
Responses are generated using AI and may contain mistakes.
