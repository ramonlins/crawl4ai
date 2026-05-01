# Source: https://www.helius.dev/docs/api-reference/authentication

Helius API uses API keys to authenticate requests. Every API request must include your API key to verify your identity and permissions.
Your API key is sensitive information that grants access to your Helius account. Never expose it in client-side code, public repositories, or browser-accessible areas.
## Getting Started
### 1. Create Your API Key
Sign up or log in
Create an account on the [Helius Dashboard](https://dashboard.helius.dev) or log in to your existing account.
Navigate to API Keys
Go to the **API Keys** section in your dashboard sidebar.
Generate a new key
Click **Create New API Key** and provide a descriptive name for your project (e.g., “Production App”, “Development Environment”).
Copy and secure your key
Copy your API key immediately and store it securely. You won’t be able to see it again once you navigate away.
### 2. Using Your API Key
Include your API key as a query parameter in all requests:
cURL
JavaScript
Python

```
curl "https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"getAccountInfo","params":["ACCOUNT_ADDRESS"]}'

```

## Getting Started (For Agents)
Agents can programmatically sign up for Helius accounts, create projects, and generate API keys using the [Helius CLI](https://www.helius.dev/docs/agents/cli). For complete instructions, read: <https://dashboard.helius.dev/agents.md>
### Install the Helius CLI

```
npm install -g helius-cli

```

### Generate a Keypair

```
helius keygen

```

### Fund the Generated Wallet (Manual)
Send 1 USDC and 0.001 SOL to the wallet address provided in Step 2.
### Signup and Get API Key

```
helius signup --json

```

## Security Best Practices
## Environment Variables
Store your API key in environment variables, not in your source code.

```
export HELIUS_API_KEY="YOUR_API_KEY"

```

## IP Restrictions
Set up IP restrictions for your API keys in the dashboard to limit access to specific IP addresses or ranges.
## Separate Keys
Use different API keys for development, staging, and production environments to isolate usage and improve security.
## Monitor Usage
Regularly check your API usage in the dashboard to detect unusual patterns or potential security issues.
### Secret Management
  * Node.js
  * Python
  * Docker



```
// Use environment variables
const apiKey = process.env.HELIUS_API_KEY;

// Or use a secrets manager
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');
const client = new SecretManagerServiceClient();

async function getApiKey() {
  const [version] = await client.accessSecretVersion({
    name: 'projects/PROJECT_ID/secrets/helius-api-key/versions/latest',
  });
  return version.payload.data.toString();


```


```
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv('HELIUS_API_KEY')

# Or use AWS Secrets Manager
import boto3

def get_secret():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='helius-api-key')
    return response['SecretString']

```


```
# In your Dockerfile
ENV HELIUS_API_KEY=""

# Or use Docker secrets
RUN --mount=type=secret,id=helius_key \
    cat /run/secrets/helius_key > /app/api_key.txt

```

## Rate Limits & Usage
Rate limits vary by subscription plan. Monitor your usage in the [Helius Dashboard](https://dashboard.helius.dev) to ensure you stay within your allocated limits.
### Understanding Rate Limits
  * **Requests per second** : Based on your subscription tier
  * **Monthly request quota** : Total requests allowed per billing cycle
  * **Burst allowance** : Short-term spikes above your base rate limit


### Handling Rate Limits
JavaScript
Python

```
async function makeRequest(url, data) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (response.status === 429) {
      const retryAfter = response.headers.get('Retry-After');
      console.log(`Rate limited. Retry after ${retryAfter} seconds`);
      await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
      return makeRequest(url, data); // Retry


    return response.json();
catch (error) {
    console.error('Request failed:', error);
    throw error;



```

## Troubleshooting
Invalid API Key Error
**Symptoms** : 401 Unauthorized or “Invalid API Key” errors**Solutions** :
  * Verify your API key is correct and hasn’t been regenerated
  * Check that you’re including the API key as a query parameter: `?api-key=YOUR_KEY`
  * Ensure there are no extra spaces or characters in your API key
  * Confirm your API key hasn’t expired or been revoked


Rate Limit Exceeded
**Symptoms** : 429 Too Many Requests errors**Solutions** :
  * Check your current usage in the dashboard
  * Implement exponential backoff in your retry logic
  * Consider upgrading your plan for higher limits
  * Optimize your requests to reduce unnecessary calls


Forbidden Access
**Symptoms** : 403 Forbidden errors**Solutions** :
  * Verify IP restrictions aren’t blocking your requests
  * Check that your subscription includes access to the endpoint
  * Ensure your API key has the necessary permissions


## Next Steps
## [Quickstart Guide Start making your first API calls with Helius ](https://www.helius.dev/docs/quickstart)
## [API Reference Explore all available endpoints and methods ](https://www.helius.dev/docs/api-reference)
## [Rate Limits Understand rate limits and upgrade options ](https://www.helius.dev/docs/billing/rate-limits)
## [Dashboard Monitor your API usage and manage keys ](https://dashboard.helius.dev)
## Support
Need help with authentication or have questions about API keys?
## [Discord Community Join our Discord for real-time help and community support ](https://discord.com/invite/6GXdee3gBj)
Email Support Contact our support team directly
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference)[ EndpointsHelius provides multiple endpoint types to suit different application needs. This guide outlines all available connection options for interacting with the Helius API. Next ](https://www.helius.dev/docs/api-reference/endpoints)
On this page
  * [1. Create Your API Key](https://www.helius.dev/docs/api-reference/authentication#1-create-your-api-key)
  * [2. Using Your API Key](https://www.helius.dev/docs/api-reference/authentication#2-using-your-api-key)
  * [Getting Started (For Agents)](https://www.helius.dev/docs/api-reference/authentication#getting-started-for-agents)
  * [Install the Helius CLI](https://www.helius.dev/docs/api-reference/authentication#install-the-helius-cli)
  * [Fund the Generated Wallet (Manual)](https://www.helius.dev/docs/api-reference/authentication#fund-the-generated-wallet-manual)
  * [Signup and Get API Key](https://www.helius.dev/docs/api-reference/authentication#signup-and-get-api-key)
  * [Security Best Practices](https://www.helius.dev/docs/api-reference/authentication#security-best-practices)
  * [Understanding Rate Limits](https://www.helius.dev/docs/api-reference/authentication#understanding-rate-limits)


Assistant
Responses are generated using AI and may contain mistakes.
