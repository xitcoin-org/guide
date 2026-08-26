---
description: Supply and denominations in the official Xitcoin Guide.
icon: scale-balanced
---

# Supply and denominations

## Maximum supply

The protocol configuration defines a maximum supply ceiling of
**5,250,000,000 XTC**. This ceiling is not the current testnet genesis supply.

The deployed Xitcoin Testnet genesis supply is **457,000,000 XTC**. Its exact
account-level allocation is published in the canonical
[Testnets repository](https://github.com/xitcoin-org/testnets).

## Inflation

The current testnet genesis configuration sets mint inflation to zero. The
faucet does not mint automatically; it spends from its 50,000,000 XTC genesis
allocation.

## Units

| Unit | Amount |
|---|---:|
| 1 XTC | 10¹⁸ axtc |
| 0.1 XTC | 10¹⁷ axtc |
| 0.000001 XTC | 10¹² axtc |

Applications should perform integer arithmetic in `axtc` and only format XTC
for display.

## Multichain supply invariant

The 5,250,000,000 XTC figure is a global economic reference ceiling, not an
amount that may be recreated independently on every connected network.

At all times:

```
Cronos $XTC outside bridge escrow
+ active bridge-minted and fully backed XTC on Xitcoin
+ any future authorized external representation
≤ effective global XTC ceiling
```

Xitcoin POS and Xitcoin EVM share the same native XTC economy and must not be
counted as separate supplies.

A bridge-authorized mint is permitted only when the same amount of canonical
`$XTC` has been finalized and locked on Cronos. It does not authorize an
unbacked supply increase. The Validator Incentive Treasury and ordinary
applications have no mint authority.

The current testnet bridge route is not configured and is disabled. No separate
active bridge allocation exists in the deployed testnet genesis.

## Burn accounting

A permanent burn of canonical `$XTC` on Cronos reduces the effective global
XTC ceiling. The corresponding unused bridge capacity on Xitcoin must be
reduced by the same amount.

Burning bridge-minted XTC on Xitcoin in order to unlock the same XTC on Cronos
is a transfer between representations, not an economic supply reduction.

Canonical `$XTC` locked as backing for an active Xitcoin representation must
not be permanently burned unless the corresponding Xitcoin amount is retired
first. Every permanent burn requires a public supply-reconciliation record.
