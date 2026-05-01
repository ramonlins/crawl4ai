# Source: https://docs.gmgn.ai/index/snipex

Try GMGN SnipeX Now 👇🏻
  * Web: <https://gmgn.ai/snipex?chain=sol>[arrow-up-right](https://gmgn.ai/snipex?chain=sol)


### 
SnipeX Instructions:
  * Monitor Twitter for new tweet, reply, updates proflie, repost. When a token contract is detected, automatically buy it with simple SnipeX parameter settings.
  * **SnipeX Task Limits** :
    * Max concurrent tasks: 10
    * Task lifetime: 7 days
  * **Supported Chain** : Solana only
  * **Access Requirement** : Telegram wallet users only


### 
SnipeX**settings:**
#### 
1) Twitter Account:
  * Enter the Twitter handle (without "@")
  * Duplicate Twitter handles are not allowed (for both paused and active SnipeX tasks)
  * The Twitter account must **exist** and **not have tweet protection enabled** to create a task


#### 
2) Monitoring Types (Select at least 1):
  * New Tweet
  * Reply
  * Update Profile
  * Repost


#### 
3) Auto-Buy Rules:
  * **Buy Not Graduated Pump tokens:** If the detected token is a Pump.fun token and not graduated, the bot will auto-buy after checking advanced settings
  * **Buy Graduated/Others Tokens:** If the detected token is a Pump.fun graduated token OR a non-Pump token, the bot will auto-buy after checking advanced settings
  * **Snipe If Immigrating:** If the token is a Pump.fun token that’s graduated but not yet migrated to raydium, the bot will bypass advanced checks and auto-snipe upon migration.


#### 
4) Sell Method:
  * **No Sells:** Manual selling required.
  * **Custom TP/SL** : Take-Profit & Stop-Loss
    * **Single** : Supports trailing stop-loss
    * **TP &SL in batches: **Max 10 TP&SL conditions; Enter a negative value in the "TP%" field to set a stop-loss.


**5) Advanced Settings**
  * **Market Cap limit:** You can set the market cap limit when buying tokens
    * For example, if you set the minimum market cap to 50,000, the purchase will only be executed when the token market cap is higher than 50,000 USD
    * For example, if you set the maximum market cap to 100,000, the purchase will only be executed when the token market cap is less than 100,000 USD
  * **Liq Limit:** You can set the liquidity (pool) limit when buying tokens
    * For example, if you set the minimum liquidity to 50,000, the purchase will only be executed when the token liquidity (pool) is higher than 50,000 USD
    * For example, if you set the maximum liquidity to 100,000, the purchase will only be executed when the token liquidity (pool) is less than 100,000 USD
  * **Age limit:** You can limit the creation time of the token. Only buy tokens whose launch time falls within this specific interval
    * For example, if you set the minimum token creation time to 10s, the purchase will only be executed if the token launch time is greater than 10 seconds
    * For example, if you set the maximum token creation time to 1D, the purchase will only be executed if the token launch time is less than 1 day
  * **Min Burnt ratio:** You can set the minimum liquid burnt ratio limit
    * For example, if you set 50%, the purchase will only be executed when the token burnt ratio is greater than or equal to 50%
  * **Skip Holdings** : Won't buy the holding tokens


#### 
6) Set SnipeX trading parameters : Priority fee, Anti-MEV, Slippage
## 
1. SnipeX - web
1) GMGN Home page, click the SnipeX
2) For the user who has obtained the SnipeX whitelist, click Create Task
3) SnipeX parameter setting:
4) View SnipeX data
  * Click SnipeX Tab to view all current and historical SnipeX task data
  * Click any SnipeX task to see its details page
    * SnipeX Data Analytics
    * All trading activities from this task
    * Failed transactions with reasons
    * Tokens filtered out (not purchased by SnipeX)


5) SnipeX alerts
  * You’ll receive SnipeX alerts via [**@GMGN_sol_bot** arrow-up-right](https://t.me/GMGN_sol_bot)


## 
2. SnipeX - bot
**1)** Send /start to [@GMGN_sol_botarrow-up-right](https://t.me/GMGN_sol_bot) , click SnipeX 
2) Click Create
3) SnipeX parameter setting:
4) View SnipeX data
  * View SnipeX data on GMGN website: <https://gmgn.ai/snipex?chain=sol>[arrow-up-right](https://gmgn.ai/snipex?chain=sol)


5) SnipeX alerts
  * You’ll receive SnipeX alerts via [**@GMGN_sol_bot** arrow-up-right](https://t.me/GMGN_sol_bot)


[PreviousX Trackerchevron-left](https://docs.gmgn.ai/index/x-tracker)[NextWallet Radarchevron-right](https://docs.gmgn.ai/index/wallet-radar)
Last updated 9 months ago
