# Source: https://pumpportal.fun/data-api/pump-swap/

[All Pump.fun websocket trading data will incur charges starting May 1, 2026.](https://pumpportal.fun/)
On this page
# PumpSwap Data API
Accessing PumpSwap data requires a [PumpPortal API key](https://pumpportal.fun/trading-api/setup) and linked wallet funded with at least 0.02 SOL. By streaming PumpSwap data your wallet will incur a charge of 0.01 SOL for every 10000 websocket messages you receive.
PumpSwap data is enabled only if you connect to the websocket using the following URL format:
`wss://pumpportal.fun/api/data?api-key=your-api-key-here`
If the wallet linked to your API key does not contain the minimum balance of SOL, the connection will be restricted to only trades on the bonding curve.
### Examples:[​](https://pumpportal.fun/data-api/pump-swap/#examples "Direct link to Examples:")
  * Python
  * JavaScript



```
import asyncioimport websocketsimport jsonasyncdefsubscribe():  uri ="wss://pumpportal.fun/api/data?api-key=your-api-key-here"asyncwith websockets.connect(uri)as websocket:# Subscribing to trades made by accounts      payload ={"method":"subscribeAccountTrade","keys":["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]# array of accounts to watchawait websocket.send(json.dumps(payload))# Subscribing to trades on tokens      payload ={"method":"subscribeTokenTrade","keys":["GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump"]# array of token CAs to watchawait websocket.send(json.dumps(payload))asyncfor message in websocket:print(json.loads(message))# Run the subscribe functionasyncio.get_event_loop().run_until_complete(subscribe())
```


```
importWebSocketfrom'ws';const ws =newWebSocket('wss://pumpportal.fun/api/data?api-key=your-api-key-here');ws.on('open',functionopen(){// Subscribing to trades made by accounts  payload ={method:"subscribeAccountTrade",keys:["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]// array of accounts to watch  ws.send(JSON.stringify(payload));// Subscribing to trades on tokens  payload ={method:"subscribeTokenTrade",keys:["GkyPYa7NnCFbduLknCfBfP7p8564X1VZhwZYJ6CZpump"]// array of token CAs to watch  ws.send(JSON.stringify(payload));});ws.on('message',functionmessage(data){console.log(JSON.parse(data));});
```

You can also unsubscribe from any data stream in the same way, using the following methods:
  * `unsubscribeTokenTrade`
  * `unsubscribeAccountTrade`


