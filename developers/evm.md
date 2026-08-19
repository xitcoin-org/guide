---
description: EVM development in the official Xitcoin Guide.
icon: ethereum
---

# EVM development

Point Ethereum-compatible tooling at:

`https://evm-rpc-testnet.xitcoin.org`

## Example chain-ID request

```json
{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}
```

The target response is `0x18ae1`. Use XTC as the native gas asset. Standard Solidity, ABI and event-log workflows apply, subject to the capabilities and limits of the deployed Xitcoin release.
