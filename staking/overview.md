---
description: How validators, delegators and admission controls work in the official Xitcoin Guide.
icon: shield-halved
---

# How staking works

Xitcoin uses delegated proof of stake. Approved validators participate in consensus, while XTC holders can delegate stake to an active validator.

## Roles

- **Validator operator:** runs consensus infrastructure under the applicable authorization.
- **Delegator:** assigns stake to an active validator without becoming a validator operator.
- **Admission authority:** accepts, refuses, suspends, reactivates or revokes validator participation through the canonical on-chain authority.
- **Institutional controller:** manages the governance mandate of a sovereign position on behalf of the relevant State.

## Capacity and active count

| Parameter | Target rule |
|---|---:|
| Maximum active validator capacity | 258 |
| Reserved Member-State capacity | 193 |
| General validator capacity | 65 |
| Minimum self-delegation per validator | 5,000,000 XTC |
| Currently approved validators | 4 |
| Additional validators announced | 0 |
| Maximum number of delegators | No protocol quota documented |

The value 258 is a ceiling, not a statement that every position is already occupied. The same five-million-XTC self-delegation requirement applies to founder, sovereign and public validators.

The 193 reserved positions remain attached to their respective Member States. Their institutional governance and operating mandates may pass between successive authorized administrations without replacing the State position.

## Delegator boundary

Delegation contributes to consensus voting power only after stake is delegated to an already approved and active validator.

A delegator:

- does not consume a separate validator position;
- does not satisfy the validator's own five-million-XTC commitment;
- does not gain validator-admission authority;
- cannot force approval of a candidate validator;
- cannot prevent an authorized suspension or revocation;
- remains subject to staking, unbonding, commission and slashing rules.

Validator capacity and delegator participation are different measurements.

## Admission and removal

Every candidate validator can be accepted or refused after individual review. Approval requires the canonical on-chain admission authority and compliance with identity, self-delegation, security, mandate and operational requirements.

An approved validator can later be suspended or revoked when those requirements are no longer satisfied. A sovereign mandate transition changes the authorized administration or operating team without transferring the State position to another participant.

Holding or staking a large quantity of XTC does not override admission controls.

## Core staking concepts

- Delegations contribute to an active validator's consensus voting power.
- Rewards and penalties depend on the active network rules.
- Unbonding is not immediate; the candidate configuration uses a 21-day period.
- Validator commission reduces delegator rewards.
- Slashing can affect delegated stake.
- Validator admission remains separate from ordinary delegation choice.
- Sovereign allocation remains separate from ordinary validator rewards.

{% hint style="warning" %}
The five-million-XTC minimum and sovereign continuity framework remain target mainnet controls until their implementation, review and on-chain activation are complete.
{% endhint %}
