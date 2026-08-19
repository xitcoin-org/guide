---
description: Scope and status of Xitcoin smart-contract reviews, blockchain validation and release checks.
icon: shield-check
---

# Audits and technical validation

Security evidence is published by scope. A token audit does not certify the Layer 1, bridge, validator infrastructure or every application in the ecosystem.

## Cronos token audit

Cyberscope publishes the current [Xitcoin contract audit record](https://www.cyberscope.io/audits/1-xtc) for proxy contract `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`.

| Field | Public record |
|---|---|
| Auditor | Cyberscope |
| Audited file | `XitcoinV3_cyberscope.sol` |
| Published iterations | 2 Jul 2025, 16 Jul 2025, 16 Feb 2026 and 17 Feb 2026 |
| Current findings shown | 0 |
| Scope | Cronos token contract source reviewed by Cyberscope |

The score displayed by an audit platform is time-dependent. The linked report, audited-file hash, deployed bytecode and proxy implementation must be checked together before relying on it.

## Native blockchain validation

The Xitcoin Layer 1 is validated through a separate engineering process:

* deterministic genesis checksum verification;
* official-binary genesis validation;
* four-validator consensus tests;
* block-production and peer-connectivity checks;
* Linux runtime and binary checksum comparison;
* public endpoint and chain-ID checks;
* continuous-integration build and test workflows.

These checks demonstrate that the tested release behaves as expected in the recorded environment. They do not eliminate software, operational or economic risk.

## Bridge review requirement

No bridge should be presented as production-ready until its contracts, relayer controls, supply invariants, emergency procedures and deployment addresses have been independently reviewed and published.

## Verification standard

For every release, retain:

1. source commit;
2. build environment and toolchain;
3. binary checksums;
4. genesis checksum;
5. chain IDs;
6. test results;
7. deployed addresses;
8. audit scope and report links;
9. known limitations;
10. incident and recovery procedures.
