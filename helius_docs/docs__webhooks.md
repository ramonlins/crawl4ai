# Source: https://www.helius.dev/docs/webhooks

## What are Solana webhooks?
Solana webhooks are real-time HTTP notifications sent to your application when on-chain events occur. Instead of continuously polling the blockchain, Helius pushes parsed transaction data directly to your endpoint whenever a wallet transfers funds, an NFT sells, or any monitored transaction type fires. Use webhooks to power trading bots, analytics dashboards, compliance pipelines, and event-driven automation. We offer a user-friendly interface, programmatic API, and SDK access for easily creating and managing webhooks. For frequently asked questions, see the [Webhooks FAQ](https://www.helius.dev/docs/faqs/webhooks).
Helius may retry webhook deliveries if your server does not respond successfully, and you might receive duplicate events. For details on retries and handling duplicates, see the [Webhooks FAQ](https://www.helius.dev/docs/faqs/webhooks#retries).
## Pricing
Webhook events are charged at **1 credit** when Helius processes and sends the event to your endpoint. You are charged regardless of whether your endpoint successfully processes the webhook or not. Editing, adding, or deleting a webhook via the API will cost 100 credits/request.
## Types of Webhooks
We currently offer several types of webhooks tailored to different needs:
### Enhanced Transaction Webhooks
Provide human-readable, parsed data for specific transaction types (e.g., NFT sales) related to the addresses you monitor. This is ideal if you want filtered, actionable insights.
### Raw Transaction Webhooks
This option delivers raw transaction data for all transactions involving the addresses you monitor. It does not allow filtering by transaction type.
Raw Transaction Webhooks offer lower latency since they do not involve parsing event types.
### Discord Webhooks
Stream updates for specific transaction types directly to a designated Discord channel as formatted messages. To use this option, you must submit your Discord Webhook URL.
### Event Payload Example
Enhanced

```


    "accountData": [

        "account": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "nativeBalanceChange": -72938049280,
        "tokenBalanceChanges": []


        "account": "NTYeYJ1wr4bpM5xo6zx5En44SvJFAd35zTxxNoERYqd",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "AAaTGaA3uVqikfVEwoSG7EwkCb4bBDsMEyueiVUS5CaU",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "D8TxfGwdu9MiNMoJmUoC9wQfNfNT7Lnm6DzifQHRTy6B",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE",
        "nativeBalanceChange": 71860273440,
        "tokenBalanceChanges": []


        "account": "25DTUAd1roBFoUQaxJQByL6Qy2cKQCBp4bK9sgfy9UiM",
        "nativeBalanceChange": -2039280,
        "tokenBalanceChanges": [

            "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
            "rawTokenAmount": {
              "decimals": 0,
              "tokenAmount": "-1"

            "tokenAccount": "25DTUAd1roBFoUQaxJQByL6Qy2cKQCBp4bK9sgfy9UiM",
            "userAccount": "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix"




        "account": "DTYuh7gAGGZg2okM7hdFfU1yMY9LUemCiPyD5Z5GCs6Z",
        "nativeBalanceChange": 2039280,
        "tokenBalanceChanges": [

            "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
            "rawTokenAmount": {
              "decimals": 0,
              "tokenAmount": "1"

            "tokenAccount": "DTYuh7gAGGZg2okM7hdFfU1yMY9LUemCiPyD5Z5GCs6Z",
            "userAccount": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX"




        "account": "rFqFJ9g7TGBD8Ed7TPDnvGKZ5pWLPDyxLcvcH2eRCtt",
        "nativeBalanceChange": 1080000000,
        "tokenBalanceChanges": []


        "account": "CgXS5xC3qAGSg9txD9bS7BUgugZwshivGXpCJcGmdwrd",
        "nativeBalanceChange": -2234160,
        "tokenBalanceChanges": []


        "account": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "11111111111111111111111111111111",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "AYZsWahcrSnkwqbA1ji7wEzgAnGjLNJhVUMDPfACECZf",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "SysvarRent111111111111111111111111111111111",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


        "account": "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix",
        "nativeBalanceChange": 0,
        "tokenBalanceChanges": []


    "description": "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE sold Fox #7637 to CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX for 72 SOL on MAGIC_EDEN.",
    "events": {
      "nft": {
        "amount": 72000000000,
        "buyer": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "description": "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE sold Fox #7637 to CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX for 72 SOL on MAGIC_EDEN.",
        "fee": 10000,
        "feePayer": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "nfts": [

            "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
            "tokenStandard": "NonFungible"


        "saleType": "INSTANT_SALE",
        "seller": "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE",
        "signature": "5nNtjezQMYBHvgSQmoRmJPiXGsPAWmJPoGSa64xanqrauogiVzFyGQhKeFataHGXq51jR2hjbzNTkPUpP787HAmL",
        "slot": 171942732,
        "source": "MAGIC_EDEN",
        "staker": "",
        "timestamp": 1673445241,
        "type": "NFT_SALE"


    "fee": 10000,
    "feePayer": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
    "nativeTransfers": [

        "amount": 72936000000,
        "fromUserAccount": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "toUserAccount": "AAaTGaA3uVqikfVEwoSG7EwkCb4bBDsMEyueiVUS5CaU"


        "amount": 2011440,
        "fromUserAccount": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "toUserAccount": "D8TxfGwdu9MiNMoJmUoC9wQfNfNT7Lnm6DzifQHRTy6B"


        "amount": 71856000000,
        "fromUserAccount": "AAaTGaA3uVqikfVEwoSG7EwkCb4bBDsMEyueiVUS5CaU",
        "toUserAccount": "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE"


        "amount": 1080000000,
        "fromUserAccount": "AAaTGaA3uVqikfVEwoSG7EwkCb4bBDsMEyueiVUS5CaU",
        "toUserAccount": "rFqFJ9g7TGBD8Ed7TPDnvGKZ5pWLPDyxLcvcH2eRCtt"


        "amount": 2039280,
        "fromUserAccount": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "toUserAccount": "DTYuh7gAGGZg2okM7hdFfU1yMY9LUemCiPyD5Z5GCs6Z"


    "signature": "5nNtjezQMYBHvgSQmoRmJPiXGsPAWmJPoGSa64xanqrauogiVzFyGQhKeFataHGXq51jR2hjbzNTkPUpP787HAmL",
    "slot": 171942732,
    "source": "MAGIC_EDEN",
    "timestamp": 1673445241,
    "tokenTransfers": [

        "fromTokenAccount": "25DTUAd1roBFoUQaxJQByL6Qy2cKQCBp4bK9sgfy9UiM",
        "fromUserAccount": "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix",
        "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
        "toTokenAccount": "DTYuh7gAGGZg2okM7hdFfU1yMY9LUemCiPyD5Z5GCs6Z",
        "toUserAccount": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
        "tokenAmount": 1,
        "tokenStandard": "NonFungible"


    "type": "NFT_SALE"



```


```


    "blockTime": 1673445241,
    "indexWithinBlock": 2557,
    "meta": {
      "err": null,
      "fee": 10000,
      "innerInstructions": [

          "index": 0,
          "instructions": [

              "accounts": [



              "data": "3Bxs3zs3x6pg4XWo",
              "programIdIndex": 12




          "index": 1,
          "instructions": [

              "accounts": [



              "data": "11112nba6qLH4BKL4MW8GP9ayKApZeYn3LQKJdPdeSXbRW1n6UPeJ8y77ps6sAVwAjdxzh",
              "programIdIndex": 12




          "index": 2,
          "instructions": [

              "accounts": [



              "data": "3Bxs3zx147oWJQej",
              "programIdIndex": 12


              "accounts": [



              "data": "3Bxs3zwT1TGLhiT9",
              "programIdIndex": 12


              "accounts": [







              "data": "1",
              "programIdIndex": 17


              "accounts": [


              "data": "84eT",
              "programIdIndex": 15


              "accounts": [



              "data": "11119os1e9qSs2u7TsThXqkBSRVFxhmYaFKFZ1waB2X7armDmvK3p5GmLdUxYdg3h7QSrL",
              "programIdIndex": 12


              "accounts": [


              "data": "P",
              "programIdIndex": 15


              "accounts": [



              "data": "6YTZgAHgNKVRJ2mAHQUYC1DgXF6dPCgbSWA5P4gZoSfGV",
              "programIdIndex": 15


              "accounts": [




              "data": "3DdGGhkhJbjm",
              "programIdIndex": 15


              "accounts": [




              "data": "A",
              "programIdIndex": 15




      "loadedAddresses": {
        "readonly": [],
        "writable": []

      "logMessages": [
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K invoke [1]",
        "Program log: Instruction: Deposit",
        "Program 11111111111111111111111111111111 invoke [2]",
        "Program 11111111111111111111111111111111 success",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K consumed 10148 of 600000 compute units",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K success",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K invoke [1]",
        "Program log: Instruction: Buy",
        "Program 11111111111111111111111111111111 invoke [2]",
        "Program 11111111111111111111111111111111 success",
        "Program log: {\"price\":72000000000,\"buyer_expiry\":0}",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K consumed 30501 of 589852 compute units",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K success",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K invoke [1]",
        "Program log: Instruction: ExecuteSaleV2",
        "Program 11111111111111111111111111111111 invoke [2]",
        "Program 11111111111111111111111111111111 success",
        "Program 11111111111111111111111111111111 invoke [2]",
        "Program 11111111111111111111111111111111 success",
        "Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL invoke [2]",
        "Program log: Create",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [3]",
        "Program log: Instruction: GetAccountDataSize",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 1622 of 497733 compute units",
        "Program return: TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA pQAAAAAAAAA=",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
        "Program 11111111111111111111111111111111 invoke [3]",
        "Program 11111111111111111111111111111111 success",
        "Program log: Initialize the associated token account",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [3]",
        "Program log: Instruction: InitializeImmutableOwner",
        "Program log: Please upgrade to SPL Token 2022 for immutable owner support",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 1405 of 491243 compute units",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [3]",
        "Program log: Instruction: InitializeAccount3",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4241 of 487361 compute units",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
        "Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL consumed 21793 of 504630 compute units",
        "Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL success",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]",
        "Program log: Instruction: Transfer",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4645 of 475696 compute units",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]",
        "Program log: Instruction: CloseAccount",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 3033 of 456654 compute units",
        "Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success",
        "Program log: {\"price\":72000000000,\"seller_expiry\":-1,\"buyer_expiry\":0}",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K consumed 109266 of 559351 compute units",
        "Program M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K success"

      "postBalances": [
        371980779080,


        100129388687,

        81872924494,

        2039280,
        993583055919,

        1141440,
        3654000,

        1461600,
        5616720,
        934087680,
        1009200,
        731913600,
        457953014766

      "postTokenBalances": [

          "accountIndex": 7,
          "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
          "owner": "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
          "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
          "uiTokenAmount": {
            "amount": "1",
            "decimals": 0,
            "uiAmount": 1,
            "uiAmountString": "1"



      "preBalances": [
        444918828360,


        100129388687,

        10012651054,
        2039280,

        992503055919,
        2234160,
        1141440,
        3654000,

        1461600,
        5616720,
        934087680,
        1009200,
        731913600,
        457953014766

      "preTokenBalances": [

          "accountIndex": 6,
          "mint": "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
          "owner": "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix",
          "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
          "uiTokenAmount": {
            "amount": "1",
            "decimals": 0,
            "uiAmount": 1,
            "uiAmountString": "1"



      "rewards": []

    "slot": 171942732,
    "transaction": {
      "message": {
        "accountKeys": [
          "CKs1E69a2e9TmH4mKKLrXFF8kD3ZnwKjoEuXa6sz9WqX",
          "NTYeYJ1wr4bpM5xo6zx5En44SvJFAd35zTxxNoERYqd",
          "AAaTGaA3uVqikfVEwoSG7EwkCb4bBDsMEyueiVUS5CaU",
          "autMW8SgBkVYeBgqYiTuJZnkvDZMVU2MHJh9Jh7CSQ2",
          "D8TxfGwdu9MiNMoJmUoC9wQfNfNT7Lnm6DzifQHRTy6B",
          "5DxD5ViWjvRZEkxQEaJHZw2sBsso6xoXx3wGFNKgXUzE",
          "25DTUAd1roBFoUQaxJQByL6Qy2cKQCBp4bK9sgfy9UiM",
          "DTYuh7gAGGZg2okM7hdFfU1yMY9LUemCiPyD5Z5GCs6Z",
          "rFqFJ9g7TGBD8Ed7TPDnvGKZ5pWLPDyxLcvcH2eRCtt",
          "CgXS5xC3qAGSg9txD9bS7BUgugZwshivGXpCJcGmdwrd",
          "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
          "E8cU1WiRWjanGxmn96ewBgk9vPTcL6AEZ1t6F6fkgUWe",
          "11111111111111111111111111111111",
          "FdsNQE5EeCe57tbEYCRV1JwW5dzNCof7MUTaGWhmzYqu",
          "AYZsWahcrSnkwqbA1ji7wEzgAnGjLNJhVUMDPfACECZf",
          "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
          "SysvarRent111111111111111111111111111111111",
          "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL",
          "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix"

        "addressTableLookups": null,
        "header": {
          "numReadonlySignedAccounts": 1,
          "numReadonlyUnsignedAccounts": 9,
          "numRequiredSignatures": 2

        "instructions": [

            "accounts": [







            "data": "3GyWrkssW12wSfxjTynBnbif",
            "programIdIndex": 10


            "accounts": [













            "data": "3Jmjmsq2jyrch5iz612vBLZCRB498owPe7qezQVetRZhiMu",
            "programIdIndex": 10


            "accounts": [





















            "data": "B2rqPwAgvj3t35y6HpdumfhdhsZMLNFLmXMC9Uz2HX4nNAwirTk3o98vTazFB1y",
            "programIdIndex": 10


        "recentBlockhash": "3NRncb7FJuDruQjMDxnHvJBQkvkHa7KSUBqBsxG21roZ"

      "signatures": [
        "5nNtjezQMYBHvgSQmoRmJPiXGsPAWmJPoGSa64xanqrauogiVzFyGQhKeFataHGXq51jR2hjbzNTkPUpP787HAmL",
        "4dWBkbLHGvU2jw9Sjj6YETtKfaVKAAN1M8aWzXRNC4aHBckUzM73n3FddNbWTtfUvkU2vFRQ7bKHMwKZQ5dGy1iH"





```

## Quick Start
We provide three convenient methods to create, edit, and manage webhooks on Helius.
### Via Helius Dashboard
The Helius UI is perfect if you prefer a no-code solution with additional features like viewing logs and sending test webhook events. You can access it directly through our [Dashboard](https://dashboard.helius.dev/webhooks). You can add up to 25 addresses via the Dashboard. To monitor more than 25 addresses, you can use our API or SDK.
Via Dashboard
You can create a webhook directly from the dashboard:
  1. Navigate to the [Helius Dashboard](https://dashboard.helius.dev/webhooks)
  2. Click “Add Webhook”
  3. Complete the required fields
  4. Click “Create Webhook”


### Via Helius API
If you’re not working with Typescript or Javascript, you’ll need to interact with our webhooks through REST API:
## [API Reference Learn about the Webhooks API endpoints and how to use them. ](https://www.helius.dev/docs/api-reference/webhooks)
### Via Helius SDK
The easiest—and most enjoyable—way to interact with Helius webhooks is through our official SDKs. We currently offer SDKs for **TypeScript** and **Rust**.
## [TypeScript SDK The TypeScript SDK provides powerful abstractions for webhooks. ](https://github.com/helius-labs/helius-sdk#webhooks)
## [Rust SDK Our Rust SDK offers native Rust support for Helius webhooks. ](https://github.com/helius-labs/helius-rust-sdk)
The SDKs provide powerful abstractions that enhance the functionality of webhooks.
## Automatic Disabling of Failing Webhooks
Helius monitors webhook endpoint health and automatically disables webhooks that consistently fail to receive deliveries. This prevents wasted delivery attempts against unreachable or broken endpoints.
### How It Works
  * **Paid plans (Dev and above):** Webhooks with a **≥ 95% failure rate over 7 days** are automatically disabled.
  * **Free plan:** Webhooks are evaluated over a **24-hour window** with the same failure threshold.

The system checks webhook health every 4 hours. When a webhook is disabled, deliveries stop within seconds.
### Email Notifications
Users on the **Dev plan and above** receive an email notification when a webhook is automatically disabled.
### Re-enabling a Disabled Webhook
Fix your endpoint
Resolve the issue causing delivery failures (e.g., server downtime, incorrect URL, endpoint errors).
Log in to the Helius Dashboard
Go to the [Helius Dashboard](https://dashboard.helius.dev/webhooks).
Re-enable the webhook
Find the disabled webhook and toggle it back on.
You can also re-enable webhooks programmatically via the [Toggle Webhook API endpoint](https://www.helius.dev/docs/api-reference/webhooks/toggle-webhook).
After re-enabling, the webhook enters a **24-hour grace period** during which it will not be automatically disabled again. This gives you time to verify that your endpoint is healthy.
## Example Uses
### Bots
  * When an NFT is listed on marketplace X, trigger an “NFT buy” action.
  * When a margin position is unhealthy, trigger a “liquidation” action.


### Monitoring & Alerts
  * When a program emits a certain log, it triggers PagerDuty integration.
  * When a token account balance changes by more than X%, use Dialect to communicate a warning action.


### Event-driven Indexing
  * When any transaction occurs for a given program, send it directly to your database or backend.


### Notifications & Activity Tracking
  * When transferring from wallet X to wallet Y — send a Slack notification or email.


### Analytics & Logs
  * When event X happens, send it to an ETL pipeline or persist it directly on Helius to view trends over time.


### Workflow Automation
  * When event X happens, trigger any set of actions.


Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/rpc/websocket/stream-pump-amm-data)[ Transaction TypesComplete reference guide to Solana webhook transaction types. Learn about NFT sales, DeFi swaps, staking, and 100+ supported blockchain transaction types. Next ](https://www.helius.dev/docs/webhooks/transaction-types)
On this page
  * [What are Solana webhooks?](https://www.helius.dev/docs/webhooks#what-are-solana-webhooks)
  * [Enhanced Transaction Webhooks](https://www.helius.dev/docs/webhooks#enhanced-transaction-webhooks)
  * [Raw Transaction Webhooks](https://www.helius.dev/docs/webhooks#raw-transaction-webhooks)
  * [Event Payload Example](https://www.helius.dev/docs/webhooks#event-payload-example)
  * [Automatic Disabling of Failing Webhooks](https://www.helius.dev/docs/webhooks#automatic-disabling-of-failing-webhooks)
  * [Re-enabling a Disabled Webhook](https://www.helius.dev/docs/webhooks#re-enabling-a-disabled-webhook)
  * [Event-driven Indexing](https://www.helius.dev/docs/webhooks#event-driven-indexing)
  * [Notifications & Activity Tracking](https://www.helius.dev/docs/webhooks#notifications-%26-activity-tracking)


Assistant
Responses are generated using AI and may contain mistakes.
