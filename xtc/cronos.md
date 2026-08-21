---
description: Cronos EVM network parameters, verified XTC contract generations and the planned transition to WXTC.
icon: hexagon
---

# XTC on Cronos EVM

<img src="../.gitbook/assets/cronos-logo.png" alt="Cronos logo" width="64">

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

## Contract generations and revisions

| Property | V1 — legacy | V2 — current Cronos generation |
|---|---|---|
| Network | Cronos EVM, chain 25 | Cronos EVM, chain 25 |
| Contract | `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd` | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Public display symbol | XTC | XTC |
| Decimals | 8 | 18 |
| Supply reference | 21,000,000,000 | 5,250,000,000 |
| Integration status | Legacy — do not use for new integrations | Current Cronos proxy |

Inspect the current proxy on the [Cronos Explorer](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991). The associated contract-audit record is published by [Cyberscope](https://www.cyberscope.io/audits/1-xtc).

### Version terminology

| Version | Technical role | Public status |
|---|---|---|
| V1 | Legacy standalone token contract | Legacy |
| V2 | Upgradeable Cronos proxy generation and 2025 migration destination | Current public proxy |
| V3 | Current audited implementation revision associated with the V2 proxy generation | Reviewed implementation record |
| V4 | Planned implementation and identity transition to `WXTC` | Planned; not active |

The proxy-generation name and implementation-revision name must not be confused. The Cyberscope record labels the reviewed source `XitcoinV3_cyberscope.sol`, while the canonical contracts repository groups the current proxy generation under `contracts/cronos/v2/`. The reviewed source hash links those records.


## Buy or swap XTC

XTC can be obtained on Cronos through decentralized-market routes that reference the current proxy contract.

| Access route | Link | Purpose |
|---|---|---|
| VVS Finance | [Open a CRO-to-XTC swap](https://vvs.finance/trade/swap?inputCurrency=cro&outputCurrency=0xe45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) | Opens the VVS swap interface with CRO as the input asset and the current XTC contract as the output asset |
| Crypto.com Onchain | [Open the official Onchain page](https://crypto.com/onchain) | Use the wallet's Swap feature on Cronos and verify XTC by its complete contract address |
| DEX Screener | [View XTC markets and pools](https://dexscreener.com/cronos/0xe45fe733bc8617fa6dac8437fc44b5fffa949991) | Compare detected pools, liquidity, activity and trading pairs |
| GeckoTerminal | [Search all pools for the XTC contract](https://www.geckoterminal.com/search?query=0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) | Independent live pool discovery by contract address |

In Crypto.com Onchain, select **Cronos** as the network, open **Swap**, and identify XTC using `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`. Before confirming, review the output amount, price impact, network fee and the protocol displayed on the confirmation screen. Token and route availability depends on the liquidity sources supported by the wallet at that time.

{% hint style="warning" %}
The legacy V1 address must not be used for a new purchase or liquidity position. A ticker or logo is not proof of identity. Verify the Cronos network and the complete current contract address before signing.
{% endhint %}

For a wider market overview and pool-verification procedure, see [Markets and liquidity](../resources/markets-and-liquidity.md).

## Current proxy controls

The current proxy lifecycle added administrative recovery support for third-party tokens sent accidentally to the token contract. It also records an **owner-restricted burn capability**. These are privileged contract controls, not public user permissions.

{% hint style="warning" %}
Never infer an administrative permission from a token symbol or interface. Integrators must verify the active proxy implementation, ownership state and verified ABI before describing or invoking a privileged function.
{% endhint %}

## 2025 migration

The migration converted eligible V1 balances to V2 at a 1:1 token ratio after the legacy tokens were transferred to the designated burn destination. The supply reference changed from 21 billion to 5.25 billion XTC.

The historical interface is [migration.xitcoin.org](https://migration.xitcoin.org). Its availability does not prove that a migration path remains open. Verify the full destination contract and the current service notice before signing.

## Planned V4 WXTC update

Some historical market listings used the temporary display ticker `$XTC` while the native Xitcoin blockchain was under development. The canonical current display symbol is `XTC`; the dollar sign never indicated a wrapped asset.

After native XTC becomes the canonical origin asset and the official bridge accounting is activated, the planned V4 update is:

| Role | Planned symbol |
|---|---|
| Native asset on the Xitcoin network | XTC |
| Verified 1:1 representation of native XTC on Cronos EVM | WXTC |

V4 and the transition from Cronos `XTC` to `WXTC` must become public only with the corresponding bridge backing, contract release and public migration notice. Renaming a token without that technical backing would be misleading.

Future bridge extensions may support additional compatible networks. Every representation must remain tied to canonical native XTC through verified contracts, published network identifiers and auditable 1:1 accounting.

{% hint style="warning" %}
A symbol is not proof of origin. Verify the network, chain ID and complete contract address.
{% endhint %}
