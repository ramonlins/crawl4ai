# Source: https://www.helius.dev/docs/das-api

**Quick Reference** : The DAS API provides a unified interface for all Solana assets. Use `getAsset` for single assets, `getAssetsByOwner` for wallet holdings, `searchAssets` for filtered queries, and specialized methods for compressed NFTs.
## What is DAS?
The Digital Asset Standard (DAS) API is an open-source specification that provides a unified interface for interacting with all types of digital assets on Solana:
  * Regular NFTs (Non-Fungible Tokens)
  * Compressed NFTs (State Compression)
  * Fungible Tokens (including SPL Tokens and Token-2022)
  * Inscriptions and SPL-20 tokens (experimental)


## Mainnet Endpoint
`https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
## Devnet Endpoint
`https://devnet.helius-rpc.com/?api-key=YOUR_API_KEY`
  * Key Features
  * Use Cases


  * Unified access to all Solana asset types
  * Comprehensive metadata retrieval
  * Off-chain data indexing (Arweave, IPFS)
  * Merkle proof support for compressed assets
  * Token price data for verified tokens
  * Advanced filtering and search capabilities


  * NFT marketplaces and storefronts
  * Wallet applications and portfolio trackers
  * Token-gated applications
  * Creator dashboards and analytics tools
  * NFT collection explorers
  * DeFi applications requiring token data


## API Methods
## [Single Asset Get detailed data for specific assets ](https://www.helius.dev/docs/das-api#fetching-individual-assets)
## [Asset Collections Get assets by owner, creator, or collection ](https://www.helius.dev/docs/das-api#fetching-asset-collections)
## [Advanced Queries Search and filter assets with complex criteria ](https://www.helius.dev/docs/das-api#advanced-query-methods)
### Fetching Individual Assets
These methods let you retrieve detailed information about specific assets by their IDs.
  * getAsset
  * getAssetBatch
  * getAssetProof
  * getAssetProofBatch



```
// Get a single asset by its ID
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAsset = async (id) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "my-request-id",
      method: "getAsset",
      params: {
        id: id,

    }),
  });

  const data = await response.json();
  return data.result;


// Example usage
getAsset("FNt6A9Mfnqbwc1tY7uwAguKQ1JcpBrxmhczDgbdJy5AC");

```

## [API Reference View detailed documentation for getAsset ](https://www.helius.dev/docs/api-reference/das/getasset)

```
// Get multiple assets (up to 1,000) in a single request
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetBatch = async (ids) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetBatch',
      params: {
        ids: ids

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetBatch([
  '81bxPqYCE8j34nQm7Rooqi8Vt3iMHLzgZJ71rUVbQQuz',
  'CWHuz6GPjWYdwt7rTfRHKaorMwZP58Spyd7aqGK7xFbn'
]);

```

## [API Reference View detailed documentation for getAssetBatch ](https://www.helius.dev/docs/api-reference/das/getassetbatch)

```
// Get Merkle proof for a compressed asset
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetProof = async (id) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetProof',
      params: {
        id: id

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetProof("Bu1DEKeawy7txbnCEJE4BU3BKLXaNAKCYcHR4XhndGss");

```

## [API Reference View detailed documentation for getAssetProof ](https://www.helius.dev/docs/api-reference/das/getassetproof)

```
// Get Merkle proofs for multiple compressed assets
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetProofBatch = async (ids) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetProofBatch',
      params: {
        ids: ids

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetProofBatch([
  '81bxPqYCE8j34nQm7Rooqi8Vt3iMHLzgZJ71rUVbQQuz',
  'CWHuz6GPjWYdwt7rTfRHKaorMwZP58Spyd7aqGK7xFbn'
]);

```

## [API Reference View detailed documentation for getAssetProofBatch ](https://www.helius.dev/docs/api-reference/das/getassetproofbatch)
### Fetching Asset Collections
These methods allow you to retrieve assets based on ownership, creation, authority, or collection membership.
All pagination in DAS API methods starts at 1 (not 0).
  * By Owner
  * By Collection
  * By Creator
  * By Authority



```
// Get all assets owned by a wallet address
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetsByOwner = async (ownerAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByOwner',
      params: {
        ownerAddress: ownerAddress,
        page: 1,
        limit: 1000,
        displayOptions: {
          showFungible: true, // Include SPL tokens
          showNativeBalance: true, // Include SOL balance
          showInscription: true, // Include inscription data


    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetsByOwner("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```

