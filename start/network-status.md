---
description: Canonical public endpoint status for Xitcoin Public Testnet.
icon: signal
---

# Network status

## Canonical testnet

**Xitcoin Public Testnet** is active as a four-validator network behind one
public sentry.

| Property | Canonical value |
|---|---|
| Public name | Xitcoin Public Testnet |
| Cosmos chain ID | `xitcoin-testnet-v2-1` |
| EVM chain ID | `101089` (`0x18ae1`) |
| Native asset | XTC |
| Base denomination | `axtc` |
| Decimals | 18 |
| Genesis supply | 477,000,000 XTC |
| Initial validators | Atlas, Borealis, Meridian and Zenith |
| Genesis SHA-256 | `5db34acf6496b2c76a6f516e0eb605caef6762552584ddbed7c8703239f33d72` |

The Cosmos chain ID is a technical network identifier. The public-facing name
remains **Xitcoin Public Testnet**.

## Public endpoints

The network is publicly available through the Xitcoin testnet RPC, API, gRPC,
EVM RPC, explorers and faucet endpoints.

{% hint style="info" %}
Before signing or broadcasting, query the RPC status endpoint and confirm that
`result.node_info.network` reports `xitcoin-testnet-v2-1`.
{% endhint %}

## Verify live public state

```bash
curl -fsS https://rpc-testnet.xitcoin.org/status | jq -r '{
  network: .result.node_info.network,
  height: .result.sync_info.latest_block_height,
  catching_up: .result.sync_info.catching_up
}'
```

A healthy public node reports `xitcoin-testnet-v2-1`, a changing height and
`catching_up: false`.

Blockscout can trail the chain head briefly while it indexes. A moving
one-to-two-block lag is normal; a persistent or increasing lag must be
investigated.

## Published public-testnet baseline

- four validators active with equal initial voting power;
- public RPC, API, gRPC, EVM RPC, explorers and faucet operational;
- faucet amount 10 XTC per accepted request, backed by a 50,000,000 XTC
  allocation with no automatic minting;
- Cosmos explorer built from the standard Ping Explorer source with an isolated
  Xitcoin faucet extension;
- Blockscout reindexed from the deployed genesis;
- automated healthcheck repeatedly successful;
- bridge route not configured and disabled.

These published network records are not a live availability monitor. The
4 September 2026 repository review did not access blockchain servers or
revalidate endpoint health. Current availability must be verified separately.

Testnet XTC has no monetary value. Mainnet has not launched.
