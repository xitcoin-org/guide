---
description: Status of the proposed validator participation framework and the controls required before mainnet.
icon: building-columns
---

# Participation framework

This page records the design under evaluation for mainnet validator participation. It does not grant a validator seat, a sovereign allocation or an economic entitlement.

## Design objectives

The framework is intended to support public, institutional and sovereign operators under one published technical standard. Admission, staking power and governance authority remain distinct.

## Current planning record

| Parameter | Planning value | Status |
|---|---:|---|
| Initial approved validators | 4 | Testnet implementation |
| Maximum validator capacity | 258 | Candidate network parameter |
| Sovereign reference positions | 195 | Deterministic planning index; not automatic admission |
| Public positions | 63 | Reserved participation capacity; not automatic admission |
| Protocol minimum self-delegation | 1,000,000 XTC | Candidate network parameter |
| Initial self-delegation per core validator | 5,000,000 XTC | Atlas, Borealis, Meridian and Zenith |
| Sovereign reference reserve | 390,000,000 XTC | Treasury planning; not an active transfer |
| Automatic validator rights | None | Enforced design objective |

The 258-position model is the sum of 195 sovereign reference positions and 63 public positions.

The sovereign reference set contains 193 United Nations Member States, the Holy See and the State of Palestine. The 39 territorial consolidations recorded in the allocation dataset are statistical population mappings, not additional validator positions.

## Allocation boundary

The 390 million XTC reference reserve and validator admission are separate controls.

The deterministic index records a reference methodology:

- 292,500,000 XTC equal component, representing 75%;
- 97,500,000 XTC demographic component, representing 25%;
- square-root population weighting for the demographic component;
- exact aggregate of 390,000,000 XTC.

The index does not itself transfer tokens, approve an operator, activate a validator or create sovereign ownership.

Before mainnet, the published policy must define:

- whether any reserve funds ownership, delegation, incentives or operating support;
- custody, vesting and release controls;
- how operators are approved, suspended and removed;
- how stake concentration is monitored;
- whether delegated public stake can change validator power;
- conflict-of-interest and disclosure requirements;
- the final on-chain authority and governance process.

## Admission and governance

Every validator requires explicit on-chain approval. Holding or staking XTC does not create an automatic validator right.

Admission, revocation and parameter updates must remain visible in blockchain state. The production authority and its multisignature custody procedures must be verified and published before mainnet.

## Equal technical standard

Every active validator must satisfy the same consensus, key-management, uptime, monitoring and incident-response requirements. A sovereign, institutional or public designation must not bypass protocol security controls.

## Publication rule

Only deployed on-chain parameters and formally approved allocations should be described as active. Draft allocations remain labeled **proposed** until the corresponding governance record, addresses and transactions are public.
