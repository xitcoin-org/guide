---
description: Deterministic sovereign reference methodology, examples and participation pathway.
icon: globe
---

# Sovereign participation reference

Xitcoin maintains a deterministic reference framework for potential sovereign participation. It provides a common technical method without granting ownership, validator status, diplomatic recognition or automatic access.

## Reference set

The framework contains **195 sovereign reference positions**:

- 193 United Nations Member States;
- the Holy See;
- the State of Palestine.

The reference set follows published United Nations identifiers for deterministic technical and statistical processing. It is not an independent statement on sovereignty, borders or diplomatic recognition.

## Fixed reference envelope

The methodology uses a fixed reference envelope of **390,000,000 XTC**:

| Component | Quantity | Weight |
|---|---:|---:|
| Equal component | 292,500,000 XTC | 75% |
| Demographic component | 97,500,000 XTC | 25% |
| Total | 390,000,000 XTC | 100% |

The equal component gives every reference position a base of **1,500,000 XTC**.

## Formula

For reference position (i):

[
A_i =
390{,}000{,}000
left(
rac{0.75}{195}
+
0.25
rac{sqrt{P_i}}{sum_{j=1}^{195}sqrt{P_j}}
ight)
]

Where:

- (A_i) is the reference quantity for position (i);
- (P_i) is its consolidated population reference for 1 July 2026;
- every position receives the same 1,500,000 XTC base;
- the remaining 97,500,000 XTC is weighted by the square root of population.

Square-root weighting recognizes population differences while deliberately reducing extreme concentration. A population four times larger produces twice the demographic weight, not four times the weight.

## Illustrative verified records

| Reference position | Consolidated population | Reference quantity |
|---|---:|---:|
| India | 1,476,625,576 | 5,981,595.563833188491971101 XTC |
| China | 1,444,027,171 | 5,931,851.000531210577457723 XTC |
| United States of America | 352,600,000 | 3,689,972.303553360381771638 XTC |
| France | 69,642,313 | 2,473,271.624383873506214429 XTC |
| State of Palestine | 5,692,790 | 1,778,265.939104903811270821 XTC |
| Holy See | 506 | 1,502,623.449609571928600114 XTC |

These are deterministic reference results, not transferred balances or offers of ownership.

## Population source and fixed date

Population values use the United Nations World Population Prospects 2024 medium variant for **1 July 2026**.

The source file is pinned by SHA-256:

`98e34d9b65b53858cd08a57a566e45050b08093ad85ba5714fe6fbd78055ae6d`

Using a fixed source, date and checksum prevents later discretionary changes to the calculation.

## Statistical consolidation

The allocation index contains 39 statistical consolidations. They contribute population data to an existing reference position and do not create extra positions.

Following the United Nations M49 statistical framework used by the dataset, the China calculation consolidates:

- China;
- China Hong Kong SAR;
- China Macao SAR;
- China Taiwan Province of China.

This is a statistical processing rule inherited from the cited dataset. It is not a separate Xitcoin political or diplomatic determination.

Cook Islands, Niue and Western Sahara remain non-consolidated statistical records. They do not create positions and are not added to another position.

## Deterministic rounding

Calculations use decimal arithmetic at 18-decimal precision. Atomic-unit remainders are assigned by descending fractional remainder, with ISO3 code as the deterministic tie-breaker.

The final aggregate is exactly:

**390,000,000.000000000000000000 XTC**

## How a sovereign participant can initiate review

A relevant public authority or its formally authorized representative can initiate contact through the [official Xitcoin channels](../start/official-links.md).

The review pathway is:

1. identify the relevant authority and authorized representative;
2. verify mandate and official contact provenance;
3. define the proposed operator and infrastructure responsibility;
4. complete legal, security, custody and technical review;
5. determine whether and how the reference quantity may be reserved, vested, delegated or used for operational support;
6. confirm the operator satisfies the validator minimum and operational requirements;
7. execute explicit on-chain approval through the canonical admission authority;
8. publish the resulting authorization and transaction evidence where appropriate.

No position activates automatically. A reference quantity does not replace the validator's minimum self-delegation requirement unless a separately approved and documented mechanism explicitly provides otherwise.

## Current boundary

Only Atlas, Borealis, Meridian and Zenith are currently approved validators. No sovereign reference position is currently described as activated by this methodology.

The complete calculation and verification sources are maintained in the Xitcoin blockchain repository:

- `docs/sovereign-allocation-2026.md`;
- `networks/testnet/sovereign-allocation-index-2026.csv`;
- `networks/testnet/sovereign-allocation-index-2026.json`;
- `networks/testnet/territorial-consolidation-2026.csv`;
- `scripts/verify-sovereign-allocation-2026.py`.
