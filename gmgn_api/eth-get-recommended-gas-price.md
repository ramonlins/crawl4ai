# Source: https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-gas-price-for-eth-base-bsc-chain

This interface is used to obtain the recommended gas price of ETH/Base chain (real time)
Access point: /defi/quotation/v1/chains/{network}/gas_price
Request method: GET
Input parameters:
none
Output parameters:
**Parameter name**
**Parameter Description**
E**xample**
msg
cause of error
success
code
error code, 0 means normal, -1 means error
data
last_block, average, high, low, suggest_base_fee, eth_usd_price, high_prio_fee, average_prio_fee, low_prio_fee and other values
`{"last_block":17527078,"average":"16493364199","high":"17493364199","low":"16493364199","suggest_base_fee":"16493364199","high_prio_fee":"300000000","average_prio_fee":"100000000","low_prio_fee":"50000000","eth_usd_price":"1809.84970000"}`
[PreviousGet the recommended slippage value of ETH/Base/BSC tokenchevron-left](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-slippage-value-of-eth-base-bsc-token)[NextSwap transaction simulation (ETH/Base/BSC)chevron-right](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/swap-transaction-simulation-eth-base-bsc)
Last updated 1 year ago
