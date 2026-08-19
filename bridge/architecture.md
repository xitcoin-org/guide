---
description: Planned accounting and security architecture connecting Cronos XTC and native XTC on Xitcoin.
icon: bridge
---

# Bridge architecture

The planned canonical bridge connects the canonical Cronos XTC contract with native XTC on the Xitcoin network.

It provides continuity between two networks. The user experience remains centered on XTC, while the bridge accounts for how value is locked, represented and returned.

## Cronos to Xitcoin: lock and backed release

1. A user deposits canonical Cronos XTC into the approved bridge contract.
2. The Cronos-side contract locks the deposited amount.
3. Relayers observe the event and wait for the required finality.
4. The Xitcoin-side bridge verifies the authorized message and replay protection.
5. The corresponding native XTC amount is minted to the destination address.
6. Public accounting records the relationship between Cronos XTC locked and native XTC released or bridge-authorized on Xitcoin.

## Xitcoin to Cronos: representation retirement and unlock

1. A user submits native XTC to the Xitcoin-side bridge.
2. The corresponding bridge-authorized representation is retired on Xitcoin.
3. Relayers observe finality and submit the authorized message to Cronos.
4. The Cronos bridge releases the corresponding locked XTC.
5. Transaction identifiers on both networks provide an auditable trail.

## Application revenue pathway

The representation retirement used for a bridge return is an accounting operation: it moves value back to Cronos and does not reduce the global economic supply.

A permanent burn of canonical XTC on Cronos is different. It reduces the effective global XTC ceiling and must be recorded in a public burn ledger. The corresponding unused Xitcoin bridge capacity must be reduced by the same amount. Cronos XTC backing an active Xitcoin representation must never be permanently burned unless the corresponding Xitcoin amount is retired first.

Buyback XTC must have one exclusive destination: reward funding, bridge backing or permanent burn. The same XTC cannot be counted in more than one destination.

The bridge may also support verified transfers from application-funded buyback and revenue-sharing mechanisms.

```mermaid
flowchart LR
    A["Application revenue"] --> B["XTC buyback"]
    B --> C["Bridge Escrow Vault"]
    C --> D["Backed XTC on Xitcoin"]
    D --> E["Validator Incentive Treasury"]
```

This pathway does not grant applications or relayers a mint authority. Every amount made available on Xitcoin must remain covered by canonical XTC locked on Cronos.

The full planned reward loop, distribution ceilings and security boundary are documented under [Validator incentives and revenue flywheel](../staking/validator-incentives.md).

## User experience

A public bridge interface should make five facts explicit before confirmation:

* source network;
* destination network;
* amount and fees;
* destination address;
* expected confirmation state.

Users should not need to understand internal supply representations to use the bridge safely. Technical accounting remains documented for auditors, integrators and operators.

## Required invariants

At all times, the system must preserve measurable relationships between:

* XTC locked on Cronos;
* bridge-authorized native XTC issued on Xitcoin;
* native XTC removed from circulation for return;
* XTC unlocked back on Cronos.

Bridge administration must not provide an unrestricted public issuance path. The canonical Cronos token must not receive new mint authority for bridge operation.

## Security controls

* explicit chain and contract allowlists;
* finality thresholds on both networks;
* message uniqueness and replay protection;
* amount and rate limits;
* emergency pause with auditable authority;
* monitored relayer quorum;
* contract and relayer version control;
* reconciliation alerts;
* tested recovery and incident procedures.

{% hint style="warning" %}
This is the planned architecture. The bridge is not presented as active until contracts, relayers, accounting and public interfaces have passed final validation.
{% endhint %}
