# Source: https://pumpportal.fun/

[All Pump.fun websocket trading data will incur charges starting May 1, 2026.](https://pumpportal.fun/)
# What is PumpPortal?
**A 3rd-Party API for Pump.fun, Raydium, and other DEXs**. We provide low latency data sources and transaction building for the Pump.fun bonding curve and Raydium LPs.
Our [Lightning Transaction API](https://pumpportal.fun/trading-api/setup) is designed to be easy to use, so you can start building in minutes: there are no libraries to install and nothing to configure. You just send an HTTPS request and we handle sending the transaction. Lightning transactions are highly optimized to achieve some of lowest latencies possible on Solana.
If you need full security and control over your transactions, you can use our [Local Transaction API](https://pumpportal.fun/local-trading-api/trading-api). Local Transactions builds a transaction that you handle signing and sending yourself with a custom RPC endpoint.
Beginning May 1, 2026, PumpPortal will charge the same fees for trading data on all platforms. After this change all buy/sell events from subscribeTokenTrade and subscribeAccountTrade methods will be charged the same way regardless of whether the coin has migrated or not.
The subscribeNewToken and subscribeMigration methods are NOT affected by this change, these methods will remain free, meaning no charge will be applied for token creation or migration events.
Beginning May 1, 2026, using subscribeTokenTrade or subscribeAccountTrade will require a [PumpPortal API key](https://pumpportal.fun/trading-api/setup) and linked wallet funded with at least 0.02 SOL. By streaming data, your wallet will incur a charge of 0.01 SOL for every 10000 websocket messages you receive.
