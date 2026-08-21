---
description: Verifiable sequence from the original Cronos token to the planned Xitcoin mainnet.
icon: timeline
---

# History and evolution

Xitcoin began as an XTC token ecosystem on Cronos and later expanded into development of a dedicated proof-of-stake Layer 1.

## Original Cronos token

The first public contract generation used:

* contract `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd`;
* 8 decimal places;
* a 21,000,000,000 XTC supply reference.

This contract is now a legacy identifier and must not be used for new integrations.

## Community-approved migration

In 2025, XTC migrated to a new Cronos contract generation. The process used a 1:1 token conversion after legacy tokens were sent to the designated burn destination. The supply reference was reduced by 75%, from 21 billion to 5.25 billion XTC.

The current proxy is:

`0xE45Fe733bC8617FA6DAC8437FC44B5FFFA949991`

It uses 18 decimal places and the canonical public ticker **XTC**. See [Contract and migration history](../xtc/migration-history.md).

## Contract revisions and security record

The public chronology distinguishes the persistent proxy generation from its implementation revisions:

1. V1 is the retired standalone Cronos token.
2. V2 is the upgradeable proxy generation used for the 2025 migration.
3. V3 is the current audited implementation revision identified by Cyberscope's source label `XitcoinV3_cyberscope.sol`.
4. V4 is reserved for the planned `WXTC` transition after the canonical native-XTC bridge is operational and verified.

Cyberscope publishes audit iterations dated July 2025 and February 2026 for the current contract record, together with a separate passed KYC record. Every implementation revision must be identified by source, bytecode, implementation address and audit scope. See [Xitcoin security and verification](../security/audits-and-validation.md).

## Dedicated blockchain development

The native network was developed with Cosmos SDK, CometBFT and Cosmos EVM. Native XTC is used for transaction fees, staking and compatible smart-contract execution.

## Public testnet

Xitcoin Testnet is active as a four-validator canonical staging network using Cosmos chain ID `xitcoin-testnet-1` and EVM chain ID `101089`. Consensus and local interfaces are active; transaction acceptance and public endpoint cutover remain release gates.

## Mainnet preparation

The mainnet target uses Cosmos chain ID `xitcoin`, EVM chain ID `101088`, native symbol XTC and base denomination `axtc`. Mainnet is not live.

Launch requires final genesis publication, security review, allocation-policy reconciliation, operational validation and a separately reviewed Cronos/native transfer mechanism.
