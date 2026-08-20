---
description: Status of the validator participation framework and the controls required before mainnet.
icon: building-columns
---

# Participation framework

Xitcoin separates validator admission, institutional continuity, sovereign allocation and ordinary staking rewards. No reference position activates automatically.

## Target configuration

| Parameter | Target value | Status |
|---|---:|---|
| Initially approved validators | 4 | Atlas, Borealis, Meridian and Zenith |
| Maximum validator capacity | 258 | Protocol target |
| Reserved Member-State positions | 193 | Institutional capacity |
| General validator positions | 65 | Open validator capacity |
| Minimum self-delegation | 5,000,000 XTC | Same rule for every validator |
| Aggregate minimum at full capacity | 1,290,000,000 XTC | 258 × 5,000,000 XTC |
| Member-State allocation reserve | 386,000,000 XTC | Finite, separately accounted reserve |
| Automatic validator rights | None | Admission remains mandatory |

The minimum self-delegation is supplied by the validator. A sovereign allocation cannot be counted toward that minimum.

The 258-position capacity is conserved between categories. A governance-approved
increase in reserved Member-State positions reduces general validator positions
one-for-one; a decrease increases them one-for-one. Changing the total capacity
requires a separate on-chain governance decision. Registry changes must follow
an objective change in United Nations membership and cannot create supply,
rewrite vested allocations or reduce accrued rights.

## Sovereign institutional continuity

Each sovereign position remains attached to the relevant State rather than to an individual office-holder, administration or service provider.

Successive administrations of the same State may transfer the institutional governance and operating mandate to their authorized successors. This succession may update the responsible representatives, mandatary, operator and payment instructions without replacing the State position, its on-chain history or its remaining allocation.

An expired or revoked mandate suspends the relevant operational authority. It does not transfer the position to another State or to the former operator.

## Sovereign allocation

The fixed 386,000,000 XTC reserve uses the published 75% equal and 25% demographic methodology.

After a sovereign position has independently satisfied the five-million-XTC minimum and all admission requirements, its own five-year vesting schedule begins at that position's activation. A position may therefore join at any future date without changing a global distribution calendar.

The allocation accrues linearly through deterministic on-chain accounting during eligible service. No quarterly company transaction or recurring manual intervention is required. The authorized institutional controller may claim the amount accrued at any time.

The allocation:

- is additional to the State-provided self-delegation;
- is funded from the existing sovereign reserve;
- does not create new supply;
- is separate from ordinary validator rewards;
- pauses its future accrual when the position no longer satisfies the applicable institutional, staking or operational conditions;
- ends after the fixed allocation has been fully released.

Unreleased quantities remain in the sovereign reserve. Previously released quantities and every mandate transition remain subject to the final protocol, legal and custody controls.

## Ordinary validator rights

An activated sovereign validator participates under the same ordinary network rules as other validators. It may receive rewards attributable to its own stake and validator commission on delegations, subject to availability, commission, distribution and slashing rules.

After the five-year sovereign allocation has ended, the position receives no new sovereign allocation. It may continue validating and earning ordinary network rewards while it remains eligible.

## Equal technical standard

Founder, sovereign and public validators must satisfy the same minimum self-delegation and the same consensus, uptime, monitoring, incident-response and slashing requirements.

A reserved institutional designation cannot bypass protocol security controls. The 65 general validator positions remain part of the target capacity to preserve independent and community participation.

## Implementation boundary

The framework remains a target policy until the position registry, institutional succession, mandate controls, activation-based vesting accounting and five-million-XTC admission rule have been implemented, tested, independently reviewed and activated through the required network process.

The canonical allocation calculations and technical specification are maintained in the [Xitcoin PoS Chain repository](https://github.com/xitcoin-org/pos-chain).
