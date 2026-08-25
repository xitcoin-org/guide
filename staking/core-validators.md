---
description: Core validators in the official Xitcoin Guide.
icon: server
---

# Core validators

The canonical Xitcoin Testnet genesis contains four KCALB Ltd core validators.

| Moniker | Role |
|---|---|
| Xitcoin Atlas | Core validator |
| Xitcoin Borealis | Core validator |
| Xitcoin Meridian | Core validator |
| Xitcoin Zenith | Core validator |

Each identity uses a distinct operator key, consensus key and node identity. Public operator addresses should be taken from the canonical genesis rather than copied from third-party lists.

## Genesis commission

The canonical Testnet genesis uses:

* commission rate: 10%;
* maximum commission rate: 20%;
* maximum daily commission-rate change: 1 percentage point.

These are genesis values, not a promise that a validator's current commission can never change. Confirm live chain data before delegating.
