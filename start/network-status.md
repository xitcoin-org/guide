---
description: Canonical staging and public endpoint status for Xitcoin Testnet.
icon: signal
---

# Network status

## Canonical testnet

**Xitcoin Testnet** is active as a four-validator canonical staging network.

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

## Public endpoint boundary

The canonical staging network and the currently published domains are separate
operational states. Public domains continue serving the historical testnet
until the coordinated canonical cutover is completed.

{% hint style="warning" %}
Do not use a public domain as proof that the canonical genesis is active there.
Query the RPC status endpoint and confirm `result.node_info.network` before
signing or broadcasting.
{% endhint %}

## Verify live public state

```bash
curl -fsS https://rpc-testnet.xitcoin.org/status | jq -r '{
  network: .result.node_info.network,
  height: .result.sync_info.latest_block_height,
  catching_up: .result.sync_info.catching_up
}'
```

A healthy node reports a changing height and `catching_up: false`. The
canonical public cutover is complete only when the endpoint reports
`xitcoin-testnet-1` and the published genesis identity has been verified.

## Remaining public-release gates

1. complete Cosmos and EVM transaction validation;
2. validate admission, revocation and administrative signing;
3. complete the public RPC, API, explorer and faucet cutover;
4. verify monitoring, rollback and recovery after cutover;
5. validate the Cronos bridge independently before activation.

Testnet XTC has no monetary value. Mainnet has not launched.
