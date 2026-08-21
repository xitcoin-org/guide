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

`690e18213298fc2ba282bbbf6b67b32f9c329f6d4d9bfead996336051724e7be`

{% hint style="warning" %}
Confirm this value against the release branch before deployment. Do not mix a genesis from one release with peers or documentation from another.
{% endhint %}
