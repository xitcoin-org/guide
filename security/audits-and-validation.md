---
description: Independent XTC contract review, Cyberscope KYC, Xitcoin Layer 1 validation and release evidence.
icon: shield-check
---

# Xitcoin security and verification

This page organizes Xitcoin security evidence by asset, contract generation, network component and verification method. A token audit, an identity verification, a blockchain test and an operational check establish different facts and must not be merged into one claim.

| Component | Review or validation | Current public status |
|---|---|---|
| XTC contract on Cronos | Independent smart-contract audit by Cyberscope | Published |
| Xitcoin project KYC | Identity verification by Cyberscope | Passed; public certificate available |
| Xitcoin Layer 1 | Engineering, consensus, genesis, build and compatibility validation | Test and CI evidence published by scope |
| Canonical bridge | Contract, relayer and operational security review | Not yet presented as production-audited |

## XTC contract on Cronos

### Version and naming record

| Label | Meaning | Status |
|---|---|---|
| V1 | Legacy standalone Cronos token, 8 decimals | Retired from new integrations |
| V2 | Cronos proxy generation created for the 2025 migration, 18 decimals | Current public proxy address |
| V3 | Audited implementation revision within the V2 proxy generation; Cyberscope source label `XitcoinV3_cyberscope.sol` | Current reviewed implementation record |
| V4 | Planned Cronos revision adopting `WXTC` after the canonical native-XTC bridge is operational and verified | Planned; not deployed or active |

The V2 proxy-generation label and V3 implementation-revision label describe different layers of the same upgradeable contract history. Integrators continue to use the proxy address. V4 must not be represented as active until its implementation, bytecode, bridge backing, deployment record and review scope are published.

### Independent Cyberscope audit

