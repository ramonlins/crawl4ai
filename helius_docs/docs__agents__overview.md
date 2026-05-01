# Source: https://www.helius.dev/docs/agents/overview

Helius provides first-class support for AI agents building on Solana. From programmatic account creation to real-time data streaming, agents can access the full power of Helius without any manual intervention.
  * [Helius MCP](https://www.helius.dev/docs/agents/mcp) — 10 routed tools that cover querying the blockchain, sending transactions, streaming, and more
  * [Claude Code Plugin](https://www.helius.dev/docs/agents/claude-code-plugin) — One install: MCP servers + skills + reference files
  * [Skills](https://www.helius.dev/docs/agents/skills/overview) — Expert instruction sets for Claude: [Build](https://www.helius.dev/docs/agents/skills/build), [Phantom](https://www.helius.dev/docs/agents/skills/phantom), [DFlow](https://www.helius.dev/docs/agents/skills/dflow), [SVM](https://www.helius.dev/docs/agents/skills/svm)
  * [TypeScript SDK](https://www.helius.dev/docs/agents/typescript-sdk) — Type-safe methods for all Helius APIs
  * [Rust SDK](https://www.helius.dev/docs/agents/rust-sdk) — High-performance Rust SDK for Helius APIs
  * [Helius CLI](https://www.helius.dev/docs/agents/cli) — Account management and shell scripting


A machine-readable version of this section is available at [agents/llms.txt](https://www.helius.dev/docs/agents/llms.txt) for AI agent consumption.
## MCP vs CLI
The [Helius MCP server](https://www.helius.dev/docs/agents/mcp) is the recommended way for AI agents to interact with Helius. It provides 10 routed tools that give AI direct, structured access to Solana — no shell commands, no output parsing, no manual API calls.  
 |  
|  |  
| **Best for**  | AI agents in Claude Code, Cursor, Claude Desktop, and any MCP-compatible tool  | Shell scripts, CI/CD pipelines, terminal workflows  |  
| **Interface**  | Structured tool calls with typed inputs/outputs  | Command-line with `--json` output  |  
| **Capabilities**  | 10 routed tools (`heliusWallet`, `heliusAsset`, `heliusTransaction`, …) covering blockchain queries, transactions, webhooks, streaming, wallet analysis, docs, and signup  | 95+ commands: same capabilities plus config management and interactive flows  |  
| **Account setup**  | Built-in: `heliusAccount` actions `generateKeypair` → `agenticSignup` — no external tools needed  |  `helius keygen` → `helius signup`  |  
| **When to use**  | Default choice for any AI agent  | When you need shell-level automation or are not using an MCP-compatible tool  |  
**Start with MCP.** If your AI tool supports MCP (Claude Code, Cursor, Claude Desktop, etc.), use the [MCP server](https://www.helius.dev/docs/agents/mcp) or the [Claude Code Plugin](https://www.helius.dev/docs/agents/claude-code-plugin). The CLI is useful for shell scripting and CI/CD, but for AI-driven workflows the MCP provides a more seamless experience — the AI calls tools directly rather than spawning shell commands and parsing output.
## Quick Start: Agent Signup
Agents can create a Helius account and get an API key in four steps using the [Helius CLI](https://www.helius.dev/docs/agents/cli):

```
npm install -g helius-cli    # Install CLI
helius keygen                 # Generate keypair
# Fund wallet with 1 USDC + ~0.001 SOL
helius signup --json          # Get API key (JSON output)

```

On success, your agent receives an API key, RPC endpoints, and 1,000,000 credits. See the [full CLI guide](https://www.helius.dev/docs/agents/cli) for details.
## Authentication
All Helius API requests require an API key passed as a query parameter:

```
?api-key=YOUR_API_KEY

```

Append this to any RPC or API endpoint. For example: `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY` Get an API key from the [Helius Dashboard](https://dashboard.helius.dev) or programmatically via the [Helius CLI](https://www.helius.dev/docs/agents/cli).
**Use Gatekeeper for lower latency** — [Gatekeeper (Beta)](https://www.helius.dev/docs/gatekeeper/overview) removes Cloudflare from the critical path, reducing response times by tens to hundreds of milliseconds. Same API key, same methods — just swap the endpoint:

```
https://beta.helius-rpc.com/?api-key=YOUR_API_KEY
wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY

```

Supports all RPC, DAS, WebSocket, ZK Compression, Priority Fee, and Enhanced Transaction methods. See the [migration guide](https://www.helius.dev/docs/gatekeeper/migration-guide) for details.
## Helius-Specific API Guidance
Use these Helius-optimized APIs instead of chaining standard Solana RPC methods:  
| Instead of…  | Use this  | Why  |  
| --- | --- | --- |  
|  `getSignaturesForAddress` + `getTransaction`  | [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress)  | Single call returns full transaction history with token account data  |  
| `getTokenAccountsByOwner`  |  [`getAssetsByOwner`](https://www.helius.dev/docs/api-reference/das/getassetsbyowner) (DAS API)  | Returns rich metadata, not just raw accounts  |  
| `getRecentPrioritizationFees`  | [`getPriorityFeeEstimate`](https://www.helius.dev/docs/api-reference/priority-fee/getpriorityfeeestimate)  | Pre-calculated optimal fees, no manual computation  |  
|  `getSignaturesForAddress` (for cNFTs)  |  [`getSignaturesForAsset`](https://www.helius.dev/docs/api-reference/das/getsignaturesforasset) (DAS API)  | Standard RPC doesn’t work for compressed NFTs  |  
|  `getProgramAccounts` (for NFT search)  |  [`searchAssets`](https://www.helius.dev/docs/api-reference/das/searchassets) or [`getAssetsByGroup`](https://www.helius.dev/docs/api-reference/das/getassetsbygroup)  | Faster, cheaper, indexed data  |  
| Polling for real-time data  |  [Enhanced WebSockets](https://www.helius.dev/docs/enhanced-websockets) or [LaserStream gRPC](https://www.helius.dev/docs/laserstream)  | Lower latency, more efficient  |  
| Standard `sendTransaction`  | Dual routing (validators + Jito), higher landing rates  |  
## Recommended Workflows  
| Building…  | Helius Products to Use  |  
| --- | --- |  
| Trading bot  |  [Gatekeeper](https://www.helius.dev/docs/gatekeeper/overview) (lowest latency RPC) + [Sender](https://www.helius.dev/docs/sending-transactions/sender) (fast tx submission) + [Priority Fee API](https://www.helius.dev/docs/priority-fee-api) + [LaserStream](https://www.helius.dev/docs/laserstream) (real-time prices)  |  
| Wallet app  |  [DAS API](https://www.helius.dev/docs/das-api) (`getAssetsByOwner`) + [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress) (complete history)  |  
| NFT marketplace  |  [DAS API](https://www.helius.dev/docs/das-api) (`searchAssets`, `getAssetsByGroup`) + [Webhooks](https://www.helius.dev/docs/webhooks) (track sales/listings)  |  
| Token sniper  |  [Gatekeeper](https://www.helius.dev/docs/gatekeeper/overview) (edge-routed RPC) + [LaserStream gRPC](https://www.helius.dev/docs/laserstream) (lowest latency) + [Sender](https://www.helius.dev/docs/sending-transactions/sender) (staked connections)  |  
| Portfolio tracker  |  [DAS API](https://www.helius.dev/docs/das-api) (`getAssetsByOwner` with `showFungible`) + [Enhanced Transactions](https://www.helius.dev/docs/enhanced-transactions/overview)  |  
| Wallet monitor  |  [Enhanced WebSockets](https://www.helius.dev/docs/enhanced-websockets) or [Webhooks](https://www.helius.dev/docs/webhooks) for real-time notifications  |  
| Analytics dashboard  |  [Enhanced Transactions API](https://www.helius.dev/docs/enhanced-transactions/overview) + [`getTransactionsForAddress`](https://www.helius.dev/docs/rpc/gettransactionsforaddress)  |  
| Airdrop tool  |  [AirShip](https://www.helius.dev/docs/airship/getting-started) (95% cheaper with ZK compression)  |  
## Rate Limits Quick Reference
Rate limits depend on your [plan](https://www.helius.dev/docs/billing/plans). Agents start on the Agent tier with 1,000,000 credits. The Agent tier requires a $1 payment to prevent abuse.  
| Plan  | Price  | Monthly Credits  | RPC Rate Limit  | DAS & Enhanced APIs  |  
| --- | --- | --- | --- | --- |  
| Agent  | $1 signup  | 1M  | 10 req/s  | 2 req/s  |  
| Developer  | $49/mo  | 10M  | 50 req/s  | 10 req/s  |  
| Business  | $499/mo  | 100M  | 200 req/s  | 50 req/s  |  
| Professional  | $999/mo  | 200M  | 500 req/s  | 100 req/s  |  
For detailed rate limits per API, see [Rate Limits](https://www.helius.dev/docs/billing/rate-limits).
## Credits Per API Call  
| API  | Credits  | Notes  |  
| --- | --- | --- |  
| Standard RPC calls  | 1  | Most Solana RPC methods  |  
| `getProgramAccounts`  | 10  | Use DAS API instead when possible  |  
| DAS API  | 10  | All DAS endpoints  |  
| Enhanced Transactions  | 100  | Parsed transaction data  |  
| `getTransactionsForAddress`  | 100  | Developer+ plans only  |  
| Wallet API  | 100  | All Wallet API endpoints  |  
| Priority Fee API  | 1  | Fee estimation  |  
| Sender  | 0  | Free on all plans  |  
| Webhook events  | 1  | Per event delivered  |  
| Webhook management  | 100  | Create, edit, delete  |  
For the full breakdown, see [Credits](https://www.helius.dev/docs/billing/credits).
## Retries and Error Handling
### HTTP Status Codes  
| Code  | Meaning  | Action  |  
| --- | --- | --- |  
| 200  | Success  | Process response  |  
| 400  | Bad request  | Fix request parameters  |  
| 401  | Unauthorized  | Check API key  |  
| 429  | Rate limited  | Back off and retry  |  
| 5xx  | Server error  | Retry with exponential backoff  |  
### Retry Pattern

```
async function heliusRequest(url: string, data: object, maxRetries = 3) {
  for (let attempt = 0; attempt maxRetries; attempt++) {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    if (response.ok) return response.json();

    if (response.status === 429) {
      const retryAfter = response.headers.get('Retry-After');
      const delay = retryAfter ? parseInt(retryAfter) * 1000 : Math.pow(2, attempt) * 1000;
      await new Promise(resolve => setTimeout(resolve, delay));
      continue;


    if (response.status >= 500) {
      await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
      continue;


    throw new Error(`Request failed: ${response.status} ${await response.text()}`);

  throw new Error('Max retries exceeded');


```

### Monitor Credit Usage

```
helius usage --json

```

## Quick Reference
  * **Mainnet RPC** : `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet RPC (Gatekeeper Beta)** : `https://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet RPC** : `https://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet WSS** : `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Mainnet WSS (Gatekeeper Beta)** : `wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Devnet WSS** : `wss://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * **Sender endpoint** : `https://sender.helius-rpc.com/fast`
  * **MCP server** : `https://www.helius.dev/docs/mcp`
  * **Dashboard** : [dashboard.helius.dev](https://dashboard.helius.dev)
  * **Status** : [helius.statuspage.io](https://helius.statuspage.io)


Was this page helpful?
Yes
[ Helius CLIFull-featured command-line interface for Helius. 95+ commands for account management, blockchain queries, transaction sending, webhooks, streaming, staking, and more. Designed for agents and automation. Next ](https://www.helius.dev/docs/agents/cli)
On this page
  * [Quick Start: Agent Signup](https://www.helius.dev/docs/agents/overview#quick-start-agent-signup)
  * [Helius-Specific API Guidance](https://www.helius.dev/docs/agents/overview#helius-specific-api-guidance)
  * [Rate Limits Quick Reference](https://www.helius.dev/docs/agents/overview#rate-limits-quick-reference)
  * [Retries and Error Handling](https://www.helius.dev/docs/agents/overview#retries-and-error-handling)


Assistant
Responses are generated using AI and may contain mistakes.
