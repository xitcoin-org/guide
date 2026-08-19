---
description: Purpose, operating model and intended participants of the Xitcoin network.
icon: lightbulb
---

# Vision and purpose

Xitcoin is a digital infrastructure project for recording transactions, executing applications and coordinating services across public, commercial and institutional environments.

## Purpose

The network is designed to provide:

* one verifiable ledger for transactions and application state;
* a native asset for fees, staking and protocol participation;
* Ethereum-compatible smart-contract execution;
* Cosmos RPC, REST and gRPC interfaces;
* independent validation through proof-of-stake consensus;
* published governance and validator-admission controls.

## Operating model

Participants retain their own legal, operational and application responsibilities. Interoperability is provided through common network protocols, transaction formats and public interfaces.

| Layer | Function |
|---|---|
| Consensus | Orders and finalizes blocks |
| Native asset | Pays fees and secures staking |
| EVM | Executes Ethereum-compatible contracts |
| Cosmos interfaces | Expose chain data and native modules |
| Applications | Deliver user-specific services |
| Governance | Manages eligible protocol decisions |
| Validator admission | Controls entry to the validator process |

## Intended participants

The protocol can support individuals, developers, businesses, infrastructure operators, institutions and public-sector entities. Participation in the network does not automatically create validator, governance or administrative rights.

## Relationship to everyday services and DeFi

Applications can connect conventional service workflows to verifiable on-chain actions. Examples include payments, membership systems, rewards, settlement records, asset transfers and decentralized-finance applications.

Xitcoin provides the execution and verification layer. Application operators remain responsible for user experience, regulatory obligations, data protection and service-specific controls.

## Design principles

1. **Verifiability:** critical state and protocol decisions can be independently checked.
2. **Compatibility:** EVM and Cosmos interfaces reduce integration friction.
3. **Separation of authority:** staking power, validator admission, governance and operations are documented independently.
4. **Controlled upgrades:** changes require an identifiable process, reviewable code and deployment records.
5. **Operational accountability:** releases include checksums, configuration references, monitoring and recovery procedures.
6. **Status accuracy:** planned capabilities are not described as active services.

## Development sequence

XTC was first issued on Cronos. The project later developed its own proof-of-stake Layer 1, validated it through a public testnet and defined the controls required for a future mainnet. The complete sequence is recorded in [History and evolution](history-and-evolution.md).
