---
description: How validators, delegators and admission controls work in the official Xitcoin Guide.
icon: shield-halved
---

# How staking works

Xitcoin uses delegated proof of stake. Approved validators participate in consensus, while XTC holders can delegate stake to an active validator.

## Roles

- **Validator operator:** runs consensus infrastructure and maintains signing-key security.
- **Delegator:** assigns stake to an active validator without becoming a validator operator.
- **Admission authority:** accepts, refuses, suspends or revokes validator operators through the canonical on-chain authority.

## Capacity and active count

| Parameter | Current rule |
|---|---:|
| Maximum active validator capacity | 258 |
| Sovereign reference capacity | 195 |
| Public validator capacity | 63 |
| Currently approved validators | 4 |
| Additional validators announced | 0 |
| Maximum number of delegators | No protocol quota documented |

The active validator count can vary between zero and the configured maximum. The value 258 is a ceiling, not a promise that every position will remain permanently occupied.

The 195 sovereign references and 63 public positions classify potential validator capacity. They do not create active validators automatically.

## Delegator boundary

Delegation contributes to consensus voting power only after stake is delegated to an already approved and active validator.

A delegator:

- does not consume a separate validator position;
- does not gain validator-admission authority;
- cannot force approval of a candidate validator;
- cannot prevent an authorized suspension or revocation;
- remains subject to staking, unbonding, commission and slashing rules.

The number of delegators may vary with network activity. Validator capacity and delegator participation are different measurements.

## Admission and removal

Every candidate validator can be accepted or refused after individual review. Approval requires the canonical on-chain admission authority and compliance with identity, self-delegation, security and operational requirements.

An approved validator can later be suspended or revoked when authorization, security, performance or mandate requirements are no longer satisfied. Admission and revocation must remain visible in blockchain state and transaction history.

Holding or staking a large quantity of XTC does not override this process.

## Core staking concepts

- Delegations contribute to an active validator's consensus voting power.
- Rewards and penalties are network-dependent.
- Unbonding is not immediate; the candidate configuration uses a 21-day period.
- Validator commission reduces delegator rewards.
- Slashing can affect delegated stake.
- Revocation of validator admission remains separate from ordinary delegation choice.

{% hint style="warning" %}
Staking carries protocol and operational risk. Review validator performance, commission, admission status and security history before delegating.
{% endhint %}
