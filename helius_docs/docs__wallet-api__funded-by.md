# Source: https://www.helius.dev/docs/wallet-api/funded-by

**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
## Overview
The Wallet Funding Source endpoint identifies who originally funded a Solana wallet by analyzing its first incoming SOL transfer. This is valuable for attribution, compliance, understanding wallet relationships, and identifying exchange-funded wallets.
## [API Reference View detailed API documentation for funding source lookup ](https://www.helius.dev/docs/api-reference/wallet-api/funded-by)
## When to Use This
Use the Wallet Funding Source API for:
  * **Wallet Attribution** : Track where new wallets are being funded from
  * **Exchange Detection** : Identify wallets funded directly from centralized exchanges
  * **Compliance & AML**: Flag wallets funded by known entities for compliance checks
  * **Bot Detection** : Identify bot farms funded from the same source
  * **Airdrop Analysis** : Track which wallets received initial funding from a project
  * **Sybil Detection** : Find clusters of wallets funded by the same address


## Quickstart
### Basic Funding Lookup
Find out who funded a wallet:
  * JavaScript
  * Python
  * cURL



```
const getWalletFundingSource = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/funded-by?api-key=YOUR_API_KEY`;

  const response = await fetch(url);

  if (response.status === 404) {
    console.log('No funding transaction found for this wallet');
    return null;


  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);


  const funding = await response.json();

  console.log(`Funding Source: ${funding.funderName || funding.funder}`);
  console.log(`Funder Type: ${funding.funderType || 'Unknown'}`);
  console.log(`Initial Amount: ${funding.amount} SOL`);
  console.log(`Date: ${new Date(funding.timestamp * 1000).toLocaleString()}`);
  console.log(`Transaction: ${funding.explorerUrl}`);

  return funding;


