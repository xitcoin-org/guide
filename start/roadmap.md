---
description: Release stages from the active Cronos token and public testnet to the planned Xitcoin mainnet.
icon: route
---

# Roadmap and release status

The roadmap separates completed public records from infrastructure currently being validated and from future mainnet work.

## Completed or publicly verifiable

* XTC contract generations on Cronos;
* 2025 migration from the legacy contract to the current proxy;
* supply-model reduction from 21 billion to 5.25 billion XTC;
* Cyberscope contract-audit iterations and passed KYC record;
* public market-information listings;
* Xitcoin Layer 1 source and testnet infrastructure.

## Current engineering phase

* canonical four-validator staging network using Cosmos chain ID `xitcoin-testnet-1`;
* EVM chain ID `101089`;
* clean validator and admission-authority identities;
* four-validator consensus validation;
* endpoint, explorer, faucet and indexer cutover preparation;
* release documentation and checksum reconciliation;
* V4 WXTC specification and bridge security review before any Cronos identity transition.

## Mainnet target

| Component | Target |
|---|---|
| Cosmos chain ID | `xitcoin` |
| EVM chain ID | `101088` |
| Native asset | XTC |
| Base denomination | `axtc` |
| Decimal precision | 18 |
| Status | Pre-launch |

## Remaining mainnet gates

1. finalize supply and allocation policy;
2. reconcile validator admission and minimum self-delegation parameters;
3. complete security review of the mainnet release;
4. publish genesis, checksums and reproducible build instructions;
5. deploy and review the Cronos/native transfer mechanism;
6. publish custody, emergency and upgrade procedures;
7. validate wallets, explorers, RPC, REST, gRPC and EVM JSON-RPC;
8. announce a coordinated launch only after all gates are satisfied.

{% hint style="warning" %}
Target identifiers are integration planning values, not proof that mainnet is live.
{% endhint %}
