# Source: https://pumpportal.fun/creator-fee/

[All Pump.fun websocket trading data will incur charges starting May 1, 2026.](https://pumpportal.fun/)
On this page
# Claiming Token Creator Fees
Pump.fun rewards token creators by allowing them to collect a fraction of the fees generated from trading activity on their token. You can use the PumpPortal Lightning or Local Transaction APIs to claim any creator fees from Pump.fun. The Lightning Transaction API can now also be used to claim creator fees from Meteora Dynamic Bonding Curves.
Examples below:
### Lightning Transaction Examples:[​](https://pumpportal.fun/creator-fee/#lightning-transaction-examples "Direct link to Lightning Transaction Examples:")
  * Python
  * JavaScript



```
import requestsresponse = requests.post(url="https://pumpportal.fun/api/trade?api-key=your-api-key-here", data={"action":"collectCreatorFee","priorityFee":0.000001,"pool":"meteora-dbc"# "pump" or "meteora-dbc""mint":"token CA"# the token for which you are claiming fees# Note: pump.fun claims creator fees all at once, so you do not need to specify "mint"data = response.json()# Tx signature or error(s)
```


```
const response =awaitfetch("https://pumpportal.fun/api/trade?api-key=your-api-key-here",{method:"POST",headers:{"Content-Type":"application/json"body:JSON.stringify({"action":"collectCreatorFee","priorityFee":0.000001,"pool":"meteora-dbc"// "pump" or "meteora-dbc""mint":"token CA"// the token for which you are claiming fees// Note: pump.fun claims creator fees all at once, so you do not need to specify "mint"});const data =await response.json();// JSON object with tx signature or error(s)
```

### Local Transaction Examples:[​](https://pumpportal.fun/creator-fee/#local-transaction-examples "Direct link to Local Transaction Examples:")
  * Python
  * JavaScript



```
import requestsfrom solders.transaction import VersionedTransactionfrom solders.keypair import Keypairfrom solders.commitment_config import CommitmentLevelfrom solders.rpc.requests import SendVersionedTransactionfrom solders.rpc.config import RpcSendTransactionConfigresponse = requests.post(url="https://pumpportal.fun/api/trade-local", data={"publicKey":"Your public key here","action":"collectCreatorFee","priorityFee":0.000001,keypair = Keypair.from_base58_string("Your base 58 private key here")tx = VersionedTransaction(VersionedTransaction.from_bytes(response.content).message,[keypair])commitment = CommitmentLevel.Confirmedconfig = RpcSendTransactionConfig(preflight_commitment=commitment)txPayload = SendVersionedTransaction(tx, config)response = requests.post(    url="Your RPC Endpoint here - Eg: https://api.mainnet-beta.solana.com/",    headers={"Content-Type":"application/json"},    data=SendVersionedTransaction(tx, config).to_json()txSignature = response.json()['result']print(f'Transaction: https://solscan.io/tx/{txSignature}')
```


```
import{VersionedTransaction,Connection,Keypair}from'@solana/web3.js';importbs58from"bs58";constRPC_ENDPOINT="Your RPC Endpoint";const web3Connection =newConnection(RPC_ENDPOINT,'confirmed',asyncfunctionsendPortalTransaction(){const response =awaitfetch(`https://pumpportal.fun/api/trade-local`,{method:"POST",headers:{"Content-Type":"application/json"body:JSON.stringify({"publicKey":"Your public key here","action":"collectCreatorFee","priorityFee":0.000001,});if(response.status===200){// successfully generated transactionconst data =await response.arrayBuffer();const tx =VersionedTransaction.deserialize(newUint8Array(data));const signerKeyPair =Keypair.fromSecretKey(bs58.decode("your-wallet-private-key"));      tx.sign([signerKeyPair]);const signature =await web3Connection.sendTransaction(tx)console.log("Transaction: https://solscan.io/tx/"+ signature);}else{console.log(response.statusText);// log errorsendPortalTransaction();
```