getWalletFundingSource("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
import requests
from datetime import datetime

def get_wallet_funding_source(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/funded-by"
    headers = {"X-Api-Key": "YOUR_API_KEY"}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print('No funding transaction found for this wallet')
        return None

    response.raise_for_status()
    funding = response.json()

    print(f"Funding Source: {funding.get('funderName') or funding['funder']}")
    print(f"Funder Type: {funding.get('funderType', 'Unknown')}")
    print(f"Initial Amount: {funding['amount']} SOL")
    print(f"Date: {datetime.fromtimestamp(funding['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Transaction: {funding['explorerUrl']}")

    return funding

get_wallet_funding_source("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```


```
curl "https://api.helius.xyz/v1/wallet/86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY/funded-by?api-key=YOUR_API_KEY"

```

## Response Format
### Successful Response

```

  "funder": "26MAyPNpK4At8LgRECMMbgiKQuJyg3oACtw1Q9FRyuba",
  "funderName": null,
  "funderType": null,
  "mint": "So11111111111111111111111111111111111111112",
  "symbol": "SOL",
  "amount": 0.09811972,
  "amountRaw": "98119720",
  "decimals": 9,
  "date": "2022-01-19T20:46:34.000Z",
  "signature": "5WX9C5kCQNULGGrSHJBR1WDFyetVyekbUpe1KQ45p3zEBe6jVgSsJuMqLWijjTDcnaAK2518ZriktRMCNycnsNAG",
  "timestamp": 1642625194,
  "slot": 116984883,
  "explorerUrl": "https://orbmarkets.io/tx/5WX9C5kCQNULGGrSHJBR1WDFyetVyekbUpe1KQ45p3zEBe6jVgSsJuMqLWijjTDcnaAK2518ZriktRMCNycnsNAG?tab=summary"


```

### 404 Response (No Funding Found)
If a wallet has never received SOL, the API returns a 404:

```

  "error": "No funding transaction found",
  "code": 404


```

## Understanding Funding Data
  * **`funder`**: The address that sent the first SOL transfer to this wallet
  * **`funderName`**: Human-readable name if the funder is a known entity (i.e., exchange, protocol, etc.)
  * **`funderType`**: Category of the funder (e.g., “exchange”, “defi-protocol”, etc.)
  * **`mint`**: Token mint address (`So11111111111111111111111111111111111111112` for SOL)
  * **`symbol`**: Token symbol (always “SOL” for funding transactions)
  * **`amount`**: Initial SOL amount received (human-readable, e.g.,`0.05` SOL)
  * **`amountRaw`**: Raw amount in lamports as a string (e.g.,`"50000000"` for 0.05 SOL)
  * **`decimals`**: Number of decimal places for the token (9 for SOL)
  * **`date`**: ISO 8601 formatted date string (e.g.,`"2024-01-01T00:00:00.000Z"`)
  * **`signature`**: Transaction signature of the funding transfer
  * **`timestamp`**: Unix timestamp (in seconds) when the wallet was funded
  * **`slot`**: Solana slot number when the funding transaction was confirmed
  * **`explorerUrl`**: Direct link to view the transaction on Orb


## Use Cases
### Detect Exchange-Funded Wallets
Identify wallets funded directly from centralized exchanges:

```
const isExchangeFunded = async (address) => {
  try {
    const funding = await getWalletFundingSource(address);

    if (!funding) {
      console.log('Wallet has no funding transaction');
      return false;


    if (funding.funderType === 'exchange') {
      console.log(`Wallet was funded by ${funding.funderName}`);
      console.log(`This is likely a retail user withdrawing from an exchange`);
      return true;


    console.log(`Wallet was not funded by an exchange`);
    return false;

catch (error) {
    console.error('Error checking funding source:', error);
    return false;



isExchangeFunded("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```

### Find Wallet Clusters (Sybil Detection)
Identify groups of wallets funded by the same source:

```
const findWalletClusters = async (walletAddresses) => {
  const fundingData = await Promise.all(
    walletAddresses.map(async address => {
      try {
        const funding = await getWalletFundingSource(address);
        return { address, funder: funding?.funder };
catch {
        return { address, funder: null };




  // Group by funder
  const clusters = {};

  fundingData.forEach(({ address, funder }) => {
    if (funder) {
      if (!clusters[funder]) {
        clusters[funder] = [];

      clusters[funder].push(address);

  });

  // Report clusters
  Object.entries(clusters).forEach(([funder, wallets]) => {
    if (wallets.length 1) {
      console.log(`\n🚨 Found cluster: ${wallets.length} wallets funded by ${funder.slice(0, 8)}...`);
      wallets.forEach(wallet => console.log(`  - ${wallet}`));

  });

  return clusters;


// Example: Check list of wallets for clusters
const suspiciousWallets = [
  "Wallet1...",
  "Wallet2...",
  "Wallet3..."


findWalletClusters(suspiciousWallets);

```

### Track Airdrop Recipients
Analyze where airdrop recipients came from:

```
const analyzeAirdropRecipients = async (airdropWallets) => {
  const fundingSources = await Promise.all(
    airdropWallets.map(async address => {
      try {
        return await getWalletFundingSource(address);
catch {
        return null;




  const stats = {
    total: airdropWallets.length,
    exchangeFunded: 0,
    unknown: 0,
    byExchange: {}


  fundingSources.forEach(funding => {
    if (!funding) {
      stats.unknown++;
      return;


    if (funding.funderType === 'exchange') {
      stats.exchangeFunded++;
      const exchange = funding.funderName || 'Unknown Exchange';
      stats.byExchange[exchange] = (stats.byExchange[exchange] || 0) + 1;

  });

  console.log('Airdrop Recipient Analysis:');
  console.log(`Total Recipients: ${stats.total}`);
  console.log(`Exchange-Funded: ${stats.exchangeFunded} (${(stats.exchangeFunded / stats.total * 100).toFixed(1)}%)`);
  console.log(`Unknown Source: ${stats.unknown}`);
  console.log('\nBy Exchange:');
  Object.entries(stats.byExchange).forEach(([exchange, count]) => {
    console.log(`  ${exchange}: ${count}`);
  });

  return stats;


```

### Build Wallet Timeline
Create a timeline starting from the wallet’s creation:

```
const buildWalletTimeline = async (address) => {
  const funding = await getWalletFundingSource(address);

  if (!funding) {
    console.log('No funding data available');
    return null;


  const creationDate = new Date(funding.timestamp * 1000);
  const ageInDays = Math.floor((Date.now() - creationDate.getTime()) / (1000 * 60 * 60 * 24));

  console.log('Wallet Timeline:');
  console.log(`Created: ${creationDate.toLocaleString()} (${ageInDays} days ago)`);
  console.log(`Initial Funding: ${funding.amount} SOL`);
  console.log(`Funded By: ${funding.funderName || funding.funder.slice(0, 8) + '...'}`);

  if (funding.funderType === 'exchange') {
    console.log(`This wallet was likely created by withdrawing from ${funding.funderName}`);


  return {
    creationDate,
    ageInDays,
    initialFunding: funding.amount,
    fundedBy: funding.funderName || funding.funder



```

### Compliance Risk Scoring
Assign risk scores based on funding source:

```
const assessWalletRisk = async (address) => {
  const funding = await getWalletFundingSource(address);

  if (!funding) {
    return { riskLevel: 'UNKNOWN', score: 50, reasons: ['No funding data available'] };


  let score = 0;
  let reasons = [];

  // Low risk: Funded by known exchange
  if (funding.funderType === 'exchange') {
    score = 20;
    reasons.push(`Funded by known exchange (${funding.funderName})`);

  // Medium risk: Unknown funder
  else if (!funding.funderName) {
    score = 50;
    reasons.push('Funded by unknown wallet');

  // High risk: Funded by flagged address
  else if (funding.funderType === 'flagged') {
    score = 90;
    reasons.push('Funded by flagged address');


  // Age factor: New wallets are higher risk
  const ageInDays = (Date.now() / 1000 - funding.timestamp) / (60 * 60 * 24);
  if (ageInDays 7) {
    score += 20;
    reasons.push('Wallet is less than 7 days old');


  // Amount factor: Very small initial funding is suspicious
  if (funding.amount 0.01) {
    score += 10;
    reasons.push('Very small initial funding amount');


  const riskLevel = score 30 ? 'LOW' : score 60 ? 'MEDIUM' : 'HIGH';

  console.log(`Risk Assessment for ${address}:`);
  console.log(`Risk Level: ${riskLevel} (Score: ${score}/100)`);
  reasons.forEach(reason => console.log(`  - ${reason}`));

  return { riskLevel, score, reasons };


```

### Attribution Tracking
Track which sources are creating the most new wallets:

```
const trackNewWalletSources = async (recentWallets) => {
  const fundingSources = await Promise.all(
    recentWallets.map(async address => {
      try {
        const funding = await getWalletFundingSource(address);
        return {
          address,
          funder: funding?.funder,
          funderName: funding?.funderName,
          funderType: funding?.funderType

catch {
        return { address, funder: null };




  // Count by source
  const sourceStats = {};

  fundingSources.forEach(({ funderName, funderType }) => {
    const sourceName = funderName || funderType || 'Unknown';
    sourceStats[sourceName] = (sourceStats[sourceName] || 0) + 1;
  });

  // Sort by count
  const sorted = Object.entries(sourceStats)
sort(([, a], [, b]) => b - a)
slice(0, 10);

  console.log('Top Wallet Funding Sources:');
  sorted.forEach(([source, count]) => {
    console.log(`${source}: ${count} wallets`);
  });

  return sourceStats;


```

## Best Practices
Handle 404 Responses
Wallets that have never received SOL will return a 404. This is expected for newly created but unfunded wallets.
Combine with Identity API
The funding data includes `funderName` and `funderType`, but you can use the Identity API on the `funder` address for more details.
Cache Funding Data
A wallet’s funding source never changes. Cache this data permanently to avoid repeated API calls.
Check Age for Context
The `timestamp` tells you when the wallet was created. Combine age with funding source for better context.
## Funder Types
The `funderType` field indicates the category of the wallet that funded the address. All values from the [Identity Categories](https://www.helius.dev/docs/wallet-api/identity#identity-categories) are supported:
### Common Funder Types  
| Type  | Description  | Examples  |  
| --- | --- | --- |  
| Centralized Exchange  | CEX hot wallets  | Binance, Coinbase, Kraken, OKX  |  
| DeFi  | DeFi protocol addresses  | Jupiter, Raydium, Marinade  |  
| Market Maker  | Market making firms  | Jump Trading, Wintermute  |  
| Trading Firm  | Proprietary trading firms  | Institutional traders  |  
| Cross-chain Bridge  | Bridge protocol addresses  | Wormhole, AllBridge, Portal  |  
| Validator  | Validator addresses  | Coinbase Validator, Jito  |  
| Key Opinion Leader  | Notable individuals  | Influencers, founders  |  
| Treasury  | Project treasuries  | Protocol treasuries  |  
| Stake Pool  | Liquid staking pools  | Marinade, Jito  |  
| null  | Unknown funder  | Regular wallet, not in identity database  |  
### All Supported Types
The complete list includes: Airdrop, Authority, Cross-chain Bridge, Casino & Gambling, DAO, DeFi, DePIN, Centralized Exchange, Exploiter/Hackers/Scams, Fees, Fundraise, Game, Genesis Block Distribution, Governance, Hacker, Jito, Key Opinion Leader, Market Maker, Memecoin, Multisig, NFT, Non-Circulating Supply, Oracle, Other, Payments, Proprietary AMM, Restaking, Rugger, Scammer, Spam, Stake Pool, System, Tools, Trading App/Bot, Trading Firm, Transaction Sending, Treasury, Validator, Vault, and X402. See the [Identity Categories](https://www.helius.dev/docs/wallet-api/identity#identity-categories) section for the complete list with descriptions.
## Common Errors  
| Error Code  | Description  | Solution  |  
| --- | --- | --- |  
| 400  | Invalid wallet address format  | Verify the address is a valid base58 Solana address  |  
| 401  | Missing or invalid API key  | Check your API key is included in the request  |  
| 404  | No funding transaction found  | This wallet has never received SOL  |  
| 429  | Rate limit exceeded  | Reduce request frequency or upgrade your plan  |  
## Limitations
**Important Limitations** :
  * This endpoint only tracks the **first SOL transfer** to a wallet
  * If a wallet was created via airdrop or program initialization without a SOL transfer, it won’t have funding data
  * The funding source represents the **immediate** funder, not necessarily the ultimate source of funds
  * Historical data is only available for wallets created after this feature was deployed


## Need Help?
## [API Reference View detailed API specs with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api/funded-by)
## [Contact Support Get help from our team ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/transfers)[ OverviewDedicated Solana nodes optimized for gRPC streaming applications. Ultra-low latency blockchain data for trading, analytics, and real-time monitoring. Next ](https://www.helius.dev/docs/dedicated-nodes)
On this page
  * [404 Response (No Funding Found)](https://www.helius.dev/docs/wallet-api/funded-by#404-response-no-funding-found)
  * [Understanding Funding Data](https://www.helius.dev/docs/wallet-api/funded-by#understanding-funding-data)
  * [Detect Exchange-Funded Wallets](https://www.helius.dev/docs/wallet-api/funded-by#detect-exchange-funded-wallets)
  * [Find Wallet Clusters (Sybil Detection)](https://www.helius.dev/docs/wallet-api/funded-by#find-wallet-clusters-sybil-detection)
  * [Track Airdrop Recipients](https://www.helius.dev/docs/wallet-api/funded-by#track-airdrop-recipients)
  * [Build Wallet Timeline](https://www.helius.dev/docs/wallet-api/funded-by#build-wallet-timeline)
  * [Compliance Risk Scoring](https://www.helius.dev/docs/wallet-api/funded-by#compliance-risk-scoring)


Assistant
Responses are generated using AI and may contain mistakes.
