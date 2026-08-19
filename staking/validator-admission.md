---
description: Validator admission in the official Xitcoin Guide.
icon: user-shield
---

# Validator admission

Xitcoin includes an on-chain validator-admission policy. Holding XTC does not automatically grant the right to join the active validator set.

## Policy model

A validator must satisfy both:

1. approval under the on-chain admission policy; and
2. the applicable staking, self-delegation, security and operational requirements.

The current Xitcoin Testnet release candidate defines:

| Parameter | Candidate value |
|---|---:|
| Maximum validator and admission capacity | 258 |
| Initially approved core validators | 4 |
| Protocol minimum self-delegation | 1,000,000 XTC |
| Initial self-delegation per core validator | 5,000,000 XTC |

The protocol minimum is the admission floor. The larger core-validator amount is the initial deployment value for Atlas, Borealis, Meridian and Zenith. These values describe different controls and are not contradictory.

## Participation capacity

The 258-position planning model separates:

- 195 sovereign reference positions; and
- 63 public positions.

A reference position is not an automatic validator right. Admission still requires an approved validator operator address and compliance with the published technical and security requirements.

The allocation dataset also contains 39 territorial statistical consolidations. Those mappings support deterministic population calculations and do not create additional validator positions.

## Revocation and access

Approval and revocation are recorded in blockchain state. A revoked validator must not be able to recreate or unjail itself without renewed authorization.

External full nodes can synchronize and relay data without becoming validators. Validator admission controls consensus participation, not public read access to the blockchain.

{% hint style="warning" %}
Candidate testnet parameters do not automatically become mainnet rights. Mainnet admission, custody and governance controls must be verified against the final genesis and active on-chain state before launch.
{% endhint %}
