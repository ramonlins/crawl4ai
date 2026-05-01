# Source: https://www.helius.dev/docs/laserstream/historical-replay

**Never miss a beat** : LaserStream’s Historical Replay ensures you can recover from disconnections and backfill missing data from the last 24 hours of blockchain activity.
## What is Historical Replay?
Historical Replay is LaserStream’s feature that lets you replay recent blockchain data from up to 216,000 slots in the past (approximately 24 hours of blockchain activity). This is useful for handling disconnections and ensuring data continuity in real-time apps.
**Limited Time Window** : Historical replay is currently limited to the last 24 hours of blockchain activity. You cannot replay data from arbitrary points in the past.
## Handle Disconnections
Recover data lost during brief disconnections (up to 24 hours)
## Bootstrap Applications
Start applications with recent context from the last 24 hours
## Analyze Recent Events
Review recent transactions and account changes
## Test with Recent Data
Use real recent data for testing and development
## How It Works
Specify Starting Point
Use the `fromSlot` parameter to set your replay starting point (must be within last ~216,000 slots)
Stream Historical Data
LaserStream delivers all events from your specified slot forward
Catch Up to Real-Time
Historical data streams until you reach the current slot
Continue Live Streaming
Seamlessly transition to real-time data streaming
**Automatic Reconnection** : The [LaserStream SDK](https://github.com/helius-labs/laserstream-sdk) handles reconnections and replay automatically. No additional code required!
## Quickstart
Interested in trying LaserStream? [Apply for a 2-day trial](https://www.helius.dev/laserstream-contact); we review every application.
  * gRPC



```
import { subscribe, CommitmentLevel, LaserstreamConfig, SubscribeRequest } from 'helius-laserstream';

const subscriptionRequest: SubscribeRequest = {
  transactions: {
    "token-filter": { // user-defined label for this filter
      accountInclude: ['TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'],
      vote: false,
      failed: false


  commitment: CommitmentLevel.CONFIRMED,
  accounts: {},
  slots: {},
  blocks: {},
  blocksMeta: {},
  entry: {},
  accountsDataSlice: [],
  fromSlot: '224339000' // Start replay from this slot (must be within last ~216,000 slots)


const config: LaserstreamConfig = {
  apiKey: 'YOUR_API_KEY',
  endpoint: 'https://laserstream-mainnet-ewr.helius-rpc.com', // Choose your closest region


await subscribe(config, subscriptionRequest, 
  async (data) => {
    console.log('Received data:', data);

  async (error) => {
    console.error('Error:', error);



```

## Configuration Options
fromSlot
string
required
The slot number to start replaying from. Must be within the replay window (last ~216,000 slots from current slot).**Example** : `"224339000"`**Important** : The slot must be recent enough to fall within the 24-hour replay window.
## Use Cases
Reconnection After Brief Disconnection
When your application reconnects after a short disconnection (under 24 hours), you can use Historical Replay to ensure no data is missed:

```
// Store the last processed slot
let lastProcessedSlot = getLastProcessedSlot();

// Check if the slot is still within the replay window
const currentSlot = await getCurrentSlot();
const maxReplaySlot = currentSlot - 216000;

if (lastProcessedSlot maxReplaySlot) {
  console.warn('Disconnection too long, some data may be lost');
  lastProcessedSlot = maxReplaySlot;


const subscriptionRequest: SubscribeRequest = {
  // ... your subscription config
  fromSlot: lastProcessedSlot.toString()


await subscribe(config, subscriptionRequest, 
  async (data) => {
    // Process data and update last processed slot
    await processData(data);
    lastProcessedSlot = data.slot;
    saveLastProcessedSlot(lastProcessedSlot);



```

Bootstrap with Recent Context
Start your application with recent context from the last few minutes:

```
// Get a slot from 10 minutes ago (within the 24-hour window)
const currentSlot = await getCurrentSlot();
const startSlot = currentSlot - 1500; // ~10 minutes ago

const subscriptionRequest: SubscribeRequest = {
  // ... your subscription config
  fromSlot: startSlot.toString()


```

Testing with Recent Data
Use recent historical data for testing (limited to last 24 hours):

```
// Test with data from the last 5 minutes
const currentSlot = await getCurrentSlot();
const testStartSlot = currentSlot - 750; // ~5 minutes ago
const testEndSlot = currentSlot - 150; // ~1 minute ago

const subscriptionRequest: SubscribeRequest = {
  // ... your subscription config
  fromSlot: testStartSlot.toString()


// Stop processing when reaching test end slot
await subscribe(config, subscriptionRequest, 
  async (data) => {
    if (data.slot >= testEndSlot) {
      // Stop processing
      return;

    await processTestData(data);



```

## Next Steps
## [LaserStream gRPC Learn more about gRPC streaming capabilities and features ](https://www.helius.dev/docs/laserstream/grpc)
## [LaserStream Trial Apply for a 2-day LaserStream trial to test before upgrading your subscription ](https://www.helius.dev/laserstream-contact)
## [SDK Documentation View the complete SDK docs ](https://github.com/helius-labs/laserstream-sdk)
## [Contact Support Get help with your implementation ](https://www.helius.dev/docs/support)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/laserstream/grpc)[ Preprocessed Transactions (Public Beta)The fastest way to stream Solana transactions. ~8ms faster than processed on average. Next ](https://www.helius.dev/docs/laserstream/preprocessed-transactions)
On this page
  * [What is Historical Replay?](https://www.helius.dev/docs/laserstream/historical-replay#what-is-historical-replay)


Assistant
Responses are generated using AI and may contain mistakes.
