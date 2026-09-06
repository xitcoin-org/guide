---
description: Genesis and verification in the official Xitcoin Guide.
icon: file-shield
---

# Genesis and verification

Verify the deployed genesis file before starting a node:

```bash
printf '%s  %s\n' \
  '5db34acf6496b2c76a6f516e0eb605caef6762552584ddbed7c8703239f33d72' \
  '/path/to/genesis.json' | sha256sum -c -
xitcoind genesis validate-genesis /path/to/genesis.json
```

The deployed Xitcoin Public Testnet genesis has:

| Property | Canonical value |
|---|---|
| Cosmos Chain ID | `xitcoin-testnet-v2-1` |
| Supply | 477,000,000 XTC |
| SHA-256 | `5db34acf6496b2c76a6f516e0eb605caef6762552584ddbed7c8703239f33d72` |

Also query `https://rpc-testnet.xitcoin.org/status` and confirm that the live
network reports `xitcoin-testnet-v2-1`, advances in height and is not catching
up.

{% hint style="warning" %}
Confirm these values against the canonical
[Testnets repository](https://github.com/xitcoin-org/testnets), the
[PoS Chain repository](https://github.com/xitcoin-org/pos-chain) and the target
network before deployment. Never use the testnet genesis, node state or keys
for mainnet.
{% endhint %}
