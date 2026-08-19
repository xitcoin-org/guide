---
description: Supply and denominations in the official Xitcoin Guide.
icon: scale-balanced
---

# Supply and denominations

## Maximum supply

The network configuration defines a maximum supply of **5,250,000,000 XTC**.

## Inflation

The current genesis configuration sets mint inflation to zero. This does not by itself describe every allocation, vesting condition or future governance decision; use the canonical genesis for exact account-level state.

## Units

| Unit | Amount |
|---|---:|
| 1 XTC | 10¹⁸ axtc |
| 0.1 XTC | 10¹⁷ axtc |
| 0.000001 XTC | 10¹² axtc |

Applications should perform integer arithmetic in `axtc` and only format XTC for display.
