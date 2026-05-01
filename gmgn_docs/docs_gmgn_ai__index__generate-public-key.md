# Source: https://docs.gmgn.ai/index/generate-public-key

### 
Steps to Generate Public Key
#### 
Method I:
  1. Paste the following text to your AI Agent


> Generate an Ed25519 key pair for me using OpenSSL and show me
#### 
Method II:
  1. Click the link below to visit the asymmetric key generator repository. Select the file (in the red box) that corresponds to your operating system, then download and install the latest version of the key generator.


> 👉 Download the generator: <https://github.com/binance/asymmetric-key-generator/releases>[arrow-up-right](https://github.com/binance/asymmetric-key-generator/releases)
Note: If the key generator fails to run properly, please download the `.CHECKSUM` file (in the green box) to verify the integrity of the generator package. Please ensure both files are downloaded to the same directory
  1. Open the key generator and simply click "Generate 1 Key Pair". You will receive one Private Key and one Public Key


⚠️ Please Note:
  * Do not share your API Key, Ed25519, or RSA Private Keys! Exposing them may result in the loss of your assets
  * Click "SAVE PAIR" or "SAVE" to securely store your keys locally


  1. Click "COPY" to copy the Public Key, then paste it into the public key input box on the GMGN platform to continue creating your GMGN API Key


### 
Introduction to Asymmetric Key Pairs (Ed25519 Recommended)
When connecting to the API, we use an asymmetric key pair for secure authentication. The core of this security model is "one key pair, two keys": a Public Key and a Private Key
They are generated through a strict mathematical relationship, but the fundamental design principle ensures that the Public Key can be safely shared openly, while the Private Key must be kept absolutely confidential
[PreviousGMGN Agent APIchevron-left](https://docs.gmgn.ai/index/gmgn-agent-api)[NextGMGN Update Announcementchevron-right](https://docs.gmgn.ai/index/gmgn-update-announcement)
Last updated 1 month ago
