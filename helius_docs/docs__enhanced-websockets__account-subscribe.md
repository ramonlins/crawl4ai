# Source: https://www.helius.dev/docs/enhanced-websockets/account-subscribe

## What is `accountSubscribe`?
Solana’s WebSockets support a method that allows you to subscribe to an account and receive notifications via the WebSocket connection whenever there are changes to the lamports or data associated with a matching account public key. This method aligns directly with the [Solana WSS API specification](https://solana.com/docs/rpc/websocket#accountsubscribe).
## Parameters
  * `string`: the account public key, sent in `base58` format (required)
  * `object`: an optional object used to pass additional parameters
  * `encoding`: specifies the format for data returned in the `AccountNotification`. Supported values: `base58` (default), `base64`, `base64+zstd`, `jsonParsed`
  * `commitment`: defines the commitment level for the transaction. Supported values: `finalized` (default), `confirmed`, `processed`


## Account Subscribe Example
In this example, we are subscribing to account changes for the account `SysvarC1ock11111111111111111111111111111111`. We will see an update whenever a change occurs to the account data or the lamports for this account. This happens at a frequent interval for this specific account as the `slot` and `unixTimestamp` are both a part of the returned account data.
Enhanced WebSockets use the same `wss://mainnet.helius-rpc.com` and `wss://devnet.helius-rpc.com` [endpoints](https://www.helius.dev/docs/api-reference/endpoints) as Standard WebSockets.

```
const WebSocket = require('ws');

// Create a WebSocket connection
const ws = new WebSocket('wss://mainnet.helius-rpc.com?api-key=<API_KEY>');

// Function to send a request to the WebSocket server
function sendRequest(ws) {
    const request = {
        jsonrpc: "2.0",
        id: 420,
        method: "accountSubscribe",
        params: [
            "SysvarC1ock11111111111111111111111111111111", // pubkey of account we want to subscribe to

                encoding: "jsonParsed", // base58, base64, base64+zstd, jsonParsed
                commitment: "confirmed", // defaults to finalized if unset



    ws.send(JSON.stringify(request));


// Function to send a ping to the WebSocket server
function startPing(ws) {
    setInterval(() => {
 (ws.readyState === WebSocket.OPEN) {
.ping();
            console.log('Ping sent');

    }, 30000); // Ping every 30 seconds


// Define WebSocket event handlers

ws.on('open', function open() {
    console.log('WebSocket is open');
    sendRequest(ws);  // Send a request once the WebSocket is open
    startPing(ws);    // Start sending pings
});

ws.on('message', function incoming(data) {
    const messageStr = data.toString('utf8');
    try {
        const messageObj = JSON.parse(messageStr);
        console.log('Received:', messageObj);
catch (e) {
        console.error('Failed to parse JSON:', e);

});

ws.on('error', function error(err) {
    console.error('WebSocket error:', err);
});

ws.on('close', function close() {
    console.log('WebSocket is closed');
});

```

### Example Notification

```

    "jsonrpc": "2.0",
    "method": "accountNotification",
    "params": {
        "subscription": 237508762798666,
        "result": {
            "context": {"slot": 235781083},
            "value": {
                "lamports": 1169280,
                "data": "BvEhEb6hixL3QPn41gHcyi2CDGKt381jbNKFFCQr6XDTzCTXCuSUG9D",
                "owner": "Sysvar1111111111111111111111111111111111111",
                "executable": false,
                "rentEpoch": 361,
                "space": 40





```

Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/enhanced-websockets/transaction-subscribe)[ Stream Pump AMM DataLearn how to stream live Solana Pump AMM data using Enhanced WebSockets. Real-time token data, price feeds, and trading activity monitoring. Next ](https://www.helius.dev/docs/enhanced-websockets/stream-pump-amm-data)
On this page
  * [What is accountSubscribe?](https://www.helius.dev/docs/enhanced-websockets/account-subscribe#what-is-accountsubscribe)
  * [Account Subscribe Example](https://www.helius.dev/docs/enhanced-websockets/account-subscribe#account-subscribe-example)
  * [Example Notification](https://www.helius.dev/docs/enhanced-websockets/account-subscribe#example-notification)


Assistant
Responses are generated using AI and may contain mistakes.
