---
description: Network status in the official Xitcoin Guide.
icon: signal
---

# Network status

## Current public service

The production-facing testnet endpoints remain the authoritative way to determine what is publicly exposed. During the coordinated reset, they may still report the existing Cosmos chain ID `xitcoin-testnet`.

## Reset target

The validated reset configuration targets:

| Property | Value |
|---|---|
| Cosmos chain ID | `xitcoin-testnet-1` |
| EVM chain ID | `101089` (`0x18ae1`) |
| Validator set at genesis | 4 KCALB Ltd core validators |
| Mainnet impact | None |

{% hint style="warning" %}
Do not assume the reset is complete from documentation alone. Query the RPC status endpoint and confirm `result.node_info.network` before use.
{% endhint %}

## Verify live state

```bash
curl -fsS https://rpc-testnet.xitcoin.org/status | jq -r '{
  network: .result.node_info.network,
  height: .result.sync_info.latest_block_height,
  catching_up: .result.sync_info.catching_up
}'
```

A healthy node reports a changing height and `catching_up: false`.
