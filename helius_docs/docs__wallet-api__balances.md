# Source: https://www.helius.dev/docs/wallet-api/balances

[Skip to main content](https://www.helius.dev/docs/wallet-api/balances#content-area)
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
How to Get Wallet Balances
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
**Beta** : The Wallet API is currently in beta. APIs and response formats may change.
##  Overview
The Wallet Balances endpoint retrieves all token and NFT holdings for a Solana wallet. Get SOL, SPL tokens, Token-2022, and NFTs with USD pricing, logos, and metadata—all sorted by value. **Pagination is manual** - the API returns up to 100 tokens per request. Results are sorted by USD value in descending order. Tokens with pricing data appear first, followed by tokens without prices. **Pagination:** Use the `page` parameter to fetch additional pages. The response includes `pagination.hasMore` to indicate if more results are available. Each request makes a single API call and costs 100 credits.
**USD Pricing** : Token prices are sourced from DAS (Digital Asset Standard) and update hourly. Pricing covers the top 10,000 tokens by market cap. Not all tokens will have pricing data—`pricePerToken` and `usdValue` will be `null` for unsupported tokens. Prices are estimates and should not be relied upon as real-time market rates; support for real-time prices will be added in the future.
## [API Reference View detailed API documentation for wallet balances ](https://www.helius.dev/docs/api-reference/wallet-api/balances)
##  When to Use This
Use the Wallet Balances API when you need to:
  * **Display Portfolio Holdings** : Show users their complete token and NFT holdings
  * **Calculate USD Values** : Get portfolio valuations with hourly-updated pricing
  * **Build Wallet UIs** : Power wallet dashboards and asset lists
  * **Track Token Holdings** : Monitor specific token balances across wallets
  * **Portfolio Analytics** : Analyze holdings distribution and concentration
  * **Tax Reporting** : Generate holdings snapshots for tax purposes


##  Quickstart
###  Basic Balance Query
Get all token balances for a wallet with USD values:
  * JavaScript
  * Python
  * cURL



```
const getWalletBalances = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY`;

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);


  const data = await response.json();

  const solBalance = data.balances[0]; // SOL is always first when showNative=true
  console.log(`SOL Balance: ${solBalance.balance} SOL ($${solBalance.usdValue})`);
  console.log(`Page ${data.pagination.page} Total Value: $${data.totalUsdValue}`);
  console.log(`Token Count (this page): ${data.balances.length}`);

  // Display top holdings
  data.balances.slice(0, 5).forEach(token => {
    console.log(`${token.symbol}: ${token.balance} ($${token.usdValue || 'N/A'})`);
  });

  return data;


