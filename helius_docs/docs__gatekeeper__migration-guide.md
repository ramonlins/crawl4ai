# Source: https://www.helius.dev/docs/gatekeeper/migration-guide

Migrating to Gatekeeper takes **less than 5 minutes**. It’s a simple URL change—your API key works without any modifications.
## Quick Migration
Simply replace your existing endpoint:
Before
After

```
const url = "https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY";

```

**That’s it!** Test your application, monitor performance, and deploy when ready.
## Framework-Specific Examples
  * Solana Web3.js
  * Anchor
  * Solana-py
  * Rust
  * Environment Variable



```
import { Connection } from '@solana/web3.js';

const connection = new Connection(
  `https://beta.helius-rpc.com/?api-key=${YOUR_API_KEY}`,
  'confirmed'


```


```
import { AnchorProvider } from '@coral-xyz/anchor';
import { Connection } from '@solana/web3.js';

const connection = new Connection(
  `https://beta.helius-rpc.com/?api-key=${YOUR_API_KEY}`,
  'confirmed'


const provider = new AnchorProvider(connection, wallet, {
  commitment: 'confirmed'
});

```


```
from solana.rpc.api import Client

rpc_url = f"https://beta.helius-rpc.com/?api-key={YOUR_API_KEY}"
client = Client(rpc_url)

```


```
use solana_client::rpc_client::RpcClient;

let rpc_url = format!("https://beta.helius-rpc.com/?api-key={}", YOUR_API_KEY);
let client = RpcClient::new(rpc_url);

```


```
# .env file
HELIUS_RPC_URL=https://beta.helius-rpc.com/?api-key=YOUR_API_KEY

```

## WebSocket Endpoints
If you’re using WebSockets, update those endpoints too:

```
// Before
const ws = new WebSocket("wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY");

// After
const ws = new WebSocket("wss://beta.helius-rpc.com/?api-key=YOUR_API_KEY");

```

## Migration Checklist
Update endpoint URL
Change `mainnet.helius-rpc.com` to `beta.helius-rpc.com`
Test in development
Verify all RPC calls work and authentication succeeds
Monitor performance
Check your metrics for improved latency and response times
Deploy to production
Roll out changes using your standard deployment process
## Gradual Rollout (Optional)
For a safer migration, you can use environment variables or feature flags:

```
// Environment-based
const endpoint = process.env.USE_GATEKEEPER
  ? "https://beta.helius-rpc.com"
  : "https://mainnet.helius-rpc.com";

const connection = new Connection(
  `${endpoint}?api-key=${YOUR_API_KEY}`,
  'confirmed'


```


```
// Percentage rollout (10% of traffic)
const useGatekeeper = Math.random()  0.1;
const endpoint = useGatekeeper
  ? "https://beta.helius-rpc.com"
  : "https://mainnet.helius-rpc.com";

```

## Rollback
If needed, simply switch back to the standard endpoint:

```
const url = "https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY";

```

## Troubleshooting
Getting 401 Unauthorized errors
Verify your API key is included: `?api-key=YOUR_API_KEY`
Not seeing performance improvements
  * Test from your production environment (not local dev)
  * Verify you’re not hitting rate limits (check for 429 errors)
  * Contact support if issues persist


WebSocket connections failing
  * Use `wss://` (not `ws://`)
  * Ensure your API key is in the URL
  * Check firewall settings


Response formats look different
Gatekeeper returns identical responses. Contact support immediately if you see differences.
## Need Help?
  * **Email** : support@helius.dev
  * **Discord** : <https://discord.com/invite/6GXdee3gBj>
  * **Documentation** : [Gatekeeper Overview](https://www.helius.dev/docs/gatekeeper/overview)


## [Questions about migration? Join our Discord to chat with the team and other developers ](https://discord.com/invite/6GXdee3gBj)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/gatekeeper/overview)[ Protect Your KeysSecure your Helius Solana API keys from malicious actors. Access control rules, RPC proxy, and security best practices to prevent unauthorized usage and charges. Next ](https://www.helius.dev/docs/rpc/protect-your-keys)
On this page
  * [Framework-Specific Examples](https://www.helius.dev/docs/gatekeeper/migration-guide#framework-specific-examples)
  * [Gradual Rollout (Optional)](https://www.helius.dev/docs/gatekeeper/migration-guide#gradual-rollout-optional)


Assistant
Responses are generated using AI and may contain mistakes.
