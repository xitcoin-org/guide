---
description: Genesis and verification in the official Xitcoin Guide.
icon: file-shield
---

# Genesis and verification

Clone the canonical network repository and verify the checksum:

```bash
git clone https://github.com/xitcoin-org/testnets.git
cd testnets/xitcoin-testnet-1
sha256sum -c genesis.sha256
xitcoind genesis validate-genesis genesis.json
```

The deployed Xitcoin Testnet genesis has:

| Property | Canonical value |
|---|---|
| Cosmos Chain ID | `xitcoin-testnet-1` |
| Genesis time | `2026-08-25T21:48:17.77229Z` |
| Supply | 457,000,000 XTC |
| SHA-256 | `55c8756a212b9e92c0e8427ea61caff7fa9dca40e801e4b848f59d1aa5f6dae6` |

The current public repository no longer resolves the historical source
revision, binary checksum and Actions run that were previously listed here.
They are therefore not presented as independently verifiable provenance.
Future releases must publish a reachable source revision and reproducible
binary checksums.

{% hint style="warning" %}
Confirm these values against the canonical
[Testnets repository](https://github.com/xitcoin-org/testnets), the
[PoS Chain repository](https://github.com/xitcoin-org/pos-chain) and the target
network before deployment. Never use the testnet genesis, node state or keys
for mainnet.
{% endhint %}
