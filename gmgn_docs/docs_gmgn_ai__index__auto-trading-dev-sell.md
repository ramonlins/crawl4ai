# Source: https://docs.gmgn.ai/index/auto-trading-dev-sell

Rule:
  * Unlimited tokens species. When the token creator sells part of holdings in a single transaction, it will be automatically sold.
  * Only when you have position, complete settings and click creater, it will automatically follow Dev to sell after Dev sells part of his holdings
  * A token only has one running Dev sell task and submits one transaction. But it can be submitted multiple times


### 
1. Dev Sell - web version
1) Create Dev Sell task:
  * Click Auto trading on the token page, click Dev Sell and enter the editing page
  * Set Sell Holdings ratio and Dev Sell ratio
  * Set slippage, priority fee, anti-MEV, and click save
  * After the settings are completed, click create in any token you want to follow dev to sell. The token will auto sell the amount of holding ratio you set when Dev actual selling ratio ≥ Dev sell ratio you set


2) View or delete your Dev Sell task:
  * In the token details page - Position, you can view your current Dev Sell tasks and could view or delete them


3) When buying any token, if Dev Sell is also selected, it will automatically create a Dev Sell task
## 
2. Dev Sell- bot vision
1) Create Dev Sell task:
  * When you enter a token contract address into the bot, you will see the Dev Sell option. Click it to create a follow-up Dev automatic sell task. When the token creator sells part of his holdings in a single transaction, the token ratio you set will be automatically sold


2) Adjust Dev Sell settings:
  * In the settings, after setting the Dev sell ratio, set the automatic Sell ratio. When the Dev sell ratio is greater than the ratio you set, your position will be automatically sold according to the automatic Sell ratio you set
  * In the settings, you can click the Dev Sell ratio and the Sell ratio, enter them in the reply box and send to complete the change


3) View or delete your Snipe Raydium tasks:
  * Currently, the GMGN TG bot does not support viewing the Dev Sell tasks. Please go to the GMGN site Auto trading dashboard to view it


[PreviousAuto Trading: Migrated Sellchevron-left](https://docs.gmgn.ai/index/auto-trading-migrated-sell)[NextAuto Trading: Quick Buy ＆ Take-Profit / Stop-Losschevron-right](https://docs.gmgn.ai/index/auto-trading-quick-buy-take-profit-stop-loss)
Last updated 8 months ago
