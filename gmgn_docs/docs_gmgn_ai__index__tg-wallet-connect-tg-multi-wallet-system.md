# Source: https://docs.gmgn.ai/index/tg-wallet-connect-tg-multi-wallet-system

  * Flexibly choose multiple ways to connect to GMGN
  * 「Connect Telegram, Connect Phantom, App Scan Code Login」 allows you to use Anti-MEV and various GMGN automation functions.Trade with plugin wallet doesn't support these features


### 
1. Connect Telegram (GMGN TG wallet login)
  * Click Connect in the upper right corner and click Connect Telegram
  * After jumping to Telegram site, click Open Telegram to jump to [@gmgnaibotarrow-up-right](https://t.me/gmgnaibot) login bot
  * Then the bot will send a new login link. Click Login Website to complete the TG wallet login site
  * When you login with GMGN TG wallet for the first time, a new wallet address will be automatically generated in the corresponding chain; the yellow frame parts are the trading bots corresponding to each chain, click them to enter, please follow this tutorial to export the private key: [TG Wallet: Import ＆ Export private key, Deposit, Withdraw](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw)
  * ⚠️ Please note that a login link can only be used once; you can copy the login link to the browser you want to use
  * ⚠️ Please note that the multi-wallet system currently only supports direct buy/sell transactions


### 
2. Connect Phantom
  * Support Phantom Wallet for Login, Custodial Account Creation, and Transactions 
    * Details: GMGN will create a multi-chain custodial wallet account based on your Phantom wallet (single-chain or multi-chain, requiring at least one Solana chain wallet). New wallet addresses are generated for each chain
    * If you need to log in with Phantom on a new device, please import the same wallet account from the old device into the new device Phantom in advance to ensure that you log in to the same escrow account
  * **For the safety of user wallet funds, GMGN all chains**( SOL chain / EVM chain / Tron chain ) **are prohibited from exporting private keys**
    * Phantom's escrow account supports Multi-wallet systems
    * SOL chain Deposit, Withdrawal, Consolidaten, Distribution, withdrawal of meme coins, please read: [3. Multi-wallet management](https://docs.gmgn.ai/index/tg-wallet-connect-tg-multi-wallet-system#id-2.-duo-qian-bao-guan-li-1)
    * For other chain Deposit, Withdrawal, please read: [TG Wallet: Import ＆ Export private key, Deposit, Withdraw](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw)
  * Phantom custodial accounts support new user referral across all chains, with independent referral data
  * ⚠️ Note: To trade with Phantom Wallet, use the “Trade with Wallet” option at the bottom. Data (Follow / Watchlist) from the two login methods are not shared, functioning as separate accounts


### 
3. Multi-wallet management
#### 
1) Multi-wallet management page:
  * After logging in with TG Wallet, click Wallet Manager in the upper right corner to enter the multi-wallet management page


#### 
2) Create Wallet, Import Wallet, Archived, Operation Log:
  * [Create wallet]: Click to generate a new SOL wallet with one click; create up to 10 wallets
  * [Import wallet]: Click to enter the SOL chain single chain wallet address private key to complete the new wallet import; import up to 10 wallets
  * [Archived]: After clicking, the archive list pops up and the wallet can be restored
  * [Operation record]: Click to view your imported private key and other operation records


#### 
3) Manage wallet:
  * [Make Primary]: Click to set this wallet as the main wallet, it will be your default trading wallet. You can also select the multi-wallets for trading on the trading page (Token page)
  * [Wallet Rename]: Rename your wallet to distinguish them
  * [Archive]: Suspend the use of this wallet
    * After the wallet is archived, all open orders, wallet copiers, CTO copier automated strategies of this address will be closed automatically! Ensure all are settled before archiving. To use again, please restore from the archive list


#### 
4) Deposit, Withdrawal, Consolidaten, Distribution:
**Deposit, Withdrawal:**
  * Click [Deposit] or [Withdraw] to complete the deposit and withdrawal of SOL in the wallet. For more details: [🔄TG Wallet: Import ＆ Export private key, Deposit, Withdraw](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw)


**Consolidate, Distribution (extraction of meme coins):**
  * [Consolidate] Multi-to-one transfer Transferring token assets from multiple wallet addresses to a single wallet address, including SOL and meme coins
  * [Distribution] One-to-multi transfer Transferring token assets from one wallet to multiple wallets at once, either proportionally or in fixed amounts, including SOL and meme coins
  * Proper use enables the withdrawal of meme coins and SOL to a designated address.
  * Consolidate and Distribution require 2FA verification and only display tokens with USD value greater than 10 USDT.


### 
4. Multi-wallet trading
  * On the token page, click the multi-wallet part, check the wallets to be used for the trading, then click Select Wallets to ensure
  * After the select trading wallets, click Buy xx SOL, and the multi-wallets you selected will buy this token at same time
  * After the select trading wallets, click Sell xx SOL, and the multi-wallets you selected will sell the percentage of this token at same time. For example: if you sell 50%, each wallet will sell 50% of the holding separately


[PreviousGMGN TG Swap Bot - ETHchevron-left](https://docs.gmgn.ai/index/gmgn-tg-swap-bot-eth)[NextTG Wallet: Import ＆ Export private key, Deposit, Withdrawchevron-right](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw)
Last updated 11 months ago
