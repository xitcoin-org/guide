---
description: Downloadable official Xitcoin artwork, approved variants, technical specifications and usage rules.
icon: palette
---

# Official brand assets

Use only the source files maintained by Xitcoin. Do not extract artwork from screenshots, explorer pages, social posts or third-party token lists.

## Official mark

![Official Xitcoin symbol](../.gitbook/assets/xitcoin-official-symbol.svg)

The Xitcoin symbol shown above is the standard project and asset mark. The authoritative source package is maintained in the [Xitcoin Brand repository](https://github.com/xitcoin-org/brand).

## Download center

| Asset | Recommended use | Download |
|---|---|---|
| Standard symbol — SVG | Websites, applications, print and scalable interfaces | [Download SVG](https://raw.githubusercontent.com/xitcoin-org/brand/main/assets/svg/xitcoin-symbol.svg) |
| White symbol — SVG | Approved dark-background layouts | [Download white SVG](https://raw.githubusercontent.com/xitcoin-org/brand/main/assets/svg/xitcoin-symbol-white.svg) |
| Standard PNG exports | Wallets, explorers, directories and fixed-size integrations | [Open PNG package](https://github.com/xitcoin-org/brand/tree/main/assets/png/standard) |
| White PNG exports | Fixed-size use on dark backgrounds | [Open white PNG package](https://github.com/xitcoin-org/brand/tree/main/assets/png/white) |
| Complete source repository | Licensing, release history and canonical files | [Open Brand repository](https://github.com/xitcoin-org/brand) |

SVG is preferred whenever the destination accepts vector artwork. Choose the smallest suitable PNG only when a platform requires a raster file.

## Approved visual specification

| Element | Specification |
|---|---|
| Primary mark | Supplied Xitcoin symbol |
| Primary accent | Xitcoin Orange — `#FB8D00` |
| Neutral component | Xitcoin Graphite — `#53585E` |
| Reverse mark | Supplied white variant — `#FFFFFF` |
| Minimum treatment | Preserve legibility and clear space at the final display size |
| Source of truth | Files in `xitcoin-org/brand` |

These values specify the supplied artwork; they are not a general website theme. Product interfaces may use their own accessible design systems while preserving the official mark.

## Clear-space and integrity rules

* preserve the original proportions and orientation;
* keep clear space around the mark so adjacent text or controls do not touch it;
* select the standard or white source variant according to background contrast;
* do not redraw, crop, stretch, rotate, outline, recolor or apply shadows and effects;
* do not place the mark inside an unrelated coin, chain or company logo;
* do not use the mark to imply endorsement, partnership or authorization;
* use the standard Xitcoin mark for every official XTC representation and identify each asset by its verified network metadata.

## Naming standard

| Context | Required form |
|---|---|
| Network and project | Xitcoin |
| Canonical native asset | XTC |
| Current Cronos proxy generation | V2 |
| Current audited implementation revision | V3 |
| Public asset symbol | XTC |
| Current Cronos contract | `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991` |
| Xitcoin native denomination | XTC (`axtc`) |
| External representations | XTC, identified by network and verified contract, mint or IBC denomination |

An external XTC representation is published only after its bridge, asset identifier and one-to-one accounting have been verified.

## Licensing and attribution

The Brand repository publishes the artwork under its included [CC0 1.0 Universal dedication](https://github.com/xitcoin-org/brand/blob/main/LICENSE). The license permits broad reuse; the integrity and non-endorsement rules above remain the official integration guidance.

## Integration checklist

Before submitting Xitcoin to a wallet, explorer, exchange, directory or media package:

1. download the asset from the official repository;
2. use the correct symbol for the asset role and network;
3. verify the complete chain and contract metadata;
4. preview the mark at the platform’s final size;
5. link users to the [official Xitcoin Guide](https://xitcoin.gitbook.io/guide/) for verification.
