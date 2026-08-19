---
description: Purpose, operating model and intended participants of the Xitcoin network.
icon: lightbulb
---

# Vision and purpose

Xitcoin is designed as a common, verifiable infrastructure layer for transactions, applications and coordinated digital services.

Its purpose is to let different categories of participants work through compatible network rules and interfaces without requiring them to become part of one central organization or adopt one proprietary application stack.

This is a design objective. It does not claim that a government, institution, bank, company or DeFi protocol already uses, operates or endorses Xitcoin.

## A shared compatibility layer

Public-sector participants, sovereign operators, companies, institutions, DeFi applications, communities and developers can require different governance, legal and application models. Xitcoin is intended to provide a shared technical language underneath those differences:

- one verifiable ledger for transactions and application state;
- one canonical native-XTC accounting model;
- Ethereum-compatible contracts, wallets and development tools;
- Cosmos-native staking, governance and protocol interfaces;
- common transaction finality and public verification;
- published validator-admission and operational controls;
- open RPC and integration standards for independently operated applications.

The shared layer does not replace each participant's legal authority, internal systems, regulatory duties or application governance.

## Cosmos and EVM interoperability

Xitcoin combines Cosmos SDK and CometBFT with native EVM execution.

| Interface | Function |
|---|---|
| Cosmos accounts and modules | Native transfers, staking, governance and protocol services |
| EVM accounts and contracts | Ethereum-compatible transactions and smart contracts |
| Shared consensus | Orders and finalizes both execution environments |
| Native XTC | Provides canonical fees, staking and application value accounting |
| Public APIs | Expose compatible data and transaction interfaces |

Cosmos and EVM activity belongs to the same sovereign chain and the same native-XTC economy. Native EVM compatibility does not create a second XTC supply.

Cross-network movement to Cronos is a separate bridge concern and must follow verified lock/mint and burn/unlock accounting before it is described as active.

## Intended use environments

### Public and sovereign infrastructure

The participation framework reserves sovereign reference capacity so eligible public-sector operators may be admitted under the same published technical and security standards. A reserved position is not endorsement, ownership, funding or active participation.

### Companies and institutions

Organizations can build settlement, record-keeping, membership, payment or coordination services using verifiable transactions and programmable rules while retaining responsibility for compliance, custody and user operations.

### DeFi and developers

Developers can use Solidity and Ethereum tooling or Cosmos-native interfaces. DeFi applications remain independently responsible for their contracts, economic design, security reviews and user disclosures.

### Individuals and communities

Users and communities can interact with applications, transfer XTC and delegate where those services are active and supported.

## Operating model

| Layer | Function |
|---|---|
| Consensus | Orders and finalizes blocks |
| Native asset | Pays fees and secures staking |
| EVM | Executes Ethereum-compatible contracts |
| Cosmos interfaces | Expose chain data and native modules |
| Applications | Deliver participant-specific services |
| Governance | Manages eligible protocol decisions |
| Validator admission | Controls entry to the validator process |
| Operations | Maintains infrastructure, keys, monitoring and recovery |

Staking power, validator admission, governance authority and infrastructure operations remain distinct. Holding XTC does not automatically create validator or administrative rights.

## Design principles

1. **Verifiability:** critical state and protocol decisions can be independently checked.
2. **Compatibility:** Cosmos and EVM interfaces reduce integration friction.
3. **Shared infrastructure, independent responsibility:** participants use common protocol rules while retaining their own obligations.
4. **Separation of authority:** staking, admission, governance and operations are documented independently.
5. **Controlled upgrades:** changes require an identifiable process, reviewable code and deployment records.
6. **Operational accountability:** releases include checksums, configuration references, monitoring and recovery procedures.
7. **Status accuracy:** intended or planned capabilities are never described as existing adoption or active services.

## Development sequence

XTC was first issued on Cronos. The project later developed its own proof-of-stake Layer 1, validated it through a public testnet and defined the controls required for a future mainnet. The complete sequence is recorded in [History and evolution](history-and-evolution.md).
