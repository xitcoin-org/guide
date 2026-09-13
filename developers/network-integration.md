---
description: Network integration in the official Xitcoin Guide.
icon: plug
---

# Network integration

Wallets and services should represent Cosmos and EVM identities separately while showing XTC consistently.

## Testnet target

| Field | Value |
|---|---|
| Cosmos chain ID | `xitcoin-testnet-v2-1` |
| EVM chain ID | `101089` |
| EVM chain ID hex | `0x18ae1` |
| Native symbol | XTC |
| Base denomination | `axtc` |
| Decimals | 18 |

Integrations should detect chain-ID mismatches, use HTTPS endpoints, support endpoint failover and link users to this guide for authoritative information.

The Cosmos and EVM public RPC endpoints can share the same upstream sentry.
Different URLs alone do not provide independent consensus sources. Explorer
availability and successful network suggestion do not certify a wallet
integration or prove a transaction was finalized by independently verified nodes.
