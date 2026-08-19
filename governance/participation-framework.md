---
description: Status of the validator participation framework and the controls required before mainnet.
icon: building-columns
---

# Participation framework

This page records the current validator-participation design. It does not grant a validator seat, a sovereign allocation or an economic entitlement.

## Current planning record

| Parameter | Current value | Status |
|---|---:|---|
| Initially approved validators | 4 | Atlas, Borealis, Meridian and Zenith |
| Additional validators announced | 0 | Every future validator requires separate approval |
| Maximum validator capacity | 258 | Candidate network parameter |
| Sovereign reference positions | 195 | Planning capacity; not automatic admission |
| Public positions | 63 | Future capacity; not active validators |
| Protocol minimum self-delegation | 1,000,000 XTC | Candidate network parameter |
| Initial self-delegation per core validator | 5,000,000 XTC | Current release candidate |
| Sovereign reference reserve | 390,000,000 XTC | Planning reference; not an active transfer |
| Automatic validator rights | None | Enforced admission boundary |

The 258-position model is the sum of 195 sovereign reference positions and 63 public positions. It does not announce 258 validators and does not commit the network to filling those positions.

The sovereign reference set contains 193 United Nations Member States, the Holy See and the State of Palestine. The 39 territorial consolidations in the allocation dataset are statistical population mappings, not additional validator positions.

## Allocation boundary

The 390 million XTC reference methodology and validator admission are separate controls:

- 292,500,000 XTC equal component, representing 75%;
- 97,500,000 XTC demographic component, representing 25%;
- square-root population weighting for the demographic component;
- exact aggregate of 390,000,000 XTC.

The index does not transfer tokens, approve an operator, activate a validator or create ownership by itself.

The exact formula, verified examples, United Nations statistical mappings, deterministic rounding rule and sovereign review pathway are published in [Sovereign participation reference](sovereign-participation-reference.md).

## Admission and decision authority

Every validator requires explicit approval by the canonical on-chain validator-admission authority. During the current launch phase, that authority is controlled through the project's authorized custody process.

Holding, staking or delegating XTC does not create an admission right. Token-weighted voting does not approve, revoke or replace a validator and does not override the admission authority.

Any future expansion beyond the four initially approved validators must be assessed and authorized individually. The 63 public positions are capacity only; they are not a list of planned operators.

Approval, revocation and parameter actions must remain visible in blockchain state. Production custody, recovery and signer-change procedures must be verified before mainnet.

## Equal technical standard

Every active validator must satisfy the same consensus, key-management, uptime, monitoring and incident-response requirements. A sovereign, institutional or public designation cannot bypass protocol security controls.

## Publication rule

Only deployed parameters and formally authorized allocations should be described as active. Planning records remain labeled as such until the relevant addresses, authority action and transaction evidence are public.
