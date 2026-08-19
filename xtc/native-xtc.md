---
description: Denominations and protocol functions of native XTC on the Xitcoin network.
icon: coins
---

# Native XTC

XTC is the protocol asset of the Xitcoin network. It is used by the execution, staking and governance layers.

## Protocol functions

* payment of transaction fees;
* validator self-delegation and delegated staking;
* economic security of proof-of-stake consensus;
* governance actions enabled by the active network;
* transfers and smart-contract interactions.

## Denominations

| User-facing symbol | Base denomination | Decimal precision |
|---|---|---:|
| XTC | `axtc` | 18 |

`1 XTC = 1,000,000,000,000,000,000 axtc`

Wallets, exchanges and applications should display XTC while using `axtc` for integer protocol amounts.

## Network distinction

Native XTC and the XTC token contract on Cronos are representations on different networks. They must be identified by chain ID and, on Cronos, by the complete contract address. The activation of a mainnet transfer mechanism will be announced separately with its verified contracts, accounting model and operating status.