## [API Reference View detailed documentation for getAssetsByOwner ](https://www.helius.dev/docs/api-reference/das/getassetsbyowner)

```
// Get all assets in a collection
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetsByGroup = async (collectionAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByGroup',
      params: {
        groupKey: 'collection',
        groupValue: collectionAddress,
        page: 1,
        limit: 1000,

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetsByGroup("J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w");

```

## [API Reference View detailed documentation for getAssetsByGroup ](https://www.helius.dev/docs/api-reference/das/getassetsbygroup)

```
// Get all assets by a specific creator
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetsByCreator = async (creatorAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByCreator',
      params: {
        creatorAddress: creatorAddress,
        onlyVerified: true,
        page: 1,
        limit: 1000,

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetsByCreator("D3XrkNZz6wx6cofot7Zohsf2KSsu2ArngNk8VqU9cTY3");

```

## [API Reference View detailed documentation for getAssetsByCreator ](https://www.helius.dev/docs/api-reference/das/getassetsbycreator)

```
// Get all assets with a specific authority
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getAssetsByAuthority = async (authorityAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByAuthority',
      params: {
        authorityAddress: authorityAddress,
        page: 1,
        limit: 1000,

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getAssetsByAuthority("2RtGg6fsFiiF1EQzHqbd66AhW7R5bWeQGpTbv2UMkCdW");

```

## [API Reference View detailed documentation for getAssetsByAuthority ](https://www.helius.dev/docs/api-reference/das/getassetsbyauthority)
### Advanced Query Methods
These methods allow for more specialized asset queries, including transaction history, NFT editions, and complex search filters.
  * searchAssets
  * getSignaturesForAsset
  * getNftEditions
  * getTokenAccounts



```
// Search for assets with flexible criteria
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const searchAssets = async (searchParams) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'searchAssets',
      params: searchParams,
    }),
  });

  const { result } = await response.json();
  return result;


// Example: Search for NFTs in a collection
searchAssets({
  ownerAddress: "86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY",
  grouping: ["collection", "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w"],
  limit: 100
});

```

## [API Reference View detailed documentation for searchAssets ](https://www.helius.dev/docs/api-reference/das/searchassets)

```
// Get transaction history for a compressed asset
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getSignaturesForAsset = async (assetId) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getSignaturesForAsset',
      params: {
        id: assetId,
        page: 1,
        limit: 1000,

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getSignaturesForAsset("FNt6A9Mfnqbwc1tY7uwAguKQ1JcpBrxmhczDgbdJy5AC");

```

## [API Reference View detailed documentation for getSignaturesForAsset ](https://www.helius.dev/docs/api-reference/das/getsignaturesforasset)

```
// Get all editions for a master NFT
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getNftEditions = async (masterMint) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "my-request-id",
      method: "getNftEditions",
      params: {
        mint: masterMint,
        page: 1,
        limit: 100

    }),
  });

  const { result } = await response.json();
  return result;


// Example usage
getNftEditions("Ey2Qb8kLctbchQsMnhZs5DjY32To2QtPuXNwWvk4NosL");

```

## [API Reference View detailed documentation for getNftEditions ](https://www.helius.dev/docs/api-reference/das/getnfteditions)

```
// Get token accounts for a mint or owner
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getTokenAccounts = async (params) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",

    body: JSON.stringify({
      jsonrpc: "2.0",
      id: "my-request-id",
      method: "getTokenAccounts",
      params: params,
    }),
  });

  const { result } = await response.json();
  return result;


// Example: Get all accounts holding a specific token
getTokenAccounts({
  mint: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", // USDC
  page: 1,
  limit: 100
});

```

## [API Reference View detailed documentation for getTokenAccounts ](https://www.helius.dev/docs/api-reference/das/gettokenaccounts)
## Working with Special Asset Types
## [Fungible Tokens Access SPL tokens and get price data ](https://www.helius.dev/docs/das-api#fungible-tokens)
## [Compressed NFTs Work with state-compressed assets ](https://www.helius.dev/docs/das-api#compressed-nfts)
## [Inscriptions Access inscription and SPL-20 data ](https://www.helius.dev/docs/das-api#inscriptions--spl-20)
## [Off-chain Data Retrieve metadata from Arweave/IPFS ](https://www.helius.dev/docs/das-api#off-chain-data)
### Fungible Tokens
Helius has extended the DAS API to support **all tokens** , including plain SPL tokens (without metadata) and Token-2022 (plus their extensions). Fungible token support is available through the `getAssetsByOwner` and `searchAssets` methods.

