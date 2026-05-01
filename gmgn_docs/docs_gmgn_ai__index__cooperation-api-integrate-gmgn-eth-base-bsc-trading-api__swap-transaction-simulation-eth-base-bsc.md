# Source: https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/swap-transaction-simulation-eth-base-bsc

After the user selects a specific route, the route information is passed to the interface as a parameter, along with the caller's wallet address and slippage value (a number above %). The interface will return the parameters required for submitting to the chain, such as inputdata, value, and gas_limit. The interface will perform a simulated transaction. If gas_limit = 0, it means that the transaction will fail.
#### 
1. Accurate input
Access point: /defi/router/v1/tx/simulate_route_exact_in
Request method: POST
Input parameters:
**Parameter name**
**Parameter Description**
**Is it necessary**
**Example**
route
a route returned by the interface
yes
{ "chain_id": 1, "to": "0x2abbEAf73456b6c0b1a1E7e32Dbd63Bf4fafAC40", "amount_in": "100000000000000000", "amount_out": "36565987379429384449", "input_token_address": "0x0000000000000000000000000000000000000000", "output_token_address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "type": "v2", "path": [ "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984" ], "pool_address": "0xdafd66636e2561b0284edde37e42d192f2844d40", "factory_address": "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac", "fee": 3000, "steps": [ { "id": 1, "type": "swap", "tool": "sushiswapv2" } ], "token_in_usd_price": "1636.24949802", "amount_in_usd": "163.624949802", "token_out_usd_price": 0, "amount_out_usd": "0", "value": "100000000000000000" }
slippage
slippage
yes
10
from_address
call wallet address
yes
0x21A2c6c70Bbbe32A9C865a305C1c490E3F40Ad36
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
tx
{chain_id: 1,to: '0x2abbEAf73456b6c0b1a1E7e32Dbd63Bf4fafAC40',amount_in: '1000000000000',amount_out: '9287306518470736046',buy_token_address: '0x0000000000000000000000000000000000000000',sell_token_address: '0xF2a79EF11ACBba33abAA7bACE0178eA66e6d80b8',type: 'v2',path: ['0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0xF2a79EF11ACBba33abAA7bACE0178eA66e6d80b8'],pool_address: '0xeb56b2cc0d2eaf6e04a52dc809019431b3b040f0',fee: 3000,steps: [ { id: 1, type: 'swap', tool: 'uniswapv2' } ],token_in_usd_price: 0.001,amount_in_usd: '1e-9',token_out_usd_price: 0.001,amount_out_usd: '0.009776112124706037943',value: '1000000000000',data: '0x5b9e90060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f2a79ef11acbba33abaa7bace0178ea66e6d80b8000000000000000000000000000000000000000000000000000000e8d4a5100000000000000000000000000000000000000000000000000080e32412819e38ae000000000000000000000000eb56b2cc0d2eaf6e04a52dc809019431b3b040f0',gas_limit: '166773'}
### 
2. Accurate output
Access point: /defi/router/v1/tx/simulate_route_exact_out
Request method: POST
Input parameters:
**Parameter name**
**Parameter Description**
**Is it necessary**
**Example**
route
one of the routes returned by the available routing interface
yes
{ "chain_id": 1, "to": "0x2abbEAf73456b6c0b1a1E7e32Dbd63Bf4fafAC40", "amount_in": "100000000000000000", "amount_out": "36565987379429384449", "input_token_address": "0x0000000000000000000000000000000000000000", "output_token_address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "type": "v2", "path": [ "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984" ], "pool_address": "0xdafd66636e2561b0284edde37e42d192f2844d40", "factory_address": "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac", "fee": 3000, "steps": [ { "id": 1, "type": "swap", "tool": "sushiswapv2" } ], "token_in_usd_price": "1636.24949802", "amount_in_usd": "163.624949802", "token_out_usd_price": 0, "amount_out_usd": "0", "value": "100000000000000000" }
slippage
slippage
yes
10
from_address
call wallet address
yes
0x21A2c6c70Bbbe32A9C865a305C1c490E3F40Ad36
Return parameter:
**Parameter name**
**Parameter Description**
**Example**
msg
error message
amountIn is required
code
correct 0, Incorrect -1
data
tx
{chain_id: 1,to: '0x2abbEAf73456b6c0b1a1E7e32Dbd63Bf4fafAC40',amount_in: '1000000000000',amount_out: '9287306518470736046',buy_token_address: '0x0000000000000000000000000000000000000000',sell_token_address: '0xF2a79EF11ACBba33abAA7bACE0178eA66e6d80b8',type: 'v2',path: ['0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6','0xF2a79EF11ACBba33abAA7bACE0178eA66e6d80b8'],pool_address: '0xeb56b2cc0d2eaf6e04a52dc809019431b3b040f0',fee: 3000,steps: [ { id: 1, type: 'swap', tool: 'uniswapv2' } ],token_in_usd_price: 0.001,amount_in_usd: '1e-9',token_out_usd_price: 0.001,amount_out_usd: '0.009776112124706037943',value: '1000000000000',data: '0x5b9e90060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f2a79ef11acbba33abaa7bace0178ea66e6d80b8000000000000000000000000000000000000000000000000000000e8d4a5100000000000000000000000000000000000000000000000000080e32412819e38ae000000000000000000000000eb56b2cc0d2eaf6e04a52dc809019431b3b040f0',gas_limit: '166773'}
[PreviousGet the recommended gas price for ETH/Base/BSC chainchevron-left](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-gas-price-for-eth-base-bsc-chain)[Next🤝🏻 Cooperation-API: 🔄Data crawling IP whitelistchevron-right](https://docs.gmgn.ai/index/cooperation-api-data-crawling-ip-whitelist)
Last updated 1 month ago
