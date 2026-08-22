---
description: Public overview of independent XTC contract reviews and Xitcoin security evidence.
icon: shield-heart
---

# Xitcoin security and verification

Xitcoin separates public security information from technical verification records. This guide explains what has been reviewed and where the canonical evidence is maintained. Detailed test logs, implementation checklists and release artifacts belong in the relevant GitHub repositories.

## Public security records

| Scope | Public status | Canonical reference |
|---|---|---|
| XTC contract on Cronos | Independent Cyberscope audit published | [Cyberscope XTC audit](https://www.cyberscope.io/audits/1-xtc) |
| Xitcoin project identity | Cyberscope KYC passed | [KYC certificate](https://github.com/cyberscope-io/kyc/blob/main/1-xtc/kyc.png) |
| XTC contract source and audit mapping | Published in the contracts repository | [Technical audit record](https://github.com/xitcoin-org/contracts/blob/main/audits/cyberscope-v2.md) |
| Xitcoin Layer 1 | Source, CI, releases and engineering evidence maintained in GitHub | [Xitcoin PoS Chain](https://github.com/xitcoin-org/pos-chain) |
| Canonical bridge | Not presented as production-audited or active | [Bridge status](../bridge/status-and-security.md) |

## XTC contract on Cronos

The current public Cronos proxy is [`0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`](https://explorer.cronos.com/token/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991). Cyberscope's published record identifies the reviewed implementation and its audit history.

The audit applies only to its stated contract, source and implementation scope. It does not automatically cover later upgrades, the Xitcoin Layer 1, validators, explorers, bridge software or operational infrastructure.

For source hashes, implementation mapping and revision history, use the [canonical contracts audit record](https://github.com/xitcoin-org/contracts/blob/main/audits/cyberscope-v2.md).

## Layer 1 verification

Layer 1 tests, CI workflows, release checksums, genesis records and implementation-specific evidence are maintained in the [Xitcoin PoS Chain repository](https://github.com/xitcoin-org/pos-chain).

A successful test or merged pull request proves only the recorded scope. Production status must additionally be confirmed through the applicable release, deployment record and live on-chain state.

## Bridge boundary

The bridge is a separate security boundary. It must not be described as production-audited or active until its contracts, deployment addresses, relayer authorization, replay protection, finality rules, supply reconciliation and independent review are published.

{% hint style="warning" %}
An audit, KYC certificate or successful test applies only to its stated scope. Verify the relevant source, deployed address, release and live network before relying on it.
{% endhint %}
