# Source: https://docs.gmgn.ai/index/cooperation-script-how-to-quickly-create-an-automated-script-for-trading-with-gmgn-bot

_**Note: This tutorial requires some programming skills and**_ _**knowledge of network security to avoid Telegram account theft.**_
You can use the Telegram API to automatically send token contract addresses to the GMGN Sniper Bot, enabling **immediate buying and selling, as well as creating limit buy/sell orders.**
Suitable scenarios include:
  1. Monitoring smart money signals for automatic buying and limit sell orders
  2. Monitoring on-chain trading signals and CTO signals for automatic buying and limit sell orders


## 
**Specific Steps:**
## 
**1.** 🔔 **Monitor GMGN Trading Signals and Smart Money**
#### 
**1)** 🔔 **Subscribe to GMGN Signal**
  * Join the signal group at <https://t.me/gmgnsignals>[arrow-up-right](https://t.me/gmgnsignals)
  * Receive specialty signal messages (10+ signals available, more are in development):
    * CTO Signal
    * Update DEX Screener Social Infos
    * PUMP Update DEX Screener Social Infos
    * PUMP FDV Surge
    * Solana FDV Surge
    * Smart Money FOMO
    * KOL FOMO
    * DEV Burnt Alert
    * All Time High Price
    * Heavy Bought
    * Sniper New


#### 
**2)** 💰**Follow Smart Money**
  * Visit the [GMGN.AIarrow-up-right](http://GMGN.AI) Smart Money leaderboard to find high win-rate smart money that matches your trading style at <https://gmgn.ai/discover/?chain=sol>[arrow-up-right](https://gmgn.ai/discover/?chain=sol)


## 
**2.** 🙋🏼‍♀️ **Apply for Telegram App API**
  * Log in at <https://my.telegram.org/auth>[arrow-up-right](https://my.telegram.org/auth)
  * Create a Telegram app, fill out the form, and obtain the app’s **api_id** and **api_hash** (Note: Do not disclose these to any third parties to prevent Telegram account theft). For detailed instructions, refer to the official Telegram documentation at <https://core.telegram.org/api/obtaining_api_id>[arrow-up-right](https://core.telegram.org/api/obtaining_api_id)


## 
**3.** 🤖 **Set Up the Automation Script**
  * You need to write an automation script or search for open-source projects on [github.comarrow-up-right](http://github.com) with similar functionality (Note: Assess code security to avoid Telegram account theft).
  * Automation script code logic:
    * Use the **api_id** and **api_hash** obtained above to receive messages from the GMGN signal group or get trading signals from other channels/groups, or monitor smart money on-chain transactions (e.g., subscribe to a paid plan from a Solana RPC provider like Alchemy to use WebSocket for monitoring specified wallet transactions).
    * Based on the received signal messages, create your own token filtering conditions and trading strategies (extract token contract address).
    * Send trading commands to [GMGN Sniper Botarrow-up-right](https://t.me/GMGN_sol03_bot):
      * Method 1 (Simpler, faster): Send the token contract address. You need to enable the automatic buy and sell features of the GMGN Sniper Bot first (pre-set stop-loss and take-profit orders; when buying, it will automatically place a limit sell order). — This feature is in development and will be available soon.
      * Method 2 (More flexible parameters): Send trading commands, such as immediate buy/sell or creating limit buy/sell orders. The trading commands are as follows:


Copy
```
Buy Immediately
/buy ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82 0.5
Indicates buy BOME token with 0.5 SOL immediately
Sell Immediately
/sell ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82 50
/sell ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82 50%
Indicates sell 50% of BOME token holdings immediately
Create Limit Buy Order at Trigger Price
/create limitbuy ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82 0.5@0.1 -exp 3600
Indicates create limit buy order for BOME token, buy 0.5 SOL, trigger price $0.1, expires in 1h (3600 seconds)
Create Limit Sell Order at Trigger Price
/create limitsell ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82 50@0.1 -exp 3600
Indicates create limit sell order for BOME token, sell 50% holdings, trigger price $0.1, expires in 1h (3600 seconds)
Tip: If the '-exp' parameter is omitted, the limit orders default expiration time is 3 days.
```

## 
**🎉 Automation Script Setup Complete**
It is recommended to start with a small amount to test your trading strategy.
If you are interested in automated trading strategies, feel free to join the GMGN official group for discussions at <https://t.me/gmgnai>[arrow-up-right](https://t.me/gmgnai)
[Previous🤝🏻 Cooperation-API: 🔄Data crawling IP whitelistchevron-left](https://docs.gmgn.ai/index/cooperation-api-data-crawling-ip-whitelist)[NextDelete APP accountchevron-right](https://docs.gmgn.ai/index/delete-app-account)
Last updated 1 year ago
