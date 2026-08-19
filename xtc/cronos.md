---
description: Cronos EVM network parameters, verified XTC contract generations and the planned transition to WXTC.
icon: ethereum
---

# XTC on Cronos EVM

XTC was issued on Cronos EVM before the native Xitcoin network was launched. This page distinguishes the Cronos token contract from native XTC and records the public migration roadmap.

## Cronos EVM network

| Property | Value |
|---|---|
| Network | Cronos EVM Mainnet |
| EVM chain ID | `25` |
| Chain ID hexadecimal | `0x19` |
| Native gas asset | CRO |
| Public RPC | `https://evm.cronos.org` |
| Explorer | [explorer.cronos.org](https://explorer.cronos.org) |

CRO pays Cronos network fees. XTC on Cronos is a CRC-20 token contract; it is not the native gas asset of chain 25.

## Contract generations

| Property | V1 — legacy | V2 — current Cronos generation |
|---|---|---|
| Network | Cronos EVM, chain 25 | Cronos EVM, chain 25 |
| Contract | `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd` | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Public display symbol | XTC | $XTC |
| Decimals | 8 | 18 |
| Supply reference | 21,000,000,000 | 5,250,000,000 |
| Integration status | Legacy — do not use for new integrations | Current Cronos proxy |

Inspect the current proxy on the [Cronos Explorer](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991). The associated contract-audit record is published by [Cyberscope](https://www.cyberscope.io/audits/1-xtc).

## V2 controls

The V2 contract lifecycle added administrative recovery support for third-party tokens sent accidentally to the token contract. It also records an **owner-restricted burn capability**. These are privileged contract controls, not public user permissions.

{% hint style="warning" %}
Never infer an administrative permission from a token symbol or interface. Integrators must verify the active proxy implementation, ownership state and verified ABI before describing or invoking a privileged function.
{% endhint %}

## 2025 migration

The migration converted eligible V1 balances to V2 at a 1:1 token ratio after the legacy tokens were transferred to the designated burn destination. The supply reference changed from 21 billion to 5.25 billion XTC.

The historical interface is [migration.xitcoin.org](https://migration.xitcoin.org). Its availability does not prove that a migration path remains open. Verify the full destination contract and the current service notice before signing.

## Planned V3 public identity update

The `$XTC` display symbol was introduced as a temporary market-facing identifier while the native Xitcoin blockchain was under development. The dollar sign is presentation metadata; it does not indicate a wrapped asset.

After native XTC becomes the canonical origin asset and the official bridge accounting is activated, the planned V3 update is:

| Role | Planned symbol |
|---|---|
| Native asset on the Xitcoin network | XTC |
| Verified 1:1 representation of native XTC on Cronos EVM | WXTC |

The transition from `$XTC` to `WXTC` must occur only with the corresponding bridge backing, contract release and public migration notice. Renaming a token without that technical backing would be misleading.

Future bridge extensions may support additional compatible networks. Every representation must remain tied to canonical native XTC through verified contracts, published network identifiers and auditable 1:1 accounting.

{% hint style="warning" %}
A symbol is not proof of origin. Verify the network, chain ID and complete contract address.
{% endhint %}
