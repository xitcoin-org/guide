---
description: Verifiable history of the XTC contracts on Cronos and their relationship to native XTC.
icon: arrow-right-arrow-left
---

# Contract and migration history

XTC was issued on Cronos EVM mainnet, chain ID `25`, before development of the native Xitcoin network.

## Contract generations

| Record | V1 — legacy XTC | V2 — current Cronos `$XTC` |
|---|---|---|
| Network | Cronos EVM — chain 25 | Cronos EVM — chain 25 |
| Contract | `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd` | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Public display symbol | XTC | `$XTC` |
| Decimals | 8 | 18 |
| Supply reference | 21,000,000,000 | 5,250,000,000 |
| Status | Legacy; do not use for new integrations | Current Cronos proxy |

Integrators must use the complete current proxy address. An implementation address is not a user-facing token address.

## 2025 migration

The migration converted eligible V1 balances to V2 at a **1:1 token ratio**. Legacy tokens were transferred to the designated burn destination before the corresponding V2 tokens were credited. The supply reference changed from 21 billion to 5.25 billion XTC, a reduction of 15.75 billion tokens (75%).

The historical migration interface is [migration.xitcoin.org](https://migration.xitcoin.org). Its availability must not be interpreted as confirmation that every migration path remains open.

## V2 proxy and V3 implementation evolution

The 2025 V2 generation introduced the persistent proxy address. Its later audited implementation revision is identified in the Cyberscope record by the source label `XitcoinV3_cyberscope.sol`. This V3 revision history introduced or preserved the following safeguards:

* recovery support for third-party tokens transferred accidentally to the token contract;
* an owner-restricted burn capability;
* continued separation between privileged administration and ordinary holder transfers.

These controls must be assessed against the verified active implementation and ownership state. The guide does not publish privileged operating instructions.

## Contract review and revisions

Cyberscope publishes the official [Xitcoin smart-contract audit record](https://www.cyberscope.io/audits/1-xtc) for the Cronos proxy contract [`0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`](https://explorer.cronos.com/token/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991).

The public record lists four audit iterations:

* [2 July 2025 and 16 July 2025](https://www.cyberscope.io/audits/1-xtc);
* [16 February 2026 and 17 February 2026](https://www.cyberscope.io/audits/1-xtc).

The corresponding technical record, including the audited source label, implementation address and SHA-256 source hash, is preserved in the [`xitcoin-org/contracts` repository](https://github.com/xitcoin-org/contracts/blob/main/audits/cyberscope-v2.md).

Cyberscope identifies the reviewed source as `XitcoinV3_cyberscope.sol`. The canonical repository source is [`contracts/cronos/v2/XTCV2.sol`](https://github.com/xitcoin-org/contracts/blob/main/contracts/cronos/v2/XTCV2.sol), with SHA-256:

`b5de4f5c4f13334bf644ec8fa97f8b0cda836ddc76935dc14c7bfcda2a73ff14`

The implementation associated with this reviewed record is [`0x6c171952999421F0DA00E14F97B9C2DfBE71D8A0`](https://explorer.cronos.com/address/0x6c171952999421F0DA00E14F97B9C2DfBE71D8A0).

The auditor's historical filename and the canonical repository filename differ. The source hash identifies the reviewed code. This audit record covers the identified Cronos token-contract source only. It does not certify the Xitcoin Layer 1, validator infrastructure, explorers, migration services, bridge software or any later proxy implementation.

Before relying on the audit after a proxy revision, verify the active implementation address, deployed bytecode, canonical source hash and applicable audit scope together.

## Planned V4 symbol update

V4 is reserved for normalization of the Cronos proxy display symbol to `XTC`.

| Stage | Public identity | Meaning |
|---|---|---|
| V2 | `$XTC` | Current Cronos proxy generation |
| V3 | `$XTC` | Current audited implementation revision within the V2 proxy generation |
| V4 | XTC | Planned metadata update; not active |
| Native network | XTC | Native gas, staking and EVM asset |

The update is limited to public asset metadata and is intended to preserve the proxy address, holder balances, decimal precision and total supply. It requires authorization review, source and bytecode verification, independent security review and a public execution record.

External representations use the public symbol `XTC` and are identified by their network and complete contract, mint or IBC denomination. Each release must preserve auditable one-to-one accounting.

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
