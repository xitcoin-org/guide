---
description: Official guide to the Xitcoin network, XTC, testnet, staking, development and node operations.
icon: circle-x
coverY: 0
layout:
  width: default
  cover:
    visible: true
    size: hero
    mask: none
---

# Xitcoin Guide

Xitcoin is an EVM-compatible proof-of-stake Layer 1 built with the Cosmos SDK, CometBFT and Cosmos EVM. It brings together Ethereum-compatible smart contracts and tooling with Cosmos-native consensus, staking, governance and interoperability.

This is the canonical public guide for users, developers, validators, infrastructure providers and integration partners.

{% hint style="warning" %}
**The canonical public testnet is active.** Xitcoin Public Testnet is publicly available with Cosmos chain ID `xitcoin-testnet-v2-1`. Always verify the live network identifier before signing or broadcasting.
{% endhint %}

## Explore the network

<table data-view="cards">
<thead><tr><th></th><th></th></tr></thead>
<tbody>
<tr><td><strong>Understand Xitcoin</strong></td><td>Purpose, architecture, history and ecosystem.</td></tr>
<tr><td><strong>Use the testnet</strong></td><td>Wallet configuration, test XTC, endpoints and explorers.</td></tr>
<tr><td><strong>Stake and validate</strong></td><td>Delegation, validator operations, admission and risks.</td></tr>
<tr><td><strong>Build on Xitcoin</strong></td><td>EVM tooling, Cosmos APIs and integration metadata.</td></tr>
</tbody>
</table>

## Start by role

| You are… | Recommended starting point |
|---|---|
| A new user | [What is Xitcoin?](start/what-is-xitcoin.md) |
| A wallet user | [Connect a wallet](testnet/connect-wallet.md) |
| A developer | [Developer overview](developers/overview.md) |
| A delegator | [How staking works](staking/overview.md) |
| A node operator | [Operator overview](operators/overview.md) |
| A public authority | [Sovereign participation](governance/sovereign-participation-reference.md) |
| An integration partner | [Network integration](developers/network-integration.md) |
| A security researcher | [Responsible disclosure](security/responsible-disclosure.md) |

## Network identity

| Property | Testnet | Mainnet |
|---|---:|---:|
| Cosmos chain ID | `xitcoin-testnet-v2-1` | `xitcoin` |
| EVM chain ID | `101089` | `101088` |
| Native asset | XTC | XTC |
| Base denomination | `axtc` | `axtc` |
| Decimals | 18 | 18 |
| Status | Canonical public testnet active | **Not launched** |

{% hint style="info" %}
Testnet XTC has no monetary value. Mainnet has not launched, and no page in this guide should be interpreted as announcing a mainnet or bridge launch.
{% endhint %}

## Public source of truth

The [Xitcoin PoS Chain repository](https://github.com/xitcoin-org/pos-chain) contains the node software and release source. Canonical public Testnet network configuration and Genesis files are maintained in the [Xitcoin Testnets repository](https://github.com/xitcoin-org/testnets). This guide makes that information understandable and operational. When a draft document differs from a validated release or live on-chain state, the validated release and live state take precedence.
