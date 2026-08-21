---
description: A clear introduction to Xitcoin, XTC and the network being built around them.
icon: circle-info
---

# What is Xitcoin?

Xitcoin is an evolving digital ecosystem built around XTC.

It began with XTC as a token on Cronos and is developing into a dedicated network where XTC becomes the native asset used for transactions, staking, security and application activity.

The goal is broader than creating another blockchain. Xitcoin is intended to provide a common, verifiable infrastructure connecting everyday digital activity, institutions, communities and decentralized applications.

## From an asset to an ecosystem

The project has progressed through several connected phases:

1. **XTC on Cronos** established the public asset and its first ecosystem.
2. **Contract migration** moved legacy XTC into an upgraded, verifiable contract architecture.
3. **Native-chain development** introduced independent consensus, validators and native XTC.
4. **Public testnet operation** validates the protocol and infrastructure.
5. **Mainnet preparation** aligns code, economics, governance, bridge continuity and public services.

Each phase is documented separately so users can understand what changed without confusing a token-contract migration, a canonical testnet release and a cross-network bridge.

## What the network provides

| Capability | What it means |
|---|---|
| Native XTC | One network asset for fees, staking and applications |
| Proof-of-stake consensus | Independent validators verify blocks and secure the chain |
| Ethereum compatibility | Existing EVM wallets, Solidity contracts and developer tools can connect |
| Cosmos infrastructure | Native staking, governance, APIs and interoperability components |
| Public verification | Source code, configuration, checksums and chain state can be inspected |
| Shared communication layer | Different applications and participants can coordinate through common rules |

## Who can use Xitcoin?

### Individuals and communities

Users can interact with applications, transfer XTC and participate in staking where supported.

### Businesses, financial services and institutions

Organizations can build services using verifiable transactions, programmable rules and shared public infrastructure.

The network is designed to support payment, transfer, settlement, treasury and accounting integrations. Delegated proof-of-stake provides finalized network state, while the EVM provides programmable accounting and compatibility with existing Ethereum development tools.

Banks, payment providers, remittance specialists, fintech companies and other regulated institutions can develop or connect their own services through published interfaces while retaining responsibility for licensing, compliance, custody, risk controls and customer operations.

### Developers

Builders can use Ethereum-compatible tooling or Cosmos-native APIs instead of learning an entirely proprietary platform.

### Validators and infrastructure operators

Professional operators can run nodes, provide public services and participate in consensus under the network's admission and staking policies.

### Jurisdictions and public-sector participants

The long-term design can support independent institutional or sovereign infrastructure connected through the same protocol, without making every participant part of one central organization.

## Technical foundation

Only after the purpose is understood does the technical architecture matter:

| Layer | Technology | Responsibility |
|---|---|---|
| Consensus | CometBFT | Agreement, finality and block production |
| Application | Cosmos SDK | Accounts, staking, governance and protocol modules |
| Smart contracts | Cosmos EVM | Ethereum-compatible execution and JSON-RPC |
| Native asset | XTC / `axtc` | Fees, staking and network participation |
| Public services | RPC, APIs, explorers and faucet | User and developer access |

## Current phase

Mainnet has not launched. Xitcoin Testnet is active as a four-validator canonical staging network using Cosmos chain ID `xitcoin-testnet-1` and EVM chain ID `101089`. Public endpoint cutover and transaction acceptance remain release gates.

Continue with [Vision and purpose](vision-and-purpose.md), [History and evolution](history-and-evolution.md) or [Mainnet readiness](mainnet-readiness.md).
