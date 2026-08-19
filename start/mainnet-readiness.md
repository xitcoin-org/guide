---
description: The public readiness framework that must be completed before the Xitcoin mainnet launches.
icon: flag-checkered
---

# Mainnet readiness

{% hint style="warning" %}
Xitcoin mainnet has not launched. This page describes the readiness framework and must not be interpreted as a launch announcement.
{% endhint %}

The public testnet validates the software and operating model that will support mainnet. Mainnet documentation is prepared in parallel so the launch does not rely on last-minute, inconsistent instructions.

## Readiness areas

### Protocol

* deterministic genesis and independently verified checksum;
* final Cosmos and EVM chain identifiers;
* finalized staking, governance and validator-admission parameters;
* validated supply and allocation invariants;
* reproducible Linux builds and signed release artifacts.

### Validator network

* independent operator and consensus identities;
* tested recovery without double-signing;
* sentry topology and restricted validator exposure;
* monitoring, alerting and coordinated upgrade procedures;
* continuity plan that avoids simultaneous validator shutdown.

### Public infrastructure

* redundant Cosmos RPC, REST, gRPC and EVM JSON-RPC;
* synchronized Cosmos and EVM explorers;
* indexed chain data and health monitoring;
* wallet and chain-registry metadata;
* documented rate limits and service status.

### XTC continuity

* public explanation of Cronos XTC and native XTC;
* final bridge contracts and accounting model;
* audited lock, mint, burn and unlock paths;
* user-facing migration or bridge instructions;
* reconciliation between represented and locked supply.

### Governance and admission

* final authority model;
* published validator criteria and review process;
* clear separation between sovereign, institutional and public participation;
* emergency, upgrade and parameter-change procedures;
* no unpublished automatic validator rights.

### Security and communication

* responsible-disclosure channel;
* dependency and contract review;
* incident-response and pause procedures;
* canonical documentation and official domains;
* launch communication that distinguishes testnet, mainnet and Cronos.

## Launch gate

Mainnet should be announced only when the code, public guide, live infrastructure and on-chain configuration agree. A percentage or internal milestone is not a launch condition by itself.
