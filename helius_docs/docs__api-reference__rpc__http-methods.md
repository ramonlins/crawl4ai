# Source: https://www.helius.dev/docs/api-reference/rpc/http-methods

## Account Information
## [getAccountInfo Retrieves information about an account from the blockchain. ](https://www.helius.dev/docs/api-reference/rpc/http/getaccountinfo)
## [getMultipleAccounts Retrieves information about multiple accounts in a single request. ](https://www.helius.dev/docs/api-reference/rpc/http/getmultipleaccounts)
## [getProgramAccounts Returns all accounts owned by a specific program. ](https://www.helius.dev/docs/api-reference/rpc/http/getprogramaccounts)
## [getBalance Returns the balance of an account at the current time. ](https://www.helius.dev/docs/api-reference/rpc/http/getbalance)
## [getMinimumBalanceForRentExemption Returns the minimum balance required to make an account rent exempt. ](https://www.helius.dev/docs/api-reference/rpc/http/getminimumbalanceforrentexemption)
## [getLargestAccounts Returns the accounts with the largest balances. ](https://www.helius.dev/docs/api-reference/rpc/http/getlargestaccounts)
## Block Information
## [getBlock Returns identity and transaction information about a confirmed block. ](https://www.helius.dev/docs/api-reference/rpc/http/getblock)
## [getBlocks Returns a list of confirmed blocks between two slots. ](https://www.helius.dev/docs/api-reference/rpc/http/getblocks)
## [getBlocksWithLimit Returns a list of confirmed blocks starting at a given slot with a limit. ](https://www.helius.dev/docs/api-reference/rpc/http/getblockswithlimit)
## [getBlockHeight Returns the current block height of the node. ](https://www.helius.dev/docs/api-reference/rpc/http/getblockheight)
## [getBlockTime Returns the estimated production time of a block. ](https://www.helius.dev/docs/api-reference/rpc/http/getblocktime)
## [getBlockCommitment Returns commitment information for a block. ](https://www.helius.dev/docs/api-reference/rpc/http/getblockcommitment)
## [getBlockProduction Returns recent block production information. ](https://www.helius.dev/docs/api-reference/rpc/http/getblockproduction)
## [getLatestBlockhash Returns the latest blockhash. ](https://www.helius.dev/docs/api-reference/rpc/http/getlatestblockhash)
## [isBlockhashValid Returns whether a blockhash is still valid or not. ](https://www.helius.dev/docs/api-reference/rpc/http/isblockhashvalid)
## Transaction Information
## [getTransaction Returns transaction details for a confirmed transaction. ](https://www.helius.dev/docs/api-reference/rpc/http/gettransaction)
## [getTransactionCount Returns the current Transaction count from the ledger. ](https://www.helius.dev/docs/api-reference/rpc/http/gettransactioncount)
## [getSignaturesForAddress Returns signatures for confirmed transactions that include the given address. ](https://www.helius.dev/docs/api-reference/rpc/http/getsignaturesforaddress)
## [getSignatureStatuses Returns the statuses of a list of signatures. ](https://www.helius.dev/docs/api-reference/rpc/http/getsignaturestatuses)
## [getFeeForMessage Returns the fee for a message. ](https://www.helius.dev/docs/api-reference/rpc/http/getfeeformessage)
## Token Information
## [getTokenAccountBalance Returns the token balance of an account. ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountbalance)
## [getTokenAccountsByOwner Returns all token accounts owned by the specified address. ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountsbyowner)
## [getTokenAccountsByDelegate Returns all token accounts that delegate to the specified address. ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenaccountsbydelegate)
## [getTokenLargestAccounts Returns the largest accounts for a specific token. ](https://www.helius.dev/docs/api-reference/rpc/http/gettokenlargestaccounts)
## [getTokenSupply Returns the total supply of a token. ](https://www.helius.dev/docs/api-reference/rpc/http/gettokensupply)
## Slot Information
## [getSlot Returns the current slot that the node is processing. ](https://www.helius.dev/docs/api-reference/rpc/http/getslot)
## [getSlotLeader Returns the identity of the current slot leader. ](https://www.helius.dev/docs/api-reference/rpc/http/getslotleader)
## [getSlotLeaders Returns the slot leaders for a slot range. ](https://www.helius.dev/docs/api-reference/rpc/http/getslotleaders)
## [getMinimumLedgerSlot Returns the lowest slot that the node has information about. ](https://www.helius.dev/docs/api-reference/rpc/http/minimumledgerslot)
## [getMaxRetransmitSlot Returns the maximum slot seen from retransmit stage. ](https://www.helius.dev/docs/api-reference/rpc/http/getmaxretransmitslot)
## [getMaxShredInsertSlot Returns the maximum slot seen from shred insert. ](https://www.helius.dev/docs/api-reference/rpc/http/getmaxshredinsertslot)
## [getHighestSnapshotSlot Returns the highest available snapshot slot. ](https://www.helius.dev/docs/api-reference/rpc/http/gethighestsnapshotslot)
## Epoch Information
## [getEpochInfo Returns information about the current epoch. ](https://www.helius.dev/docs/api-reference/rpc/http/getepochinfo)
## [getEpochSchedule Returns epoch schedule information. ](https://www.helius.dev/docs/api-reference/rpc/http/getepochschedule)
## [getLeaderSchedule Returns the leader schedule for an epoch. ](https://www.helius.dev/docs/api-reference/rpc/http/getleaderschedule)
## Inflation & Rewards
## [getInflationGovernor Returns the current inflation governor parameters. ](https://www.helius.dev/docs/api-reference/rpc/http/getinflationgovernor)
## [getInflationRate Returns the specific inflation values for the current epoch. ](https://www.helius.dev/docs/api-reference/rpc/http/getinflationrate)
## [getInflationReward Returns the inflation reward for a list of addresses for an epoch. ](https://www.helius.dev/docs/api-reference/rpc/http/getinflationreward)
## System Information
## [getHealth Returns the current health status of the node. ](https://www.helius.dev/docs/api-reference/rpc/http/gethealth)
## [getIdentity Returns the identity pubkey for the current node. ](https://www.helius.dev/docs/api-reference/rpc/http/getidentity)
## [getVersion Returns the current software version running on the node. ](https://www.helius.dev/docs/api-reference/rpc/http/getversion)
## [getClusterNodes Returns information about all the nodes in the cluster. ](https://www.helius.dev/docs/api-reference/rpc/http/getclusternodes)
## [getGenesisHash Returns the genesis hash. ](https://www.helius.dev/docs/api-reference/rpc/http/getgenesishash)
## [getFirstAvailableBlock Returns the lowest slot that the node has information about. ](https://www.helius.dev/docs/api-reference/rpc/http/getfirstavailableblock)
## [getRecentPerformanceSamples Returns a list of recent performance samples. ](https://www.helius.dev/docs/api-reference/rpc/http/getrecentperformancesamples)
## [getRecentPrioritizationFees Returns recent block hash fee information. ](https://www.helius.dev/docs/api-reference/rpc/http/getrecentprioritizationfees)
## [getVoteAccounts Returns the current vote accounts. ](https://www.helius.dev/docs/api-reference/rpc/http/getvoteaccounts)
## [getSupply Returns information about the current supply. ](https://www.helius.dev/docs/api-reference/rpc/http/getsupply)
## Stake Information
## [getStakeMinimumDelegation Returns the minimum delegation required for staking. ](https://www.helius.dev/docs/api-reference/rpc/http/getstakeminimumdelegation)
## Transaction Submission
## [sendTransaction Submits a signed transaction to the cluster for processing. ](https://www.helius.dev/docs/api-reference/rpc/http/sendtransaction)
## [simulateTransaction Simulates the execution of a transaction. ](https://www.helius.dev/docs/api-reference/rpc/http/simulatetransaction)
## [requestAirdrop Requests an airdrop of lamports to a Pubkey. ](https://www.helius.dev/docs/api-reference/rpc/http/requestairdrop)
Was this page helpful?
Yes
[Previous](https://www.helius.dev/docs/api-reference/endpoints)[ getAccountInfoReturns all information associated with the account of provided Pubkey. Next ](https://www.helius.dev/docs/api-reference/rpc/http/getaccountinfo)
On this page
  * [Transaction Information](https://www.helius.dev/docs/api-reference/rpc/http-methods#transaction-information)


Assistant
Responses are generated using AI and may contain mistakes.
