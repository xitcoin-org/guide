---
description: Verifiable history of the XTC contracts on Cronos and their relationship to native XTC.
icon: arrow-right-arrow-left
---

# Contract and migration history

XTC was issued on Cronos EVM mainnet, chain ID `25`, before development of the native Xitcoin network.

## Contract generations

| Record | V1 — legacy XTC | V2 — current Cronos XTC |
|---|---|---|
| Network | Cronos EVM — chain 25 | Cronos EVM — chain 25 |
| Contract | `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd` | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Public display symbol | XTC | $XTC |
| Decimals | 8 | 18 |
| Supply reference | 21,000,000,000 | 5,250,000,000 |
| Status | Legacy; do not use for new integrations | Current Cronos proxy |

Integrators must use the complete current proxy address. An implementation address is not a user-facing token address.

## 2025 migration

The migration converted eligible V1 balances to V2 at a **1:1 token ratio**. Legacy tokens were transferred to the designated burn destination before the corresponding V2 tokens were credited. The supply reference changed from 21 billion to 5.25 billion XTC, a reduction of 15.75 billion tokens (75%).

The historical migration interface is [migration.xitcoin.org](https://migration.xitcoin.org). Its availability must not be interpreted as confirmation that every migration path remains open.

## V2 contract evolution

The V2 lifecycle introduced a proxy-based upgrade path and later administrative safeguards:

* recovery support for third-party tokens transferred accidentally to the token contract;
* an owner-restricted burn capability;
* continued separation between privileged administration and ordinary holder transfers.

These controls must be assessed against the verified active implementation and ownership state. The guide does not publish privileged operating instructions.

The current contract and its audit iterations are available through the [Cronos Explorer](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) and [Cyberscope audit record](https://www.cyberscope.io/audits/1-xtc).

## Planned V3 update

V3 is the planned public transition for the Cronos representation after native XTC and the canonical bridge are operational.

| Stage | Public identity | Meaning |
|---|---|---|
| V2 | $XTC | Temporary Cronos display symbol used while the native chain was under development |
| V3 | WXTC | Verified 1:1 Cronos representation of canonical native XTC |
| Native network | XTC | Canonical Xitcoin asset |

The `W` prefix must describe technical provenance, not marketing. V3 must not be presented as WXTC until bridge contracts, supply accounting, migration instructions and public verification records are released.

## Cross-network accounting

A contract migration and a blockchain bridge are different operations. Future bridge extensions may support other compatible networks, but each representation must satisfy the same controls:

1. a single canonical native-XTC origin;
2. a verified destination contract or asset identifier;
3. auditable lock, burn, mint and release accounting;
4. a documented 1:1 supply relationship;
5. public status and security notices before activation.

## Verification checklist

1. Confirm the origin and destination networks.
2. Verify every chain ID and complete contract or asset address.
3. Confirm the bridge’s lock, burn, mint and release accounting.
4. Open interfaces only from an official Xitcoin link.
5. Confirm the service is active before signing.
6. Test with a small amount.
7. Retain transaction hashes and receipts.
