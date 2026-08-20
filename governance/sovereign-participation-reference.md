---
description: Whole-XTC sovereign reference methodology, complete table and participation pathway.
icon: globe
---

# Xitcoin Sovereign Reference Index 2026

The Xitcoin Sovereign Reference Index 2026 establishes a deterministic framework for potential sovereign participation. It provides a common technical method without granting ownership, validator status, diplomatic recognition or automatic access.

## Reference set

The framework contains **195 sovereign reference positions**:

- 193 United Nations Member States;
- the Holy See;
- the State of Palestine.

The set follows published United Nations identifiers for deterministic technical and statistical processing. It is not an independent statement on sovereignty, borders or diplomatic recognition.

## Fixed reference envelope

| Component | Quantity | Weight |
|---|---:|---:|
| Equal component | 292 500 000 XTC | 75% |
| Demographic component | 97 500 000 XTC | 25% |
| Total | **390 000 000 XTC** | 100% |

Every position starts with the same **1 500 000 XTC** base.

## Mathematical formula

Before whole-XTC rounding, the exact reference for position \(i\) is:

\[
A_i =
390{,}000{,}000
\left(
\frac{0.75}{195}
+
0.25
\frac{\sqrt{P_i}}{\sum_{j=1}^{195}\sqrt{P_j}}
\right)
\]

Where \(P_i\) is the consolidated population reference for 1 July 2026.

Square-root weighting recognizes population differences while limiting concentration. Four times the population produces twice the demographic weight, not four times the weight.

## Neutrality and equal treatment

The methodology uses only two components: an identical base and a pinned population reference. It does not use:

- gross domestic product, national wealth or market size;
- land area, natural resources or military capacity;
- political alignment, diplomatic influence or institutional seniority;
- current XTC holdings, investment size or ability to purchase tokens;
- discretionary scoring by the Xitcoin operator.

Because 75% of the envelope is equal, every reference receives the same 1 500 000 XTC base. Only 25% varies, and the square-root transformation deliberately compresses population differences. The same source, date, formula, precision and rounding rule apply to all 195 references.

## Whole-XTC rounding

The published table contains no fractional XTC:

1. calculate every exact result with deterministic decimal arithmetic;
2. take its whole-XTC floor;
3. rank fractional remainders from largest to smallest;
4. distribute the remaining XTC in that order;
5. use ascending ISO3 code to resolve an exact tie.

The 195 floors total **389 999 907 XTC**. The method distributes the remaining **93 XTC**, producing exactly **390 000 000 XTC**.

## Population source

- United Nations World Population Prospects 2024;
- medium variant;
- reference date: **1 July 2026**;
- source SHA-256: `98e34d9b65b53858cd08a57a566e45050b08093ad85ba5714fe6fbd78055ae6d`.

## Statistical consolidation

The index contains 39 statistical consolidations. They contribute population data to an existing reference and do not create extra positions.

Following the United Nations M49 statistical framework used by the dataset, the China calculation consolidates China, China Hong Kong SAR, China Macao SAR and China Taiwan Province of China.

This is a statistical processing rule inherited from the cited dataset. It is not a separate political or diplomatic determination by Xitcoin.

Cook Islands, Niue and Western Sahara remain non-consolidated statistical records. They do not create positions and are not added to another position.

### Complete consolidation table

| Statistical record | ISO3 | 2026 reference population | Consolidated into reference | Target ISO3 |
|---|---:|---:|---|---:|
| Aruba | `ABW` | 108 164 | Netherlands | `NLD` |
| Anguilla | `AIA` | 14 817 | United Kingdom | `GBR` |
| American Samoa | `ASM` | 45 319 | United States of America | `USA` |
| Bonaire, Sint Eustatius and Saba | `BES` | 31 913 | Netherlands | `NLD` |
| Saint Barthélemy | `BLM` | 11 550 | France | `FRA` |
| Bermuda | `BMU` | 64 459 | United Kingdom | `GBR` |
| Curaçao | `CUW` | 185 440 | Netherlands | `NLD` |
| Cayman Islands | `CYM` | 77 196 | United Kingdom | `GBR` |
| Falkland Islands (Malvinas) | `FLK` | 3 465 | United Kingdom | `GBR` |
| Faroe Islands | `FRO` | 56 526 | Denmark | `DNK` |
| Guernsey | `GGY` | 64 609 | United Kingdom | `GBR` |
| Gibraltar | `GIB` | 40 867 | United Kingdom | `GBR` |
| Guadeloupe | `GLP` | 372 453 | France | `FRA` |
| Greenland | `GRL` | 55 629 | Denmark | `DNK` |
| French Guiana | `GUF` | 318 872 | France | `FRA` |
| Guam | `GUM` | 170 185 | United States of America | `USA` |
| China, Hong Kong SAR | `HKG` | 7 378 602 | China | `CHN` |
| Isle of Man | `IMN` | 84 055 | United Kingdom | `GBR` |
| Jersey | `JEY` | 104 106 | United Kingdom | `GBR` |
| China, Macao SAR | `MAC` | 723 188 | China | `CHN` |
| Saint Martin (French part) | `MAF` | 23 898 | France | `FRA` |
| Northern Mariana Islands | `MNP` | 42 914 | United States of America | `USA` |
| Montserrat | `MSR` | 4 328 | United Kingdom | `GBR` |
| Martinique | `MTQ` | 337 711 | France | `FRA` |
| Mayotte | `MYT` | 347 536 | France | `FRA` |
| New Caledonia | `NCL` | 297 892 | France | `FRA` |
| Puerto Rico | `PRI` | 3 222 688 | United States of America | `USA` |
| French Polynesia | `PYF` | 283 076 | France | `FRA` |
| Réunion | `REU` | 886 298 | France | `FRA` |
| Saint Helena | `SHN` | 5 147 | United Kingdom | `GBR` |
| Saint Pierre and Miquelon | `SPM` | 5 513 | France | `FRA` |
| Sint Maarten (Dutch part) | `SXM` | 44 447 | Netherlands | `NLD` |
| Turks and Caicos Islands | `TCA` | 47 148 | United Kingdom | `GBR` |
| Tokelau | `TKL` | 2 691 | New Zealand | `NZL` |
| China, Taiwan Province of China | `TWN` | 23 011 292 | China | `CHN` |
| British Virgin Islands | `VGB` | 39 936 | United Kingdom | `GBR` |
| United States Virgin Islands | `VIR` | 83 400 | United States of America | `USA` |
| Wallis and Futuna Islands | `WLF` | 11 113 | France | `FRA` |
| Kosovo (under UNSC res. 1244) | `XKX` | 1 666 992 | Serbia | `SRB` |

