---
description: Build Xitcoin in the official Xitcoin Guide.
icon: hammer
---

# Build Xitcoin

Use the canonical [pos-chain repository](https://github.com/xitcoin-org/pos-chain) and a documented release or commit.

```bash
git clone https://github.com/xitcoin-org/pos-chain.git
cd pos-chain/evmd
go build -o xitcoind ./cmd/evmd
./xitcoind version --long
```

Record the source commit, Go version, target architecture and binary SHA-256. Production operators should build reproducibly and test the binary before installation.
