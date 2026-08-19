---
description: How staking works in the official Xitcoin Guide.
icon: shield-halved
---

# How staking works

Xitcoin uses delegated proof of stake. Validators participate in consensus, while XTC holders can delegate stake to validators.

## Roles

* **Validator operator:** runs consensus infrastructure and maintains signing-key security.
* **Delegator:** assigns voting power to a validator without transferring ownership of the delegation.
* **Admission authority:** manages the protocol allowlist for validator operators according to the public network policy.

## Core concepts

* Delegations contribute to a validator's voting power.
* Rewards and penalties are network-dependent.
* Unbonding is not immediate; the configured period is 21 days.
* Validator commission can reduce delegator rewards.
* Slashing can affect delegated stake.

{% hint style="warning" %}
Staking carries protocol and operational risk. Review validator performance, commission and security history before delegating.
{% endhint %}
