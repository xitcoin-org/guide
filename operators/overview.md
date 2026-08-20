---
description: Operator overview in the official Xitcoin Guide.
icon: rectangle-server
---

# Operator overview

A Xitcoin node runs the official `xitcoind` binary and maintains local blockchain state.

## Node types

* **Full node:** verifies and serves chain data.
* **Sentry:** exposes controlled P2P or API access while shielding validators.
* **Validator:** signs consensus blocks and requires on-chain admission.

Running a full node does not automatically make it a validator. Start with the canonical source, verify the genesis checksum and keep operator and consensus keys separated.