```
// Get all tokens for a wallet including price data
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getTokensWithPrices = async (ownerAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByOwner',
      params: {
        ownerAddress: ownerAddress,
        displayOptions: {
          showFungible: true,


    }),
  });

  const { result } = await response.json();

  // Filter tokens that have price data
  const tokensWithPrices = result.items.filter(
    asset => asset.token_info?.price_info


  return tokensWithPrices;


// Example usage
getTokensWithPrices("86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY");

```

### Compressed NFTs
State-compressed NFTs (cNFTs) require special handling for operations like retrieving Merkle proofs and transaction history.
#### Getting Compressed NFT Data

```
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getCompressedNft = async (id) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAsset',
      params: { id },
    }),
  });

  const { result } = await response.json();
  return result;


```

#### Retrieving Merkle Proofs
Merkle proofs are required for verifying and performing on-chain operations with compressed NFTs like transfers and burns.

```
const getProof = async (id) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetProof',
      params: { id },
    }),
  });

  const { result } = await response.json();
  return result;


```

#### Checking Transaction History

```
const getTransactionHistory = async (id) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getSignaturesForAsset',
      params: {

        page: 1,
        limit: 100

    }),
  });

  const { result } = await response.json();
  return result;


```

### Inscriptions & SPL-20
You can optionally display inscription and SPL-20 token data with the `showInscription` flag. This is an experimental feature.

```
// Get inscriptions for a wallet
const url = `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`;

const getInscriptionsForWallet = async (ownerAddress) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',

    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 'my-request-id',
      method: 'getAssetsByOwner',
      params: {
        ownerAddress: ownerAddress,
        displayOptions: {
          showInscription: true,


    }),
  });

  const { result } = await response.json();

  // Filter results to only include assets with inscription data
  const inscriptions = result.items.filter(
    asset => asset.inscription


  return inscriptions;


// Example usage
getInscriptionsForWallet("6GmTFg5SCs4zGfDEidUAJjS5pSrXEPwW8Rpfs3RHrbc5");

```

### Off-chain Data
Off-chain Data Retrieval
Most NFT collections store additional metadata (attributes, images, etc.) off-chain on platforms like Arweave or IPFS. The DAS API automatically indexes this off-chain data and provides it alongside on-chain data in a single API call.
Helius cannot detect off-chain data mutations. The off-chain data will only be updated once the NFT is seen by the system again (e.g., when the NFT is modified on-chain). If you need the off-chain data for a collection to be re-indexed, please reach out to Helius support.
## Best Practices
## Pagination
  * Start at page 1 (not 0)
  * Use reasonable limit values (100-1000)
  * Implement robust pagination for large datasets


## Error Handling
  * Always check for errors in responses
  * Implement retries with exponential backoff
  * Handle edge cases like invalid parameters


## Performance
  * Use batch methods when possible
  * Cache responses when appropriate
  * Avoid chaining multiple requests when one will do


## Security
  * Never expose your API key in client-side code
  * Use server-side functions to proxy API requests
  * Set up appropriate CORS policies


## Resources
## [API References Full API documentation for all DAS methods ](https://www.helius.dev/docs/api-reference/das)
## [GitHub Repository DAS API open-source specification ](https://github.com/metaplex-foundation/digital-asset-standard-api)
## [Examples & SDKs Get started with client libraries and code samples ](https://www.helius.dev/docs/sdks)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/gettransactionsforaddress)[ Get SPL TokensLearn how to retrieve and query Solana SPL token data using Helius APIs. Token balances, accounts, supply information, and holder data with code examples. Next ](https://www.helius.dev/docs/das/get-tokens)
On this page
  * [Fetching Individual Assets](https://www.helius.dev/docs/das-api#fetching-individual-assets)
  * [Fetching Asset Collections](https://www.helius.dev/docs/das-api#fetching-asset-collections)
  * [Advanced Query Methods](https://www.helius.dev/docs/das-api#advanced-query-methods)
  * [Working with Special Asset Types](https://www.helius.dev/docs/das-api#working-with-special-asset-types)
  * [Getting Compressed NFT Data](https://www.helius.dev/docs/das-api#getting-compressed-nft-data)
  * [Retrieving Merkle Proofs](https://www.helius.dev/docs/das-api#retrieving-merkle-proofs)
  * [Checking Transaction History](https://www.helius.dev/docs/das-api#checking-transaction-history)


Assistant
Responses are generated using AI and may contain mistakes.
