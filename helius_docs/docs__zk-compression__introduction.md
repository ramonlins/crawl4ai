# Source: https://www.helius.dev/docs/zk-compression/introduction

[ZK Compression](https://www.zkcompression.com/) is a generalized compression framework that allows developers to store data on Solana at a fraction of the cost. After helping develop cNFT compression, Helius saw the need to build a generalized system. So, along with the [Light team](https://lightprotocol.com/), we built ZK Compression to allow developers to store arbitrary data in _compressed accounts_ , akin to native Solana accounts.
## Photon: the ZK Compression Indexer
Helius built [Photon](https://github.com/helius-labs/photon), the ZK Compression indexer. In ZK Compression, programs log compressed account data in Solana transactions and store the fingerprint of that data in validator memory. Photon indexes Solana transactions to parse and store compressed account data. It then exposes a [ZK Compression](https://www.helius.dev/docs/api-reference/zk-compression) API similar to Solana’s native API to help users access compression data. Though developers can directly host Photon, we expose a Photon API to streamline the developer experience.
Please visit the official [ZK Compression docs](https://www.zkcompression.com/) to learn more about ZK Compression and Photon.
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/nfts/cnft-event-listening)[ OverviewCost-effective Solana token airdrops using ZK compression. Reduce airdrop costs by 95% with Helius AirShip's open-source distribution tool. Next ](https://www.helius.dev/docs/airship/overview)
On this page
  * [Photon: the ZK Compression Indexer](https://www.helius.dev/docs/zk-compression/introduction#photon-the-zk-compression-indexer)


Assistant
Responses are generated using AI and may contain mistakes.
