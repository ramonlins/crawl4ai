# Source: https://pumpportal.fun/create-wallet

[All Pump.fun websocket trading data will incur charges starting May 1, 2026.](https://pumpportal.fun/)
On this page
# Create a New Wallet and API Key
You can programmatically create new Lightning wallets and linked api keys by sending a GET request to:
`https://pumpportal.fun/api/create-wallet`
### Examples[​](https://pumpportal.fun/create-wallet/#examples "Direct link to Examples")
  * Python
  * JavaScript
  * CURL



```
import requestsresponse = requests.get(url="https://pumpportal.fun/api/create-wallet")# JSON with keys for a newly generated wallet and the linked API keydata = response.json()
```


```
const response =awaitfetch("https://pumpportal.fun/api/create-wallet",{method:"GET",});// JSON Object with keys for a newly generated wallet and the linked API keyconst data =await response.json();
```


```
curl -L \-X GET \'https://pumpportal.fun/api/create-wallet'
```

