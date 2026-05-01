# Source: https://www.helius.dev/docs/sdks

At Helius, we’ve developed a [Node.js](https://github.com/helius-labs/helius-sdk) and a [Rust SDK](https://github.com/helius-labs/helius-rust-sdk) to make developing on Solana easier. The following page includes information on installing and using these SDKs. It also covers common error handling, where to find the latest documentation, and how to contribute to these SDKs. We also outline a list of unofficial community SDKs made by our wonderful community. Note that those SDKs are not officially maintained by our team — only the Node.js and Rust SDKs are.
## [Node.js SDK Official Helius Node.js SDK for Solana development ](https://github.com/helius-labs/helius-sdk)
## [Rust SDK Official Helius Rust SDK for Solana development ](https://github.com/helius-labs/helius-rust-sdk)
## Node.js SDK
Note the Node.js SDK has been rewritten as of version 2.0.0. This was done to use `@solana/kit` and remove the dependency on `@solana/web3.js` versions higher than 1.73.2. For those migrating to the latest version, please refer to our [migration guide](https://github.com/helius-labs/helius-sdk/blob/main/MIGRATION.md).
### Installation
The Helius Node.js SDK can be installed with any of the following package managers:
  * pnpm
  * Yarn



```
npm install helius-sdk

```


```
pnpm install helius-sdk

```


```
yarn add helius-sdk

```

### Quick Start
Below is a straightforward example of how to use the Node.js SDK to fetch a list of assets owned by a given address:

```
import { createHelius } from "helius-sdk";

(async () => {
  const apiKey = ""; // From Helius dashboard
  const helius = createHelius({ apiKey });

  try {
    const assets = await helius.getAssetsByOwner({
      ownerAddress: "owner_address_goes_here",
      page: 1,
      limit: 50,
      sortBy: { sortBy: "created", sortDirection: "asc" },
    });

    console.log("Fetched assets:", assets);
catch (error) {
    console.error("Error:", error);

})();

```

### Documentation
The [examples directory](https://github.com/helius-labs/helius-sdk/tree/main/examples) is filled with in-depth code examples covering each method and basic usage, organized by namespace. For API reference documentation, refer to our [documentation](https://www.helius.dev/docs/api-reference) and the [official Solana documentation](https://solana.com/docs/rpc) for general Solana JSON RPC API help. For general help with Kit, please refer to [Kit’s documentation](https://www.solanakit.com/).
## Rust SDK
### Installation
Add dependency to Cargo.toml
To start using the Helius Rust SDK in your project, add it as a dependency via [`cargo`](https://doc.rust-lang.org/cargo/). Open your project’s `Cargo.toml` and add the following line under `[dependencies]`:

```
helius = "x.y.z"

```

where `x.y.z` is your desired version.
Alternative: Use cargo add command
Alternatively, use `cargo add helius` to add the dependency directly via the command line. This will automatically find the latest version compatible with your project and add it to your `Cargo.toml`.
Keep your SDK updated
Remember to run `cargo update` regularly to fetch the latest version of the SDK.
### Quick Start
Below is a straightforward example of using the [Enhanced Transactions API](https://www.helius.dev/docs/enhanced-transactions) to [parse a given transaction](https://www.helius.dev/docs/api-reference/enhanced-transactions/gettransactions):

```
use helius::error::Result;
use helius::types::*;
use helius::Helius;

#[tokio::main]
async fn main() -> Result<()> {
    let api_key:str = "your_api_key";
    let cluster: Cluster = Cluster::MainnetBeta;

    let helius: Helius = Helius::new(api_key, cluster).unwrap();

    let request: ParseTransactionsRequest = ParseTransactionsRequest {
        transactions: vec![
            "2sShYqqcWAcJiGc3oK74iFsYKgLCNiY2DsivMbaJGQT8pRzR8z5iBcdmTMXRobH8cZNZgeV9Ur9VjvLsykfFE2Li".to_string(),



    let response: ResultVecEnhancedTransaction>, HeliusError= helius.parse_transactions(request).await;
    println!("Assets: {:?}", response);

    Ok(())


```

### Documentation
## [Rust Docs Latest documentation on docs.rs ](https://docs.rs/helius/latest/helius/)
## [API Reference Helius API documentation ](https://www.helius.dev/docs/api-reference)
## [Examples Code examples in the GitHub repo ](https://github.com/helius-labs/helius-rust-sdk/tree/dev/examples)
## Error Handling
An error message will be thrown when the API returns a non-success (i.e., 4xx or 5xx status code).
For example, below is a 401 thrown for an incorrect getAsset call using the Node.js SDK:

```

  "jsonrpc": "2.0",
  "error": {
    "code": -32001,
    "message": "Authentication failed. Missing or invalid API key."

  "id": "1"


```

### Common Error Codes
When working with the Helius SDK, you may encounter several error codes. Below is a table detailing some of the common error codes along with additional information to help you troubleshoot:
400: Bad Request
This occurs when a request has invalid parameters.
401: Unauthorized
This occurs when an invalid API key is provided or access is restricted due to RPC rules.
429: Too Many Requests
This indicates that the user has exceeded the request limit in a given timeframe or is out of credits.
5XX: Internal Server Error
This is a generic error message for server-side issues. Please contact Helius support for assistance.
If you encounter any of these errors:
Check error documentation
Refer to [`errors.rs`](https://github.com/helius-labs/helius-rust-sdk/blob/dev/src/error.rs) for a list of all possible errors returned by the `Helius` client, if using the Rust SDK. For the Node.js SDK, refer to [Kit’s errors](https://www.solanakit.com/docs/concepts/errors)
Review the documentation
Refer to the [Helius documentation](https://www.helius.dev/docs) for further guidance
Contact support
Reach out to the Helius support team for more detailed assistance
## Contribution to Our SDKs
We welcome all contributions to our SDKs! If you’re interested, here are our GitHub Repositories:
## [Node.js SDK Contribute to our Node.js SDK ](https://github.com/helius-labs/helius-sdk/blob/main/CONTRIBUTING.md)
## [Rust SDK Contribute to our Rust SDK ](https://github.com/helius-labs/helius-rust-sdk/blob/dev/CONTRIBUTIONS.md)
Interested in contributing to the Helius Rust SDK specifically? Read the following [contributions guide](https://github.com/helius-labs/helius-rust-sdk/blob/dev/CONTRIBUTIONS.md) before opening up a pull request!
## Unofficial Community SDKs
Our amazing community members have also created their own SDKs to interact with our REST APIs. Please note our team does not officially maintain these.
## [Rust SDK (Synchronous)](https://github.com/bgreni/helius-rust-sdk)
## [Rust SDK (Asynchronous)](https://github.com/dougEfresh/selene-helius-sdk)
Was this page helpful?
Yes
[ Previous GlossaryDeveloper-focused definitions for terms used across the Helius docs and the Solana ecosystem — DAS, LaserStream, priority fees, compressed NFTs, PDAs, compute units, and more. ](https://www.helius.dev/docs/glossary)
On this page
  * [Contribution to Our SDKs](https://www.helius.dev/docs/sdks#contribution-to-our-sdks)
  * [Unofficial Community SDKs](https://www.helius.dev/docs/sdks#unofficial-community-sdks)


Assistant
Responses are generated using AI and may contain mistakes.
