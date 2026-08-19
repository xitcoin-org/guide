---
description: Configure and start a node in the official Xitcoin Guide.
icon: gears
---

# Configure and start a node

1. Initialize a dedicated node home.
2. Install the validated genesis.
3. configure persistent peers for the intended network.
4. set the exact Cosmos chain ID.
5. restrict RPC and API listeners according to the node role.
6. start under a dedicated, unprivileged service account.

Do not expose validator RPC, consensus keys or administrative interfaces publicly. Use sentry architecture for public P2P access and verify peer IDs from official metadata.
