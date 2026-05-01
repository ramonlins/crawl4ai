# Source: https://docs.gmgn.ai/index/transaction-limit-order-failure

## 
Suggest failed users check the slippage ratio, priority fee, and anti-MEV settings first
  * Slippage ratio: Manual buy/sell is recommended to be automatic; auto buy/sell and other limit order operations recommend slippage of 30%-35%; for new and popular coins,suggest 50% or more
  * If there is no requirement for transaction speed, suggest 0.002 SOL ; for auto buy/sell and other limit orders, suggest 0.006 SOL or above. If the transaction amount is greater than 1 SOL,suggest 0.01 SOL or above
  * Enabling the anti-MEV mode can effectively prevent transactions from being sandwiched by MEV bots, but enabling the anti-MEV mode requires a priority fee of at least 0.002 SOL


✅Tips: To learn about common fees/settings such as slippage and priority fees, please click: [GMGN Fees and Common Fees/Settingsarrow-up-right](https://docs-gmgn-ai.translate.goog/cn/~/changes/WZ0l4KjzcPDGB69hW3nh/gmgn-shou-xu-fei-he-chang-jian-fei-yong-she-zhi)
## 
Transaction timeout/failure reason
### 
**1. Reasons and solutions for timeout in obtaining transaction status**
In most cases, it is caused by low priority fees and slippage settings in the wallet; the transaction may be successful even if it is timed out, and you need to check the status on the chain
Error number
Transaction timeout reason
Solution
A1
The priority fee is low, the node packaging speed is slow, and it is easy to time out after the countdown ends.
Increase priority fees
A2
The slippage is low and cannot be triggered when the token price fluctuates greatly (such as violent fluctuations )
Increase slippage ratio
A3
Anti-MEV RPC service failure
Switch to normal mode (turn off anti-pinch)
### 
**2. Reasons for transaction failure (submission failure/execution failure/no available route)**
1) Transaction submission failed (not uploaded to the chain):
Error number
Reasons for transaction submission failure
Solution
B1
Insufficient wallet balance. The wallet SOL balance is insufficient for the purchase and sale amount, or insufficient to pay for Gas. It is recommended that the SOL chain wallet reserve an amount of at least 0.05 SOL.
Make sure there is still a certain balance in the wallet after the transaction
B2
Insufficient wallet tokens when selling. When there are no tokens in the wallet, the transaction cannot be submitted.
Check the amount of tokens in your wallet to ensure the selling amount is within the range
B3
The purchase submission failed. The token itself is limited. It may be that the purchase is limited during the initial stage of the project.
You need to find relevant information on the token social media to confirm
B4
The sale submission failed, maybe because the item is Pixiu or you are on the blacklist
If it is confirmed to be a Pixiu/blacklisted, it cannot be sold
B5
The wallet still shows login, but the wallet login status is abnormal at this time
Reconnect your wallet
2) Transaction execution failed (already uploaded to the chain):
Error number
Reasons for transaction failure
Solution
C1
Usually, the transaction execution fails due to low slippage. Failure to submit to the chain for execution will consume Gas/priority fee.
It is recommended to increase the transaction slippage when the market is in a new market or when the token is in fomo, suggest use auto slippage
3) No available route (not on the chain):
Error number
Reasons for transaction failure
Solution
D1
The token creator/project owner remove Liq, resulting in no available routing
Please confirm whether the project party has burned the pool before trading. Trading will not be possible after the pool is removed
D2
Solana pump.fun, moonshot and other tokens cannot be traded when the token market value reaches $69K and the official is adding a pool and waiting for the opening of Raydium/Meteora DEX
Wait for the token launch to raydium before trading can resume
D3
The sol chain is crowded or there is a problem with the node service provider
If the problem cannot be solved, please give feedback to the community in time.
## 
Order timeout/failure reason
### 
**1. Web page/BOT pending orders and automated trading timeouts**
In most cases, it is caused by low priority fees and slippage settings in the wallet; the transaction may be successful even if it is timed out, and you need to check the status on the chain
Error number
Reasons for timeout of pending orders and automated trading
Solution
H1
The priority fee is low, the node packaging speed is slow, and it is easy to time out after the countdown ends.
Increase priority fees
H2
The slippage is low and cannot be triggered when the token price fluctuates greatly (such as violent fluctuations such as K-line pins)
Increase slippage ratio
H3
Anti-pinch RPC service failure
Switch to normal mode (turn off anti-pinch)
### 
**2. Web page/BOT pending orders and automated transactions failed (pending orders not triggered/pending orders triggered but transaction failed/no available routing)**
1) Limit order creation failed:
Error number
Reasons why limit order creation failed
Solution
G1
The network is unstable
Please try refreshing the page to recreate the limit order
2) Limit order is not triggered (not uploaded to the chain):
Error number
Reasons why limit orders are not triggered
Solution
J1
Due to the pin, it is mistakenly believed that the limit order price has been reached, but it cannot actually be triggered
The pin insertion situation basically cannot be triggered, which is a normal situation and does not need to be solved
J2
If you place an order or perform other operations on the web page, the wallet may still show login, but the login status of the wallet may be abnormal.
Reconnect your wallet
3) Limit order is triggered but the transaction fails:
Error number
Reasons why limit order is triggered but transaction fails
Solution
K1
After the limit order is triggered due to low slippage, the submission to the chain fails to execute, which will consume Gas/priority fee (already on the chain)
Increase transaction slippage, such as automatically or by more than 30%
K2
The wallet balance is insufficient when the order is triggered, the wallet SOL balance is insufficient for the order amount, or insufficient to pay for Gas. It is recommended that the SOL chain wallet reserve amount is at least greater than 0.05 (not on the chain)
Make sure there is still a certain balance in the wallet to execute the order after the order is successfully placed
K3
When the sell order is triggered, there are not enough tokens in the wallet. When there are no tokens in the wallet, the transaction cannot be made (not on the chain)
Check the amount of tokens in your wallet
K4
The buy order failed. The token itself is limited. It may be the initial purchase time limit of the project (not on the chain).
You need to find relevant information on token social media
K5
The sell order failed, maybe because the project is Pixiu or you are on the blacklist (not on the chain)
If it is confirmed to be a Pixiu/blacklisted, it cannot be sold
4) No available route (not on the chain):
Error number
No route available reason
Solution
L1
The token creator/project owner remove Liq, resulting in no available routing
Please confirm whether the project party has burned the pool before trading. Trading will not be possible after the pool is removed
L2
Solana pump.fun, moonshot and other tokens cannot be traded when the token market value reaches $69K and the official is adding a pool and waiting for the opening of Raydium/Meteora DEX
Wait for the token launch to raydium before trading can resume
L3
SOL chain is crowded or there is a problem with the node service provider
If the problem cannot be solved, please give feedback to the community in time.
✅Tips: If the execution fails, you can go to <https://solscan.io/>[arrow-up-right](https://solscan.io/) to query the failure hash to understand the failure reason
### 
TG wallet transaction error information
Check the TG wallet transaction error information and match it with the error number above to find out the timeout/failure reason. We cannot count the transaction error information of the web3 plug-in wallet, so we do not collect it.
TG Wallet transaction error message
Error number
Other reasons
trade_error_0x1: "Insufficient funds in wallet.",
B1
trade_error_0x11: "Account is frozen.",
B2/B3
trade_error_0x1e: "Exceeds desired slippage limit.",
C1
trade_error_0x28: "Insufficient funds in pool.",
D1
trade_error_0xbc4: "Duplicate submission is invalid.",
The transaction order has been submitted
trade_error_0x1773: "Exceeds desired slippage limit.",
C1
trade_error_0x1775: "Liquidity has migrated to Raydium.",
D2
trade_errtrade_error_40001300: "haven't bind tg",
The login status is abnormal, please log in to your TG wallet account again.
ttrade_error_40001400: "build withdraw tx error",
B1
trade_error_40001700: "insufficient tokens",
B2
trade_error_40002700: "No Available Router",
D1/2/3
trade_error_timeout: "Network Error",
G1
Network error caused the failure, please check the network
TG Wallet limid order error message
Error number
Other reasons
order10001: "To increase success rate, set more tip and trade again.",
H1
order10002: "Insufficient",
K2
order10003: "Insufficient",
K3
order10005: "Transaction is still pending(20 seconds)",
J1/H1/2/3
order10006: "Liquidity less than 500U",
L1
oorder10007: "Buy value is 20% higher than liquidity",
Failure due to excessive purchase quantity
order10008: "The total number of active personal orders exceeds 100"
The upper limit of limit orders is 100
order10009: "Status timed out",
J1/H1/2/3
oorder10011: "The priority fee is too low, please increase it",
H1
oorder10012: "Slippage is too low",
H2
order10013: "No Available Router",
L1/2/3
order10014: "Parsing of on-chain data failed",
The coin network may not be supported
order10015: "Insufficient handling fee required for selling",
K2
order10017: "Account frozen",
K4/K5
## 
**If you still have questions about the reasons for transaction failure/timeout, you can go to the GMGN official community to provide feedback. ✈️ GMGN community:**[**https://t.me/gmgnai** arrow-up-right](https://t.me/gmgnai)
[PreviousToken page: Chart - multicharts, Activity, Trading systemchevron-left](https://docs.gmgn.ai/index/token-page-chart-multicharts-activity-trading-system)[NextGMGN Fees ＆ Settingschevron-right](https://docs.gmgn.ai/index/gmgn-fees-settings)
Last updated 8 months ago