Cyberscope publishes the official [Xitcoin smart-contract audit record](https://www.cyberscope.io/audits/1-xtc) for the Cronos proxy contract [`0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991).

| Field | Public record |
|---|---|
| Auditor | Cyberscope |
| Network | Cronos EVM Mainnet, chain ID `25` |
| Proxy | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Reviewed implementation | `0x6c171952999421F0DA00E14F97B9C2DfBE71D8A0` |
| Auditor source label | `XitcoinV3_cyberscope.sol` |
| Canonical repository source | `contracts/cronos/v2/XTCV2.sol` |
| SHA-256 | `b5de4f5c4f13334bf644ec8fa97f8b0cda836ddc76935dc14c7bfcda2a73ff14` |
| Published iterations | 2 Jul 2025, 16 Jul 2025, 16 Feb 2026 and 17 Feb 2026 |

Public references:

* [Cyberscope audit record and iteration history](https://www.cyberscope.io/audits/1-xtc)
* [Xitcoin technical audit record](https://github.com/xitcoin-org/contracts/blob/main/audits/cyberscope-v2.md)
* [Canonical reviewed source](https://github.com/xitcoin-org/contracts/blob/main/contracts/cronos/v2/XTCV2.sol)
* [Cronos proxy](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991)
* [Reviewed implementation](https://explorer.cronos.org/address/0x6c171952999421F0DA00E14F97B9C2DfBE71D8A0)
* [Contract and migration history](../xtc/migration-history.md#contract-review-and-revisions)

The auditor's historical filename and the canonical repository filename differ. The source hash identifies the reviewed code. The audit does not automatically extend to a later proxy implementation, the Layer 1, validators, explorers, migration services or bridge software.

The score and project statistics displayed by an audit platform may change independently. Before relying on the record, verify the active implementation, deployed bytecode, source hash and applicable audit scope together.

### Cyberscope KYC

Cyberscope displays the Xitcoin KYC status as passed and publishes the corresponding [Xitcoin KYC certificate](https://github.com/cyberscope-io/kyc/blob/main/1-xtc/kyc.png).

KYC verifies identity under the provider's process. It is separate from technical auditing and does not certify source code, token economics, blockchain security, bridge operation or future releases.

## Xitcoin Layer 1 validation

The Xitcoin Layer 1 is validated separately from the Cronos token contract. The current record consists of repository tests, continuous-integration definitions, deterministic build controls and recorded multi-validator operational checks.

### Recorded network and genesis checks

The release process records the following checks:

* deterministic genesis checksum verification;
* genesis validation with the official binary;
* four-validator consensus testing;
* block-production continuity;
* peer discovery and connectivity;
* consistent genesis state across validators;
* Linux runtime and binary checksum comparison;
* Cosmos and EVM chain-ID verification;
* public RPC, REST, gRPC and JSON-RPC endpoint checks;
* validator health and monitoring checks.

These are engineering and operational validation results for the tested release and environment. They are not described as an independent third-party Layer 1 audit.

### Repository test and build evidence

| Control | What it validates | Public definition |
|---|---|---|
| Unit and coverage tests | Go modules, application logic and scripts | [Tests workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/test.yml) |
| System tests | Integrated node and EVM system behaviour | [System Test workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/system-test.yml) |
| JSON-RPC compatibility | Ethereum-compatible JSON-RPC behaviour and failure criteria | [JSON-RPC Compatibility workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/jsonrpc-compatibility.yml) |
| Reproducible Linux builds | amd64 and arm64 binaries with commit identity and SHA-256 files | [Build workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/build.yml) |
| Static Solidity analysis | Solidity security scanning | [Slither workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/slither.yml) |
| Solidity tests | Smart-contract and EVM component testing | [Solidity Test workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/solidity-test.yml) |
| Foundry compatibility | Ethereum tooling and contract compatibility | [Foundry workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/tests-compatibility-foundry.yml) |
| Hardhat compatibility | Hardhat deployment and interaction compatibility | [Hardhat workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/tests-compatibility-hardhat.yml) |
| viem compatibility | viem client integration | [viem workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/tests-compatibility-viem.yml) |
| web3.js compatibility | web3.js client integration | [web3.js workflow](https://github.com/xitcoin-org/pos-chain/blob/main/.github/workflows/tests-compatibility-web3js.yml) |

Workflow definitions prove which checks are encoded. A specific release claim must also reference the applicable commit, completed run and retained artifacts.

### Validator-admission validation

The validator-admission module is tested independently from ordinary staking behaviour. The required policy cases include:

1. rejection of an unapproved validator creation;
2. acceptance of an approved validator creation;
3. deactivation after revocation;
4. prevention of creation or unjailing after revocation;
5. identical results across nodes starting from the same genesis.

The public policy record is available in [XITCOIN-VALIDATOR-ADMISSION.md](https://github.com/xitcoin-org/pos-chain/blob/main/XITCOIN-VALIDATOR-ADMISSION.md). Release documentation must distinguish policy requirements from tests confirmed for a specific release.

### What blockchain validation establishes

The checks above provide evidence that the tested source, binary, genesis and validator set behave as recorded in the tested environment. They reduce implementation and operational uncertainty but do not eliminate software defects, validator failures, governance risk or economic risk.

No statement about the Cronos token audit or KYC should be interpreted as an independent audit of the Xitcoin Layer 1.

## Bridge review requirement

The bridge is a separate security boundary. It must not be presented as production-audited or production-ready until the following are reviewed and published:

1. canonical lock, mint, burn and release invariants;
2. destination contracts and deployment addresses;
3. relayer and signer authorization;
4. replay protection and finality rules;
5. rate limits and emergency controls;
6. supply reconciliation;
7. upgrade and incident procedures;
8. independent review scope and report.

## Release evidence standard

For every network or contract release, retain and publish where appropriate:

1. source commit;
2. build environment and toolchain;
3. binary checksums;
4. genesis checksum;
5. Cosmos and EVM chain IDs;
6. completed test results and CI run;
7. release artifacts;
8. deployed addresses;
9. audit scope and report links;
10. known limitations;
11. incident and recovery procedures.

{% hint style="warning" %}
An audit, KYC certificate, test workflow or successful testnet run applies only to its stated scope. Verify the relevant source, release, network and deployed address before relying on it.
{% endhint %}
