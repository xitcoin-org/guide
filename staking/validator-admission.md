---
description: Validator admission in the official Xitcoin Guide.
icon: user-shield
---

# Validator admission

Xitcoin includes an on-chain validator-admission policy. Holding, receiving, staking or delegating XTC does not grant the right to join the active validator set.

## Current release candidate

| Parameter | Candidate value |
|---|---:|
| Maximum validator and admission capacity | 258 |
| Initially approved validators | 4 |
| Additional validators currently announced | 0 |
| Protocol minimum self-delegation | 1,000,000 XTC |
| Initial self-delegation per core validator | 5,000,000 XTC |

The four initially approved validators are Xitcoin Atlas, Xitcoin Borealis, Xitcoin Meridian and Xitcoin Zenith.

The protocol minimum is the admission floor. The larger core-validator amount is the initial deployment value. These are different controls and are not contradictory.

## Required admission conditions

A validator must satisfy all applicable conditions:

1. a separately reviewed operator identity;
2. explicit approval by the canonical on-chain admission authority;
3. the applicable self-delegation requirement;
4. security, key-management and operational requirements;
5. an auditable on-chain approval record.

The 258-position parameter is a maximum capacity, not a target validator count.

## Participation capacity

The planning model separates 195 sovereign reference positions and 63 public positions. These categories do not announce additional validators, transfer funds or grant consensus power.

Any expansion beyond the four initially approved validators will be considered individually. No operator is approved merely because capacity remains available.

## Authority boundary

Only the canonical validator-admission authority can execute the defined approval and revocation actions during the current launch phase.

Token holdings, staking balances, delegation weight and ordinary governance voting do not replace or override this authority. The technical presence of a Cosmos governance module does not give token holders validator-admission control.

Approval and revocation are recorded in blockchain state. A revoked validator must not be able to recreate or unjail itself without renewed authorization.

External full nodes can synchronize and relay data without becoming validators. Validator admission controls consensus participation, not public read access.

{% hint style="warning" %}
Candidate testnet parameters do not automatically become mainnet rights. Mainnet authority custody and recovery controls must be verified against final on-chain state before launch.
{% endhint %}
