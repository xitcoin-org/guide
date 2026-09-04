---
description: Bridge status and security in the official Xitcoin Guide.
icon: shield-check
---

# Bridge status and security

{% hint style="danger" %}
**The canonical Xitcoin bridge is not currently presented as active.** Do not send funds to an address or application claiming to provide the official bridge unless activation is announced through verified Xitcoin channels.
{% endhint %}

Before activation, the project must verify contracts, relayer configuration, monitoring, recovery, rate limits and end-to-end accounting.

## Implementation and activation status

Repository review on 4 September 2026 distinguishes the following stages:

| Component | Status | Evidence |
|---|---|---|
| Destination manifest checks and startup boundary | Implemented and merged; both destinations fail closed | [Relayer PR #38](https://github.com/xitcoin-org/bridge-relayer/pull/38) |
| Phase-one relayer validation | 113 automated tests passed, with a zero-vulnerability production dependency audit at review time | [Merged validation record](https://github.com/xitcoin-org/bridge-relayer/pull/38) |
| Coordinator | Approval-only; no destination submission in its runtime | [Coordinator source](https://github.com/xitcoin-org/bridge-relayer/blob/aee181bf465d4dbd6a49a760f7be98be2d9a49b0/src/coordinator-bootstrap.js) |
| Destination adapter prerequisites | Under development in an unmerged PR; offline tests do not establish operational readiness | [Relayer PR #39](https://github.com/xitcoin-org/bridge-relayer/pull/39) |
| Testnet bridge transfers | Not activated; destination startup remains disabled | [Submitter scope](https://github.com/xitcoin-org/bridge-relayer/blob/aee181bf465d4dbd6a49a760f7be98be2d9a49b0/docs/SUBMITTERS.md) |
| Mainnet bridge | Future work, subject to separate review and activation | [Mainnet readiness](../start/mainnet-readiness.md) |

The testnet route connects **Cronos testnet (chain ID 338)** and **Xitcoin
Public Testnet (Cosmos chain ID `xitcoin-testnet-v2-1`, EVM chain ID `101089`)**.
This development route must not be confused with the existing Cronos token.
No successful bridge transfer or live destination submission is claimed here.

The chain source includes an attestation message and a replay-status query.
A processed replay flag alone does not prove a matching transaction or finality.
Automated source and fixture tests are engineering evidence, not activation,
independent security certification or proof of current service availability.

## Checks after a separately announced activation

* start from the official [Xitcoin Guide](https://xitcoin.gitbook.io/guide/);
* verify the source and destination networks;
* verify complete contract addresses;
* test with a small amount;
* wait for the required confirmations;
* retain transaction hashes for both networks.

Report suspicious bridge links through the security process.
