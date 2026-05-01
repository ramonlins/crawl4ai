# Source: https://www.helius.dev/docs/api-reference/sender/getbundlestatuses

Returns the status of submitted bundles. If a bundle has not landed or is not found, it returns `null`.
## Endpoint

```
POST https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY

```

## Request
jsonrpc
string
required
`"2.0"`
id
number
required
Request identifier.
method
string
required
`"getBundleStatuses"`
params[0]
array[string]
required
Array of up to 5 bundle IDs to check.
## Request Example

```
curl "https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBundleStatuses",
    "params": [

        "892b79ed49138bfb3aa5441f0df6e06ef34f9ee8f3976c15b323605bae0cf51d"




```

## Response
result.context.slot
number
The slot at which the request was processed.
result.value
array
Array of bundle status objects. `null` for bundles not found.
result.value[].bundle_id
string
The bundle ID.
result.value[].transactions
array[string]
Base-58 encoded transaction signatures in the bundle.
result.value[].slot
number
Slot the bundle was processed in.
result.value[].confirmation_status
string
`"processed"`, `"confirmed"`, or `"finalized"`.
result.value[].err
object
Error information, if any.

```

  "jsonrpc": "2.0",
  "result": {
    "context": {
      "slot": 242806119

    "value": [

        "bundle_id": "892b79ed49138bfb3aa5441f0df6e06ef34f9ee8f3976c15b323605bae0cf51d",
        "transactions": [
          "3bC2M9fiACSjkTXZDgeNAuQ4ScTsdKGwR42ytFdhUvikqTmBheUxfsR1fDVsM5ADCMMspuwGkdm1uKbU246x5aE3",
          "8t9hKYEYNbLvNqiSzP96S13XF1C2f1ro271Kdf7bkZ6EpjPLuDff1ywRy4gfaGSTubsM2FeYGDoT64ZwPm1cQUt"

        "slot": 242804011,
        "confirmation_status": "finalized",
        "err": {
          "Ok": null




  "id": 1


```

## See Also
  * [sendBundle](https://www.helius.dev/docs/api-reference/sender/sendbundle) — submit bundles
  * [Jito Bundles via Helius](https://www.helius.dev/docs/sending-transactions/send-bundle) — full guide


Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/sender/sendbundle)[ OverviewComplete API reference for Helius DAS (Digital Asset Standard) endpoints. Query NFTs, compressed NFTs, fungible tokens, ownership, and metadata on Solana. Next ](https://www.helius.dev/docs/api-reference/das)
On this page


Assistant
Responses are generated using AI and may contain mistakes.
