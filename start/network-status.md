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
| Genesis time | `2026-08-25T21:48:17.77229Z` |
| Genesis supply | 457,000,000 XTC |
| Initial validators | Atlas, Borealis, Meridian and Zenith |
| Validator capacity | 258 |
| Minimum self-delegation | 5,000,000 XTC |
| Genesis SHA-256 | `55c8756a212b9e92c0e8427ea61caff7fa9dca40e801e4b848f59d1aa5f6dae6` |

The `-1` suffix belongs to the Cosmos chain identifier for this genesis. It is
not a public network version or server number.

## Public endpoints

The canonical network is publicly available through the Xitcoin testnet RPC,
API, EVM RPC, explorers and faucet endpoints. The sentry, four validators,
Blockscout, faucet and automated healthcheck were certified together on
2026-08-26.

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

Blockscout can trail the chain head briefly while it indexes. A moving
one-to-two-block lag is normal; a persistent or increasing lag must be
investigated.

## Certified public-testnet state

- four validators active with equal initial voting power;
- public RPC, API, EVM RPC, explorers and faucet operational;
- faucet amount 10 XTC per accepted request, backed by a 50,000,000 XTC
  allocation with no automatic minting;
- Blockscout reindexed from the deployed genesis;
- automated healthcheck repeatedly successful;
- bridge route not configured and disabled.

Testnet XTC has no monetary value. Mainnet has not launched.
