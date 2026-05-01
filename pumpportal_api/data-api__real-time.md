# Source: https://pumpportal.fun/data-api/real-time/

[All Pump.fun websocket trading data will incur charges starting May 1, 2026.](https://pumpportal.fun/)
On this page
# Real-time Updates
Beginning May 1, 2026, PumpPortal will charge the same fees for trading data on all platforms. After this change all buy/sell events from subscribeTokenTrade and subscribeAccountTrade methods will be charged the same way regardless of whether the coin has migrated or not.
The subscribeNewToken and subscribeMigration methods are NOT affected by this change, these methods will remain free, meaning no charge will be applied for token creation or migration events.
Beginning May 1, 2026, using subscribeTokenTrade or subscribeAccountTrade will require a [PumpPortal API key](https://pumpportal.fun/trading-api/setup) and linked wallet funded with at least 0.02 SOL. By streaming data, your wallet will incur a charge of 0.01 SOL for every 10000 websocket messages you receive.
Stream real-time trading and token creation data by connecting to the PumpPortal Websocket at `wss://pumpportal.fun/api/data?api-key=your-api-key-here`.
Once you connect, you can subscribe to different data streams. The following methods are available:
  * `subscribeNewToken` For token creation events.
  * `subscribeTokenTrade` For all trades made on specific token(s).
  * `subscribeAccountTrade` For all trades made by specific account(s).
  * `subscribeMigration` For subscribing to token migration events.


You should NOT open a new Websocket connection for every token or account you subscribe to. Instead, you should send any new subscribe messages to the same connection. Clients that repeatedly attempt to open many websocket connections at once may be timed out. Bans expire every hour, so if you accidentally get banned you can fix your code and connect again soon.
### Examples:[​](https://pumpportal.fun/data-api/real-time/#examples "Direct link to Examples:")
  * Python
  * JavaScript



```
import asyncioimport websocketsimport jsonasyncdefsubscribe():  uri ="wss://pumpportal.fun/api/data?api-key=your-api-key-here"asyncwith websockets.connect(uri)as websocket:# Subscribing to token creation events      payload ={"method":"subscribeNewToken",await websocket.send(json.dumps(payload))# Subscribing to migration events      payload ={"method":"subscribeMigration",await websocket.send(json.dumps(payload))# Subscribing to trades made by accounts      payload ={"method":"subscribeAccountTrade","keys":["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]# array of accounts to watchawait websocket.send(json.dumps(payload))# Subscribing to trades on tokens      payload ={"method":"subscribeTokenTrade","keys":["91WNez8D22NwBssQbkzjy4s2ipFrzpmn5hfvWVe2aY5p"]# array of token CAs to watchawait websocket.send(json.dumps(payload))asyncfor message in websocket:print(json.loads(message))# Run the subscribe functionasyncio.get_event_loop().run_until_complete(subscribe())
```


```
importWebSocketfrom'ws';const ws =newWebSocket('wss://pumpportal.fun/api/data?api-key=your-api-key-here');ws.on('open',functionopen(){// Subscribing to token creation eventslet payload ={method:"subscribeNewToken",  ws.send(JSON.stringify(payload));// Subscribing to migration eventslet payload ={method:"subscribeMigration",  ws.send(JSON.stringify(payload));// Subscribing to trades made by accounts  payload ={method:"subscribeAccountTrade",keys:["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]// array of accounts to watch  ws.send(JSON.stringify(payload));// Subscribing to trades on tokens  payload ={method:"subscribeTokenTrade",keys:["91WNez8D22NwBssQbkzjy4s2ipFrzpmn5hfvWVe2aY5p"]// array of token CAs to watch  ws.send(JSON.stringify(payload));});ws.on('message',functionmessage(data){console.log(JSON.parse(data));});
```

You can also unsubscribe from any data stream in the same way, using the following methods:
  * `unsubscribeNewToken`
  * `unsubscribeTokenTrade`
  * `unsubscribeAccountTrade`


  * Python
  * JavaScript



```
import asyncioimport websocketsimport jsonasyncdefsubscribe():uri ="wss://pumpportal.fun/api/data?api-key=your-api-key-here"asyncwith websockets.connect(uri)as websocket:# Subscribing to token creation events    payload ={"method":"subscribeNewToken",await websocket.send(json.dumps(payload))# Unsubscribing from new token events    payload ={"method":"unsubscribeNewToken",await websocket.send(json.dumps(payload))asyncfor message in websocket:print(json.loads(message))# Run the subscribe functionasyncio.get_event_loop().run_until_complete(subscribe())
```


```
const ws =newWebSocket(`wss://pumpportal.fun/api/data?api-key=your-api-key-here`);ws.on('open',functionopen(){  ws.send(JSON.stringify({method:"subscribeTokenTrade",keys:["Bwc4EBE65qXVzZ9ZiieBraj9GZL4Y2d7NN7B9pXENWR2"]}));// unsubscribe after 10 secondssetTimeout(()=>{    ws.send(JSON.stringify({method:"unsubscribeTokenTrade",keys:["Bwc4EBE65qXVzZ9ZiieBraj9GZL4Y2d7NN7B9pXENWR2"]}));},10000);});
```

