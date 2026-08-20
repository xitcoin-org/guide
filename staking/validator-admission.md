---
description: Validator admission in the official Xitcoin Guide.
icon: user-shield
---

# Validator admission

Xitcoin includes an on-chain validator-admission policy. Holding, receiving, staking or delegating XTC does not grant the right to join the active validator set.

## Target protocol configuration

| Parameter | Target value |
|---|---:|
| Maximum validator and admission capacity | 258 |
| Initially approved validators | 4 |
| Additional validators currently announced | 0 |
| Minimum self-delegation for every validator | 5,000,000 XTC |
| Initial self-delegation per core validator | 5,000,000 XTC |

The four initially approved validators are Xitcoin Atlas, Xitcoin Borealis, Xitcoin Meridian and Xitcoin Zenith.

The same minimum self-delegation applies to founder, sovereign and public validators. It represents the validator's own commitment and cannot be satisfied by a sovereign allocation or by third-party delegations.

If all 258 positions were active at the minimum, their aggregate self-delegation would be 1,290,000,000 XTC.

## Required admission conditions

A validator must satisfy all applicable conditions:

1. a separately reviewed operator identity;
2. explicit approval by the canonical on-chain admission authority;
3. at least 5,000,000 XTC of self-delegation;
4. security, governance, mandate and operational requirements;
5. an auditable on-chain approval record.

The 258-position parameter is a maximum capacity, not an announcement that every position is active.

## Participation capacity

The planning model separates:

- 195 positions reserved for sovereign institutional participation;
- 63 public positions;
- 258 positions in total.

A sovereign position remains attached to the relevant State. Successive administrations of that State may transfer the institutional governance and operating mandate to their authorized successors without changing the position, its history or its remaining allocation.

A reserved position receives no validator reward and no sovereign allocation tranche until all activation conditions have been satisfied.

## Authority boundary

Only the canonical validator-admission authority can execute the defined approval, suspension, reactivation and revocation actions during the current launch phase.

Token holdings, staking balances, delegation weight and ordinary governance voting do not replace or override this authority. Approval and revocation remain visible in blockchain state.

External full nodes can synchronize and relay data without becoming validators. Validator admission controls consensus participation, not public read access.

{% hint style="warning" %}
The five-million-XTC minimum is part of the target configuration under development. Mainnet activation requires validated source, final genesis or upgrade parameters, security review and verified on-chain state.
{% endhint %}
