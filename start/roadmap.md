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

* four-validator public testnet active with Cosmos chain ID `xitcoin-testnet-v2-1`;
* EVM chain ID `101089`;
* clean validator and admission-authority identities;
* four-validator consensus validation;
* public endpoints, standard Ping Explorer and 10 XTC faucet operational;
* release documentation, canonical genesis checksum and CI security lock completed;
* reproducible Linux AMD64 `xitcoind` release artifact validation;
* Cronos symbol-normalization specification, proxy authorization review and bridge security review before any production transition.

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
