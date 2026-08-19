---
description: Supply, verified testnet accounting and denominations in the official Xitcoin Guide.
icon: scale-balanced
---

# Supply and denominations

## Mainnet supply boundary

The planned maximum supply for Xitcoin mainnet is **5,250,000,000 XTC**.

This mainnet ceiling must not be confused with the supply of a test network, a Cronos token representation or a planning allocation. The canonical mainnet genesis and its published checksum will remain the authoritative account-level record at launch.

## Verified Xitcoin Testnet accounting

The current candidate genesis for **Xitcoin Testnet** (`xitcoin-testnet-1`, EVM chain ID `101089`) contains a total testnet supply of **1,250,000,000 XTC**.

| Candidate testnet component | Verified quantity |
|---|---:|
| Total genesis supply | 1,250,000,000 XTC |
| Initial stake bonded by four core validators | 20,000,000 XTC |
| Remaining liquid genesis balances | 1,230,000,000 XTC |
| Initial stake per core validator | 5,000,000 XTC |

Atlas, Borealis, Meridian and Zenith each start with 5,000,000 XTC bonded in the candidate testnet. Their corresponding liquid account balances can therefore be zero while their validator stake remains active.

The five verified non-zero liquid genesis balances are **1,020,000,000 XTC**, **100,000,000 XTC**, **50,000,000 XTC**, **40,000,000 XTC** and **20,000,000 XTC**. These values describe the current testnet release only. They do not create mainnet ownership, sovereign admission, validator rights or a public distribution commitment.

Account labels and operational custody roles are published only after they are formally verified. The canonical candidate genesis remains the source of truth for addresses and exact atomic balances.

## Participation reference boundary

The **390,000,000 XTC sovereign reference reserve** described in the [participation framework](../governance/participation-framework.md) is a planning methodology, not proof of an executed transfer or a separately activated on-chain allocation.

Likewise, the model of **195 sovereign reference positions plus 63 public positions** defines participation capacity. It does not assign token balances automatically.

## Inflation

The current candidate genesis sets mint inflation to zero. This does not by itself describe every allocation, vesting condition or future governance decision.

## Units

| Unit | Amount |
|---|---:|
| 1 XTC | 10¹⁸ axtc |
| 0.1 XTC | 10¹⁷ axtc |
| 0.000001 XTC | 10¹² axtc |

Applications should perform integer arithmetic in `axtc` and only format XTC for display.

## Publication rule

Supply figures must always identify their network and status: verified testnet state, planned mainnet parameter, reference allocation or externally deployed token representation. Figures from those categories must not be added together or presented as interchangeable.
