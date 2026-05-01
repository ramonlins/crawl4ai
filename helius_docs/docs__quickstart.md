# Source: https://www.helius.dev/docs/quickstart

## What does Helius provide?
Helius provides REST and JSON-RPC APIs for building any Solana application — from analytic platforms and DeFi dashboards to trading bots and compliance tools. Query token balances, fetch NFT metadata, stream real-time blockchain events, send optimized transactions, and monitor wallets with a single API key. This guide walks you through your first API call and a working application in minutes.
## Create Your Free Helius Account
Start by creating your free account at the [Helius Dashboard](https://dashboard.helius.dev/dashboard). Your free tier includes 100,000 DAS API calls per month; perfect for getting started and building prototypes.Agents looking to programmatically create a Helius account should use the [Helius CLI](https://www.helius.dev/docs/agents/cli) and reference the [Agent signup instructions](https://dashboard.helius.dev/agents.md).
## Get Your API Key
Navigate to the [API Keys](https://dashboard.helius.dev/api-keys) section and copy your key. This key gives you access to all Helius APIs, including RPC nodes, DAS API, and enhanced transaction data.
**Performance Tip** : Use our Gatekeeper (Beta) endpoint: `https://beta.helius-rpc.com` instead of `https://mainnet.helius-rpc.com` for lower latency. Your API key works on both. [Learn more →](https://www.helius.dev/docs/gatekeeper/overview)
## Make Your First API Call
Let’s start with a practical example: fetching NFTs from a wallet. We’ll use the [getAssetsByOwner](https://www.helius.dev/docs/api-reference/das/getassetsbyowner) method to query assets owned by `86xCn…o2MMY` (Anatoly Yakovenko’s wallet, co-founder of Solana). **What’s happening here?** The DAS API allows you to query compressed and standard NFTs with a single call. Notice how the response includes metadata, image URLs, and ownership information - all the data you need to build rich user experiences.
## Understanding the Response
Great! You’ve successfully fetched NFT data. The response includes:
  * **Asset ID** : Unique identifier for each NFT
  * **Metadata** : Name, symbol, description, and attributes
  * **Content** : Image URLs and file information
  * **Ownership** : Current owner and authority information


## Build It with Code
Now let’s implement this in a real application. We’ll create a simple NFT portfolio viewer that you can expand upon.
We’ll use Node.js for this example. Make sure you have it installed from [nodejs.org](https://nodejs.org/en/download).
### Set up your project

```
mkdir solana-nft-viewer
cd solana-nft-viewer
npm init -y
npm install node-fetch

```

### Create the NFT portfolio viewer
nft-portfolio.js

```
const fetch = require('node-fetch');

class NFTPortfolioViewer {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://mainnet.helius-rpc.com';


  async fetchNFTsByOwner(ownerAddress, limit = 10) {
    try {
      const response = await fetch(`${this.baseUrl}/?api-key=${this.apiKey}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',

        body: JSON.stringify({
          jsonrpc: '2.0',
          id: '1',
          method: 'getAssetsByOwner',
          params: {
            ownerAddress,
            page: 1,
            limit,
            displayOptions: {
              showFungible: false,
              showNativeBalance: false,



      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error.message);


      return data.result;
catch (error) {
      console.error('Error fetching NFTs:', error.message);
      throw error;



  displayNFTPortfolio(nfts) {
    console.log('\n🖼️  NFT Portfolio Summary');
    console.log('========================');
    console.log(`Total NFTs: ${nfts.total}`);
    console.log(`Showing: ${nfts.items.length} items\n`);

    nfts.items.forEach((nft, index) => {
      console.log(`${index + 1}. ${nft.content?.metadata?.name || 'Unnamed NFT'}`);
      console.log(`   Collection: ${nft.grouping?.[0]?.group_value || 'Individual'}`);
      console.log(`   Compressed: ${nft.compression?.compressed ? 'Yes' : 'No'}`);
      console.log(`   Image: ${nft.content?.files?.[0]?.uri || 'No image'}`);
      console.log(`   ID: ${nft.id}\n`);
    });


  async getRandomNFT(ownerAddress) {
    const portfolio = await this.fetchNFTsByOwner(ownerAddress, 50);

    if (portfolio.items.length === 0) {
      console.log('No NFTs found for this address.');
      return null;


    const randomIndex = Math.floor(Math.random() * portfolio.items.length);
    return portfolio.items[randomIndex];



// Usage example
async function main() {
  const viewer = new NFTPortfolioViewer('YOUR_API_KEY');

  // Anatoly's wallet address
  const walletAddress = '86xCnPeV69n6t3DnyGvkKobf9FdN2H9oiVDdaMpo2MMY';

  console.log('🚀 Fetching NFT portfolio...');

  try {
    // Get full portfolio overview
    const portfolio = await viewer.fetchNFTsByOwner(walletAddress);
    viewer.displayNFTPortfolio(portfolio);

    // Get a random NFT for featured display
    console.log('🎲 Featured Random NFT:');
    console.log('=====================');
    const randomNFT = await viewer.getRandomNFT(walletAddress);

    if (randomNFT) {
      console.log(`Name: ${randomNFT.content?.metadata?.name}`);
      console.log(`Description: ${randomNFT.content?.metadata?.description || 'No description'}`);
      console.log(`Image: ${randomNFT.content?.files?.[0]?.uri}`);


catch (error) {
    console.error('Failed to fetch NFT data:', error.message);



main();

```

### Add your API key
Replace `YOUR_API_KEY` with your actual API key from the Helius dashboard.
### Run your NFT portfolio viewer

```
node nft-portfolio.js

```

### Success! 🎉
You’ve built your first Solana application! The output shows:
  * Total NFT count in the wallet
  * Individual NFT details including compression status
  * Collection information
  * A featured random NFT

**What you’ve learned:**
  * How to structure API calls to Helius
  * Working with the DAS API response format
  * Handling compressed vs standard NFTs
  * Building reusable code for NFT operations


## Take It Further
Now that you understand the basics, explore these advanced features:
## [Send Transactions Learn transaction optimization, priority fees, and smart routing for reliable execution. ](https://www.helius.dev/docs/sending-transactions/overview)
## [Advanced NFT Operations Search NFTs by traits, fetch collection stats, and work with token metadata at scale. ](https://www.helius.dev/docs/das/get-nfts)
## [Real-Time Data Streaming Stream live blockchain data with sub-second latency using gRPC or enhanced WebSockets. ](https://www.helius.dev/docs/data-streaming/quickstart)
## [Automate with Webhooks Set up intelligent notifications for wallet activity, NFT sales, and custom on-chain events. ](https://www.helius.dev/docs/webhooks)
## What’s Next?
You’ve successfully built your first Solana application with Helius! Here are some ideas to expand your project:
  * **Add wallet connection** : Integrate with wallets
  * **Build a UI** : Create a React/Vue frontend to display the portfolio
  * **Add filtering** : Search by collection, traits, or mint date
  * **Real-time updates** : Use WebSockets to show live portfolio changes
  * **Analytics** : Track portfolio value and NFT price history


Was this page helpful?
Yes
On this page
  * [What does Helius provide?](https://www.helius.dev/docs/quickstart#what-does-helius-provide)


Assistant
Responses are generated using AI and may contain mistakes.
