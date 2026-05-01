# Source: https://www.helius.dev/docs/wallet-api/identity

[Skip to main content](https://www.helius.dev/docs/wallet-api/identity#content-area)
New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
Search...
Ctrl K


##### Get Started


##### Solana RPC Nodes
  * Gatekeeper (Beta)
  * RPC Method Guides


##### Data Streaming & Event Listening
  * Shred Delivery
  * LaserStream
  * Yellowstone gRPC
  * Enhanced Websockets
  * Standard Websockets
  * Webhooks


##### How to Send Transactions
  * Helius Sender (For Traders)
  * Priority Fee API


##### Getting Data
  * [getTransactionsForAddress 🔥](https://www.helius.dev/docs/rpc/gettransactionsforaddress)
  * Digital Asset Standard (DAS)
  * Indexing & Historical Data
  * Enhanced Transactions API
  * Wallet API (Beta)


##### Dedicated Nodes


##### Compression
  * [What is ZK Compression on Solana?](https://www.helius.dev/docs/zk-compression/introduction)
  * Helius AirShip


##### Staking
  * [Programmatic Solana Staking with Helius SDK](https://www.helius.dev/docs/staking/how-to-stake-with-helius-programmatically)


##### Billing


##### Using Orb


##### Resources


  * English


New: Try Gatekeeper (Beta) for significantly lower latency. [Learn More](https://www.helius.dev/docs/gatekeeper/overview)
[Helius Docs home page](https://www.helius.dev)
English
Search...
Ctrl KAsk AI
Search...
Navigation
Wallet API (Beta)
How to Look Up a Solana Wallet Identity
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
##  Overview
The Wallet Identity endpoint identifies known wallet addresses on Solana, including centralized exchanges, DeFi protocols, institutions, and other recognized entities. This is useful for compliance, analytics, and displaying human-readable names for known addresses. Both the single and batch endpoints accept **SNS`.sol` domains** and **ANS custom TLDs** (e.g. `.bonk`, `.poor`, `.abc`) in addition to raw Solana addresses. Domain resolution is mainnet-only.
## [API Reference View detailed API documentation for wallet identity lookup ](https://www.helius.dev/docs/api-reference/wallet-api/identity)
This endpoint uses the same identity system that powers [Orb](https://orbmarkets.io/), our Solana block explorer. Our database includes 12,500+ labels (human-readable primary names, including 2,250+ programs) and 10.7M+ tags (categorical properties like “Binance deposit address” or “Seeker Phone”), and is continuously growing.
##  When to Use This
Use the Wallet Identity API when you need to:
  * **Identify Exchange Wallets** : Determine if a wallet belongs to Binance, Coinbase, Kraken, etc.
  * **Track Protocol Activity** : Identify DeFi protocol wallets and treasury addresses
  * **Compliance & AML**: Flag transactions involving known entities
  * **Analytics** : Categorize wallet types in your data pipeline
  * **User Experience** : Display “Sent to Binance 1” instead of a raw address
  * **Batch Processing** : Look up hundreds of addresses efficiently


##  Quickstart
###  Single Wallet Lookup
Look up identity information for a single wallet address:
  * JavaScript
  * Python
  * cURL



```
const getWalletIdentity = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/identity?api-key=YOUR_API_KEY`;

  const response = await fetch(url);
  if (!response.ok) {
    if (response.status === 404) {
      console.log("No identity found for this address");
      return null;

    throw new Error(`HTTP error! status: ${response.status}`);


  const identity = await response.json();
  console.log(`Found: ${identity.name} (${identity.category})`);
  return identity;


// Example: Binance wallet
getWalletIdentity("HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664");

```


```
import requests

def get_wallet_identity(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/identity"
    headers = {"X-Api-Key": "YOUR_API_KEY"}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print("No identity found for this address")
        return None

    response.raise_for_status()
    identity = response.json()
    print(f"Found: {identity['name']} ({identity['category']})")
    return identity

# Example: Binance wallet
get_wallet_identity("HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664")

```


```
curl "https://api.helius.xyz/v1/wallet/HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664/identity?api-key=YOUR_API_KEY"

```

####  Look Up by Domain Name
You can also pass an SNS `.sol` domain or an ANS custom TLD directly — the endpoint resolves the domain and returns the identity of the owner address:
  * JavaScript
  * Python
  * cURL



```
// Works identically — the endpoint resolves the domain first.
const identity = await getWalletIdentity("toly.sol");

// ANS custom TLD
await getWalletIdentity("miester.bonk");

```


```
# Works identically — the endpoint resolves the domain first.
identity = get_wallet_identity("toly.sol")

# ANS custom TLD
get_wallet_identity("miester.bonk")

```


```
# SNS (.sol) domain
curl "https://api.helius.xyz/v1/wallet/toly.sol/identity?api-key=YOUR_API_KEY"

# ANS custom TLD
curl "https://api.helius.xyz/v1/wallet/miester.bonk/identity?api-key=YOUR_API_KEY"

```

The single-endpoint response is the standard identity object for the **resolved** address — there is no `inputDomain` marker. If you need to correlate inputs with outputs (for example, when looking up many domains at once), use the batch endpoint.
Domain resolution is mainnet-only. On devnet/testnet, a domain input to this endpoint returns `400`. Positive resolutions are cached for up to 2 hours, so a recently-transferred domain may briefly resolve to the prior owner’s identity.
###  Batch Lookup (Up to 100 Entries)
Look up multiple entries in a single request for better performance. Each entry can be either an address or a domain name:
  * JavaScript
  * Python
  * cURL



```
const batchIdentityLookup = async (addresses) => {
  const url = "https://api.helius.xyz/v1/wallet/batch-identity?api-key=YOUR_API_KEY";

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"

    body: JSON.stringify({ addresses })
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);


  const identities = await response.json();
  return identities;


// Example: Mix addresses and domains in a single request
const addresses = [
  "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664", // Binance (address)
  "toly.sol"// SNS domain
  "miester.bonk"                                   // ANS custom TLD


batchIdentityLookup(addresses).then(identities => {
  identities.forEach(identity => {
    if (identity.unresolved) {
      console.log(`${identity.inputDomain}: could not be resolved`);
      return;

    const label = identity.inputDomain
 `${identity.inputDomain} → ${identity.address}`
 identity.address;
    console.log(`${label}: ${identity.name}`);
  });
});

```


```
import requests

def batch_identity_lookup(addresses: list[str]):
    url = "https://api.helius.xyz/v1/wallet/batch-identity"
    headers = {
        "X-Api-Key": "YOUR_API_KEY",
        "Content-Type": "application/json"


    response = requests.post(
        url,
        headers=headers,
        json={"addresses": addresses}


    response.raise_for_status()
    return response.json()

# Example: Mix addresses and domains in a single request
addresses = [
    "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",  # Binance (address)
    "toly.sol"# SNS domain
    "miester.bonk"                                    # ANS custom TLD


identities = batch_identity_lookup(addresses)
for identity in identities:
    if identity.get("unresolved"):
        print(f"{identity['inputDomain']}: could not be resolved")
        continue
    label = f"{identity['inputDomain']} -> {identity['address']}" if identity.get("inputDomain") else identity["address"]
    print(f"{label}: {identity['name']}")

```


```
curl -X POST "https://api.helius.xyz/v1/wallet/batch-identity?api-key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "addresses": [
      "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
      "toly.sol",
      "miester.bonk"



```

##  Response Format
###  Successful Response

```

  "address": "HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664",
  "type": "exchange",
  "name": "Binance 1",
  "category": "Centralized Exchange",
  "tags": ["Centralized Exchange"]


```

###  Batch: Resolved Domain Entry
In a batch response, any entry whose input was a domain name carries an additional `inputDomain` field so you can correlate the response back to the original request:

```

  "address": "7v91N7iZ9mNicL8WfG6cgSCKyRXydQjLh6UYBWwm6y1Q",
  "type": "wallet",
  "name": "toly",
  "category": "Key Opinion Leader",
  "tags": ["Key Opinion Leader"],
  "inputDomain": "toly.sol"


```

###  Batch: Unresolved Domain Entry
When a domain in a batch request cannot be resolved, the batch does not fail — the entry is returned in place with `address: null`, `type: "unknown"`, and `unresolved: true`. Request order is preserved.

```

  "address": null,
  "type": "unknown",
  "inputDomain": "nonexistent-xyz.sol",
  "unresolved": true


```

###  404 Response (Unknown Wallet or Unresolvable Domain)
On the single endpoint, a 404 is returned if the wallet has no identity entry **or** if a domain input could not be resolved:

```

  "error": "No identity information available for this address",
  "code": 404


```


```

  "error": "Domain 'nonexistent-xyz.sol' could not be resolved",
  "code": 404


```

##  Identity Categories
Wallets can be classified into the following categories powered by the Orb identity database:
###  Account Tag Types  
| Category  | Description  | Examples  |  
| --- | --- | --- |  
| Centralized Exchange  | CEX wallets and hot wallets  | Binance 1, Coinbase 1, Kraken, OKX Exchange 1, Bybit Hot Wallet  |  
| Cross-chain Bridge  | Bridge protocol addresses  | Wormhole Bridge, AllBridge, Portal Bridge, deBridge  |  
| DeFi  | DeFi protocol addresses  | Jupiter, Raydium, Orca, Marinade Finance, Kamino  |  
| Key Opinion Leader  | Notable individuals and influencers  | Anatoly Yakovenko, Raj Gokal  |  
| Market Maker  | Market making firms  | Jump Trading, Wintermute, GSR Markets  |  
| Trading Firm  | Proprietary trading firms  | Alameda Research, DRW Trading  |  
| Validator  | Validator and stake pool addresses  | Coinbase Validator, Jito Validator, Figment Validator  |  
| Treasury  | Project and protocol treasuries  | Marinade Treasury, Helium Treasury, Solana Foundation Treasury  |  
| DAO  | Decentralized autonomous organizations  | Mango DAO, Grape DAO, MonkeDAO Treasury  |  
| NFT  | NFT marketplaces and projects  | Magic Eden, Tensor, OpenSea Solana, DeGods Treasury  |  
| Stake Pool  | Liquid staking pool addresses  | Marinade Stake Pool, Jito Stake Pool, BlazeStake  |  
| Multisig  | Multi-signature wallets  | Squads Multisig, Solana Foundation Multisig  |  
| Oracle  | Price feed and oracle providers  | Pyth Network, Switchboard Oracle, Chainlink Solana  |  
| Game  | Gaming and GameFi projects  | Star Atlas, Aurory, Genopets Treasury  |  
| Payments  | Payment processors  | Solana Pay, Sphere, Helio Pay  |  
| Tools  | Developer tools and utilities  | Phantom Wallet, Backpack, Solflare Wallet  |  
| Airdrop  | Airdrop distribution addresses  | Jupiter Airdrop, Pyth Airdrop Distributor  |  
| Governance  | Governance program addresses  | Realms Governance, SPL Governance  |  
| Authority  | Program authorities and admins  | Token Program Authority, Metaplex Authority  |  
| Jito  | Jito-specific addresses  | Jito Tip 1, Jito Tip 2, Jito MEV Payment  |  
| Memecoin  | Memecoin projects  | Bonk Treasury, Dogwifhat, Book of Meme  |  
| Casino & Gambling  | Gambling and casino dApps  | Stake.com Hot Wallet, Rollbit, DexSport  |  
| DePIN  | Decentralized physical infrastructure  | Helium Network, Render Network, Hivemapper  |  
| Proprietary AMM  | Custom AMM implementations  | Phoenix DEX, GooseFX  |  
| Restaking  | Restaking protocols  | Solayer, Fragmetric  |  
| Vault  | Vault and custody addresses  | Solend Vault, Tulip Vault, Francium Vault  |  
| Fees  | Fee collection addresses  | Jupiter Fee Collector, Raydium Fees  |  
| Fundraise  | Fundraising and ICO addresses  | Token Sale Wallet, Fundraise Multisig  |  
| Genesis Block Distribution  | Genesis distribution addresses  | Solana Genesis Distribution  |  
| Non-Circulating Supply  | Non-circulating token addresses  | Team Vesting Wallet, Foundation Reserve  |  
| Transaction Sending  | Transaction sending services  | Jito Tip 1, Jito Tip 2, Helius Sender Tip 1  |  
| System  | Solana system programs  | System Program, Config Program  |  
| X402  | X402 protocol addresses  | X402 Protocol  |  
| Other  | Uncategorized known addresses  | Various known wallets  |  
###  Malicious Categories  
| Category  | Description  | Examples  |  
| --- | --- | --- |  
| Exploiter, Hackers & Scams  | Known exploit and hack addresses  | Wormhole Exploiter Wallet, SagaDAO Hacker Wallet, Mango Exploiter  |  
| Hacker  | Confirmed hacker addresses  | Solana Hack 2022, DeFi Protocol Hacker  |  
| Rugger  | Rug pull perpetrators  | Squid Game Token Rugger, Known Rug Pull Wallet  |  
| Scammer  | Confirmed scam addresses  | Fake Airdrop Scammer, Phishing Scam Wallet  |  
| Spam  | Spam token creators  | Spam Token Creator, Airdrop Spammer  |  
###  Program Categories
Programs (smart contracts) are classified separately:  
| Category  | Description  | Examples  |  
| --- | --- | --- |  
| Swap  | Token swap protocols  | Jupiter, Raydium, Orca  |  
| DeFi  | General DeFi protocols  | Drift, Mango  |  
| Borrow Lend  | Lending protocols  | Solend, MarginFi  |  
| NFT  | NFT marketplaces  | Magic Eden, Tensor  |  
| Staking  | Staking programs  | Marinade, Jito  |  
| Bridge  | Cross-chain bridges  | Wormhole, AllBridge  |  
| Aggregator  | DEX aggregators  | Jupiter Aggregator  |  
| Perpetuals  | Perpetual futures  | Drift, Mango  |  
| Oracle  | Oracle providers  | Pyth, Switchboard  |  
| Launchpad  | Token launchpads  | Raydium Launchpad  |  
| Governance  | Governance programs  | SPL Governance  |  
| Game or Casino  | Gaming programs  | Star Atlas  |  
| Prediction Market  | Prediction markets  | Drift Predictions  |  
| Payments  | Payment protocols  | Solana Pay  |  
| Privacy  | Privacy protocols  | Elusiv  |  
| Compression  | State compression  | Bubblegum  |  
| Infrastructure  | Core infrastructure  | Metaplex  |  
| Tools  | Developer tools  | Clockwork  |  
| RWA  | Real-world assets  | Ondo Finance  |  
| DePIN  | Decentralized infrastructure  | Helium, Render  |  
| DeSci  | Decentralized science  | VitaDAO  |  
| Airdrop  | Airdrop programs  | Merkle distributors  |  
| Web3  | Web3 applications  | Various  |  
| Native  | Solana native programs  | System Program  |  
| Proprietary AMM  | Custom AMM designs  | Phoenix  |  
| Trading Sniper  | Trading bots  | MEV bots  |  
| Arbitrage or Sandwich Bot  | MEV and arb bots  | Jito bundles  |  
| Spam  | Spam programs  | Spam tokens  |  
| Other  | Uncategorized programs  | Various  |  
##  Use Cases
###  Flag Exchange Deposits
Identify when funds are sent to a centralized exchange:

```
const checkIfExchange = async (address) => {
  try {
    const identity = await getWalletIdentity(address);
    if (identity identity.category === "Centralized Exchange") {
      console.log(`Funds sent to ${identity.name}`);
      return true;

catch (error) {
    // Not a known exchange

  return false;


```

###  Display Human-Readable Names
Show friendly names in your UI instead of addresses:

```
const getDisplayName = async (address) => {
  try {
    const identity = await getWalletIdentity(address);
    return identity ? identity.name : shortenAddress(address);
catch (error) {
    return shortenAddress(address);



// Usage in UI
const displayName = await getDisplayName("HXsKP7wrBWaQ8T2Vtjry3Nj3oUgwYcqq9vrHDM12G664");
// Returns: "Binance 1" instead of "HXsKP...G664"

```

###  Batch Process Transaction Counterparties
Efficiently identify all counterparties in a list of transactions:

```
const identifyTransactionCounterparties = async (transactions) => {
  // Extract all unique addresses
  const addresses = [...new Set(
    transactions.map(tx => tx.counterparty)
  )];

  // Batch lookup (up to 100 at a time)
  const allIdentities = [];
  for (let i = 0; i addresses.length; i += 100) {
    const chunk = addresses.slice(i, i + 100);
    const identities = await batchIdentityLookup(chunk);
    allIdentities.push(...identities);


  // Create a map for quick lookup
  const identityMap = new Map(
    allIdentities.map(id => [id.address, id])


  // Enrich transactions with identity info
  return transactions.map(tx => ({
    ...tx,
    counterpartyName: identityMap.get(tx.counterparty)?.name || "Unknown"
  }));


```

##  Best Practices
Use Batch Endpoint for Multiple Lookups
When looking up more than one address, always use the batch endpoint (`POST /v1/wallet/batch-identity`). It’s significantly faster and more efficient than making individual requests.
Handle 404 Responses Gracefully
Not all wallets will have identity information. Design your application to handle 404 responses and fall back to displaying the raw address.
Cache Results
Identity data changes infrequently. Cache results locally to reduce API calls and improve performance.
Batch Size Limits
The batch endpoint supports up to 100 addresses per request. For larger datasets, chunk your requests accordingly.
##  Common Errors  
| Error Code  | Description  | Solution  |  
| --- | --- | --- |  
| 400  | Invalid wallet address or domain format, or domain input on non-mainnet  | Verify the input is a valid base58 Solana address or a well-formed domain (e.g. `toly.sol`), and that you’re targeting mainnet  |  
| 401  | Missing or invalid API key  | Check your API key is included in the request  |  
| 404  | No identity found, or domain could not be resolved  | Single endpoint only — the wallet has no identity entry, or the domain does not exist. In batch requests, unresolvable domains are returned as `unresolved: true` entries rather than 404  |  
| 429  | Rate limit exceeded  | Reduce request frequency or upgrade your plan  |  
##  Need Help?
## [API Reference View detailed API specs with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api/identity)
## [Contact Support Get help from our team ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/overview)[ Wallet BalancesRetrieve all token and NFT balances for any Solana wallet with USD values, logos, and metadata. Sorted by value for easy portfolio tracking. Next ](https://www.helius.dev/docs/wallet-api/balances)
Ctrl+I
On this page
  * [Look Up by Domain Name](https://www.helius.dev/docs/wallet-api/identity#look-up-by-domain-name)
  * [Batch Lookup (Up to 100 Entries)](https://www.helius.dev/docs/wallet-api/identity#batch-lookup-up-to-100-entries)
  * [Batch: Resolved Domain Entry](https://www.helius.dev/docs/wallet-api/identity#batch-resolved-domain-entry)
  * [Batch: Unresolved Domain Entry](https://www.helius.dev/docs/wallet-api/identity#batch-unresolved-domain-entry)
  * [404 Response (Unknown Wallet or Unresolvable Domain)](https://www.helius.dev/docs/wallet-api/identity#404-response-unknown-wallet-or-unresolvable-domain)
  * [Flag Exchange Deposits](https://www.helius.dev/docs/wallet-api/identity#flag-exchange-deposits)
  * [Display Human-Readable Names](https://www.helius.dev/docs/wallet-api/identity#display-human-readable-names)
  * [Batch Process Transaction Counterparties](https://www.helius.dev/docs/wallet-api/identity#batch-process-transaction-counterparties)


Assistant
Responses are generated using AI and may contain mistakes.