getWalletBalances("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
import requests

def get_wallet_balances(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/balances"
    headers = {"X-Api-Key": "YOUR_API_KEY"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    sol_balance = data['balances'][0]  # SOL is always first when showNative=true
    print(f"SOL Balance: {sol_balance['balance']} SOL (${sol_balance['usdValue']})")
    print(f"Page {data['pagination']['page']} Total Value: ${data['totalUsdValue']}")
    print(f"Token Count (this page): {len(data['balances'])}")

    # Display top holdings
    for token in data['balances'][:5]:
        usd_value = token.get('usdValue', 'N/A')
        print(f"{token['symbol']}: {token['balance']} (${usd_value})")

    return data

get_wallet_balances("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```


```
curl "https://api.helius.xyz/v1/wallet/86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY/balances?api-key=YOUR_API_KEY"

```

###  Include NFTs in Results
Get both tokens and NFTs in a single request:
  * JavaScript
  * Python



```
const getWalletWithNfts = async (address) => {
  const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY&showNfts=true`;

  const response = await fetch(url);
  const data = await response.json();

  console.log(`Tokens: ${data.balances.length}`);
  console.log(`NFTs: ${data.nfts?.length || 0}`);

  // Display NFTs
  data.nfts?.forEach(nft => {
    console.log(`NFT: ${nft.name || 'Unnamed'} (${nft.collectionName || 'Unknown Collection'})`);
  });

  return data;


getWalletWithNfts("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```


```
def get_wallet_with_nfts(address: str):
    url = f"https://api.helius.xyz/v1/wallet/{address}/balances"
    params = {
        "api-key": "YOUR_API_KEY",
        "showNfts": "true"


    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    print(f"Tokens: {len(data['tokens'])}")
    print(f"NFTs: {len(data.get('nfts', []))}")

    # Display NFTs
    for nft in data.get('nfts', []):
        name = nft.get('name', 'Unnamed')
        collection = nft.get('collectionName', 'Unknown Collection')
        print(f"NFT: {name} ({collection})")

    return data

get_wallet_with_nfts("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY")

```

###  Filter Options
Customize the results with query parameters:
####  Hide Zero Balances

```
// Only show tokens with non-zero balances
const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY&showZeroBalance=false`;

```

####  Hide Native SOL

```
// Exclude native SOL from results
const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY&showNative=false`;

```

####  Limit Results

```
// Get only top 50 tokens by value
const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY&limit=50`;

```

##  Query Parameters  
| Parameter  | Type  | Default  | Description  |  
| --- | --- | --- | --- |  
| `page`  | integer  | 1  | Page number for pagination (1-indexed)  |  
| `limit`  | integer  | 100  | Maximum number of tokens per page (1-100)  |  
| `showZeroBalance`  | boolean  | false  | Include tokens with zero balance  |  
| `showNative`  | boolean  | true  | Include native SOL in results  |  
| `showNfts`  | boolean  | false  | Include NFTs in results (max 100, first page only)  |  
##  Response Format

```

  "balances": [

      "mint": "So11111111111111111111111111111111111111112",
      "symbol": "SOL",
      "name": "Solana",
      "balance": 1.5,
      "decimals": 9,
      "pricePerToken": 145.32,
      "usdValue": 217.98,
      "logoUri": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/So11111111111111111111111111111111111111112/logo.png",
      "tokenProgram": "spl-token"


      "mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
      "symbol": "USDC",
      "name": "USD Coin",
      "balance": 1000.5,
      "decimals": 6,
      "pricePerToken": 1.0,
      "usdValue": 1000.5,
      "logoUri": "https://example.com/usdc-logo.png",
      "tokenProgram": "spl-token"


  "nfts": [

      "mint": "7Xq8wXyXVqfBPPqVJjPDwG9zN5wCVxBYZ6z7vPYBzr6F",
      "name": "Degen Ape #1234",
      "imageUri": "https://example.com/nft.png",
      "collectionName": "Degen Ape Academy",
      "collectionAddress": "DegN1dXmU2uYa4n7U9qTh7YNYpK4u8L9qXx7XqYqJfGH",
      "compressed": false


  "totalUsdValue": 1218.48,
  "pagination": {
    "page": 1,
    "limit": 100,
    "hasMore": true



```

**Amounts are human-readable.** The `balance` field is already adjusted for decimals — `1.5` means 1.5 SOL and `1000.5` means 1000.5 USDC. No lamport conversion is needed. The `decimals` field is provided for reference only. This endpoint does not expose a raw `amountRaw` field; if you need the exact integer value, derive it as `Math.round(balance * 10 ** decimals)`.
##  Use Cases
###  Build a Portfolio Dashboard
Display user holdings with USD values:

```
const renderPortfolio = async (address) => {
  const { balances, totalUsdValue } = await getWalletBalances(address);

  console.log(`Total Portfolio Value: $${totalUsdValue.toLocaleString()}`);
  console.log(`\nTop Holdings:`);

  // Display top 10 holdings (SOL is first, then other tokens sorted by value)
  balances.slice(0, 10).forEach((token, i) => {
    if (token.usdValue) {
      console.log(`${i + 1}. ${token.symbol}: ${token.balance.toFixed(4)} ($${token.usdValue.toFixed(2)})`);

  });


```

###  Calculate Token Concentration
Analyze portfolio diversification:

```
const analyzeConcentration = async (address) => {
  const { balances, totalUsdValue } = await getWalletBalances(address);

  const tokensWithValue = balances.filter(t => t.usdValue);

  if (tokensWithValue.length === 0) {
    console.log('No tokens with USD pricing data available');
    return null;


  const topToken = tokensWithValue[0];
  const concentration = (topToken.usdValue / totalUsdValue) * 100;

  console.log(`Largest Position: ${topToken.symbol} (${concentration.toFixed(1)}%)`);

  if (concentration 50) {
    console.log(`Warning: Portfolio is highly concentrated in ${topToken.symbol}`);


  return { topToken, concentration };


```

###  Track Specific Token Balance
Monitor a specific token across multiple wallets:

```
const getTokenBalance = async (address, tokenMint) => {
  const { balances } = await getWalletBalances(address);

  const token = balances.find(t => t.mint === tokenMint);

  if (!token) {
    console.log(`Token not found in wallet`);
    return null;


  console.log(`${token.symbol} Balance: ${token.balance}`);
  console.log(`USD Value: $${token.usdValue || 'N/A'}`);

  return token;


// Example: Check USDC balance
getTokenBalance(
  "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
  "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" // USDC mint


```

###  Export Holdings for Tax Reporting
Generate a holdings snapshot:

```
const exportHoldingsSnapshot = async (address) => {
  const { balances, totalUsdValue } = await getWalletBalances(address);

  const snapshot = {
    date: new Date().toISOString(),
    address,
    totalValueUSD: totalUsdValue,
    holdings: balances
filter(t => t.usdValue)
map(t => ({
        symbol: t.symbol,
        mint: t.mint,
        balance: t.balance,
        pricePerToken: t.pricePerToken,
        usdValue: t.usdValue
      }))


  console.log(JSON.stringify(snapshot, null, 2));
  return snapshot;


```

##  Token Program Support
The Wallet API supports both token standards:  
| Token Program  | Description  | Support  |  
| --- | --- | --- |  
| `spl-token`  | Legacy SPL Token standard  | Full support  |  
| `token-2022`  | New Token Extensions standard  | Full support  |  
The `tokenProgram` field in the response indicates which standard each token uses.
##  Pagination
For wallets with many tokens (>100), use manual pagination with the `page` parameter:

```
const getAllBalances = async (address) => {
  let allBalances = [];
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    const url = `https://api.helius.xyz/v1/wallet/${address}/balances?api-key=YOUR_API_KEY&page=${page}&limit=100`;

    const response = await fetch(url);
    const data = await response.json();

    allBalances = allBalances.concat(data.balances);
    hasMore = data.pagination.hasMore;
    page++;

    console.log(`Fetched page ${data.pagination.page}, total tokens so far: ${allBalances.length}`);


  console.log(`Total tokens: ${allBalances.length}`);
  return allBalances;


```

##  Best Practices
Filter Zero Balances for Cleaner UI
Use `showZeroBalance=false` to hide tokens the wallet no longer holds. This prevents cluttered portfolio views.
Include NFTs When Needed
NFTs are excluded by default for performance. Only set `showNfts=true` when you need to display them.
Handle Missing Price Data
USD prices are sourced from DAS and only cover the top 10,000 tokens with hourly updates. Always check if `pricePerToken` and `usdValue` are `null` before displaying. These are estimates, not real-time market rates.
Cache Aggressively
Balance data can be cached for several seconds without issue. Reduce API calls by caching responses.
Use Pagination for Large Wallets
Some wallets hold thousands of tokens. Implement pagination to handle large datasets efficiently.
##  Common Errors  
| Error Code  | Description  | Solution  |  
| --- | --- | --- |  
| 400  | Invalid wallet address format  | Verify the address is a valid base58 Solana address  |  
| 401  | Missing or invalid API key  | Check your API key is included in the request  |  
| 429  | Rate limit exceeded  | Reduce request frequency or upgrade your plan  |  
##  Need Help?
## [API Reference View detailed API specs with request/response schemas ](https://www.helius.dev/docs/api-reference/wallet-api/balances)
## [Contact Support Get help from our team ](https://www.helius.dev/docs/support/contact-support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/wallet-api/identity)[ Wallet HistoryGet complete transaction history for any Solana wallet with balance changes for each transaction. Perfect for portfolio trackers, accounting tools, and analytics platforms. Next ](https://www.helius.dev/docs/wallet-api/history)
Ctrl+I
On this page
  * [Include NFTs in Results](https://www.helius.dev/docs/wallet-api/balances#include-nfts-in-results)
  * [Build a Portfolio Dashboard](https://www.helius.dev/docs/wallet-api/balances#build-a-portfolio-dashboard)
  * [Calculate Token Concentration](https://www.helius.dev/docs/wallet-api/balances#calculate-token-concentration)
  * [Track Specific Token Balance](https://www.helius.dev/docs/wallet-api/balances#track-specific-token-balance)
  * [Export Holdings for Tax Reporting](https://www.helius.dev/docs/wallet-api/balances#export-holdings-for-tax-reporting)


Assistant
Responses are generated using AI and may contain mistakes.
