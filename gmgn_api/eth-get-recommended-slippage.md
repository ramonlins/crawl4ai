# Source: https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-slippage-value-of-eth-base-bsc-token

Get the recommended slippage value based on the input blockchain code and token contract address
Access point: https://gmgn.ai/api/v1/recommend_slippage/sol/9U1NKvb9bUTrqcdymkQ2kDkLxSVyCLUrAfVswcSZPUMP
Request method: GET
Request parameters:
**Parameter name**
**Parameter Description**
**Is it necessary**
**Example**
token_address
the contract address of the output token
yes
0xbacacd83b68c92ae07ef382d0c0277d1bd1c7c4d
token_in_address
enter the token contract address
no, the main purpose is to solve the problem of accumulated slippage when swapping two alt coins
0x0c48250eb1f29491f1efbeec0261eb556f0973c7
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
returns the recommended slippage value. If it is 10%, it returns "10". display_slippage is the displayed slippage value.
{
"recommend_slippage":"1",
"display_slippage":"1",
"has_tax":false
}
[PreviousGet the available routing for ETH/Base/BSC transactionschevron-left](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-available-routing-for-eth-base-bsc-transactions)[NextGet the recommended gas price for ETH/Base/BSC chainchevron-right](https://docs.gmgn.ai/index/cooperation-api-integrate-gmgn-eth-base-bsc-trading-api/get-the-recommended-gas-price-for-eth-base-bsc-chain)
Last updated 1 year ago
