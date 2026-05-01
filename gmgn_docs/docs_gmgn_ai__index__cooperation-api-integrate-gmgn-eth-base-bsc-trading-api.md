# Source: https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api

✅ Approved: API Key sent to your email ❌ Rejected: No notification sent
#### 
Authentication
  * GMGN provides professional users with SOL/BSC/Base/ETH Trading API. Access is granted solely based on sufficient**Trading Volume** on GMGN. Review will be completed within 24 hours after submission
  * To access the GMGN Trade API, apply for permission by filling out the following Google Form: <https://forms.gle/CWABDLRe8twvygvy5>[arrow-up-right](https://forms.gle/CWABDLRe8twvygvy5)
  * Upon approval, GMGN will issue an API Key to your email. Include the API Key in the request header with the name: `x-route-key`
  * Each API Key is rate-limited to one call every 5 seconds


**ETH/Base chain Swap transaction steps:**
  1. **Get the transaction route, recommended slippage, and recommended gas price at the same time**


  * Get transaction routing: [Get the available routing for ETH/Base transactions](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-available-routing-for-eth-base-bsc-transactions)
  * Get recommended slippage: [Get the recommended slippage value of ETH/Base token](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-slippage-value-of-eth-base-bsc-token)
  * Get recommended gas price: [Get the recommended gas price for ETH/Base chain](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-gas-price-for-eth-base-bsc-chain)


  1. **After selecting the route, call the simulated transaction**


[💻Swap transaction simulation (ETH/Base)](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/swap-transaction-simulation-eth-base-bsc)
  1. **After the simulated transaction is passed, get the returned data field and use normal rpc or anti-pinch rpc to submit the formal transaction**


Submit transaction signature, you can use ethers js library
Signature transaction tutorial <https://docs.ethers.org/v6/api/providers/#Signer-signTransaction>[arrow-up-right](https://docs.ethers.org/v6/api/providers/#Signer-signTransaction)
Ethers js library <https://github.com/ethers-io/ethers.js>[arrow-up-right](https://github.com/ethers-io/ethers.js)
[Previous🤝🏻 Cooperation-API:🕹Integrate GMGN Solana Trading APIchevron-left](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-solana-trading-api)[NextGet the available routing for ETH/Base/BSC transactionschevron-right](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-available-routing-for-eth-base-bsc-transactions)
Last updated 3 months ago
