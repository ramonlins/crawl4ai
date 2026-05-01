# Source: https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw

  *   * 

  1.   2.   3.   4. [Security- Google Authenticator](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw#id-4.-security-google-authenticator)
  5. [Deposit USDT/USDC to GMGN wallet, withdraw meme coin, Reclaim Token Rent](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw#id-5.-deposit-usdt-usdc-to-the-tg-wallet-withdraw-meme-coin-recover-token-rent)


## 
Export private key:
⚠️The first time you use the GMGN TG bots, it will automatically generate the SOL chain, EVM chain (ETH/Base/BSC chains share the same address, only the network is different), and Tron chain wallet addresses
  * For the safety of user wallet funds, GMGN all chains ( SOL chain / EVM chain / Tron chain ) are prohibited from exporting private keys; Wallets imported from outside also can‘t export private keys
  * Please note that when you import the private key to any EVM chain bot, the wallet address of the GMGN ETH, Base, BSC chain bots will be changed at the same time. Please pay attention to whether the wallet address has assets in other networks


## 
Import private key:
  * Please enter /start in bot, click wallet, click Add New Wallet/Change Private Key, click import private key, and enter the private key in the reply box (Tron bot doesn't support import peivate key currently)
    * SOL bot: [@GMGN_sol_botarrow-up-right](https://t.me/GMGN_sol_bot) , the transaction network for deposit: Solana
    * ETH bot: [@GMGN_swap_botarrow-up-right](https://t.me/GMGN_swap_bot) , the transaction network for deposit: Ethereum
    * Base bot: [@GMGN_base_botarrow-up-right](https://t.me/GMGN_base_bot) , the transaction network for deposit: Base
    * Bsc bot: [@GMGN_bsc_botarrow-up-right](https://t.me/GMGN_bsc_bot) , the transaction network for deposit: BNB smart chain
    * Tron bot: [@GMGN_tron_botarrow-up-right](https://t.me/GMGN_tron_bot) , the transaction network for deposit: Tron (TRC20) (Tron bot doesn't support import wallet now)
  * When you import a new wallet address to SOL chain bot, it will jump to the GMGN web multi-wallet management page and will not delete the old wallet address. Read more information about multi-wallet system, please click: [🔄 TG Wallet: Connect TG, Multi-Wallet system](https://docs.gmgn.ai/index/tg-wallet-connect-tg-multi-wallet-system)
  * When you import a new wallet address to EVM chain bots, the old wallet address will be automatically deleted. There is no way to help you recover your assets!
  * ⚠️Please ensure the private key is safe and no dangerous program accesses your clipboard. Suggest not to copy the entire private key, but to copy and enter part of it manually


GMGN TG wallet does not support exchanging stablecoins such as USDT/USDC to SOL/ETH. If you deposit USDT/USDC by mistake, please check:[Deposit USDT/USDC to TG wallet, withdraw meme coin, recover token ren](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw#id-5.-deposit-usdt-usdc-to-the-tg-wallet-withdraw-meme-coin-recover-token-rent)
## 
1. TG wallet deposite - web
  * After connecting to the TG wallet on the GMGN official website, click Transfer Funds in the upper right corner


  * When the web3 plug-in wallet is not connected: Use the web3 wallet APP on a mobile phone or other mobile device to scan the code to deposit SOL/ETH; or copy the wallet address below the QR code and transfer SOL/ETH directly to the TG wallet
  * When connected to the web3 plug-in wallet: Enter the number of tokens you want to deposit to the TG wallet in the input box, then click Deposit 
  * Please make sure that the transfer network is correct. If you deposit via the wrong network, there is no way to retrieve it!
    * The transfer network for SOL chain is: Solana, please deposit SOL
    * The transfer network for ETH chain is: Ethereum, please deposit ETH
    * The transfer network for Base chain is: Base, please deposit ETH
    * The transfer network for Bsc chain is: BNB smart chain, please deposit BNB
    * The transfer network for Tron chain is: Tron (TRC20), please deposit TRX


## 
2. TG wallet deposit - bot
  * Enter /wallet in the bot or click on the wallet to enter the wallet page to see your TG wallet address
    * SOL bot: [@GMGN_sol_botarrow-up-right](https://t.me/GMGN_sol_bot) . The transfer network for is: Solana, please deposit SOL
    * ETH bot: [@GMGN_swap_botarrow-up-right](https://t.me/GMGN_swap_bot) . The transfer network is: Ethereum, please deposit ETH
    * Base bot: [@GMGN_base_botarrow-up-right](https://t.me/GMGN_base_bot) . The transfer network is: Base, please deposit ETH
    * Bsc bot: [@GMGN_bsc_botarrow-up-right](https://t.me/GMGN_bsc_bot) . The transfer network is: BNB smart chain, please deposit BNB
    * Tron bot: [@GMGN_tron_botarrow-up-right](https://t.me/GMGN_tron_bot) . The transfer network is: Tron (TRC20), please deposit TRX
  * After clicking ‘Tap to copy’ to copy the wallet address, perform transfer and deposit operations in your other web3 wallets
  * ⚠️ Please ensure the transfer network is correct


## 
3. TG wallet withdrawal
  * For the security of user funds, the GMGN Telegram Bot doesn't support direct withdrawal operations. The token withdrawal feature has been fully migrated to the GMGN Website.
Bot users, please follow these steps to withdraw: 
  * Please complete the account security verification process before withdrawal. Withdrawals locked until security setup is complete: [4. Security- Google Authenticator](https://docs.gmgn.ai/index/tg-wallet-import-export-private-key-deposit-withdraw#id-4.-security-google-authenticator)


#### 
1) Set the extraction whitelist address:
  * After completing the account security binding, please complete the whitelist address setting in the upper right corner of the [Deposit/Withdrawal] page. Transfers are limited to whitelisted addresses, after which transfers bypass 2FA for safer, quicker withdrawals
  * No withdrawals allowed until 3 hours after:
    * First-time whitelist setup
    * Whitelist address change
  * 24-hour withdrawal hold after Google Authenticator re-binding


#### 
2) withdrawal steps:
  * For the safety of your funds, GMGN TG bot cannot directly perform withdrawal operations. Click [Withdraw] in the bot to jump to the GMGN site. Click [Deposit/Withdraw] in the upper right corner to enter the withdrawal page. You can withdraw after setting the withdrawal whitelist wallet


  * Enter the [Deposit/Withdraw] page from the upper right corner of the SOL chain, and the current main wallet will be deposited/withdrawn by default
  * If you need to deposit/withdraw other wallets, please go to the multi-wallet manager page to deposit/withdraw


#### 
3) Maximum Withdrawal Amount Notice:
  * ⚠️ Each on-chain wallet must maintain a minimum balance to preserve data storage and cover transfer gas fees. Therefore, clicking "Max" will not transfer the entire balance


## 
4. Security- Google Authenticator
  * Google Authenticator: a TOTP/HOTP-based 2FA solution, It is primarily used to enhance the security of your GMGN account and protect your assets. After binding, you will be able to perform withdrawal transfers to whitelisted addresses
  * To bind Google Authenticator, go to "Security" in the upper right corner of the GMGN site


  * After you have installed Google Authenticator, suggest click the avatar in the upper right corner, choose "Use Authenticator without an account" to turn off the cloud synchronization function. Turning off cloud synchronization has the following benefits:
    * **Avoid centralization risks** : If the verification code is synchronized to the cloud through the Google account, once a hacker breaks into your Google account (such as through phishing or password leakage), they can obtain **all 2FA verification codes** , making the two-factor authentication invalid
    * **Full control over 2FA** : Turning off cloud sync means that users have full control over their 2FA keys and do not need to trust a third party to store them
    * **Avoid accidental overwriting** : When logging into a Google account on multiple devices, automatic synchronization may cause the authenticator data to be accidentally overwritten or lost
  * Use Google Authenticator to scan the QR code to add the GMGN 2FA verification code, and fill in the generated verification code in the specified location


  * Now you have successfully completed the Google Authenticator binding and can start binding the whitelist address for withdrawal


## 
5. Deposit USDT/USDC to the GMGN wallet, withdraw meme coin, Reclaim Token Rent
### 
1) Deposited USDT/USDC
  * USDT: On SOL, ETH, Base, or BSC chains, you can directly swap USDT for SOL, ETH, BNB Search for USDT on GMGN, find the corresponding CA for each chain, and sell your holdings (ensure your wallet has enough balance for gas fees)


  * USDC: On SOL, ETH, Base, or BSC chains, you can directly swap USDC for SOL, ETH, BNB Search for USDC on GMGN, find the corresponding CA for each chain, and sell your holdings (ensure your wallet has enough balance for gas fees)


### 
2) Withdraw meme coins
  * For withdrawal of meme coins, please check: [4) Deposit, Withdrawal, Consolidaten, Distributionarrow-up-right](https://docs.gmgn.ai/index/tg-wallet-connect-tg-multi-wallet-system#id-4-deposit-withdrawal-consolidaten-distribution)


### 
3) Reclaim token rent (SOL Incinerator)
  * Tokens with a total holding value under $10 can be closed on the asset page to reclaim rent
    * If you can't find the Reclaim Rent button, it may be because: you hold no tokens, and GMGN automatically reclaim rent upon clearing, no manual action needed
    * For tokens cleared before the Reclaim Rent feature was launched, approximately 0.002 SOL in account rent was automatically refunded upon sell-off. You can verify this via historical sold off tx hashes


[PreviousTG Wallet: Connect TG, Multi-Wallet systemchevron-left](https://docs.gmgn.ai/index/tg-wallet-connect-tg-multi-wallet-system)[NextCookingchevron-right](https://docs.gmgn.ai/index/cooking)
Last updated 3 months ago
