---
description: Validator admission in the official Xitcoin Guide.
icon: user-shield
---

# Validator admission

Xitcoin includes an on-chain validator-admission policy. Holding XTC does not automatically grant the right to join the active validator set.

## Policy model

A validator must satisfy both:

1. approval under the on-chain admission policy; and
2. the applicable staking and self-delegation requirements.

The initial reset configuration approves four KCALB Ltd core validators and permits a maximum active/approved set of 258.

{% hint style="warning" %}
The final minimum self-delegation policy is being reconciled with the release configuration. Until the validated genesis and on-chain state agree, do not rely on a numeric threshold copied from draft documentation.
{% endhint %}

External full nodes can synchronize and relay data without becoming validators. Validator admission controls consensus participation, not public read access to the blockchain.
