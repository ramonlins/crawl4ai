# Source: https://www.helius.dev/docs/glossary

Quick-reference definitions for terms used throughout Helius documentation and on Solana. Each entry links to the relevant product page or guide where applicable. Jump to:
  * [Helius Products & Platform](https://www.helius.dev/docs/glossary#helius-products-and-platform)
  * [Solana Fundamentals](https://www.helius.dev/docs/glossary#solana-fundamentals)
  * [Transaction Mechanics](https://www.helius.dev/docs/glossary#transaction-mechanics)
  * [Tokens & Assets](https://www.helius.dev/docs/glossary#tokens-and-assets)
  * [Connectivity & Streaming](https://www.helius.dev/docs/glossary#connectivity-and-streaming)


## Helius Products and Platform
### Autoscaling
Helius’s automatic credit top-up mechanism for fiat plans. When the monthly credit allowance is exhausted, autoscaling purchases additional credits up to a user-set cap, preventing `429` errors from interrupting production traffic. Crypto plans don’t have autoscaling. Instead, they use [prepaid credits](https://www.helius.dev/docs/billing/autoscaling#crypto-plans), which are purchased manually. See [Autoscaling](https://www.helius.dev/docs/billing/autoscaling).
### Credit
The unit Helius bills API and streaming usage in. RPC methods, DAS calls, and streaming throughput each have a specific credit cost. Every plan includes a monthly credit allowance that resets each billing cycle (unused credits don’t roll over). See [Credits](https://www.helius.dev/docs/billing/credits) for the full cost table.
### DAS API
Digital Asset Standard — an open specification for a unified interface for Solana digital assets (NFTs, compressed NFTs, fungible tokens, inscriptions). Helius’s DAS API implementation returns enriched metadata, ownership, and pricing in a single structured response, eliminating the need for custom parsers over onchain asset data. See [DAS API](https://www.helius.dev/docs/das-api).
### Dedicated Nodes
Private Helius RPC nodes with no rate limits or credit metering, billed at a fixed monthly rate. They suit narrow use cases needing unlimited throughput; most applications are better served by regular Helius RPC due to superior performance, failover, and feature coverage. See [Dedicated Nodes](https://www.helius.dev/docs/dedicated-nodes).
### Enhanced Transactions
Helius’s parsed transaction API that decodes raw Solana transactions into human-readable events — token transfers, NFT sales, swaps, staking operations, and more — without requiring per-program instruction parsers. See [Enhanced Transactions](https://www.helius.dev/docs/enhanced-transactions).
### Enhanced WebSockets
Helius’s persistent WSS streaming service with extended filtering and granular subscription controls beyond standard Solana WebSocket methods. Powered by the same infrastructure that powers LaserStream. See [Enhanced WebSockets](https://www.helius.dev/docs/enhanced-websockets).
### Error Codes
Standard HTTP status codes returned by Helius APIs, with Helius-specific context:
  * `400 Bad Request` — invalid parameters or malformed request (e.g., invalid address format, missing required fields, malformed JSON)
  * `401 Unauthorized` — missing or invalid API key
  * `403 Forbidden` — access denied, typically from IP restrictions, a subscription that doesn’t include the endpoint, or insufficient API-key permissions
  * `404 Not Found` — no data available for the requested resource (normal for identity lookups on unknown wallets)
  * `429 Too Many Requests` — credit allowance exhausted, rate limit exceeded, or concurrent-request limit hit
  * `5xx` — Helius-side issues; retry with exponential backoff

See [Error Codes](https://www.helius.dev/docs/faqs/error-codes) for full details and troubleshooting steps.
### Gatekeeper
Helius’s edge gateway that delivers significantly lower latency than standard RPC calls by routing requests through a globally distributed proxy fleet. Accessed by swapping `mainnet.helius-rpc.com` for `beta.helius-rpc.com` in the RPC URL. See [Gatekeeper](https://www.helius.dev/docs/gatekeeper/overview) and the [Introducing Gatekeeper blog post](https://www.helius.dev/blog/introducing-gatekeeper) for architectural background.
### LaserStream
Helius’s high-performance gRPC streaming service for Solana onchain data, featuring historical replay, multi-region failover, and the richest feature set among Helius streaming products. Official SDKs ship for JavaScript/TypeScript, Rust, and Go. Enhanced WebSockets run on the same infrastructure. See [LaserStream](https://www.helius.dev/docs/laserstream) and the [LaserStream SDK performance blog post](https://www.helius.dev/blog/laserstream-sdks) for a deep dive on SDK benchmarks.
### Priority Fee API
Helius’s fee estimation endpoint that returns recommended priority fee values based on real-time onchain fee markets. Enables competitive fee pricing without guesswork or overpaying during congestion. See [Priority Fee API](https://www.helius.dev/docs/priority-fee-api).
### Rate Limit
The maximum requests per second allowed under a given Helius plan. Rate limits vary by plan tier and by API family (standard RPC, Enhanced APIs, streaming). Exceeding them returns `429 Too Many Requests`. See [Rate Limits](https://www.helius.dev/docs/billing/rate-limits).
### Sender
Helius’s specialized transaction landing service built for low latency traders, combining priority fees, Jito tips, and staked connection routing to maximize landing rates. Available at `https://sender.helius-rpc.com/fast`.
### Shred Delivery
Helius’s service for streaming raw Solana shreds over UDP — the earliest possible onchain signal, delivered before final block assembly. Helius aggregates shreds from a distributed network of validators across regions to minimize the geographic latency variance of any single validator. Useful for high-frequency trading, arbitrage, and other low latency applications. See [Shred Delivery](https://www.helius.dev/docs/shred-delivery) and the blog post [Winning the Millisecond Game: Shreds, LaserStream, and the Edge of Solana](https://www.helius.dev/blog/solana-shreds) for a deep dive on how shreds work.
### Staked Connections
The default transaction submission path for Helius paid plans. Staked connections route transactions to upcoming block leaders via Solana’s protocol-level Stake-Weighted Quality of Service (SWQoS), which grants preferential connection slots based on validator stake and reduces packet drops during congestion. Helius’s paid plans inherit this landing-rate advantage without callers needing to operate a heavily staked validator directly. See [Optimizing Transactions](https://www.helius.dev/docs/sending-transactions/optimizing-transactions) and the blog post [Stake-Weighted Quality of Service: Everything You Need to Know](https://www.helius.dev/blog/stake-weighted-quality-of-service-everything-you-need-to-know).
### Wallet API
Helius’s REST API for querying a Solana wallet’s balances, transaction history, transfers, identity, and funding source — structured, USD-priced responses instead of raw RPC output. It accepts SNS `.sol` and ANS domain names in addition to addresses. See [Wallet API](https://www.helius.dev/docs/wallet-api/overview).
## Solana Fundamentals
### Account
A container that holds data persistently on Solana, identified by a 32-byte public key. All onchain state — user balances, program code, token metadata — lives in accounts, including the programs themselves. Every account has an owner, which is a program that is allowed to modify its data or withdraw lamports, and must maintain a minimum SOL balance (rent-exempt) to persist. See the blog post [The Solana Programming Model: An Introduction to Developing on Solana](https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana) for a deeper dive.
### Airdrop
A grant of SOL or SPL tokens to an address. On Devnet and Testnet, an airdrop typically refers to a small amount of test SOL from a faucet used to fund development wallets; on Mainnet, it refers to bulk token distributions to existing holders. Devnet airdrops are available via the [Devnet faucet](https://www.helius.dev/docs/rpc/devnet-sol).
### Associated Token Account (ATA)
A deterministically derived token account holding a specific SPL token for a given wallet address. Each wallet has at most one ATA per token mint, making ATAs the canonical place to look up a user’s token balance. It is derived using the wallet address and token mint as seeds.
### Commitment Level
The degree of confidence that a transaction has been included onchain:
  * `processed` — seen by the current leader but not yet voted on; can still be dropped if the block loses consensus (~0.4s)
  * `confirmed` — ≥66% stake-weighted validator votes on the block; historically, no confirmed block has reverted (~0.6s)
  * `finalized` — the block has ≥66% votes plus 31 subsequent blocks built atop it (i.e., the Tower BFT maximum lockout), making it effectively irreversible (~13s)

`confirmed` is the recommended default. Use `processed` for UI feedback, `finalized` for high-value operations like exchange deposits or cross-chain bridges. Blockhashes fetched at `finalized` expire sooner than `confirmed` ones, shrinking the window before transaction expiry. See the blog post [What are Solana Commitment Levels?](https://www.helius.dev/blog/solana-commitment-levels) for a deeper dive.
### Compute Units (CU)
Solana’s measure of computational work performed by a transaction, analogous to gas on Ethereum. Each transaction specifies a compute unit limit and a compute unit price (priority fee in microlamports per CU); the product determines total priority fee cost. Exceeding the limit fails the transaction.
### Epoch
A cluster of approximately 432,000 Solana slots — the higher-level organizational interval at which Solana updates its validator set, leader schedule, stake delegations, and reward distributions. Each epoch takes ~2 days at the current slot target. See the blog post [Understanding Slots, Blocks, and Epochs on Solana](https://www.helius.dev/blog/solana-slots-blocks-and-epochs) for a deeper dive.
### Instruction
The smallest unit of work inside a Solana transaction — a single program invocation with the relevant accounts and data. A transaction bundles one or more instructions, executed atomically (all succeed or all revert together). See the blog post [The Solana Programming Model: An Introduction to Developing on Solana](https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana) for a deeper dive.
### Lamport
The smallest unit of SOL: 1 SOL = 1,000,000,000 lamports (10⁻⁹ SOL), named after Leslie Lamport, the Turing Award winner for foundational work in distributed systems. Raw Solana RPC methods return balances and fees in lamports; Helius’s [Wallet API](https://www.helius.dev/docs/wallet-api/overview) handles the conversion automatically. Priority fees are denominated in microlamports — one millionth of a lamport (10⁻¹⁵ SOL).
### Program
An executable account containing compiled sBPF bytecode (i.e., a smart contract on Solana). Programs are stateless — they read and write data accounts they own, and are identified by a program ID (their 32-byte address). Solana ships with a set of native programs (System, Stake, Vote, etc.) built into the runtime; everything else is a user-deployed program. See the blog post [The Solana Programming Model: An Introduction to Developing on Solana](https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana) for a deeper dive.
### Program Derived Address (PDA)
A deterministic address derived from a program ID and a set of seeds. PDAs let programs sign for accounts they control, making them essential for stateful program design. PDAs are intentionally off-curve, so no private key exists for them.
### Rent / Rent-exempt
The SOL balance every Solana account must hold to persist onchain, scaled to the account’s storage size. Accounts must be created rent-exempt: transactions that would leave an account below the minimum fail. Once rent-exempt, the account persists indefinitely without further payments.
### Slot
Solana’s fundamental time unit, during which a designated leader validator has the opportunity to produce a block. Slots currently target 400ms, though actual durations can vary with network conditions. If a leader fails to produce a block during its slot, the slot is skipped — the network moves on to the next slot rather than waiting, so not every slot results in a block. See the blog post [Understanding Slots, Blocks, and Epochs on Solana](https://www.helius.dev/blog/solana-slots-blocks-and-epochs) for a deeper dive.
### Validator
A node on the Solana network that participates in consensus by producing blocks during its assigned leader slots and voting on blocks from other validators. Validators are selected for leader slots proportionally to their active stake.
## Transaction Mechanics
### Address Lookup Table (ALT)
An onchain table of Solana addresses that a versioned transaction can reference using a 1-byte index instead of a full 32-byte pubkey, letting a single transaction reference up to 256 accounts. ALTs are essential for complex DeFi operations that would otherwise exceed transaction size limits.
### Blockhash
A 32-byte hash identifying a recent block, included in every Solana transaction to prove freshness. Blockhashes expire after ~150 slots (~1 minute); transactions with expired blockhashes are rejected. Clients fetch a recent blockhash via [`getLatestBlockhash`](https://www.helius.dev/docs/api-reference/rpc/http/getlatestblockhash) just before signing.
### Priority Fee
A per-compute-unit tip paid to validators to give a transaction priority over others, improving its time to inclusion. Priority fees are set in microlamports per compute unit (µLamports/CU). Helius’s [Priority Fee API](https://www.helius.dev/docs/priority-fee-api) returns real-time estimates based on recent onchain fee markets.
### Shred
The smallest unit of a Solana block. Blocks are split (i.e., shredded) into shreds for parallel propagation across the validator network via [Turbine](https://www.helius.dev/blog/turbine-block-propagation-on-solana). Shred-level access gives the earliest possible onchain signal, ahead of block assembly. See [Shred Delivery](https://www.helius.dev/docs/shred-delivery).
### Versioned Transaction
A newer Solana transaction format that supports Address Lookup Tables, allowing one transaction to reference up to 256 accounts (vs. ~35 in legacy transactions). Versioned transactions are required for most modern DeFi integrations. They are denoted by a version byte at the start of the serialized transaction.
## Tokens and Assets
### Compressed Account
A compressed account is a Solana account whose data is committed to the ledger via transaction logs, with only a hash fingerprint stored in validator state — rather than the full data occupying a traditional account slot on validator disks. Developers can treat compressed accounts like regular accounts; indexers (such as Photon) parse transaction logs to reconstruct current state, and a constant-size Groth16 zero-knowledge proof verifies integrity when accounts are read or modified via ZK Compression. This model is best suited to small-data accounts — larger data (above ~100 bytes) makes compression impractical.
### Compressed NFT (cNFT)
A Solana NFT represented as a leaf in an onchain concurrent Merkle tree rather than its own account. The tree lives in a Solana account and its state transitions are secured by the ledger; the NFT’s current state is derived from transaction history by indexers, which produce Merkle proofs verifiable against the tree’s onchain root. Reading a cNFT therefore requires an indexer like the [DAS API](https://www.helius.dev/docs/das-api) — standard Solana RPC cannot return cNFT data directly. This model reduces mint costs by up to 99% versus standard NFTs.
### Mint Account
The onchain account defining an SPL token’s properties — supply, decimals, and mint/freeze authorities. The mint account’s address is the token’s canonical identifier (its “contract address” in Ethereum terms).
### SPL Token
A token on Solana issued via the Solana Program Library’s (SPL) Token Program. Fungible tokens (USDC, BONK, JUP, etc.) are SPL tokens; standard (non-compressed) NFTs are also SPL tokens, minted with supply 1 and 0 decimals. SPL tokens are roughly the Solana equivalent of ERC-20 and ERC-721 on Ethereum. Token-2022 is a newer program that extends this interface with optional features like transfer fees and confidential transfers.
### Token Account
An onchain account holding a balance of a specific SPL token for a specific owner. A wallet can own arbitrary token accounts, but the convention is to use an Associated Token Account (ATA) — a deterministically derived token account per (wallet, mint) pair created by the Associated Token Account Program.
### Token-2022 (Token Extensions)
A variant of the SPL Token Program supporting optional extensions (e.g., transfer fees, confidential transfers, interest-bearing tokens, non-transferable tokens). Token-2022 runs as a separate onchain program, with its own program ID, but is designed as a compatible successor to the classic Token Program, so SDKs can typically handle both. Mints must be created under the Token-2022 program to use extensions. See the blog post [What are Token Extensions?](https://www.helius.dev/blog/what-is-token-2022).
### ZK Compression
ZK Compression is a Solana primitive developed by Helius and Light Protocol that dramatically reduces onchain storage costs by committing account data to transaction logs in the ledger and storing only a hash fingerprint in validator state. Cryptographic integrity is preserved via constant-size Groth16 zero-knowledge proofs generated from indexed transaction data. This primitive is distinct from compressed NFTs, which use concurrent Merkle trees without zero-knowledge proofs. See [ZK Compression](https://www.helius.dev/docs/zk-compression/introduction) and the blog post [Solana Builders: ZK Compression](https://www.helius.dev/blog/solana-builders-zk-compression) for a deeper dive.
## Connectivity and Streaming
### gRPC
gRPC is a general-purpose, high-performance binary RPC protocol (a recursive acronym for “gRPC Remote Procedure Call”). In Solana contexts, “gRPC” typically refers to Yellowstone gRPC — a streaming interface built on Solana’s Geyser plugin system that exposes account and transaction updates over gRPC. Helius’s [LaserStream](https://www.helius.dev/docs/laserstream) service is built on a Yellowstone-based interface with added features like historical replay, multi-region failover, and managed infrastructure.
### RPC
RPC stands for Remote Procedure Call, which is a general pattern for calling a server method as if it were a local function. In Solana, “RPC” most often refers to an RPC node — a node that tracks Solana’s state, but doesn’t participate in consensus, specializing in serving data requests (i.e., account state, transaction history, transaction submission) over a JSON-RPC interface. Validators, by contrast, produce blocks and vote on them. Helius’s [RPC service](https://www.helius.dev/docs/rpc/overview) is a globally distributed fleet of RPC nodes optimized for production workloads. See the blog post [Solana Nodes — A Primer on Solana RPCs, Validators, and RPC Providers](https://www.helius.dev/blog/solana-nodes-a-primer-on-solana-rpcs-validators-and-rpc-providers) for a deeper dive.
### Webhook
A webhook is an HTTP POST request sent by a server to a receiver URL when a subscribed event occurs — “reverse” HTTP, where the server initiates the call. Helius [Webhooks](https://www.helius.dev/docs/webhooks) push Solana onchain events (transfers, NFT sales, custom program activity) to a registered endpoint, eliminating the need for polling.
### WebSocket (WSS)
A WebSocket is a persistent bidirectional TCP connection upgraded from HTTP, used for push-based streaming of Solana data without repeated HTTP requests. WSS (WebSocket Secure) is the same protocol running over TLS, and is the variant used for production Solana connections. Helius’s standard and [Enhanced WebSockets](https://www.helius.dev/docs/enhanced-websockets) both use WSS.
## Ecosystem
### Anchor
Anchor is a Rust framework for building Solana programs quickly and securely. It handles boilerplate like account serialization, validation, and instruction dispatch through procedural macros, letting developers focus on program logic instead of low-level details. Most Solana developers use Anchor rather than writing programs in native Rust. See the blog post [An Introduction to Anchor: A Beginner’s Guide to Building Solana Programs](https://www.helius.dev/blog/an-introduction-to-anchor-a-beginners-guide-to-building-solana-programs) for a deeper dive.
### IDL
IDL stands for Interface Definition Language. An IDL is a JSON schema describing a Solana program’s instructions, accounts, and data types; clients use it to construct transactions and decode program data without hand-rolling instruction layouts. Anchor generates IDLs automatically and publishes them onchain by default in a dedicated account for public discoverability.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/orb/explore-mint-addresses)[ Helius Solana SDKsOfficial Helius SDKs for Solana development in Node.js and Rust. Simplify blockchain integration with comprehensive APIs, enhanced transactions, and DAS support. Next ](https://www.helius.dev/docs/sdks)
On this page
  * [Helius Products and Platform](https://www.helius.dev/docs/glossary#helius-products-and-platform)
  * [Enhanced Transactions](https://www.helius.dev/docs/glossary#enhanced-transactions)
  * [Associated Token Account (ATA)](https://www.helius.dev/docs/glossary#associated-token-account-ata)
  * [Program Derived Address (PDA)](https://www.helius.dev/docs/glossary#program-derived-address-pda)
  * [Address Lookup Table (ALT)](https://www.helius.dev/docs/glossary#address-lookup-table-alt)
  * [Versioned Transaction](https://www.helius.dev/docs/glossary#versioned-transaction)
  * [Compressed NFT (cNFT)](https://www.helius.dev/docs/glossary#compressed-nft-cnft)
  * [Token-2022 (Token Extensions)](https://www.helius.dev/docs/glossary#token-2022-token-extensions)
  * [Connectivity and Streaming](https://www.helius.dev/docs/glossary#connectivity-and-streaming)


Assistant
Responses are generated using AI and may contain mistakes.
