# Source: https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-available-routing-for-eth-base-bsc-transactions

This interface is divided into two parts. One is to accurately specify the input and obtain the output currency quantity. The other is to accurately specify the output and obtain the minimum amount of the input currency.
### 
1. Accurate input
Access point: /defi/router/v1/tx/available_routes_exact_in
Request method: GET
Input parameters:
**Parameter name**
**Parameter Description**
**Is it necessary**
**Example**
token_in_chain
network code, such as eth/polygon/arb, etc.
yes
eth
token_out_chain
network code, such as eth/polygon/arb, etc.
yes
arb
token_in_address
enter the contract address of the token
yes
0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
token_out_address
output token contract address
yes
0xb44C0A4624eaEd2C41EB8437d0Fb5A28F91E7335
in_amount
enter the number of tokens in the smallest unit
yes
100000000
src
source, you can choose gmgn or swapx, the default is gmgn
no
swapx
Return parameter:
**Parameter name**
**Parameter Description**
**Example**
msg
error message
amountIn is required
code
correct 0, incorrect -1
data
Returns the basic information of the cross-chain transaction, mainly including the following information:
Source chain ID: chain_id,
Contract address: to,
Source currency quantity: amount_in,
Source currency USD value: amount_in_usd,
Get the amount of currency: amount_out,
Get the value of USD currency: amount_out_usd,
Purchase token address: buy_token_address,
Selling token address: sell_token_address,
After the step list: steps,
(Steps has three fields: id/type/tool)
**{**`"routes": [{"chain_id": 1,"to": "0x4313C378Cc91eA583C91387B9216e2c03096b27f","amount_in": "10000000000000000","amount_out": "299609399139476657","input_token_address": "0x0000000000000000000000000000000000000000","output_token_address": "0x81de6d37439afb8c5c0a6d6e39e764c89e81d6b5","type": "v2","path": ["0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2","0x81de6d37439afb8c5c0a6d6e39e764c89e81d6b5"],"pool_address": "0xc8d39a869dee360e19d2a2f189c5b87f013d9f85","factory_address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f","fee": 3000,"steps": [{"id": 1,"type": "swap","tool": "uniswapv2"`**}]** ,`"token_in_usd_price": "2246.46","amount_in_usd": "22.4646","token_out_usd_price": "0.00000008532060895067131","amount_out_usd": "25.56285638192488514528660222461067","value": "10000000000000000","price_impact": "0.01","gas_limit": "221343"`**}]** ,`"volatilities": {"token_in": 0,"token_out": 10}`
Returns the routes field of data
**Field Name**
**type**
**Is simulation used?**
**Example**
chain_id
number
yes
to
string
yes
0xb2C435F236AE7697341beb0D98EceD5AB7d35052
amount_in
string
yes
129470074265000000
amount_in2
string
yes
1232343
amount_out
string
yes
1000000000
input_token_address
string
yes
0x0c48250eb1f29491f1efbeec0261eb556f0973c7
output_token_address
string
yes
0x75c97384ca209f915381755c582ec0e2ce88c1ba
type
string
yes
v0, v2, v3, v2-v2, v2-v3, v3-v2
path
string | string[]
yes
[
'0x0c48250eb1f29491f1efbeec0261eb556f0973c7',
'0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
'0x75c97384ca209f915381755c582ec0e2ce88c1ba'
]
path_bytes
string
Yes, V3 multi-hop
pool_address
string | string[]
yes
[
'0xe05d099bfd7f4aa9f2e696f6c3ebe181479961a5',
'0xb54ce26f2e30f64c5b684b141311ce138ab5e00e'
]
factory_address
string | string[]
Yes, V2 multi-hop
0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f
fee
string | string[]
Yes, V3
3000
Steps
array
no
[ { id: 1, type: 'swap', tool: 'uniswapv2' } ]
token_in_usd_price
string
no
10.3099800923283
amount_in_usd
string
no
1.334833
token_out_usd_price
string
no
0.00000000474642715895
amount_out_usd
string
no
1.3226
value
string
yes
10000
gas_limit
string
no
21000
from_address
string
yes
The address of the wallet that initiated the transaction. e.g: 0xb2bA9EA690428E01d82572438De4514F16446251
Description of the fields of returned data `volatilities`:
**Field Name**
**type**
**Example**
token_in
Int, 5-minute price volatility% above
token_out
Int, 5-minute price volatility % above
10
is_fomo
bool, true or false
true
### 
2. Accurate output
Access point: /defi/router/v1/tx/available_routes_exact_out
Request method: GET
Input parameters:
**Parameter name**
**Parameter Description**
**Is it necessary**
**Example**
token_in_chain
Network code, such as eth/polygon/arb, etc.
yes
eth
token_out_chain
Network code, such as eth/polygon/arb, etc.
yes
arb
token_in_address
Enter the contract address of the token
yes
0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
token_out_address
Output token contract address
yes
0xb44C0A4624eaEd2C41EB8437d0Fb5A28F91E7335
out_amount
The number of output tokens, in the smallest unit
yes
100000000
src
Source, you can choose gmgn or swapx, the default is gmgn
no
swapx
Return parameter:
**Parameter name**
**Parameter Description**
**Example**
msg
error message
amountIn is required
code
correct 0, incorrect -1
data
Returns the basic information of the cross-chain transaction, mainly including the following information:Source chain ID: chain_id,Contract address: to,Source currency quantity: amount_in,Source currency USD value: amount_in_usd,Output currency quantity: amount_out,Get the value of USD currency: amount_out_usd,Purchase token address: buy_token_address,Selling token address: sell_token_address,After the step list: steps,(Steps has three fields: id/type/tool)
{"routes":[{"chain_id":1,"to":"0x2abbEAf73456b6c0b1a1E7e32Dbd63Bf4fafAC40","amount_in":"987855194221161593","amount_out":"100000000000000000","input_token_address":"0x481c4572e017e636177920D79db157c0Cf3A4697","output_token_address":"0x2C3Bc638031AAbB701EA5f30c522379dEE5c2B22","type":"v3","path":["0x481c4572e017e636177920D79db157c0Cf3A4697","0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6","0x2C3Bc638031AAbB701EA5f30c522379dEE5c2B22"],"pool_address":["0x717BFacEBD23A5505b061Cf15a9C0fB2Ac1CABE4","0x20A741900D8b8Fcd10b4Af1822EE07622aF165C3"],"fee":[3000,3000],"steps":[{"id":1,"type":"swap","tool":"uniswapv3"}],"token_in_usd_price":0,"amount_in_usd":"0","token_out_usd_price":0,"amount_out_usd":"0","value":0}]}
[Previous🤝🏻 Cooperation-API:🕹Integrate GMGN ETH/Base/BSC Trading APIchevron-left](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api)[NextGet the recommended slippage value of ETH/Base/BSC tokenchevron-right](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-slippage-value-of-eth-base-bsc-token)
Last updated 1 month ago
