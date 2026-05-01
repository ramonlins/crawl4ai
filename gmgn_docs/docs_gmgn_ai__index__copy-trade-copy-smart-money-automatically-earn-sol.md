# Source: https://docs.gmgn.ai/index/copy-trade-copy-smart-money-automatically-earn-sol

⚠️ Please note that if you copy the wallet and his transactions frequently, it may quickly consume your SOL balance; if you do not have high requirements for the speed of copytrade. it is recommended to set up: auto slippage , turn off the Anti-MEV and give less gas priority fee, for example, 0.002-0.006 SOL (a lot of users, although their copy trades profit, but the gas priority fee is too high, resulting in the end of the still lose money)
One copytrade transaction= buying/selling amount + Gas priority fee + 1% GMGN handling fee, no other factors
  *   *   *   *   * [1. Wallet Copy Trading-Web side](https://docs.gmgn.ai/index/copy-trade-copy-smart-money-automatically-earn-sol#web-gen-dan-ru-kou)
  * [2. Wallet Copy Trade-TG Bot side](https://docs.gmgn.ai/index/copy-trade-copy-smart-money-automatically-earn-sol#zhu-yi-shi-xiang)


## 
Copy Trade instructions:
  * By simply setting the copy trading parameters, you can easily copy KOLs and smart money and catch the next golden dog
  * Currently, the Copy Trade supports automatic copy wallets‘ buying, selling, or setting it to sell at take profit and stop loss.
  * You are allowed to create a maximum of **10** wallet copy tasks
  * Currently, only the SOL chain supports wallet copying, and users who have logged in to TG can use the wallet copying function.


## 
**Copy Trade Settings:**
  1. **Single copy buying method**
     * **Fixed buy** : Regardless of the purchase amount of the copy address, purchase is made according to the fixed purchase quantity
     * **Maximum follow-buy** : If the purchase amount of the copy address is less than the set maximum purchase amount, the purchase amount will be based on the purchase amount of the copy address. If the purchase amount of the copy address exceeds the set maximum purchase amount, the purchase will be based on the set maximum volume.
  2. **Selling method**
     * **Automatic follow-up selling:** When the copy address sells coins, it will be sold in proportion to the proportion of its position (only the tokens bought by the copy trade will be sold). For example: the user chooses to copy address A. When address A sells 10% of its own position, the user's follow-up buy will be sold in proportion to 10% (the user's own bought coins or the coins bought by other copy addresses will not be sold)
     * **No follow-up selling:** The system does not automatically sell coins, you need to sell manually
     * **Take profit and stop loss:** You can set the take profit and stop loss ratio by yourself, and the TP/SL will be monitored according to the average price of the position bought by the copy trade. After the TP/SL are turned on, if the copy address sells the currency, it will not follow the selling
     * **Take profit and stop loss( batch) :** The position of the copy trade supports batch selling and can be configured with multiple take profit / stop loss rules
       * When the rule triggered, X% of the copy position will be sold.
       * The same rule will be triggered only once without new add positions.
       * When add position, the rule will be recalculate based on the average price.
  3. **Set copy trading parameters** : Priority fee, Anti-MEV, Slippage
  4. **Advanced copy order settings:**
     * **Market Cap limit:** You can set the market cap limit when target wallet buying tokens
       * For example, if you set the minimum market cap to 50,000, the purchases will only be executed when the target wallet buys a token with a MC higher than $50,000
       * For example, if you set the maximum market cap to 100,000, the purchase will only be executed when the target wallet buys a token with a MC less than $100,000
     * **Liquidity Limit:** You can set the liquidity (pool) limit when target wallet buying tokens
       * For example, if you set the minimum liquidity to 50,000, the purchase will only be executed when the target wallet buys a token with liquidity (pool) higher than $50,000
       * For example, if you set the maximum liquidity to 100,000, the purchase will only be executed when the target wallet buys a token with liquidity (pool) less than $100,000
     * **Token creation time limit:** You can limit the creation time of the copy token. Please note that the system judges based on the time when the token was first created, not the creation time of a certain pool of tokens.
       * For example, if you set the minimum token creation time to 10s, the purchase will only be executed if the token creation time is greater than 10 seconds.
       * For example, if you set the maximum token creation time to 1D, the purchase will only be executed if the token creation time is less than 1 day.
     * **Minimum Pool Burnt ratio:** You can set the minimum liquid burnt ratio limit
       * For example, if you set 50%, the purchase will only be executed when the token burnt ratio is greater than or equal to 50%.
     * **Minimum copy amount:** You can set the minimum copy amount for the target address. Only when the purchase amount of the copy address is greater than the minimum copy amount, the copy purchase will be carried out. 
       * For example, if the minimum copy amount is set to 0.5 SOL, the purchase will be executed only when the target address buys more than or equal to 0.5 SOL.
     * **Maximum copy amount:** You can set the maximum copy amount for the target address. Only when the purchase amount of the copy address is less than or equal to the maximum copy amount, the copy purchase will be carried out. Prevent the target address to buy large amounts of coins to pull up the price then rug pull
       * For example, if the maximum copy amount is set to 10 SOL, when the target address purchase is greater than 10 SOL, no purchase will be made
     * **Single coin position increase times:** You can set the maximum position increase times for the same token. Note: This is the maximum position increase times for the same token under the position holding conditions. The times will be restored after the position is cleared
       * For example, if you set the number of times you add a single coin to your position: 0, it means that if you have a copy order, you will not buy the same token repeatedly (after clearing the position and selling it, you will buy it again).
       * For example, if you set the number of times to add a single coin to your position: 1, it means that if you have a copy order, you can add the same token once, that is, buy it again (after clearing the position and selling, the number of times will be restored)
     * **Filter platform:** filter the token issuance platform. Only when the token purchased by the target wallet is the token of the selected platform, it will copy the purchase (it does not affect the copy selling)
If token A is created in Pump, user settings: only buy coins in Pump
       * When the target wallet buys A in the Pump, you can copy the trade and buy in
       * When the liquidity of A is transferred to Raydium, the target wallet buys A again and no longer copy the purchase.
       * If target wallet sells A on Raydium, you will copy the trade and sell it.
If the user adjusts the copy trading platform to: PumpFun + Raydium
       * When the target wallet buys again on Raydium, you can copy the purchase
     * **Blacklist:** Tokens added to the blacklist **will no longer be copied for buying and selling**
       * Maximum add 20 tokens


## 
**Lightning Mode:**
  * After turning on this mode, your copy trading speed can be increased by about 2s (under the same parameters)
  * However, since this mode uses unconfirmed messages (process) on the chain, the chain may be rolled back, so it is possible that the transaction of the target address is not seen on the chain but your transaction is executed. In extreme cases, the transaction may be executed repeatedly.
  * Please carefully weigh the speed and stability of copy trading to decide whether to turn on the lightning mode


Risk phenomenon:
  * The Lightning mode may monitor selling first and then buying, resulting in the failure of auto-sell


## 
Notice:
  * If copy trade order failed or copy bought is missed, please check whether the copy trade filtering with advanced settings has been enabled
  * If copy **Buy/Sell Fails** (for example: the slippage, low SOL balance, network congestion, timeout, or low priority fee). Buy/sell will be retried 1~3 times depending on the error type, the system will not retry the purchase/selling, you should buy/sell the token manually
  * If 3 consecutive copy trading (including buy/sell transactions) fails, the system will automatically pause the copy task and send a message reminder. When the balance is sufficient, you need to manually restart the copy task, **the system will not automatically restart**


## 
1. Wallet Copy Trading-Web side
1) On the wallet personal page, click Copy Trade
2) Copy Trade -> Rank, click to start copy trade
3) Click Create Copy Trade in Copy Trade page or Rank
4) Copy trading parameter settings:
5) View order data
  * After clicking the Copy Trade tab, you can see all current and historical copy data
  * After clicking any data, you can see the corresponding copy details page: copy data statistics, all copied buy/sell transactions that were successful, all copied failed transactions and the failure reasons


6) Copy Trade notification:
Copy Trade order notifications and limit order notifications are integrated into transaction notifications
## 
2. Wallet Copy Trade-TG Bot side
1) Create New Copy Task:
2) Enter the wallet address you want to copy trade from
3) Set up
添加标签
[PreviousWallet Radarchevron-left](https://docs.gmgn.ai/index/wallet-radar)[NextAuto Trading: Migrated Snipechevron-right](https://docs.gmgn.ai/index/auto-trading-migrated-snipe)
Last updated 3 months ago
