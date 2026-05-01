# Source: https://www.helius.dev/docs/agents/cli/commands

Every command supports `--json` for machine-readable output and `--api-key <key>` / `--network <net>` global overrides. See [Global Options](https://www.helius.dev/docs/agents/cli#global-options) for details.
## Account Management
Create Helius accounts, generate keypairs, authenticate, upgrade plans, and pay renewals.  
| Command  | Description  |  
| --- | --- |  
| `helius keygen`  | Generate a new Solana keypair  |  
| `helius signup`  | Create a Helius account (requires `--email`, `--first-name`, `--last-name`; supports `--plan`, `--period`, `--coupon`)  |  
| `helius login`  | Authenticate with an existing wallet  |  
| `helius upgrade`  | Upgrade your plan (requires `--email`, `--first-name`, `--last-name`; supports `--plan`, `--period`, `--coupon`)  |  
| `helius pay <id>`  | Pay an existing payment intent (e.g., renewal)  |  
## Project & API Key Management
List projects, create and manage API keys, check credit usage, and get RPC endpoints.  
| Command  | Description  |  
| --- | --- |  
| `helius projects`  | List all projects  |  
| `helius project [id]`  | Get project details  |  
| `helius apikeys [project-id]`  | List API keys for a project  |  
| `helius apikeys create [project-id]`  | Create a new API key  |  
| `helius usage [project-id]`  | Show credits usage  |  
| `helius rpc [project-id]`  | Show RPC endpoints  |  
## Configuration
Manage local CLI config — API key, network, default project, and stored credentials.  
| Command  | Description  |  
| --- | --- |  
| `helius config show`  | Show current config (`--reveal` to show full API key)  |  
| `helius config set-api-key <key>`  | Set Helius API key  |  
| `helius config set-network <net>`  | Set network (mainnet or devnet)  |  
| `helius config set-project <id>`  | Set default project ID  |  
| `helius config clear`  | Clear all configuration  |  
## Balance & Tokens
Query native SOL balances, fungible token holdings, and top token holders.  
| Command  | Description  |  
| --- | --- |  
| `helius balance <address>`  | Get native SOL balance  |  
| `helius tokens <address>`  | Get fungible token balances (`--limit`)  |  
| `helius token-holders <mint>`  | Get top holders of a token (`--limit`)  |  
## Transactions
Parse transactions into human-readable format, fetch enhanced history, and estimate priority fees.  
| Command  | Description  |  
| --- | --- |  
| `helius tx parse <signatures...>`  | Parse transaction(s) into human-readable format  |  
| `helius tx history <address>`  | Get enhanced transaction history (`--limit`, `--before`, `--type`)  |  
| `helius tx fees`  | Get priority fee estimates (`--accounts`)  |  
## Digital Assets (DAS API)
Query NFTs, compressed NFTs, fungible tokens, and token accounts using the Digital Asset Standard API.  
| Command  | Description  |  
| --- | --- |  
| `helius asset get <id>`  | Get asset details by mint address  |  
| `helius asset batch <ids...>`  | Get multiple assets  |  
| `helius asset owner <address>`  | Get assets by owner (`--page`, `--limit`)  |  
| `helius asset creator <address>`  | Get assets by creator (`--verified`)  |  
| `helius asset authority <address>`  | Get assets by update authority  |  
| `helius asset collection <address>`  | Get assets in a collection  |  
| `helius asset search`  | Search with filters (`--owner`, `--creator`, `--compressed`, `--burnt`)  |  
| `helius asset proof <id>`  | Get Merkle proof for a compressed NFT  |  
| `helius asset proof-batch <ids...>`  | Batch Merkle proofs  |  
| `helius asset editions <mint>`  | Get NFT editions  |  
| `helius asset signatures <id>`  | Get transaction signatures for an asset  |  
| `helius asset token-accounts`  | Query token accounts (`--owner`, `--mint`)  |  
## Wallet API
Look up wallet identities, get portfolio balances with USD values, view transaction history, and trace funding sources.  
| Command  | Description  |  
| --- | --- |  
| `helius wallet identity <address-or-domain>`  | Look up who owns a wallet (accepts `.sol` and ANS domains)  |  
| `helius wallet identity-batch <addrs-or-domains...>`  | Batch identity lookup (mixes addresses and domains)  |  
| `helius wallet balances <address>`  | Get all token balances with USD values (`--show-nfts`)  |  
| `helius wallet history <address>`  | Transaction history with balance changes (`--type`, `--limit`)  |  
| `helius wallet transfers <address>`  | Token transfers with sender/recipient info  |  
| `helius wallet funded-by <address>`  | Find original funding source  |  
## Webhooks
Create, update, list, and delete real-time HTTP webhooks for monitoring on-chain events.  
| Command  | Description  |  
| --- | --- |  
| `helius webhook list`  | List all webhooks  |  
| `helius webhook get <id>`  | Get webhook details  |  
| `helius webhook create`  | Create a webhook (`--url`, `--accounts`, `--types`, `--webhook-type`)  |  
| `helius webhook update <id>`  | Update a webhook  |  
| `helius webhook delete <id>`  | Delete a webhook  |  
## Transaction Sending
Broadcast signed transactions, send via Helius Sender for ultra-low latency, and estimate compute units.  
| Command  | Description  |  
| --- | --- |  
| `helius send broadcast <base64-tx>`  | Broadcast a signed transaction and poll for confirmation  |  
| `helius send raw <base64-tx>`  | Send a raw transaction  |  
| `helius send sender <base64-tx>`  | Send via Helius Sender for ultra-low latency (`--region`)  |  
| `helius send poll <signature>`  | Poll transaction status until confirmed  |  
| `helius send compute-units <base64-tx>`  | Simulate and return compute unit estimate  |  
## WebSocket Subscriptions
Stream real-time account changes, transaction logs, slot updates, and program activity over WebSockets.  
| Command  | Description  |  
| --- | --- |  
| `helius ws account <address>`  | Stream account change notifications  |  
| `helius ws logs`  | Stream log notifications (`--mentions`)  |  
| `helius ws slot`  | Stream slot notifications  |  
| `helius ws signature <sig>`  | Stream signature confirmation  |  
| `helius ws program <program-id>`  | Stream program account changes  |  
## Program Accounts
Fetch accounts owned by a Solana program, with optional filtering and auto-pagination.  
| Command  | Description  |  
| --- | --- |  
| `helius program accounts <program-id>`  | Get accounts owned by a program (`--data-size`, `--limit`)  |  
| `helius program accounts-all <program-id>`  | Get all program accounts (auto-paginate)  |  
| `helius program token-accounts <owner>`  | Get token accounts by owner  |  
## Staking
Create stake transactions, unstake, withdraw, and inspect Helius stake accounts.  
| Command  | Description  |  
| --- | --- |  
| `helius stake create <amount>`  | Create a stake transaction (SOL)  |  
| `helius stake unstake <stake-account>`  | Unstake  |  
| `helius stake withdraw <stake-account>`  | Withdraw staked SOL  |  
| `helius stake accounts <wallet>`  | List Helius stake accounts  |  
| `helius stake withdrawable <stake-account>`  | Check withdrawable amount  |  
| `helius stake instructions <amount>`  | Get stake instructions  |  
| `helius stake unstake-instruction <account>`  | Get unstake instruction  |  
| `helius stake withdraw-instruction <account>`  | Get withdraw instruction  |  
## ZK Compression
Query compressed accounts, token balances, Merkle proofs, validity proofs, and compression signatures.  
| Command  | Description  |  
| --- | --- |  
| `helius zk account <addr-or-hash>`  | Get compressed account  |  
| `helius zk accounts-by-owner <owner>`  | Get compressed accounts by owner  |  
| `helius zk balance <addr-or-hash>`  | Get compressed balance  |  
| `helius zk balance-by-owner <owner>`  | Get compressed balance by owner  |  
| `helius zk token-holders <mint>`  | Get compressed token holders  |  
| `helius zk token-balance <account>`  | Get compressed token balance  |  
| `helius zk token-accounts-by-owner <owner>`  | Get compressed token accounts by owner  |  
| `helius zk token-accounts-by-delegate <delegate>`  | Get compressed token accounts by delegate  |  
| `helius zk token-balances-by-owner <owner>`  | Get compressed token balances (V2)  |  
| `helius zk proof <addr-or-hash>`  | Get compressed account proof  |  
| `helius zk proofs <addresses...>`  | Get multiple proofs  |  
| `helius zk multiple-accounts <addresses...>`  | Get multiple compressed accounts  |  
| `helius zk address-proofs <addresses...>`  | Get new address proofs (V2)  |  
| `helius zk signatures-account <account>`  | Signatures for compressed account  |  
| `helius zk signatures-address <address>`  | Signatures for address  |  
| `helius zk signatures-owner <owner>`  | Signatures for owner  |  
| `helius zk signatures-token-owner <owner>`  | Signatures for token owner  |  
| `helius zk latest-signatures`  | Latest compression signatures  |  
| `helius zk latest-non-voting`  | Latest non-voting signatures  |  
| `helius zk tx <signature>`  | Transaction with compression info  |  
| `helius zk validity-proof`  | Get validity proof (`--hashes`, `--addresses`)  |  
| `helius zk indexer-health`  | Check ZK indexer health  |  
| `helius zk indexer-slot`  | Get ZK indexer slot  |  
| `helius zk signatures-for-asset <id>`  | Compression signatures for asset  |  
## Account & Network
Inspect individual Solana accounts, check network status, and fetch block details.  
| Command  | Description  |  
| --- | --- |  
| `helius account <address>`  | Get Solana account info  |  
| `helius network-status`  | Get Solana network status  |  
| `helius block <slot>`  | Get block details by slot number  |  
## Solana Improvement Documents
Browse and read SIMD proposals that define changes to the Solana protocol.  
| Command  | Description  |  
| --- | --- |  
| `helius simd list`  | List all SIMD proposals  |  
| `helius simd get <number>`  | Read a specific SIMD by number  |  
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/agents/cli)[ Helius MCPMCP server for Helius — 10 routed tools that give AI assistants full access to Solana querying, transaction sending, webhooks, streaming, wallet analysis, and autonomous account signup. Next ](https://www.helius.dev/docs/agents/mcp)
On this page
  * [Project & API Key Management](https://www.helius.dev/docs/agents/cli/commands#project-%26-api-key-management)
  * [Digital Assets (DAS API)](https://www.helius.dev/docs/agents/cli/commands#digital-assets-das-api)
  * [WebSocket Subscriptions](https://www.helius.dev/docs/agents/cli/commands#websocket-subscriptions)
  * [Solana Improvement Documents](https://www.helius.dev/docs/agents/cli/commands#solana-improvement-documents)


Assistant
Responses are generated using AI and may contain mistakes.
