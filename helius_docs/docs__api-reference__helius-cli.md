# Source: https://www.helius.dev/docs/api-reference/helius-cli

The [Helius CLI](https://www.npmjs.com/package/helius-cli) is a full-featured command-line interface for the Helius platform. It provides 95+ commands for account management, blockchain data queries, transaction sending, webhooks, real-time streaming, staking, ZK Compression, and more — with machine-readable JSON output for every command.
**Using an MCP-compatible AI tool?** The [Helius MCP server](https://www.helius.dev/docs/agents/mcp) is the recommended way for AI agents to interact with Helius — it provides 10 routed tools with structured inputs/outputs, including built-in account signup. Use the CLI for shell scripts, CI/CD pipelines, or when MCP is not available.
## Installation

```
npm install -g helius-cli

```

## Quick Start — Existing Users
If you already have a Helius API key, just set it and go:

```
helius config set-api-key YOUR_API_KEY

```

Get your key from [dashboard.helius.dev](https://dashboard.helius.dev). That’s it — skip the signup steps below.
## Quick Start — New Users
Generate a keypair

```
helius keygen

```

Output:

```
✓ Keypair generated
Path: ~/.helius/keypair.json
Address: 7xKp...3nQm

To use this wallet, fund it with:
  • ~0.001 SOL for transaction fees
  • 1 USDC for Helius signup

```

Fund the wallet
Send funds to the wallet address from the previous step:  
| Asset  | Amount  | Purpose  |  
| --- | --- | --- |  
| SOL  | ~0.001  | Transaction fees + rent  |  
| 1+  | Plan payment (see pricing below)  |  
Create account

```
helius signup

```

This checks balances, sends the USDC payment, and creates your Helius account and project.
Get your API keys and endpoints

```
helius projects
helius apikeysproject-id
helius rpcproject-id

```

Your API key is sensitive information that grants access to your Helius account. Never expose it in client-side code, public repos, or browser-accessible areas.
## Plans & Pricing
You can purchase any Helius shared plan directly through the CLI. Pass `--plan` during signup or use `helius upgrade` later:  
| Plan  | Price  | Credits  |  `--plan` value  |  
| --- | --- | --- | --- |  
| Agent (Basic)  | $1 one-time  | 1,000,000  | `basic`  |  
| Developer  | $49/mo  | 10,000,000  | `developer`  |  
| Business  | $499/mo  | 100,000,000  | `business`  |  
| Professional  | $999/mo  | 200,000,000  | `professional`  |  
The **Agent** plan (`basic`) is the default. It costs $1 (paid in USDC) to prevent abuse and gives you 1,000,000 credits. For higher rate limits and more credits, sign up with a paid plan or upgrade later.
### Signup with a specific plan

```
# Default: Agent plan ($1)
helius signup

# Developer plan ($49/mo)
helius signup --plan developer --email you@example.com --first-name Jane --last-name Doe

# Yearly billing (paid plans only)
helius signup --plan business --period yearly --email you@example.com --first-name Jane --last-name Doe

```

### Upgrade an existing account

```
helius upgrade --plan developer --email you@example.com --first-name Jane --last-name Doe

```

### Pay a renewal
When a subscription renewal is due (monthly or yearly), Helius creates a **payment intent** — a pending payment with a unique ID, amount, and expiration. You’ll receive the payment intent ID via email or the [dashboard](https://dashboard.helius.dev).

```
helius paypayment-intent-id

```

The command fetches the intent details, shows the amount and expiration, asks for confirmation, then sends the USDC payment from your keypair wallet.
## Command Reference
The CLI provides 95+ commands across 14 categories. Every command supports `--json` for machine-readable output and `--api-key <key>` / `--network <net>` global overrides.
## [Full Command Reference All 95+ commands — account management, blockchain queries, DAS API, wallet, webhooks, transaction sending, WebSockets, staking, ZK compression, and more ](https://www.helius.dev/docs/agents/cli/commands)
## JSON Output Mode
Add `--json` to any command for machine-readable output:

```
helius projects --json
helius balance Gh9ZwEm... --json
helius asset owner 86xCnPe... --json

```

Example:

```

  "projects": [

      "id": "67b9d260-726b-4ba3-8bb0-dbbf794641bf",
      "name": "My Project",
      "plan": "free"




```

## Exit Codes
Agents should check exit codes for reliable automation:  
| Code  | Meaning  |  
| --- | --- |  
| 0  | Success  |  
| 1  | General error  |  
| 10  | Not logged in  |  
| 11  | Keypair not found  |  
| 20  | Insufficient SOL  |  
| 21  | Insufficient USDC  |  
| 30  | No projects found  |  
| 31  | Project not found  |  
| 40  | API error  |  
## Configuration
Config is stored in `~/.helius/`:

```
~/.helius/
├── config.json    # JWT token, API key, network, default project
└── keypair.json   # Solana keypair (if generated with keygen)

```

Manage config with:

```
helius config show              # View current config
helius config set-api-keykey # Set API key
helius config set-network devnet # Switch to devnet
helius config set-projectid  # Set default project
helius config clear             # Reset everything

```

### API Key Resolution Order
API keys are resolved in this order:
  1. `--api-key <key>` flag (per-command override)
  2. `HELIUS_API_KEY` environment variable
  3. `~/.helius/config.json` (set via `helius config set-api-key`)


## Global Options
All commands accept these flags:  
| Flag  | Description  |  
| --- | --- |  
| `--api-key <key>`  | Override the configured API key  |  
| `--network <net>`  | Override the network (`mainnet` or `devnet`)  |  
| `--json`  | Output in JSON format  |  
| `-k, --keypair <path>`  | Path to keypair file (commands that require signing)  |  
## Full Agent Workflow

```
# Step 1: Generate keypair
helius keygen

# Step 2: Fund wallet externally
# Send ~0.001 SOL + 1 USDC to the address

# Step 3: Create account
helius signup

# Step 4: Get API keys
helius projects
helius apikeysproject-id

# Step 5: Get RPC endpoints
helius rpcproject-id

# Step 6: Start querying
helius balanceaddress
helius asset ownerwallet-address
helius tx historyaddress --limit 10

```

## Next Steps
## [Agents Overview API guidance, workflows, and error handling for agents ](https://www.helius.dev/docs/agents/overview)
## [Helius MCP Connect AI tools directly to Helius APIs ](https://www.helius.dev/docs/agents/mcp)
## [View Plans Understand Helius plans and upgrade options ](https://www.helius.dev/docs/billing/plans)
## [Dashboard Monitor your API usage and manage keys ](https://dashboard.helius.dev)
## Support
## [Discord Community Join our Discord for real-time help and community support ](https://discord.com/invite/6GXdee3gBj)
Email Support Contact our support team directly
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/agents/overview)[ Command ReferenceFull reference for all 95+ Helius CLI commands — account management, blockchain queries, transactions, DAS API, wallet, webhooks, streaming, staking, ZK compression, and more. Next ](https://www.helius.dev/docs/agents/cli/commands)
On this page
  * [Quick Start — Existing Users](https://www.helius.dev/docs/agents/cli#quick-start-%E2%80%94-existing-users)
  * [Quick Start — New Users](https://www.helius.dev/docs/agents/cli#quick-start-%E2%80%94-new-users)
  * [Signup with a specific plan](https://www.helius.dev/docs/agents/cli#signup-with-a-specific-plan)
  * [Upgrade an existing account](https://www.helius.dev/docs/agents/cli#upgrade-an-existing-account)
  * [API Key Resolution Order](https://www.helius.dev/docs/agents/cli#api-key-resolution-order)


Assistant
Responses are generated using AI and may contain mistakes.
