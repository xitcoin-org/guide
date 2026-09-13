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

## EVM statistics

As observed on 13 September 2026, the EVM explorer uses backend **11.2.8**
and serves Stats through its own HTTPS origin at `/stats-service/`.
The main page shows total blocks, total transactions and daily new transactions.
These are counts: daily transaction values use **Tx/day**, not XTC.

The home-page chart covers 30 completed days. Today's incomplete total is
separate from that window. Backend counters, Stats calculations and browser
refreshes run periodically, around 60 seconds; their timestamps can differ.
A short delay in a counter does not by itself mean the chain has stopped.

The existing 0.01 XTC native transfer remains a currency amount with 18 decimals.
This update does not change network identity or enable a bridge.

Operators can consult the [deployment and recovery notes](https://github.com/xitcoin-org/explorer-evm-testnet/blob/d33eb171032137008299bf00b63db63efb4bdc2e/docs/DEPLOYMENT.md).
