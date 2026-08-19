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

It uses 18 decimal places and is publicly displayed with the ticker **$XTC**. See [Contract and migration history](../xtc/migration-history.md).

## Contract review and revisions

Cyberscope publishes audit iterations dated July 2025 and February 2026 for the current Xitcoin contract record. Later contract revisions form part of the proxy implementation history. Every revision must be identified by source, bytecode, implementation address and audit scope.

## Dedicated blockchain development

The native network was developed with Cosmos SDK, CometBFT and Cosmos EVM. Native XTC is used for transaction fees, staking and compatible smart-contract execution.

## Public testnet

The public testnet is used to validate consensus, EVM execution, staking, validator operations, explorers and public interfaces. The coordinated release target uses Cosmos chain ID `xitcoin-testnet-1` and EVM chain ID `101089`.

## Mainnet preparation

The mainnet target uses Cosmos chain ID `xitcoin`, EVM chain ID `101088`, native symbol XTC and base denomination `axtc`. Mainnet is not live.

Launch requires final genesis publication, security review, allocation-policy reconciliation, operational validation and a separately reviewed Cronos/native transfer mechanism.
