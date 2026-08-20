---
description: Verified market-information pages and rules for identifying XTC venues and liquidity pools.
icon: chart-candlestick
---

# Markets and liquidity

Market availability changes independently of the Xitcoin protocol. This page provides verification sources, not investment advice, an endorsement of a venue or a guarantee of liquidity.

## Buy or swap on Cronos

The current Cronos XTC proxy is:

`0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`

| Access route | Official or live link | Use |
|---|---|---|
| VVS Finance | [CRO → XTC swap](https://vvs.finance/trade/swap?inputCurrency=cro&outputCurrency=0xe45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) | Direct swap interface prefilled with the current XTC contract |
| Crypto.com Onchain | [Official Onchain wallet](https://crypto.com/onchain) | Self-custodial wallet with native Swap support on Cronos |
| DEX Screener | [XTC markets on Cronos](https://dexscreener.com/cronos/0xe45fe733bc8617fa6dac8437fc44b5fffa949991) | Live market, pair and liquidity comparison |
| GeckoTerminal | [Pools matching the XTC contract](https://www.geckoterminal.com/search?query=0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) | Contract-based discovery across detected Cronos pools |

### Crypto.com Onchain

Crypto.com Onchain is a self-custodial wallet. To request a swap:

1. select the **Cronos** network;
2. open **Swap**;
3. select the input asset;
4. locate or import XTC using the complete current proxy address;
5. enter the amount;
6. review the quoted output, price impact, network fee and selected protocol;
7. confirm only if every identifier and amount is correct.

Cronos support does not guarantee that an XTC route will always be available. The tokens and routes shown by Onchain depend on its supported decentralized exchanges and the liquidity available when the quote is requested. The protocol used for a route is displayed on the confirmation screen.

## Liquidity pools

XTC may appear in pools paired with assets such as WCRO, WBTC, WETH or other Cronos tokens. Pool creation is permissionless, and availability, composition, activity and liquidity can change without action by Xitcoin.

The guide therefore does not maintain a supposedly exhaustive static list. Use the live [DEX Screener XTC market view](https://dexscreener.com/cronos/0xe45fe733bc8617fa6dac8437fc44b5fffa949991) and [GeckoTerminal contract search](https://www.geckoterminal.com/search?query=0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) to discover currently detected pools. For each pool, verify:

1. the XTC side is exactly `0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991`;
2. the paired asset and its contract;
3. the decentralized exchange and pool contract;
4. available liquidity and recent activity;
5. price impact and slippage;
6. whether the route uses multiple pools or intermediate assets.

Anyone can create a pool or token with a similar name. Inclusion on a market-data site does not make a pool official.

## Market-information pages

| Service | Reference |
|---|---|
| CoinMarketCap | [Xitcoin](https://coinmarketcap.com/currencies/xitcoin/) |
| CoinGecko | [Xitcoin](https://www.coingecko.com/fr/coins/xitcoin) |
| GeckoTerminal | [Search by the canonical Cronos proxy](https://www.geckoterminal.com/search?query=0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) |
| Cronos Explorer | [Canonical proxy contract](https://explorer.cronos.org/address/0xE45Fe733bC8617FA6Dac8437Fc44B5ffFA949991) |

Listings may show the Cronos ticker as **$XTC**. Verify the complete contract address; ticker text and token names are not unique identifiers.

## Transaction checks

Before using any decentralized venue or liquidity pool:

1. verify that the interface references the canonical Cronos proxy;
2. confirm both assets in the trading pair;
3. review liquidity, price impact and slippage;
4. confirm that Cronos is selected in the wallet;
5. retain enough CRO for network fees;
6. inspect the approval and swap transaction before signing;
7. test with a small amount.

## Legacy pools

Pools referencing `0xDD646291D2fff52c75F27CCDAdD0D4C2A24f37Dd` belong to the legacy token generation. They must not be presented as current XTC access points.

## No fixed market claims

Prices, rankings, volumes, circulating-supply displays and pool liquidity can change at any time. The guide links to live services instead of copying volatile figures.
