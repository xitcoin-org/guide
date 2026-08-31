---
description: Network endpoints in the official Xitcoin Guide.
icon: tower-broadcast
---

# Network endpoints

| Service | Public endpoint |
|---|---|
| CometBFT RPC | `https://rpc-testnet.xitcoin.org` |
| Cosmos REST API | `https://api-testnet.xitcoin.org` |
| gRPC | `grpc-testnet.xitcoin.org:443` |
| EVM JSON-RPC | `https://evm-rpc-testnet.xitcoin.org` |
| Cosmos explorer | `https://explorer-testnet.xitcoin.org` |
| EVM explorer | `https://evm-explorer-testnet.xitcoin.org` |
| Faucet | `https://faucet-testnet.xitcoin.org` |

## Verify the Cosmos network

```bash
curl -fsS https://rpc-testnet.xitcoin.org/status
```

Read `result.node_info.network`, the latest block height and `catching_up`. The
expected Cosmos chain ID is `xitcoin-testnet-v2-1`.

## Verify the EVM chain ID

```bash
curl -fsS https://evm-rpc-testnet.xitcoin.org \
  -H 'content-type: application/json' \
  --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}'
```

The target testnet result is `0x18ae1`, which is decimal `101089`.

{% hint style="info" %}
Public endpoints are shared infrastructure and may be rate-limited. Production applications should operate redundant RPC infrastructure.
{% endhint %}
