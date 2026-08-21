---
description: Canonical public endpoint status for Xitcoin Testnet.
icon: signal
---

# Network status

## Canonical testnet

**Xitcoin Testnet** is active publicly as a four-validator canonical network.

| Property | Canonical value |
|---|---|
| Public name | Xitcoin Testnet |
| Cosmos chain ID | `xitcoin-testnet-1` |
| EVM chain ID | `101089` (`0x18ae1`) |
| Native asset | XTC |
| Base denomination | `axtc` |
| Decimals | 18 |
| Initial validators | Atlas, Borealis, Meridian and Zenith |
| Validator capacity | 258 |
| Minimum self-delegation | 5,000,000 XTC |
| Genesis SHA-256 | `7d13d7ed6a19ea48e2ce3c408f1f457e0961e72df6dd480d8200a6db5bae8414` |

The `-1` suffix belongs to the Cosmos chain identifier for the current
genesis. It is not a public network version or server number.

## Public endpoints

The canonical network is publicly available through the Xitcoin testnet RPC,
API, EVM RPC, explorers and faucet endpoints.

{% hint style="info" %}
Before signing or broadcasting, query the RPC status endpoint and confirm that
`result.node_info.network` reports `xitcoin-testnet-1`.
{% endhint %}

## Verify live public state

```bash
curl -fsS https://rpc-testnet.xitcoin.org/status | jq -r '{
  network: .result.node_info.network,
  height: .result.sync_info.latest_block_height,
  catching_up: .result.sync_info.catching_up
}'
```

A healthy public node reports `xitcoin-testnet-1`, a changing height and
`catching_up: false`.

## Validated public-testnet state

The canonical public testnet has completed Cosmos and EVM transaction
validation, validator admission and revocation testing, multisignature
administrative validation, public endpoint cutover, monitoring validation and
rollback preparation.

The Cronos bridge remains separate and inactive. It must be validated
independently before any future activation.

Testnet XTC has no monetary value. Mainnet has not launched.
