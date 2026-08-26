---
description: Get test XTC in the official Xitcoin Guide.
icon: faucet-drip
---

# Get test XTC

Use the [official Xitcoin testnet faucet](https://faucet-testnet.xitcoin.org/)
to request test XTC.

## Deployed policy

| Property | Value |
|---|---:|
| Amount per accepted request | 10 XTC |
| Address cooldown | 24 hours |
| IP window | 24 hours |
| Accepted requests per IP per window | 3 |
| Genesis faucet allocation | 50,000,000 XTC |
| Automatic minting | Disabled |

The IP limit means that, during any 24-hour window, no more than three accepted
requests may originate from the same public IP address. The address cooldown is
checked separately.

1. Connect or enter a testnet address.
2. Confirm the address belongs to the Xitcoin testnet workflow.
3. Submit the request.
4. Verify receipt in the appropriate explorer.

The faucet spends from its finite genesis allocation; it does not create new
XTC. If that balance becomes low, an explicitly approved on-chain transfer from
an authorized testnet reserve can refill it without resetting the chain or
changing genesis.

Testnet XTC is free testing material and has no monetary value. Do not purchase
it and do not send real assets in exchange for it.
