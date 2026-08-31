---
description: Explorers in the official Xitcoin Guide.
icon: magnifying-glass-chart
---

# Explorers

Xitcoin provides separate views for Cosmos-native and EVM activity.

* [Cosmos explorer](https://explorer-testnet.xitcoin.org/) — standard Ping
  Explorer for blocks, validators, staking, governance, Cosmos transactions and
  the isolated 10 XTC faucet extension.
* [EVM explorer](https://evm-explorer-testnet.xitcoin.org/) — EVM accounts,
  contracts, logs and transactions.

Explorers are indexing interfaces, not consensus authorities. For critical
verification, compare explorer data with RPC responses.

The Cosmos explorer source is published in the
[explorer-testnet repository](https://github.com/xitcoin-org/explorer-testnet).

Blockscout indexes blocks after they are produced. A moving lag of one or two
blocks can therefore be normal. Investigate when the lag persists, increases
across repeated measurements, or the explorer stops responding.
