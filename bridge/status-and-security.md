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

Repository review on 5 September 2026 distinguishes the following stages:

| Component | Status | Evidence |
|---|---|---|
| Destination manifest checks and startup boundary | Implemented and merged; both destinations fail closed | [Relayer PR #38](https://github.com/xitcoin-org/bridge-relayer/pull/38) |
| Phase-one relayer validation | 113 automated tests passed, with no production dependency advisories reported by npm at review time | [Merged validation record](https://github.com/xitcoin-org/bridge-relayer/pull/38) |
| Coordinator | Approval-only; no destination submission in its runtime | [Coordinator source](https://github.com/xitcoin-org/bridge-relayer/blob/aee181bf465d4dbd6a49a760f7be98be2d9a49b0/src/coordinator-bootstrap.js) |
| Destination adapter prerequisites | Merged as `9fe70ca`; offline journal and replay-schema prerequisites only; no operational submission | [Relayer PR #39](https://github.com/xitcoin-org/bridge-relayer/pull/39) |
| Testnet bridge transfers | Not activated; destination startup remains disabled | [Submitter scope](https://github.com/xitcoin-org/bridge-relayer/blob/9fe70ca158feb18d27765472e45a8936fbc0b1c4/docs/ADAPTERS.md) |
| Mainnet bridge | Future work, subject to separate review and activation | [Mainnet readiness](../start/mainnet-readiness.md) |

The testnet route connects **Cronos testnet (chain ID 338)** and **Xitcoin
Public Testnet (Cosmos chain ID `xitcoin-testnet-v2-1`, EVM chain ID `101089`)**.
This development route must not be confused with the existing Cronos token.
No successful bridge transfer or live destination submission is claimed here.

The chain source includes an attestation message and a replay-status query.
A processed replay flag alone does not prove a matching transaction or finality.
Automated source and fixture tests are engineering evidence, not activation,
independent security certification or proof of current service availability.

## Status terms

**Implemented** means source exists. **Tested offline** means the recorded
checks used local fixtures. **Tested on testnet** requires transaction and
finality evidence from that network. **Deployed but inactive** means an
identified release exists without enabled operation. **Active** requires
current operational evidence. **Planned** is future work; **blocked** identifies
a missing prerequisite. These stages are not interchangeable.

The remaining adapter work includes signed-transaction encoding and custody,
account sequence or nonce ownership, fee bounds, bounded network responses,
approval revalidation, canonical receipt and finality verification, and atomic
recovery with RelayStore. The Xitcoin replay flag cannot establish completion
or authorize a resend after an ambiguous outcome. See the
[exact activation blockers](https://github.com/xitcoin-org/bridge-relayer/blob/9fe70ca158feb18d27765472e45a8936fbc0b1c4/docs/ADAPTERS.md#remaining-activation-blockers).

## Checks after a separately announced activation

* start from the official [Xitcoin Guide](https://xitcoin.gitbook.io/guide/);
* verify the source and destination networks;
* verify complete contract addresses;
* test with a small amount;
* wait for the required confirmations;
* retain transaction hashes for both networks.

Report suspicious bridge links through the security process.
