---
description: Genesis and verification in the official Xitcoin Guide.
icon: file-shield
---

# Genesis and verification

Download `genesis.json` and its checksum from the same validated network release.

```bash
sha256sum -c genesis.sha256
xitcoind genesis validate-genesis genesis.json
```

The canonical Xitcoin Testnet genesis has SHA-256:

`7d13d7ed6a19ea48e2ce3c408f1f457e0961e72df6dd480d8200a6db5bae8414`

The verified Linux AMD64 testnet release deployed on 22 August 2026 was built
from source revision
`2aa39b8c2ce7ac06278d58f2970225fd450e2c2c`. Its `xitcoind` binary has
SHA-256:

`1958ca411353e79d3ff62a262960378141afb0343ab22689a759dffc610a9ecc`

{% hint style="warning" %}
Confirm these values against the canonical
[PoS Chain repository](https://github.com/xitcoin-org/pos-chain) and the target
network before deployment. Never use the testnet genesis, node state or keys
for mainnet.
{% endhint %}
