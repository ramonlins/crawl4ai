# Source: https://www.helius.dev/docs/das/get-nfts

[Skip to main content](https://www.helius.dev/docs/das/get-nfts#content-area)
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
Digital Asset Standard (DAS)
How to Get Solana Assets: NFTs, Tokens & Price Data
> ## Documentation Index
> Fetch the complete documentation index at: <https://www.helius.dev/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
The Helius Digital Asset Standard (DAS) API provides powerful tools for reading and querying both NFT and token data on Solana. This guide shows you how to work with different types of Solana assets effectively.
## [Query NFTs Retrieve, search, and manage NFT data and collections ](https://www.helius.dev/docs/das/get-nfts#working-with-nfts-and-digital-collectibles)
## [Access SPL Tokens Get token balances, accounts, and holder information ](https://www.helius.dev/docs/das/get-nfts#working-with-spl-tokens)
## [Token Pricing Access real-time price data for the top 10k tokens by 24h volume ](https://www.helius.dev/docs/das/get-nfts#price-data-for-tokens)
## [API Reference View detailed API documentation ](https://www.helius.dev/docs/api-reference/das)
##  Price Data for Tokens
Price data returned by getAsset is cached and may not be fresh. The price information has a 600-second cache, meaning the data can be up to 600 seconds old.

```
const fetchTokenPriceData = async () => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAsset",
      params: {
        id: "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263", // Bonk token mint address
        displayOptions: {
          showFungibleTokens: true


    }),
  });

  const data = await response.json();

  // Calculate market cap
  if (data.result?.token_info?.price_info) {
    const { price_per_token } = data.result.token_info.price_info;
    const { supply, decimals } = data.result.token_info;

    // Adjust supply for decimals
    const adjustedSupply = supply / Math.pow(10, decimals);
    const marketCap = price_per_token * adjustedSupply;

    console.log(`Market Cap: $${marketCap.toLocaleString()}`);


  return data;


```

## [API Reference View detailed documentation for getAsset ](https://www.helius.dev/docs/api-reference/das/getasset)
###  Response Structure
The price data is available in the response under `token_info.price_info`:

```

  "token_info": {
    "symbol": "Bonk",
    "supply": 8881594973561640000,
    "decimals": 5,
    "token_program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
    "price_info": {
      "price_per_token": 0.0000192271,
      "currency": "USDC"




```

###  Calculating Market Cap
To calculate a token’s market cap, multiply its price by the adjusted supply (accounting for decimals):

```
const adjustedSupply = supply / Math.pow(10, decimals);
const marketCap = pricePerToken * adjustedSupply;

```

This calculation gives you the total market valuation of the token by properly accounting for the token’s decimal places.
##  Working with NFTs and Digital Collectibles
The DAS API offers several methods for working with NFTs and digital collectibles. These methods allow you to retrieve individual assets, query by owner or creator, and verify on-chain authenticity.
  * Get Single NFT
  * Find by Owner
  * Advanced Search


###  Getting a Single NFT
Retrieve comprehensive data for a specific NFT:

```
const getNFT = async (mintAddress) => {
  const response = await fetch('https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAsset",
      params: {
        id: mintAddress,

    }),
  });

  const data = await response.json();
  return data;


// Example usage
getNFT("F9Lw3ki3hJ7PF9HQXsBzoY8GyE6sPoEZZdXJBsTTD2rk");

```

###  Finding NFTs by Owner
Retrieve all NFTs owned by a specific wallet address:

```
const getNFTsByOwner = async (ownerAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAssetsByOwner",
      params: {
        ownerAddress: ownerAddress,
        page: 1,
        limit: 10,

    }),
  });

  const data = await response.json();
  return data;


// Example usage
getNFTsByOwner("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```

###  Searching Assets with Advanced Filters
Search for assets by various attributes with detailed filters:

```
const searchAssets = async (params) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "searchAssets",
      params: params,
    }),
  });

  const data = await response.json();
  return data;


// Example: Find all NFTs owned by an address
searchAssets({
  ownerAddress: "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
  tokenType: "all",
  limit: 50,
});

```

## [getAsset Detailed data for a single asset ](https://www.helius.dev/docs/api-reference/das/getasset)
## [getAssetsByOwner All assets owned by an address ](https://www.helius.dev/docs/api-reference/das/getassetsbyowner)
## [searchAssets Filter assets by multiple criteria ](https://www.helius.dev/docs/api-reference/das/searchassets)
###  Advanced NFT Query Methods
  * By Creator
  * By Collection
  * Transaction History
  * On-Chain Proof



```
const getAssetsByCreator = async (creatorAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAssetsByCreator",
      params: {
        creatorAddress: creatorAddress,
        page: 1,
        limit: 100,

    }),
  });

  const data = await response.json();
  return data;


// Example usage
getAssetsByCreator("9uBX3ASjxWvNBAD1xjbVaKA74mWGZys3RGSF7DdeDD3F");

```


```
const getAssetsByCollection = async (collectionAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAssetsByGroup",
      params: {
        groupKey: "collection",
        groupValue: collectionAddress,
        page: 1,
        limit: 100,

    }),
  });

  const data = await response.json();
  return data;


// Example usage
getAssetsByCollection("J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w");

```


```
const getNFTTransactionHistory = async (mintAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getSignaturesForAsset",
      params: {
        id: mintAddress,
        page: 1,
        limit: 100,

    }),
  });

  const data = await response.json();
  return data;


// Example usage
getNFTTransactionHistory("FNt6A9Mfnqbwc1tY7uwAguKQ1JcpBrxmhczDgbdJy5AC");

```


```
const getNFTProof = async (mintAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "1",
      method: "getAssetProof",
      params: {
        id: mintAddress,

    }),
  });

  const proof = await response.json();
  return proof;


// Example usage
getNFTProof("Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss");

```

## [By Creator API Reference ](https://www.helius.dev/docs/api-reference/das/getassetsbycreator)
## [By Collection API Reference ](https://www.helius.dev/docs/api-reference/das/getassetsbygroup)
## [Transaction History API Reference ](https://www.helius.dev/docs/api-reference/das/getsignaturesforasset)
## [On-Chain Proof API Reference ](https://www.helius.dev/docs/api-reference/das/getassetproof)
##  Working with SPL Tokens
SPL tokens can be queried through multiple methods in the Helius API. These methods let you check balances, find token accounts, and get token metadata.
###  Common SPL Token Operations
  * Token Balance
  * Tokens by Owner
  * Token Supply
  * Largest Holders



```
const getTokenBalance = async (tokenAccountAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getTokenAccountBalance',
      params: [tokenAccountAddress]

  });

  const data = await response.json();
  return data;


// Example usage
getTokenBalance("3emsAVdmGKERbHjmGfQ6oZ1e35dkf5iYcS6U4CPKFVaa");

```

## [API Reference View getTokenAccountBalance documentation ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountbalance)

```
const getTokensByOwner = async (ownerAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getTokenAccountsByOwner',
      params: [
        ownerAddress,

          programId: 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'


          encoding: 'jsonParsed'



  });

  const data = await response.json();
  return data;


// Example usage
getTokensByOwner("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```

## [API Reference View getTokenAccountsByOwner documentation ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountsbyowner)

```
const getTokenSupply = async (mintAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getTokenSupply',
      params: [mintAddress]

  });

  const data = await response.json();
  return data;


// Example usage
getTokenSupply("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");

```

## [API Reference View getTokenSupply documentation ](https://www.helius.dev/docs/api-reference/rpc/http/gettokensupply)

```
const getTokenLargestAccounts = async (mintAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getTokenLargestAccounts',
      params: [mintAddress]

  });

  const data = await response.json();
  return data;


// Example usage
getTokenLargestAccounts("he1iusmfkpAdwvxLNGV8Y1iSbj4rUy6yMhEA3fotn9A");

```

## [API Reference View getTokenLargestAccounts documentation ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenlargestaccounts)
###  Advanced SPL Token Queries
You can also find all accounts holding a specific token mint:

```
const getTokenAccountsByMint = async (mintAddress) => {
  const response = await fetch("https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: '1',
      method: 'getTokenAccountsByOwner',
      params: [
        'CEXq1uy9y15PL2Wb4vDQwQfcJakBGjaAjeuR2nKLj8dk', // Owner address

          mint: mintAddress


          encoding: 'jsonParsed'



  });

  const data = await response.json();
  return data;


// Example usage
getTokenAccountsByMint("8wXtPeU6557ETkp9WHFY1n1EcU6NxDvbAggHGsMYiHsB");

```

##  Best Practices
When working with the DAS API, keep these best practices in mind:
  1. **Use pagination** for methods that return large data sets
  2. **Handle errors gracefully** by implementing try/catch blocks
  3. **Cache responses** when appropriate to reduce API calls
  4. **Respect rate limits** to avoid disruptions in your application
  5. **Verify price data** is available before calculating market cap


##  Questions?
For frequently asked questions about the DAS API including asset data, price information, and API usage, visit our comprehensive [DAS API FAQ](https://www.helius.dev/docs/faqs/das-api).
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/das/get-tokens)[ Search AssetsMaster the searchAssets endpoint to discover NFTs, compressed assets, and fungible tokens on Solana. Advanced filtering, pagination, and efficient asset discovery. Next ](https://www.helius.dev/docs/das/search)
Ctrl+I
On this page
  * [Calculating Market Cap](https://www.helius.dev/docs/das/get-nfts#calculating-market-cap)
  * [Working with NFTs and Digital Collectibles](https://www.helius.dev/docs/das/get-nfts#working-with-nfts-and-digital-collectibles)
  * [Advanced NFT Query Methods](https://www.helius.dev/docs/das/get-nfts#advanced-nft-query-methods)
  * [Working with SPL Tokens](https://www.helius.dev/docs/das/get-nfts#working-with-spl-tokens)
  * [Common SPL Token Operations](https://www.helius.dev/docs/das/get-nfts#common-spl-token-operations)
  * [Advanced SPL Token Queries](https://www.helius.dev/docs/das/get-nfts#advanced-spl-token-queries)


Assistant
Responses are generated using AI and may contain mistakes.
