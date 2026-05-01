# Source: https://docs.gmgn.ai/index/zero-latency-wallet-tracking-bot

Push wallet monitoring messages in milliseconds
### 
**Zero-Latency Wallet Tracking Bot**
  * Exclusive private node, push channel acceleration, millisecond-level monitoring speed, one-click fast transaction
  * Zero-Latency Wallet Tracking Notification - SOL: [https://gmgn.ai/follow?chain=sol&tab=follow&groupid=groupidarrow-up-right](https://gmgn.ai/follow?chain=sol&tab=follow&groupid=groupid)
  * Zero-Latency Wallet Tracking Notification - BSC: [https://gmgn.ai/follow?chain=bsc&tab=follow&groupid=groupidarrow-up-right](https://gmgn.ai/follow?chain=bsc&tab=follow&groupid=groupid)


### 
**Setup steps:**
  1. Click to create a Telegram group


  1. invite Bot [@GMGN_vip_Botarrow-up-right](https://t.me/GMGN_vip_bot) to the newly created Telegram group


Copy
```
/start@GMGN_vip_bot
```

Or click info in the upper right corner of the group, click Add to add members, and search for "@GMGN_vip_Bot" (Note that the Bot's unique ID is "@GMGN_vip_Bot", do not add other scammers' bots)
  1. Copy the group ID, or click the "Create Alerts" button to automatically fill in the group ID after jumping


  1. Create a group bot: Click [@BotFatherarrow-up-right](https://t.me/BotFather) , enter /newbot in the dialog box, fill in the bot name first, then fill in the bot username (must end with "bot" and cannot be repeated with other people's bots). After successful creation, copy the bot API token in the red box in the figure below


  1. Paste the bot API token into the form. A maximum of 10 bot tokens can be entered


  1. Invite the newly created bot to the Telegram group


  1. Set group admin rights for your bot


  1. Click the Test Push button to see if the message is sent successfully. If it fails, please check whether the group ID and bot token are correct, and whether Telegram has given the bot permission to send messages.


Click Test Push Button
Click Test Push Button
Message sent failed
Test message sent successfully
  1. Set message parameters: support setting transaction type (all/buy/sell), notification language, transaction amount (under development), and then click Save


  1. After successfully saving, the wallet transaction dynamics you follow will be pushed to the Telegram group in real time


### 
**Frequently Asked Questions**
**Q: Why can’t test messages be sent?**
**Solution:** In general, group IDs starting with -4 or -1 can be used to send test messages. If your Telegram account is registered with a virtual phone number, it may trigger Telegram’s security risk controls, causing the bot to fail to send messages within the group you created.
To troubleshoot:
1. Try typing /groupid in the group. If @GMGN_vip_bot can send a response, it indicates that the group permissions are configured correctly.
2. If the bot does not respond, try adding @GMGN_vip_bot as a group admin or invite a few more friends to the group. Then, try sending the /groupid command again to check if the bot can send messages.
Note: The group ID is not permanent. As the number of group members increases, the group ID may change from starting with -4 to starting with -1. In such cases, you will need to reconfigure the bot form for instant notifications.
[PreviousWallet Alert on Telegramchevron-left](https://docs.gmgn.ai/index/wallet-alert-on-telegram)[NextGMGN TG Alert Channel＆Botchevron-right](https://docs.gmgn.ai/index/gmgn-tg-alert-channel-bot)
Last updated 1 month ago