Every consolidation above is applied before the formula. The complete target population is then used once in the demographic component. No consolidated record receives a separate position or a second quantity.

## Complete Xitcoin Sovereign Reference Index 2026

The first column displays national flag images sourced through Wikimedia Commons, the media repository used by Wikipedia. They are non-authoritative and do not affect identity, eligibility or quantity. United Nations M49 and ISO identifiers remain canonical.

| Wikipedia/Wikimedia flag | Sovereign reference | ISO3 | 2026 reference population | Equal component | Demographic component | 2026 reference quantity |
|---|---|---:|---:|---:|---:|---:|
| ![Afghanistan reference flag (2013–2021)](https://upload.wikimedia.org/wikipedia/commons/c/cd/Flag_of_Afghanistan_%282013%E2%80%932021%29.svg) | Afghanistan | `AFG` | 45 047 069 | 1 500 000 XTC | 782 764 XTC | **2 282 764 XTC** |
| ![Albania flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Albania.svg?width=48) | Albania | `ALB` | 2 751 025 | 1 500 000 XTC | 193 439 XTC | **1 693 439 XTC** |
| ![Algeria flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Algeria.svg?width=48) | Algeria | `DZA` | 48 028 334 | 1 500 000 XTC | 808 251 XTC | **2 308 251 XTC** |
| ![Andorra flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Andorra.svg?width=48) | Andorra | `AND` | 83 753 | 1 500 000 XTC | 33 752 XTC | **1 533 752 XTC** |
| ![Angola flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Angola.svg?width=48) | Angola | `AGO` | 40 215 179 | 1 500 000 XTC | 739 592 XTC | **2 239 592 XTC** |
| ![Antigua and Barbuda flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Antigua_and_Barbuda.svg?width=48) | Antigua and Barbuda | `ATG` | 94 626 | 1 500 000 XTC | 35 876 XTC | **1 535 876 XTC** |
| ![Argentina flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Argentina.svg?width=48) | Argentina | `ARG` | 46 003 734 | 1 500 000 XTC | 791 032 XTC | **2 291 032 XTC** |
| ![Armenia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Armenia.svg?width=48) | Armenia | `ARM` | 2 930 915 | 1 500 000 XTC | 199 664 XTC | **1 699 664 XTC** |
| ![Australia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Australia.svg?width=48) | Australia | `AUS` | 27 227 096 | 1 500 000 XTC | 608 553 XTC | **2 108 553 XTC** |
| ![Austria flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Austria.svg?width=48) | Austria | `AUT` | 9 107 266 | 1 500 000 XTC | 351 959 XTC | **1 851 959 XTC** |
| ![Azerbaijan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Azerbaijan.svg?width=48) | Azerbaijan | `AZE` | 10 454 855 | 1 500 000 XTC | 377 100 XTC | **1 877 100 XTC** |
| ![Bahamas flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Bahamas.svg?width=48) | Bahamas | `BHS` | 404 628 | 1 500 000 XTC | 74 187 XTC | **1 574 187 XTC** |
| ![Bahrain flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bahrain.svg?width=48) | Bahrain | `BHR` | 1 675 572 | 1 500 000 XTC | 150 966 XTC | **1 650 966 XTC** |
| ![Bangladesh flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bangladesh.svg?width=48) | Bangladesh | `BGD` | 177 818 044 | 1 500 000 XTC | 1 555 197 XTC | **3 055 197 XTC** |
| ![Barbados flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Barbados.svg?width=48) | Barbados | `BRB` | 282 724 | 1 500 000 XTC | 62 012 XTC | **1 562 012 XTC** |
| ![Belarus flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Belarus.svg?width=48) | Belarus | `BLR` | 8 937 018 | 1 500 000 XTC | 348 653 XTC | **1 848 653 XTC** |
| ![Belgium flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Belgium.svg?width=48) | Belgium | `BEL` | 11 774 642 | 1 500 000 XTC | 400 195 XTC | **1 900 195 XTC** |
| ![Belize flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Belize.svg?width=48) | Belize | `BLZ` | 428 644 | 1 500 000 XTC | 76 356 XTC | **1 576 356 XTC** |
| ![Benin flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Benin.svg?width=48) | Benin | `BEN` | 15 170 419 | 1 500 000 XTC | 454 251 XTC | **1 954 251 XTC** |
| ![Bhutan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bhutan.svg?width=48) | Bhutan | `BTN` | 802 214 | 1 500 000 XTC | 104 458 XTC | **1 604 458 XTC** |
| ![Bolivia (Plurinational State of) flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bolivia.svg?width=48) | Bolivia (Plurinational State of) | `BOL` | 12 749 291 | 1 500 000 XTC | 416 429 XTC | **1 916 429 XTC** |
| ![Bosnia and Herzegovina flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bosnia_and_Herzegovina.svg?width=48) | Bosnia and Herzegovina | `BIH` | 3 114 242 | 1 500 000 XTC | 205 813 XTC | **1 705 813 XTC** |
| ![Botswana flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Botswana.svg?width=48) | Botswana | `BWA` | 2 603 388 | 1 500 000 XTC | 188 177 XTC | **1 688 177 XTC** |
| ![Brazil flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Brazil.svg?width=48) | Brazil | `BRA` | 213 562 666 | 1 500 000 XTC | 1 704 355 XTC | **3 204 355 XTC** |
| ![Brunei Darussalam flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Brunei.svg?width=48) | Brunei Darussalam | `BRN` | 469 775 | 1 500 000 XTC | 79 936 XTC | **1 579 936 XTC** |
| ![Bulgaria flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Bulgaria.svg?width=48) | Bulgaria | `BGR` | 6 667 659 | 1 500 000 XTC | 301 151 XTC | **1 801 151 XTC** |
| ![Burkina Faso flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Burkina_Faso.svg?width=48) | Burkina Faso | `BFA` | 24 601 700 | 1 500 000 XTC | 578 469 XTC | **2 078 469 XTC** |
| ![Burundi flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Burundi.svg?width=48) | Burundi | `BDI` | 14 729 157 | 1 500 000 XTC | 447 596 XTC | **1 947 596 XTC** |
| ![Cabo Verde flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Cape_Verde.svg?width=48) | Cabo Verde | `CPV` | 529 630 | 1 500 000 XTC | 84 876 XTC | **1 584 876 XTC** |
| ![Cambodia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Cambodia.svg?width=48) | Cambodia | `KHM` | 18 051 219 | 1 500 000 XTC | 495 508 XTC | **1 995 508 XTC** |
| ![Cameroon flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Cameroon.svg?width=48) | Cameroon | `CMR` | 30 640 817 | 1 500 000 XTC | 645 576 XTC | **2 145 576 XTC** |
| ![Canada flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Canada.svg?width=48) | Canada | `CAN` | 40 467 728 | 1 500 000 XTC | 741 911 XTC | **2 241 911 XTC** |
| ![Central African Republic flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Central_African_Republic.svg?width=48) | Central African Republic | `CAF` | 5 698 984 | 1 500 000 XTC | 278 417 XTC | **1 778 417 XTC** |
| ![Chad flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Chad.svg?width=48) | Chad | `TCD` | 21 560 380 | 1 500 000 XTC | 541 534 XTC | **2 041 534 XTC** |
| ![Chile flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Chile.svg?width=48) | Chile | `CHL` | 19 945 850 | 1 500 000 XTC | 520 863 XTC | **2 020 863 XTC** |
| ![China flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_China.svg?width=48) | China | `CHN` | 1 444 027 171 | 1 500 000 XTC | 4 431 851 XTC | **5 931 851 XTC** |
| ![Colombia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Colombia.svg?width=48) | Colombia | `COL` | 53 936 226 | 1 500 000 XTC | 856 520 XTC | **2 356 520 XTC** |
| ![Comoros flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Comoros.svg?width=48) | Comoros | `COM` | 899 010 | 1 500 000 XTC | 110 581 XTC | **1 610 581 XTC** |
| ![Congo flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Republic_of_the_Congo.svg?width=48) | Congo | `COG` | 6 637 785 | 1 500 000 XTC | 300 476 XTC | **1 800 476 XTC** |
| ![Costa Rica flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Costa_Rica.svg?width=48) | Costa Rica | `CRI` | 5 174 789 | 1 500 000 XTC | 265 304 XTC | **1 765 304 XTC** |
| ![Croatia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Croatia.svg?width=48) | Croatia | `HRV` | 3 822 345 | 1 500 000 XTC | 228 014 XTC | **1 728 014 XTC** |
| ![Cuba flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Cuba.svg?width=48) | Cuba | `CUB` | 10 892 659 | 1 500 000 XTC | 384 915 XTC | **1 884 915 XTC** |
| ![Cyprus flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Cyprus.svg?width=48) | Cyprus | `CYP` | 1 382 334 | 1 500 000 XTC | 137 121 XTC | **1 637 121 XTC** |
| ![Czechia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Czech_Republic.svg?width=48) | Czechia | `CZE` | 10 527 781 | 1 500 000 XTC | 378 413 XTC | **1 878 413 XTC** |
| ![Côte d'Ivoire flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ivory_Coast.svg?width=48) | Côte d'Ivoire | `CIV` | 33 494 346 | 1 500 000 XTC | 674 968 XTC | **2 174 968 XTC** |
| ![Democratic People’s Republic of Korea flag](https://upload.wikimedia.org/wikipedia/commons/5/51/Flag_of_North_Korea.svg) | Democratic People’s Republic of Korea | `PRK` | 26 633 691 | 1 500 000 XTC | 601 885 XTC | **2 101 885 XTC** |
| ![Democratic Republic of the Congo flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Democratic_Republic_of_the_Congo.svg?width=48) | Democratic Republic of the Congo | `COD` | 116 452 162 | 1 500 000 XTC | 1 258 552 XTC | **2 758 552 XTC** |
| ![Denmark flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Denmark.svg?width=48) | Denmark | `DNK` | 6 135 675 | 1 500 000 XTC | 288 887 XTC | **1 788 887 XTC** |
| ![Djibouti flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Djibouti.svg?width=48) | Djibouti | `DJI` | 1 199 459 | 1 500 000 XTC | 127 729 XTC | **1 627 729 XTC** |
| ![Dominica flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Dominica.svg?width=48) | Dominica | `DMA` | 65 511 | 1 500 000 XTC | 29 851 XTC | **1 529 851 XTC** |
| ![Dominican Republic flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Dominican_Republic.svg?width=48) | Dominican Republic | `DOM` | 11 609 500 | 1 500 000 XTC | 397 378 XTC | **1 897 378 XTC** |
| ![Ecuador flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ecuador.svg?width=48) | Ecuador | `ECU` | 18 444 506 | 1 500 000 XTC | 500 877 XTC | **2 000 877 XTC** |
| ![Egypt flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Egypt.svg?width=48) | Egypt | `EGY` | 120 101 175 | 1 500 000 XTC | 1 278 118 XTC | **2 778 118 XTC** |
| ![El Salvador flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_El_Salvador.svg?width=48) | El Salvador | `SLV` | 6 391 253 | 1 500 000 XTC | 294 843 XTC | **1 794 843 XTC** |
| ![Equatorial Guinea flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Equatorial_Guinea.svg?width=48) | Equatorial Guinea | `GNQ` | 1 984 468 | 1 500 000 XTC | 164 293 XTC | **1 664 293 XTC** |
| ![Eritrea flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Eritrea.svg?width=48) | Eritrea | `ERI` | 3 682 669 | 1 500 000 XTC | 223 810 XTC | **1 723 810 XTC** |
| ![Estonia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Estonia.svg?width=48) | Estonia | `EST` | 1 331 062 | 1 500 000 XTC | 134 554 XTC | **1 634 554 XTC** |
| ![Eswatini flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Eswatini.svg?width=48) | Eswatini | `SWZ` | 1 269 859 | 1 500 000 XTC | 131 424 XTC | **1 631 424 XTC** |
| ![Ethiopia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ethiopia.svg?width=48) | Ethiopia | `ETH` | 138 902 185 | 1 500 000 XTC | 1 374 523 XTC | **2 874 523 XTC** |
| ![Fiji flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Fiji.svg?width=48) | Fiji | `FJI` | 937 282 | 1 500 000 XTC | 112 910 XTC | **1 612 910 XTC** |
| ![Finland flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Finland.svg?width=48) | Finland | `FIN` | 5 621 739 | 1 500 000 XTC | 276 524 XTC | **1 776 524 XTC** |
| ![France flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_France.svg?width=48) | France | `FRA` | 69 642 313 | 1 500 000 XTC | 973 272 XTC | **2 473 272 XTC** |
| ![Gabon flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Gabon.svg?width=48) | Gabon | `GAB` | 2 647 399 | 1 500 000 XTC | 189 761 XTC | **1 689 761 XTC** |
| ![Gambia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Gambia.svg?width=48) | Gambia | `GMB` | 2 884 079 | 1 500 000 XTC | 198 062 XTC | **1 698 062 XTC** |
| ![Georgia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Georgia.svg?width=48) | Georgia | `GEO` | 3 804 642 | 1 500 000 XTC | 227 486 XTC | **1 727 486 XTC** |
| ![Germany flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Germany.svg?width=48) | Germany | `DEU` | 83 644 258 | 1 500 000 XTC | 1 066 634 XTC | **2 566 634 XTC** |
| ![Ghana flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ghana.svg?width=48) | Ghana | `GHA` | 35 697 557 | 1 500 000 XTC | 696 814 XTC | **2 196 814 XTC** |
| ![Greece flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Greece.svg?width=48) | Greece | `GRC` | 9 897 115 | 1 500 000 XTC | 366 903 XTC | **1 866 903 XTC** |
| ![Grenada flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Grenada.svg?width=48) | Grenada | `GRD` | 117 362 | 1 500 000 XTC | 39 954 XTC | **1 539 954 XTC** |
| ![Guatemala flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Guatemala.svg?width=48) | Guatemala | `GTM` | 18 967 978 | 1 500 000 XTC | 507 935 XTC | **2 007 935 XTC** |
| ![Guinea flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Guinea.svg?width=48) | Guinea | `GIN` | 15 441 993 | 1 500 000 XTC | 458 299 XTC | **1 958 299 XTC** |
| ![Guinea-Bissau flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Guinea-Bissau.svg?width=48) | Guinea-Bissau | `GNB` | 2 297 808 | 1 500 000 XTC | 176 789 XTC | **1 676 789 XTC** |
| ![Guyana flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Guyana.svg?width=48) | Guyana | `GUY` | 840 890 | 1 500 000 XTC | 106 947 XTC | **1 606 947 XTC** |
| ![Haiti flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Haiti.svg?width=48) | Haiti | `HTI` | 12 037 506 | 1 500 000 XTC | 404 637 XTC | **1 904 637 XTC** |
| ![Holy See flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Vatican_City.svg?width=48) | Holy See | `VAT` | 506 | 1 500 000 XTC | 2 623 XTC | **1 502 623 XTC** |
| ![Honduras flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Honduras.svg?width=48) | Honduras | `HND` | 11 184 760 | 1 500 000 XTC | 390 042 XTC | **1 890 042 XTC** |
| ![Hungary flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Hungary.svg?width=48) | Hungary | `HUN` | 9 585 818 | 1 500 000 XTC | 361 087 XTC | **1 861 087 XTC** |
| ![Iceland flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Iceland.svg?width=48) | Iceland | `ISL` | 402 329 | 1 500 000 XTC | 73 976 XTC | **1 573 976 XTC** |
| ![India flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_India.svg?width=48) | India | `IND` | 1 476 625 576 | 1 500 000 XTC | 4 481 596 XTC | **5 981 596 XTC** |
| ![Indonesia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Indonesia.svg?width=48) | Indonesia | `IDN` | 287 886 782 | 1 500 000 XTC | 1 978 829 XTC | **3 478 829 XTC** |
| ![Iran (Islamic Republic of) flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Iran.svg?width=48) | Iran (Islamic Republic of) | `IRN` | 93 168 497 | 1 500 000 XTC | 1 125 724 XTC | **2 625 724 XTC** |
| ![Iraq flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Iraq.svg?width=48) | Iraq | `IRQ` | 48 007 437 | 1 500 000 XTC | 808 075 XTC | **2 308 075 XTC** |
| ![Ireland flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ireland.svg?width=48) | Ireland | `IRL` | 5 356 950 | 1 500 000 XTC | 269 933 XTC | **1 769 933 XTC** |
| ![Israel flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Israel.svg?width=48) | Israel | `ISR` | 9 647 689 | 1 500 000 XTC | 362 251 XTC | **1 862 251 XTC** |
| ![Italy flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Italy.svg?width=48) | Italy | `ITA` | 58 926 166 | 1 500 000 XTC | 895 265 XTC | **2 395 265 XTC** |
| ![Jamaica flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Jamaica.svg?width=48) | Jamaica | `JAM` | 2 833 403 | 1 500 000 XTC | 196 314 XTC | **1 696 314 XTC** |
| ![Japan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Japan.svg?width=48) | Japan | `JPN` | 122 427 731 | 1 500 000 XTC | 1 290 439 XTC | **2 790 439 XTC** |
| ![Jordan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Jordan.svg?width=48) | Jordan | `JOR` | 11 589 532 | 1 500 000 XTC | 397 037 XTC | **1 897 037 XTC** |
| ![Kazakhstan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Kazakhstan.svg?width=48) | Kazakhstan | `KAZ` | 21 083 626 | 1 500 000 XTC | 535 513 XTC | **2 035 513 XTC** |
| ![Kenya flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Kenya.svg?width=48) | Kenya | `KEN` | 58 636 412 | 1 500 000 XTC | 893 061 XTC | **2 393 061 XTC** |
| ![Kiribati flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Kiribati.svg?width=48) | Kiribati | `KIR` | 138 445 | 1 500 000 XTC | 43 395 XTC | **1 543 395 XTC** |
| ![Kuwait flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Kuwait.svg?width=48) | Kuwait | `KWT` | 5 102 773 | 1 500 000 XTC | 263 451 XTC | **1 763 451 XTC** |
| ![Kyrgyzstan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Kyrgyzstan.svg?width=48) | Kyrgyzstan | `KGZ` | 7 400 465 | 1 500 000 XTC | 317 269 XTC | **1 817 269 XTC** |
| ![Lao People's Democratic Republic flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Laos.svg?width=48) | Lao People's Democratic Republic | `LAO` | 7 974 017 | 1 500 000 XTC | 329 334 XTC | **1 829 334 XTC** |
| ![Latvia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Latvia.svg?width=48) | Latvia | `LVA` | 1 835 935 | 1 500 000 XTC | 158 025 XTC | **1 658 025 XTC** |
| ![Lebanon flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Lebanon.svg?width=48) | Lebanon | `LBN` | 5 897 467 | 1 500 000 XTC | 283 224 XTC | **1 783 224 XTC** |
| ![Lesotho flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Lesotho.svg?width=48) | Lesotho | `LSO` | 2 389 336 | 1 500 000 XTC | 180 275 XTC | **1 680 275 XTC** |
| ![Liberia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Liberia.svg?width=48) | Liberia | `LBR` | 5 853 949 | 1 500 000 XTC | 282 177 XTC | **1 782 177 XTC** |
| ![Libya flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Libya.svg?width=48) | Libya | `LBY` | 7 539 851 | 1 500 000 XTC | 320 242 XTC | **1 820 242 XTC** |
| ![Liechtenstein flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Liechtenstein.svg?width=48) | Liechtenstein | `LIE` | 40 368 | 1 500 000 XTC | 23 432 XTC | **1 523 432 XTC** |
| ![Lithuania flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Lithuania.svg?width=48) | Lithuania | `LTU` | 2 797 338 | 1 500 000 XTC | 195 061 XTC | **1 695 061 XTC** |
| ![Luxembourg flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Luxembourg.svg?width=48) | Luxembourg | `LUX` | 687 448 | 1 500 000 XTC | 96 698 XTC | **1 596 698 XTC** |
| ![Madagascar flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Madagascar.svg?width=48) | Madagascar | `MDG` | 33 522 052 | 1 500 000 XTC | 675 247 XTC | **2 175 247 XTC** |
| ![Malawi flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Malawi.svg?width=48) | Malawi | `MWI` | 22 785 535 | 1 500 000 XTC | 556 708 XTC | **2 056 708 XTC** |
| ![Malaysia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Malaysia.svg?width=48) | Malaysia | `MYS` | 36 385 115 | 1 500 000 XTC | 703 492 XTC | **2 203 492 XTC** |
| ![Maldives flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Maldives.svg?width=48) | Maldives | `MDV` | 531 517 | 1 500 000 XTC | 85 027 XTC | **1 585 027 XTC** |
| ![Mali flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mali.svg?width=48) | Mali | `MLI` | 25 932 275 | 1 500 000 XTC | 593 906 XTC | **2 093 906 XTC** |
| ![Malta flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Malta.svg?width=48) | Malta | `MLT` | 549 011 | 1 500 000 XTC | 86 415 XTC | **1 586 415 XTC** |
| ![Marshall Islands flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Marshall_Islands.svg?width=48) | Marshall Islands | `MHL` | 35 075 | 1 500 000 XTC | 21 842 XTC | **1 521 842 XTC** |
| ![Mauritania flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mauritania.svg?width=48) | Mauritania | `MRT` | 5 461 319 | 1 500 000 XTC | 272 550 XTC | **1 772 550 XTC** |
| ![Mauritius flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mauritius.svg?width=48) | Mauritius | `MUS` | 1 265 059 | 1 500 000 XTC | 131 176 XTC | **1 631 176 XTC** |
| ![Mexico flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mexico.svg?width=48) | Mexico | `MEX` | 132 997 658 | 1 500 000 XTC | 1 344 991 XTC | **2 844 991 XTC** |
| ![Federated States of Micronesia flag](https://upload.wikimedia.org/wikipedia/commons/e/e4/Flag_of_the_Federated_States_of_Micronesia.svg) | Federated States of Micronesia | `FSM` | 114 183 | 1 500 000 XTC | 39 409 XTC | **1 539 409 XTC** |
| ![Monaco flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Monaco.svg?width=48) | Monaco | `MCO` | 38 087 | 1 500 000 XTC | 22 761 XTC | **1 522 761 XTC** |
| ![Mongolia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mongolia.svg?width=48) | Mongolia | `MNG` | 3 556 798 | 1 500 000 XTC | 219 952 XTC | **1 719 952 XTC** |
| ![Montenegro flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Montenegro.svg?width=48) | Montenegro | `MNE` | 626 233 | 1 500 000 XTC | 92 292 XTC | **1 592 292 XTC** |
| ![Morocco flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Morocco.svg?width=48) | Morocco | `MAR` | 38 762 441 | 1 500 000 XTC | 726 111 XTC | **2 226 111 XTC** |
| ![Mozambique flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Mozambique.svg?width=48) | Mozambique | `MOZ` | 36 639 851 | 1 500 000 XTC | 705 951 XTC | **2 205 951 XTC** |
| ![Myanmar flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Myanmar.svg?width=48) | Myanmar | `MMR` | 55 184 819 | 1 500 000 XTC | 866 378 XTC | **2 366 378 XTC** |
| ![Namibia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Namibia.svg?width=48) | Namibia | `NAM` | 3 153 246 | 1 500 000 XTC | 207 098 XTC | **1 707 098 XTC** |
| ![Nauru flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Nauru.svg?width=48) | Nauru | `NRU` | 12 101 | 1 500 000 XTC | 12 829 XTC | **1 512 829 XTC** |
| ![Nepal flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Nepal.svg?width=48) | Nepal | `NPL` | 29 629 410 | 1 500 000 XTC | 634 832 XTC | **2 134 832 XTC** |
| ![Netherlands flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Netherlands.svg?width=48) | Netherlands | `NLD` | 18 818 739 | 1 500 000 XTC | 505 933 XTC | **2 005 933 XTC** |
| ![New Zealand flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_New_Zealand.svg?width=48) | New Zealand | `NZL` | 5 290 170 | 1 500 000 XTC | 268 245 XTC | **1 768 245 XTC** |
| ![Nicaragua flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Nicaragua.svg?width=48) | Nicaragua | `NIC` | 7 097 329 | 1 500 000 XTC | 310 703 XTC | **1 810 703 XTC** |
| ![Niger flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Niger.svg?width=48) | Niger | `NER` | 28 814 878 | 1 500 000 XTC | 626 045 XTC | **2 126 045 XTC** |
| ![Nigeria flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Nigeria.svg?width=48) | Nigeria | `NGA` | 242 431 832 | 1 500 000 XTC | 1 815 902 XTC | **3 315 902 XTC** |
| ![North Macedonia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_North_Macedonia.svg?width=48) | North Macedonia | `MKD` | 1 804 063 | 1 500 000 XTC | 156 647 XTC | **1 656 647 XTC** |
| ![Norway flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Norway.svg?width=48) | Norway | `NOR` | 5 652 989 | 1 500 000 XTC | 277 292 XTC | **1 777 292 XTC** |
| ![Oman flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Oman.svg?width=48) | Oman | `OMN` | 5 671 458 | 1 500 000 XTC | 277 744 XTC | **1 777 744 XTC** |
| ![Pakistan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Pakistan.svg?width=48) | Pakistan | `PAK` | 259 299 791 | 1 500 000 XTC | 1 878 013 XTC | **3 378 013 XTC** |
| ![Palau flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Palau.svg?width=48) | Palau | `PLW` | 17 614 | 1 500 000 XTC | 15 478 XTC | **1 515 478 XTC** |
| ![Panama flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Panama.svg?width=48) | Panama | `PAN` | 4 625 718 | 1 500 000 XTC | 250 834 XTC | **1 750 834 XTC** |
| ![Papua New Guinea flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Papua_New_Guinea.svg?width=48) | Papua New Guinea | `PNG` | 10 947 848 | 1 500 000 XTC | 385 889 XTC | **1 885 889 XTC** |
| ![Paraguay flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Paraguay.svg?width=48) | Paraguay | `PRY` | 7 095 279 | 1 500 000 XTC | 310 658 XTC | **1 810 658 XTC** |
| ![Peru flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Peru.svg?width=48) | Peru | `PER` | 34 922 148 | 1 500 000 XTC | 689 204 XTC | **2 189 204 XTC** |
| ![Philippines flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_Philippines.svg?width=48) | Philippines | `PHL` | 117 724 471 | 1 500 000 XTC | 1 265 409 XTC | **2 765 409 XTC** |
| ![Poland flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Poland.svg?width=48) | Poland | `POL` | 37 843 188 | 1 500 000 XTC | 717 449 XTC | **2 217 449 XTC** |
| ![Portugal flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Portugal.svg?width=48) | Portugal | `PRT` | 10 395 362 | 1 500 000 XTC | 376 026 XTC | **1 876 026 XTC** |
| ![Qatar flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Qatar.svg?width=48) | Qatar | `QAT` | 3 173 559 | 1 500 000 XTC | 207 764 XTC | **1 707 764 XTC** |
| ![Republic of Korea flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_South_Korea.svg?width=48) | Republic of Korea | `KOR` | 51 600 388 | 1 500 000 XTC | 837 768 XTC | **2 337 768 XTC** |
| ![Republic of Moldova flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Moldova.svg?width=48) | Republic of Moldova | `MDA` | 2 961 253 | 1 500 000 XTC | 200 694 XTC | **1 700 694 XTC** |
| ![Romania flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Romania.svg?width=48) | Romania | `ROU` | 18 800 605 | 1 500 000 XTC | 505 689 XTC | **2 005 689 XTC** |
| ![Russian Federation flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Russia.svg?width=48) | Russian Federation | `RUS` | 143 394 458 | 1 500 000 XTC | 1 396 573 XTC | **2 896 573 XTC** |
| ![Rwanda flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Rwanda.svg?width=48) | Rwanda | `RWA` | 14 889 693 | 1 500 000 XTC | 450 029 XTC | **1 950 029 XTC** |
| ![Saint Kitts and Nevis flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Saint_Kitts_and_Nevis.svg?width=48) | Saint Kitts and Nevis | `KNA` | 46 992 | 1 500 000 XTC | 25 282 XTC | **1 525 282 XTC** |
| ![Saint Lucia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Saint_Lucia.svg?width=48) | Saint Lucia | `LCA` | 180 488 | 1 500 000 XTC | 49 548 XTC | **1 549 548 XTC** |
| ![Saint Vincent and the Grenadines flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Saint_Vincent_and_the_Grenadines.svg?width=48) | Saint Vincent and the Grenadines | `VCT` | 99 245 | 1 500 000 XTC | 36 741 XTC | **1 536 741 XTC** |
| ![Samoa flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Samoa.svg?width=48) | Samoa | `WSM` | 220 528 | 1 500 000 XTC | 54 768 XTC | **1 554 768 XTC** |
| ![San Marino flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_San_Marino.svg?width=48) | San Marino | `SMR` | 33 605 | 1 500 000 XTC | 21 380 XTC | **1 521 380 XTC** |
| ![Sao Tome and Principe flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe.svg?width=48) | Sao Tome and Principe | `STP` | 244 994 | 1 500 000 XTC | 57 727 XTC | **1 557 727 XTC** |
| ![Saudi Arabia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Saudi_Arabia.svg?width=48) | Saudi Arabia | `SAU` | 35 165 787 | 1 500 000 XTC | 691 604 XTC | **2 191 604 XTC** |
| ![Senegal flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Senegal.svg?width=48) | Senegal | `SEN` | 19 366 548 | 1 500 000 XTC | 513 244 XTC | **2 013 244 XTC** |
| ![Serbia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Serbia.svg?width=48) | Serbia | `SRB` | 8 308 956 | 1 500 000 XTC | 336 179 XTC | **1 836 179 XTC** |
| ![Seychelles flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Seychelles.svg?width=48) | Seychelles | `SYC` | 134 959 | 1 500 000 XTC | 42 845 XTC | **1 542 845 XTC** |
| ![Sierra Leone flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Sierra_Leone.svg?width=48) | Sierra Leone | `SLE` | 8 996 745 | 1 500 000 XTC | 349 816 XTC | **1 849 816 XTC** |
| ![Singapore flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Singapore.svg?width=48) | Singapore | `SGP` | 5 905 748 | 1 500 000 XTC | 283 423 XTC | **1 783 423 XTC** |
| ![Slovakia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Slovakia.svg?width=48) | Slovakia | `SVK` | 5 451 342 | 1 500 000 XTC | 272 301 XTC | **1 772 301 XTC** |
| ![Slovenia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Slovenia.svg?width=48) | Slovenia | `SVN` | 2 114 573 | 1 500 000 XTC | 169 593 XTC | **1 669 593 XTC** |
| ![Solomon Islands flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Solomon_Islands.svg?width=48) | Solomon Islands | `SLB` | 858 288 | 1 500 000 XTC | 108 047 XTC | **1 608 047 XTC** |
| ![Somalia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Somalia.svg?width=48) | Somalia | `SOM` | 20 305 907 | 1 500 000 XTC | 525 544 XTC | **2 025 544 XTC** |
| ![South Africa flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_South_Africa.svg?width=48) | South Africa | `ZAF` | 65 453 084 | 1 500 000 XTC | 943 545 XTC | **2 443 545 XTC** |
| ![South Sudan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_South_Sudan.svg?width=48) | South Sudan | `SSD` | 12 436 037 | 1 500 000 XTC | 411 281 XTC | **1 911 281 XTC** |
| ![Spain flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Spain.svg?width=48) | Spain | `ESP` | 47 850 793 | 1 500 000 XTC | 806 756 XTC | **2 306 756 XTC** |
| ![Sri Lanka flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Sri_Lanka.svg?width=48) | Sri Lanka | `LKA` | 23 348 315 | 1 500 000 XTC | 563 541 XTC | **2 063 541 XTC** |
| ![State of Palestine flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Palestine.svg?width=48) | State of Palestine | `PSE` | 5 692 790 | 1 500 000 XTC | 278 266 XTC | **1 778 266 XTC** |
| ![Sudan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Sudan.svg?width=48) | Sudan | `SDN` | 53 282 719 | 1 500 000 XTC | 851 316 XTC | **2 351 316 XTC** |
| ![Suriname flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Suriname.svg?width=48) | Suriname | `SUR` | 645 256 | 1 500 000 XTC | 93 684 XTC | **1 593 684 XTC** |
| ![Sweden flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Sweden.svg?width=48) | Sweden | `SWE` | 10 701 047 | 1 500 000 XTC | 381 514 XTC | **1 881 514 XTC** |
| ![Switzerland flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Switzerland.svg?width=48) | Switzerland | `CHE` | 9 007 798 | 1 500 000 XTC | 350 031 XTC | **1 850 031 XTC** |
| ![Syrian Arab Republic flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Syria.svg?width=48) | Syrian Arab Republic | `SYR` | 26 472 497 | 1 500 000 XTC | 600 060 XTC | **2 100 060 XTC** |
| ![Tajikistan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Tajikistan.svg?width=48) | Tajikistan | `TJK` | 10 978 599 | 1 500 000 XTC | 386 430 XTC | **1 886 430 XTC** |
| ![Thailand flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Thailand.svg?width=48) | Thailand | `THA` | 71 559 614 | 1 500 000 XTC | 986 578 XTC | **2 486 578 XTC** |
| ![Timor-Leste flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Timor-Leste.svg?width=48) | Timor-Leste | `TLS` | 1 436 923 | 1 500 000 XTC | 139 802 XTC | **1 639 802 XTC** |
| ![Togo flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Togo.svg?width=48) | Togo | `TGO` | 9 930 918 | 1 500 000 XTC | 367 529 XTC | **1 867 529 XTC** |
| ![Tonga flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Tonga.svg?width=48) | Tonga | `TON` | 103 291 | 1 500 000 XTC | 37 483 XTC | **1 537 483 XTC** |
| ![Trinidad and Tobago flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Trinidad_and_Tobago.svg?width=48) | Trinidad and Tobago | `TTO` | 1 513 268 | 1 500 000 XTC | 143 468 XTC | **1 643 468 XTC** |
| ![Tunisia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Tunisia.svg?width=48) | Tunisia | `TUN` | 12 415 138 | 1 500 000 XTC | 410 935 XTC | **1 910 935 XTC** |
| ![Turkmenistan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Turkmenistan.svg?width=48) | Turkmenistan | `TKM` | 7 736 632 | 1 500 000 XTC | 324 394 XTC | **1 824 394 XTC** |
| ![Tuvalu flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Tuvalu.svg?width=48) | Tuvalu | `TUV` | 9 362 | 1 500 000 XTC | 11 285 XTC | **1 511 285 XTC** |
| ![Türkiye flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Turkey.svg?width=48) | Türkiye | `TUR` | 87 926 082 | 1 500 000 XTC | 1 093 595 XTC | **2 593 595 XTC** |
| ![Uganda flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Uganda.svg?width=48) | Uganda | `UGA` | 52 761 469 | 1 500 000 XTC | 847 141 XTC | **2 347 141 XTC** |
| ![Ukraine flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Ukraine.svg?width=48) | Ukraine | `UKR` | 39 535 849 | 1 500 000 XTC | 733 319 XTC | **2 233 319 XTC** |
| ![United Arab Emirates flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_United_Arab_Emirates.svg?width=48) | United Arab Emirates | `ARE` | 11 574 682 | 1 500 000 XTC | 396 782 XTC | **1 896 782 XTC** |
| ![United Kingdom flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_United_Kingdom.svg?width=48) | United Kingdom | `GBR` | 70 481 661 | 1 500 000 XTC | 979 119 XTC | **2 479 119 XTC** |
| ![United Republic of Tanzania flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Tanzania.svg?width=48) | United Republic of Tanzania | `TZA` | 72 563 780 | 1 500 000 XTC | 993 476 XTC | **2 493 476 XTC** |
| ![United States of America flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_the_United_States.svg?width=48) | United States of America | `USA` | 352 600 000 | 1 500 000 XTC | 2 189 972 XTC | **3 689 972 XTC** |
| ![Uruguay flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Uruguay.svg?width=48) | Uruguay | `URY` | 3 382 537 | 1 500 000 XTC | 214 496 XTC | **1 714 496 XTC** |
| ![Uzbekistan flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Uzbekistan.svg?width=48) | Uzbekistan | `UZB` | 37 724 223 | 1 500 000 XTC | 716 321 XTC | **2 216 321 XTC** |
| ![Vanuatu flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Vanuatu.svg?width=48) | Vanuatu | `VUT` | 342 564 | 1 500 000 XTC | 68 260 XTC | **1 568 260 XTC** |
| ![Venezuela (Bolivarian Republic of) flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Venezuela.svg?width=48) | Venezuela (Bolivarian Republic of) | `VEN` | 28 633 711 | 1 500 000 XTC | 624 074 XTC | **2 124 074 XTC** |
| ![Viet Nam flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Vietnam.svg?width=48) | Viet Nam | `VNM` | 102 177 431 | 1 500 000 XTC | 1 178 895 XTC | **2 678 895 XTC** |
| ![Yemen flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Yemen.svg?width=48) | Yemen | `YEM` | 42 961 653 | 1 500 000 XTC | 764 430 XTC | **2 264 430 XTC** |
| ![Zambia flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Zambia.svg?width=48) | Zambia | `ZMB` | 22 521 915 | 1 500 000 XTC | 553 478 XTC | **2 053 478 XTC** |
| ![Zimbabwe flag](https://commons.wikimedia.org/wiki/Special:Redirect/file/Flag_of_Zimbabwe.svg?width=48) | Zimbabwe | `ZWE` | 17 273 580 | 1 500 000 XTC | 484 717 XTC | **1 984 717 XTC** |

## Reserved sovereign validator participation

The reference quantity is a finite protocol-funded contribution supporting an activated sovereign validator position. It is not an automatic validator right, an immediate distribution or a substitute for the validator's own commitment.

Before activation, the relevant State must independently satisfy:

1. verified institutional identity and authority;
2. a valid institutional governance mandate;
3. an authorized operating team;
4. legal, security, custody and infrastructure review;
5. at least **5,000,000 XTC** of State-provided self-delegation;
6. explicit approval by the canonical validator-admission authority.

The sovereign allocation cannot be counted toward the five-million-XTC activation minimum.

## Activation-based five-year allocation

Each position receives an individual five-year vesting schedule when it is activated. A position may join years or decades after network launch without requiring a new global calendar or a recurring company transaction.

The allocation accrues linearly through deterministic on-chain accounting during eligible service:

```
vested allocation =
fixed ISO3 allocation × eligible service blocks / five-year service blocks

claimable allocation =
vested allocation - allocation already released
```

The authorized institutional controller may claim the accrued amount at any time. An unclaimed amount remains recorded as claimable.

If the position no longer satisfies the applicable institutional, staking, availability or security conditions, future accrual pauses. Reactivation resumes the schedule without retroactive accrual for the suspended interval. An amount already vested cannot be removed arbitrarily.

The reserve is fixed at 390,000,000 XTC. This release does not create new supply.

## Institutional continuity

Each position remains attached to the relevant State. It is not attached permanently to a president, minister, administration, individual signatory or infrastructure provider.

Successive administrations of the same State may transfer the institutional governance and operating mandate to their authorized successors without replacing the State position, its history or its remaining allocation.

A mandate transition may update the responsible representatives, mandatary, operator and payment instructions. The former team loses its authority when its mandate expires or is revoked. The State position continues under the authorized successor.

Buying tokens from a State or former operator does not grant control of the State position.

## Ordinary validator rights

Sovereign allocation and ordinary validator rewards are separate.

An activated sovereign validator participates under the same ordinary staking, commission, delegation, fee-distribution and slashing rules as other eligible validators. The sovereign position receives its finite allocation over five years while also participating in ordinary network rewards.

After all 20 valid tranches have been released, no further sovereign allocation is created. The position may continue validating and receiving ordinary network rewards while it remains eligible.

## How an institutional review begins

A public authority or formally authorized representative may initiate a review through the [institutional contact pathway](../start/official-links.md).

The first contact creates a case reference only. Before any application is accepted, Xitcoin independently verifies the public institution, official-domain contact, authority of the representative and operating mandate through separate official sources and a secure communication channel.

Personal email, social-media identity or submitted documentation alone never proves governmental authority. No credentials, private keys or confidential identity documents should be sent through social media.

No position activates automatically. Activation requires verified institutional authority, the five-million-XTC self-delegation, operational review and explicit on-chain admission.

## Current boundary

The sovereign position registry, institutional succession controls and activation-based vesting mechanism remain under development and are not deployed.

The complete allocation data and technical verification sources are maintained in the Xitcoin blockchain repository:

- `docs/sovereign-allocation-2026.md`;
- `docs/sovereign-validator-framework.md`;
- `networks/testnet/sovereign-allocation-index-2026.csv`;
- `networks/testnet/sovereign-allocation-index-2026.json`;
- `networks/testnet/territorial-consolidation-2026.csv`;
- `scripts/verify-sovereign-allocation-2026.py`.
