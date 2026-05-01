# Source: https://www.helius.dev/docs/api-reference/rpc/http/sendtransaction

POST
https://mainnet.helius-rpc.com https://devnet.helius-rpc.com
Try it
sendTransaction
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "sendTransaction",
  "params": [
    "4hXTCkRzt9WyecNzV1XPgCDfGAZzQKNxLXgynz5QDuWWPSAZBZSHptvWRL3BjCvzUXRdKvHL2b7yGrRQcWyaqsaBCncVG7BFggS8w9snUts67BSh3EqKpXLUm5UMHfD7ZBe9GhARjbNQMLJ1QD3Spr6oMTBU6EhdB4RD8CP2xUxr2u3d6fos36PD98XS6oX8TQjLpsMwncs5DAMiD4nNnR8NBfyghGCWvCVifVwvA8B8TJxE1aiyiv2L429BCWfyzAme5sZW8rDb14NeCQHhZbtNqfXhcp2tAnaAT"



```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": "2id3YC2jK9G5Wo2phDx4gJVAew8DcY5NAojnVuao8rkxwPYPe8cSwE5GzhEgJA2y8fVjDEo6iR6ykBvDxrTQrtpb"

```

This method does not alter the transaction in any way; it relays the transaction created by clients to the node as-is. If the node’s rpc service receives the transaction, this method immediately succeeds, without waiting for any confirmations. A successful response from this method does not guarantee the transaction is processed or confirmed by the cluster. While the rpc service will reasonably retry to submit it, the transaction could be rejected if transaction’s recent_blockhash expires before it lands. Use [getSignatureStatuses](https://www.helius.dev/docs/api-reference/rpc/http/getsignaturestatuses) to ensure a transaction is processed and confirmed. Before submitting, the following preflight checks are performed:
  1. The transaction signatures are verified
  2. The transaction is simulated against the bank slot specified by the preflight commitment. On failure an error will be returned. Preflight checks may be disabled if desired. It is recommended to specify the same commitment and preflight commitment to avoid confusing behavior.

The returned signature is the first signature in the transaction, which is used to identify the transaction (transaction id). This identifier can be easily extracted from the transaction data before submission.
## Request Parameters
transaction
string
required
The fully-signed Solana transaction encoded as a base-58 string for blockchain submission.
encoding
string
Data encoding format used for the Solana transaction payload.
  * `base58`
  * `base64`


skipPreflight
boolean
When true, bypasses Solana’s preflight transaction validation for faster submission.
preflightCommitment
string
Solana network commitment level for transaction validation checks.
  * `confirmed`
  * `finalized`
  * `processed`


maxRetries
number
Maximum number of automatic retry attempts for failed Solana transaction submissions.
minContextSlot
number
Minimum Solana blockchain slot required for transaction processing.
#### Authorizations
api-key
string
query
required
Your Helius API key. You can get one for free in the [dashboard](https://dashboard.helius.dev/api-keys).
#### Body
application/json
jsonrpc
enum<string>
default:2.0
The JSON-RPC protocol version.
Available options: 
`2.0`
Example:
`"2.0"`
id
string
default:1
A unique identifier for the request.
Example:
`"1"`
method
enum<string>
default:sendTransaction
The name of the RPC method to invoke.
Available options: 
`sendTransaction`
Example:
`"sendTransaction"`
params
(string | object)[]
Parameters for sending a transaction.
The fully-signed Solana transaction encoded as a base-58 string for blockchain submission.
Example:
`"4hXTCkRzt9WyecNzV1XPgCDfGAZzQKNxLXgynz5QDuWWPSAZBZSHptvWRL3BjCvzUXRdKvHL2b7yGrRQcWyaqsaBCncVG7BFggS8w9snUts67BSh3EqKpXLUm5UMHfD7ZBe9GhARjbNQMLJ1QD3Spr6oMTBU6EhdB4RD8CP2xUxr2u3d6fos36PD98XS6oX8TQjLpsMwncs5DAMiD4nNnR8NBfyghGCWvCVifVwvA8B8TJxE1aiyiv2L429BCWfyzAme5sZW8rDb14NeCQHhZbtNqfXhcp2tAnaAT"`
#### Response
application/json
Successfully sent the transaction.
jsonrpc
enum<string>
The JSON-RPC protocol version.
Available options: 
`2.0`
Example:
`"2.0"`
id
string
Identifier matching the request.
Example:
`"1"`
result
string
The unique Solana transaction signature for tracking confirmation status and transaction history.
Example:
`"2id3YC2jK9G5Wo2phDx4gJVAew8DcY5NAojnVuao8rkxwPYPe8cSwE5GzhEgJA2y8fVjDEo6iR6ykBvDxrTQrtpb"`
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/rpc/http/requestairdrop)[ simulateBundleSimulate a JITO bundle without executing it on the blockchain. Next ](https://www.helius.dev/docs/api-reference/rpc/http/simulatebundle)
sendTransaction
cURL

```
curl --request POST \
  --url 'https://mainnet.helius-rpc.com/?api-key=' \
  --header 'Content-Type: application/json' \
  --data '

  "jsonrpc": "2.0",
  "id": "1",
  "method": "sendTransaction",
  "params": [
    "4hXTCkRzt9WyecNzV1XPgCDfGAZzQKNxLXgynz5QDuWWPSAZBZSHptvWRL3BjCvzUXRdKvHL2b7yGrRQcWyaqsaBCncVG7BFggS8w9snUts67BSh3EqKpXLUm5UMHfD7ZBe9GhARjbNQMLJ1QD3Spr6oMTBU6EhdB4RD8CP2xUxr2u3d6fos36PD98XS6oX8TQjLpsMwncs5DAMiD4nNnR8NBfyghGCWvCVifVwvA8B8TJxE1aiyiv2L429BCWfyzAme5sZW8rDb14NeCQHhZbtNqfXhcp2tAnaAT"



```


```

  "jsonrpc": "2.0",
  "id": "1",
  "result": "2id3YC2jK9G5Wo2phDx4gJVAew8DcY5NAojnVuao8rkxwPYPe8cSwE5GzhEgJA2y8fVjDEo6iR6ykBvDxrTQrtpb"

```

Assistant
Responses are generated using AI and may contain mistakes.
