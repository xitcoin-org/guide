---
description: Methodology, allocation reference and participation requirements for institutional validator positions.
icon: globe
---

# Sovereign Index 2026

This publication defines a deterministic technical reference for potential institutional participation in the Xitcoin validator network. It standardizes allocation calculations, eligibility requirements and operational continuity. It does not confer asset ownership, validator appointment, legal status, diplomatic recognition, endorsement or automatic access.

{% hint style="info" %}
**Protocol neutrality.** Xitcoin is general-purpose digital infrastructure. Like electricity and communications networks, it operates through common technical rules that do not depend on political alignment. A statistical reference in this index has no diplomatic, legal or political effect.
{% endhint %}

The methodology covers **193 reserved positions**, corresponding to the United Nations Member States recorded at the 2026 reference date.

## Fixed reference envelope

| Component | Quantity | Weight |
|---|---:|---:|
| Equal component | 289 500 000 XTC | 75% |
| Demographic component | 96 500 000 XTC | 25% |
| Total | **386 000 000 XTC** | 100% |

Every position starts with the same **1 500 000 XTC** base.

## Allocation formula

Before rounding to whole XTC, each Member State's reference quantity is calculated as follows:

$\displaystyle A_i = 386{,}000{,}000 \left( \frac{0.75}{193} + 0.25 \frac{\sqrt{P_i}}{\sum_{j=1}^{193}\sqrt{P_j}} \right)$

**Formula key**

- **i** — the Member State currently being calculated;
- **Aᵢ** — its calculated reference quantity before rounding;
- **Pᵢ** — its consolidated population on 1 July 2026;
- **j** — each of the 193 Member States included in the population calculation;
- **Σ** — add the values for all 193 Member States;
- **√** — apply the square-root function to reduce concentration.

In plain language, 75% of the reserve is divided equally. The remaining 25% is distributed using population, with the square-root function limiting the difference between larger and smaller populations. Four times the population therefore produces twice the demographic weight, rather than four times the weight.

## Neutrality and equal treatment

The methodology uses only two components: an identical base and a pinned population reference. It does not use:

- gross domestic product, national wealth or market size;
- land area, natural resources or military capacity;
- political alignment, diplomatic influence or institutional seniority;
- current XTC holdings, investment size or ability to purchase tokens;
- discretionary scoring by the Xitcoin operator.

Because 75% of the envelope is equal, every reference receives the same 1 500 000 XTC base. Only 25% varies, and the square-root transformation deliberately compresses population differences. The same source, date, formula, precision and rounding rule apply to all 193 references.

## Integer allocation and rounding

The published allocation table uses integer XTC only:

1. calculate every exact result with deterministic decimal arithmetic;
2. take its integer floor;
3. rank fractional remainders from largest to smallest;
4. distribute the remaining XTC in that order;
5. use ascending ISO3 code to resolve an exact tie.

The 193 floors total **385,999,899 XTC**. The method distributes the remaining **101 XTC**, producing exactly **386,000,000 XTC**.

## Population source

- United Nations World Population Prospects 2024;
- medium variant;
- reference date: **1 July 2026**;
- source SHA-256: `98e34d9b65b53858cd08a57a566e45050b08093ad85ba5714fe6fbd78055ae6d`.

## Statistical treatment

Population inputs follow the United Nations World Population Prospects dataset
and the United Nations M49 statistical framework. Statistical records do not
create additional validator positions.

For the China calculation, the source data for China, Hong Kong SAR, Macao SAR
and Taiwan Province of China are consolidated into the single China reference.
This is a reproducible statistical treatment inherited from the cited United
Nations framework; it is not a political or diplomatic determination by
Xitcoin.

The complete 39-record consolidation mapping is maintained with the blockchain
source in
`networks/testnet/territorial-consolidation-2026.csv`.

## Complete allocation index

The first column displays locally hosted reference flags for navigation. They are non-authoritative and do not affect identity, eligibility or quantity. United Nations M49 and ISO identifiers remain canonical.

**Allocation currency: XTC**

| Flag | State | ISO | Pop. | Base | Variable | Total |
|---|---|---:|---:|---:|---:|---:|
| <img src="../.gitbook/assets/flags/af.svg" alt="Afghanistan flag" data-size="line"> | Afghanistan | AFG | 45 047 069 | 1 500 000 | 776 974 | **2 276 974** |
| <img src="../.gitbook/assets/flags/al.svg" alt="Albania flag" data-size="line"> | Albania | ALB | 2 751 025 | 1 500 000 | 192 008 | **1 692 008** |
| <img src="../.gitbook/assets/flags/dz.svg" alt="Algeria flag" data-size="line"> | Algeria | DZA | 48 028 334 | 1 500 000 | 802 272 | **2 302 272** |
| <img src="../.gitbook/assets/flags/ad.svg" alt="Andorra flag" data-size="line"> | Andorra | AND | 83 753 | 1 500 000 | 33 502 | **1 533 502** |
| <img src="../.gitbook/assets/flags/ao.svg" alt="Angola flag" data-size="line"> | Angola | AGO | 40 215 179 | 1 500 000 | 734 122 | **2 234 122** |
| <img src="../.gitbook/assets/flags/ag.svg" alt="Antigua and Barbuda flag" data-size="line"> | Antigua and Barbuda | ATG | 94 626 | 1 500 000 | 35 611 | **1 535 611** |
| <img src="../.gitbook/assets/flags/ar.svg" alt="Argentina flag" data-size="line"> | Argentina | ARG | 46 003 734 | 1 500 000 | 785 181 | **2 285 181** |
| <img src="../.gitbook/assets/flags/am.svg" alt="Armenia flag" data-size="line"> | Armenia | ARM | 2 930 915 | 1 500 000 | 198 187 | **1 698 187** |
| <img src="../.gitbook/assets/flags/au.svg" alt="Australia flag" data-size="line"> | Australia | AUS | 27 227 096 | 1 500 000 | 604 051 | **2 104 051** |
| <img src="../.gitbook/assets/flags/at.svg" alt="Austria flag" data-size="line"> | Austria | AUT | 9 107 266 | 1 500 000 | 349 355 | **1 849 355** |
| <img src="../.gitbook/assets/flags/az.svg" alt="Azerbaijan flag" data-size="line"> | Azerbaijan | AZE | 10 454 855 | 1 500 000 | 374 311 | **1 874 311** |
| <img src="../.gitbook/assets/flags/bs.svg" alt="Bahamas flag" data-size="line"> | Bahamas | BHS | 404 628 | 1 500 000 | 73 638 | **1 573 638** |
| <img src="../.gitbook/assets/flags/bh.svg" alt="Bahrain flag" data-size="line"> | Bahrain | BHR | 1 675 572 | 1 500 000 | 149 849 | **1 649 849** |
| <img src="../.gitbook/assets/flags/bd.svg" alt="Bangladesh flag" data-size="line"> | Bangladesh | BGD | 177 818 044 | 1 500 000 | 1 543 693 | **3 043 693** |
| <img src="../.gitbook/assets/flags/bb.svg" alt="Barbados flag" data-size="line"> | Barbados | BRB | 282 724 | 1 500 000 | 61 554 | **1 561 554** |
| <img src="../.gitbook/assets/flags/by.svg" alt="Belarus flag" data-size="line"> | Belarus | BLR | 8 937 018 | 1 500 000 | 346 074 | **1 846 074** |
| <img src="../.gitbook/assets/flags/be.svg" alt="Belgium flag" data-size="line"> | Belgium | BEL | 11 774 642 | 1 500 000 | 397 235 | **1 897 235** |
| <img src="../.gitbook/assets/flags/bz.svg" alt="Belize flag" data-size="line"> | Belize | BLZ | 428 644 | 1 500 000 | 75 792 | **1 575 792** |
| <img src="../.gitbook/assets/flags/bj.svg" alt="Benin flag" data-size="line"> | Benin | BEN | 15 170 419 | 1 500 000 | 450 891 | **1 950 891** |
| <img src="../.gitbook/assets/flags/bt.svg" alt="Bhutan flag" data-size="line"> | Bhutan | BTN | 802 214 | 1 500 000 | 103 686 | **1 603 686** |
| <img src="../.gitbook/assets/flags/bo.svg" alt="Bolivia (Plurinational State of) flag" data-size="line"> | Bolivia (Plurinational State of) | BOL | 12 749 291 | 1 500 000 | 413 348 | **1 913 348** |
| <img src="../.gitbook/assets/flags/ba.svg" alt="Bosnia and Herzegovina flag" data-size="line"> | Bosnia and Herzegovina | BIH | 3 114 242 | 1 500 000 | 204 291 | **1 704 291** |
| <img src="../.gitbook/assets/flags/bw.svg" alt="Botswana flag" data-size="line"> | Botswana | BWA | 2 603 388 | 1 500 000 | 186 785 | **1 686 785** |
| <img src="../.gitbook/assets/flags/br.svg" alt="Brazil flag" data-size="line"> | Brazil | BRA | 213 562 666 | 1 500 000 | 1 691 749 | **3 191 749** |
| <img src="../.gitbook/assets/flags/bn.svg" alt="Brunei Darussalam flag" data-size="line"> | Brunei Darussalam | BRN | 469 775 | 1 500 000 | 79 345 | **1 579 345** |
| <img src="../.gitbook/assets/flags/bg.svg" alt="Bulgaria flag" data-size="line"> | Bulgaria | BGR | 6 667 659 | 1 500 000 | 298 923 | **1 798 923** |
| <img src="../.gitbook/assets/flags/bf.svg" alt="Burkina Faso flag" data-size="line"> | Burkina Faso | BFA | 24 601 700 | 1 500 000 | 574 190 | **2 074 190** |
| <img src="../.gitbook/assets/flags/bi.svg" alt="Burundi flag" data-size="line"> | Burundi | BDI | 14 729 157 | 1 500 000 | 444 285 | **1 944 285** |
| <img src="../.gitbook/assets/flags/cv.svg" alt="Cabo Verde flag" data-size="line"> | Cabo Verde | CPV | 529 630 | 1 500 000 | 84 248 | **1 584 248** |
| <img src="../.gitbook/assets/flags/kh.svg" alt="Cambodia flag" data-size="line"> | Cambodia | KHM | 18 051 219 | 1 500 000 | 491 843 | **1 991 843** |
| <img src="../.gitbook/assets/flags/cm.svg" alt="Cameroon flag" data-size="line"> | Cameroon | CMR | 30 640 817 | 1 500 000 | 640 801 | **2 140 801** |
| <img src="../.gitbook/assets/flags/ca.svg" alt="Canada flag" data-size="line"> | Canada | CAN | 40 467 728 | 1 500 000 | 736 423 | **2 236 423** |
| <img src="../.gitbook/assets/flags/cf.svg" alt="Central African Republic flag" data-size="line"> | Central African Republic | CAF | 5 698 984 | 1 500 000 | 276 358 | **1 776 358** |
| <img src="../.gitbook/assets/flags/td.svg" alt="Chad flag" data-size="line"> | Chad | TCD | 21 560 380 | 1 500 000 | 537 528 | **2 037 528** |
| <img src="../.gitbook/assets/flags/cl.svg" alt="Chile flag" data-size="line"> | Chile | CHL | 19 945 850 | 1 500 000 | 517 011 | **2 017 011** |
| <img src="../.gitbook/assets/flags/cn.svg" alt="China flag" data-size="line"> | China | CHN | 1 444 027 171 | 1 500 000 | 4 399 069 | **5 899 069** |
| <img src="../.gitbook/assets/flags/co.svg" alt="Colombia flag" data-size="line"> | Colombia | COL | 53 936 226 | 1 500 000 | 850 185 | **2 350 185** |
| <img src="../.gitbook/assets/flags/km.svg" alt="Comoros flag" data-size="line"> | Comoros | COM | 899 010 | 1 500 000 | 109 763 | **1 609 763** |
| <img src="../.gitbook/assets/flags/cg.svg" alt="Congo flag" data-size="line"> | Congo | COG | 6 637 785 | 1 500 000 | 298 253 | **1 798 253** |
| <img src="../.gitbook/assets/flags/cr.svg" alt="Costa Rica flag" data-size="line"> | Costa Rica | CRI | 5 174 789 | 1 500 000 | 263 342 | **1 763 342** |
| <img src="../.gitbook/assets/flags/hr.svg" alt="Croatia flag" data-size="line"> | Croatia | HRV | 3 822 345 | 1 500 000 | 226 328 | **1 726 328** |
| <img src="../.gitbook/assets/flags/cu.svg" alt="Cuba flag" data-size="line"> | Cuba | CUB | 10 892 659 | 1 500 000 | 382 067 | **1 882 067** |
| <img src="../.gitbook/assets/flags/cy.svg" alt="Cyprus flag" data-size="line"> | Cyprus | CYP | 1 382 334 | 1 500 000 | 136 107 | **1 636 107** |
| <img src="../.gitbook/assets/flags/cz.svg" alt="Czechia flag" data-size="line"> | Czechia | CZE | 10 527 781 | 1 500 000 | 375 614 | **1 875 614** |
| <img src="../.gitbook/assets/flags/ci.svg" alt="Côte d'Ivoire flag" data-size="line"> | Côte d'Ivoire | CIV | 33 494 346 | 1 500 000 | 669 975 | **2 169 975** |
| <img src="../.gitbook/assets/flags/kp.svg" alt="Dem. People's Republic of Korea flag" data-size="line"> | Dem. People's Republic of Korea | PRK | 26 633 691 | 1 500 000 | 597 432 | **2 097 432** |
| <img src="../.gitbook/assets/flags/cd.svg" alt="Democratic Republic of the Congo flag" data-size="line"> | Democratic Republic of the Congo | COD | 116 452 162 | 1 500 000 | 1 249 243 | **2 749 243** |
| <img src="../.gitbook/assets/flags/dk.svg" alt="Denmark flag" data-size="line"> | Denmark | DNK | 6 135 675 | 1 500 000 | 286 751 | **1 786 751** |
| <img src="../.gitbook/assets/flags/dj.svg" alt="Djibouti flag" data-size="line"> | Djibouti | DJI | 1 199 459 | 1 500 000 | 126 784 | **1 626 784** |
| <img src="../.gitbook/assets/flags/dm.svg" alt="Dominica flag" data-size="line"> | Dominica | DMA | 65 511 | 1 500 000 | 29 630 | **1 529 630** |
| <img src="../.gitbook/assets/flags/do.svg" alt="Dominican Republic flag" data-size="line"> | Dominican Republic | DOM | 11 609 500 | 1 500 000 | 394 439 | **1 894 439** |
| <img src="../.gitbook/assets/flags/ec.svg" alt="Ecuador flag" data-size="line"> | Ecuador | ECU | 18 444 506 | 1 500 000 | 497 172 | **1 997 172** |
| <img src="../.gitbook/assets/flags/eg.svg" alt="Egypt flag" data-size="line"> | Egypt | EGY | 120 101 175 | 1 500 000 | 1 268 664 | **2 768 664** |
| <img src="../.gitbook/assets/flags/sv.svg" alt="El Salvador flag" data-size="line"> | El Salvador | SLV | 6 391 253 | 1 500 000 | 292 662 | **1 792 662** |
| <img src="../.gitbook/assets/flags/gq.svg" alt="Equatorial Guinea flag" data-size="line"> | Equatorial Guinea | GNQ | 1 984 468 | 1 500 000 | 163 078 | **1 663 078** |
| <img src="../.gitbook/assets/flags/er.svg" alt="Eritrea flag" data-size="line"> | Eritrea | ERI | 3 682 669 | 1 500 000 | 222 154 | **1 722 154** |
| <img src="../.gitbook/assets/flags/ee.svg" alt="Estonia flag" data-size="line"> | Estonia | EST | 1 331 062 | 1 500 000 | 133 559 | **1 633 559** |
| <img src="../.gitbook/assets/flags/sz.svg" alt="Eswatini flag" data-size="line"> | Eswatini | SWZ | 1 269 859 | 1 500 000 | 130 452 | **1 630 452** |
| <img src="../.gitbook/assets/flags/et.svg" alt="Ethiopia flag" data-size="line"> | Ethiopia | ETH | 138 902 185 | 1 500 000 | 1 364 356 | **2 864 356** |
| <img src="../.gitbook/assets/flags/fj.svg" alt="Fiji flag" data-size="line"> | Fiji | FJI | 937 282 | 1 500 000 | 112 075 | **1 612 075** |
| <img src="../.gitbook/assets/flags/fi.svg" alt="Finland flag" data-size="line"> | Finland | FIN | 5 621 739 | 1 500 000 | 274 479 | **1 774 479** |
| <img src="../.gitbook/assets/flags/fr.svg" alt="France flag" data-size="line"> | France | FRA | 69 642 313 | 1 500 000 | 966 073 | **2 466 073** |
| <img src="../.gitbook/assets/flags/ga.svg" alt="Gabon flag" data-size="line"> | Gabon | GAB | 2 647 399 | 1 500 000 | 188 357 | **1 688 357** |
| <img src="../.gitbook/assets/flags/gm.svg" alt="Gambia flag" data-size="line"> | Gambia | GMB | 2 884 079 | 1 500 000 | 196 597 | **1 696 597** |
| <img src="../.gitbook/assets/flags/ge.svg" alt="Georgia flag" data-size="line"> | Georgia | GEO | 3 804 642 | 1 500 000 | 225 803 | **1 725 803** |
| <img src="../.gitbook/assets/flags/de.svg" alt="Germany flag" data-size="line"> | Germany | DEU | 83 644 258 | 1 500 000 | 1 058 745 | **2 558 745** |
| <img src="../.gitbook/assets/flags/gh.svg" alt="Ghana flag" data-size="line"> | Ghana | GHA | 35 697 557 | 1 500 000 | 691 660 | **2 191 660** |
| <img src="../.gitbook/assets/flags/gr.svg" alt="Greece flag" data-size="line"> | Greece | GRC | 9 897 115 | 1 500 000 | 364 190 | **1 864 190** |
| <img src="../.gitbook/assets/flags/gd.svg" alt="Grenada flag" data-size="line"> | Grenada | GRD | 117 362 | 1 500 000 | 39 659 | **1 539 659** |
| <img src="../.gitbook/assets/flags/gt.svg" alt="Guatemala flag" data-size="line"> | Guatemala | GTM | 18 967 978 | 1 500 000 | 504 178 | **2 004 178** |
| <img src="../.gitbook/assets/flags/gn.svg" alt="Guinea flag" data-size="line"> | Guinea | GIN | 15 441 993 | 1 500 000 | 454 909 | **1 954 909** |
| <img src="../.gitbook/assets/flags/gw.svg" alt="Guinea-Bissau flag" data-size="line"> | Guinea-Bissau | GNB | 2 297 808 | 1 500 000 | 175 481 | **1 675 481** |
| <img src="../.gitbook/assets/flags/gy.svg" alt="Guyana flag" data-size="line"> | Guyana | GUY | 840 890 | 1 500 000 | 106 156 | **1 606 156** |
| <img src="../.gitbook/assets/flags/ht.svg" alt="Haiti flag" data-size="line"> | Haiti | HTI | 12 037 506 | 1 500 000 | 401 644 | **1 901 644** |
| <img src="../.gitbook/assets/flags/hn.svg" alt="Honduras flag" data-size="line"> | Honduras | HND | 11 184 760 | 1 500 000 | 387 156 | **1 887 156** |
| <img src="../.gitbook/assets/flags/hu.svg" alt="Hungary flag" data-size="line"> | Hungary | HUN | 9 585 818 | 1 500 000 | 358 416 | **1 858 416** |
| <img src="../.gitbook/assets/flags/is.svg" alt="Iceland flag" data-size="line"> | Iceland | ISL | 402 329 | 1 500 000 | 73 428 | **1 573 428** |
| <img src="../.gitbook/assets/flags/in.svg" alt="India flag" data-size="line"> | India | IND | 1 476 625 576 | 1 500 000 | 4 448 446 | **5 948 446** |
| <img src="../.gitbook/assets/flags/id.svg" alt="Indonesia flag" data-size="line"> | Indonesia | IDN | 287 886 782 | 1 500 000 | 1 964 192 | **3 464 192** |
| <img src="../.gitbook/assets/flags/ir.svg" alt="Iran (Islamic Republic of) flag" data-size="line"> | Iran (Islamic Republic of) | IRN | 93 168 497 | 1 500 000 | 1 117 397 | **2 617 397** |
| <img src="../.gitbook/assets/flags/iq.svg" alt="Iraq flag" data-size="line"> | Iraq | IRQ | 48 007 437 | 1 500 000 | 802 098 | **2 302 098** |
| <img src="../.gitbook/assets/flags/ie.svg" alt="Ireland flag" data-size="line"> | Ireland | IRL | 5 356 950 | 1 500 000 | 267 937 | **1 767 937** |
| <img src="../.gitbook/assets/flags/il.svg" alt="Israel flag" data-size="line"> | Israel | ISR | 9 647 689 | 1 500 000 | 359 571 | **1 859 571** |
| <img src="../.gitbook/assets/flags/it.svg" alt="Italy flag" data-size="line"> | Italy | ITA | 58 926 166 | 1 500 000 | 888 643 | **2 388 643** |
| <img src="../.gitbook/assets/flags/jm.svg" alt="Jamaica flag" data-size="line"> | Jamaica | JAM | 2 833 403 | 1 500 000 | 194 862 | **1 694 862** |
| <img src="../.gitbook/assets/flags/jp.svg" alt="Japan flag" data-size="line"> | Japan | JPN | 122 427 731 | 1 500 000 | 1 280 894 | **2 780 894** |
| <img src="../.gitbook/assets/flags/jo.svg" alt="Jordan flag" data-size="line"> | Jordan | JOR | 11 589 532 | 1 500 000 | 394 100 | **1 894 100** |
| <img src="../.gitbook/assets/flags/kz.svg" alt="Kazakhstan flag" data-size="line"> | Kazakhstan | KAZ | 21 083 626 | 1 500 000 | 531 552 | **2 031 552** |
| <img src="../.gitbook/assets/flags/ke.svg" alt="Kenya flag" data-size="line"> | Kenya | KEN | 58 636 412 | 1 500 000 | 886 455 | **2 386 455** |
| <img src="../.gitbook/assets/flags/ki.svg" alt="Kiribati flag" data-size="line"> | Kiribati | KIR | 138 445 | 1 500 000 | 43 074 | **1 543 074** |
| <img src="../.gitbook/assets/flags/kw.svg" alt="Kuwait flag" data-size="line"> | Kuwait | KWT | 5 102 773 | 1 500 000 | 261 503 | **1 761 503** |
| <img src="../.gitbook/assets/flags/kg.svg" alt="Kyrgyzstan flag" data-size="line"> | Kyrgyzstan | KGZ | 7 400 465 | 1 500 000 | 314 922 | **1 814 922** |
| <img src="../.gitbook/assets/flags/la.svg" alt="Lao People's Democratic Republic flag" data-size="line"> | Lao People's Democratic Republic | LAO | 7 974 017 | 1 500 000 | 326 898 | **1 826 898** |
| <img src="../.gitbook/assets/flags/lv.svg" alt="Latvia flag" data-size="line"> | Latvia | LVA | 1 835 935 | 1 500 000 | 156 856 | **1 656 856** |
| <img src="../.gitbook/assets/flags/lb.svg" alt="Lebanon flag" data-size="line"> | Lebanon | LBN | 5 897 467 | 1 500 000 | 281 129 | **1 781 129** |
| <img src="../.gitbook/assets/flags/ls.svg" alt="Lesotho flag" data-size="line"> | Lesotho | LSO | 2 389 336 | 1 500 000 | 178 942 | **1 678 942** |
| <img src="../.gitbook/assets/flags/lr.svg" alt="Liberia flag" data-size="line"> | Liberia | LBR | 5 853 949 | 1 500 000 | 280 090 | **1 780 090** |
| <img src="../.gitbook/assets/flags/ly.svg" alt="Libya flag" data-size="line"> | Libya | LBY | 7 539 851 | 1 500 000 | 317 874 | **1 817 874** |
| <img src="../.gitbook/assets/flags/li.svg" alt="Liechtenstein flag" data-size="line"> | Liechtenstein | LIE | 40 368 | 1 500 000 | 23 259 | **1 523 259** |
| <img src="../.gitbook/assets/flags/lt.svg" alt="Lithuania flag" data-size="line"> | Lithuania | LTU | 2 797 338 | 1 500 000 | 193 618 | **1 693 618** |
| <img src="../.gitbook/assets/flags/lu.svg" alt="Luxembourg flag" data-size="line"> | Luxembourg | LUX | 687 448 | 1 500 000 | 95 983 | **1 595 983** |
| <img src="../.gitbook/assets/flags/mg.svg" alt="Madagascar flag" data-size="line"> | Madagascar | MDG | 33 522 052 | 1 500 000 | 670 252 | **2 170 252** |
| <img src="../.gitbook/assets/flags/mw.svg" alt="Malawi flag" data-size="line"> | Malawi | MWI | 22 785 535 | 1 500 000 | 552 590 | **2 052 590** |
| <img src="../.gitbook/assets/flags/my.svg" alt="Malaysia flag" data-size="line"> | Malaysia | MYS | 36 385 115 | 1 500 000 | 698 289 | **2 198 289** |
| <img src="../.gitbook/assets/flags/mv.svg" alt="Maldives flag" data-size="line"> | Maldives | MDV | 531 517 | 1 500 000 | 84 398 | **1 584 398** |
| <img src="../.gitbook/assets/flags/ml.svg" alt="Mali flag" data-size="line"> | Mali | MLI | 25 932 275 | 1 500 000 | 589 513 | **2 089 513** |
| <img src="../.gitbook/assets/flags/mt.svg" alt="Malta flag" data-size="line"> | Malta | MLT | 549 011 | 1 500 000 | 85 776 | **1 585 776** |
| <img src="../.gitbook/assets/flags/mh.svg" alt="Marshall Islands flag" data-size="line"> | Marshall Islands | MHL | 35 075 | 1 500 000 | 21 681 | **1 521 681** |
| <img src="../.gitbook/assets/flags/mr.svg" alt="Mauritania flag" data-size="line"> | Mauritania | MRT | 5 461 319 | 1 500 000 | 270 534 | **1 770 534** |
| <img src="../.gitbook/assets/flags/mu.svg" alt="Mauritius flag" data-size="line"> | Mauritius | MUS | 1 265 059 | 1 500 000 | 130 205 | **1 630 205** |
| <img src="../.gitbook/assets/flags/mx.svg" alt="Mexico flag" data-size="line"> | Mexico | MEX | 132 997 658 | 1 500 000 | 1 335 043 | **2 835 043** |
| <img src="../.gitbook/assets/flags/fm.svg" alt="Micronesia (Fed. States of) flag" data-size="line"> | Micronesia (Fed. States of) | FSM | 114 183 | 1 500 000 | 39 118 | **1 539 118** |
| <img src="../.gitbook/assets/flags/mc.svg" alt="Monaco flag" data-size="line"> | Monaco | MCO | 38 087 | 1 500 000 | 22 592 | **1 522 592** |
| <img src="../.gitbook/assets/flags/mn.svg" alt="Mongolia flag" data-size="line"> | Mongolia | MNG | 3 556 798 | 1 500 000 | 218 325 | **1 718 325** |
| <img src="../.gitbook/assets/flags/me.svg" alt="Montenegro flag" data-size="line"> | Montenegro | MNE | 626 233 | 1 500 000 | 91 610 | **1 591 610** |
| <img src="../.gitbook/assets/flags/ma.svg" alt="Morocco flag" data-size="line"> | Morocco | MAR | 38 762 441 | 1 500 000 | 720 740 | **2 220 740** |
| <img src="../.gitbook/assets/flags/mz.svg" alt="Mozambique flag" data-size="line"> | Mozambique | MOZ | 36 639 851 | 1 500 000 | 700 729 | **2 200 729** |
| <img src="../.gitbook/assets/flags/mm.svg" alt="Myanmar flag" data-size="line"> | Myanmar | MMR | 55 184 819 | 1 500 000 | 859 969 | **2 359 969** |
| <img src="../.gitbook/assets/flags/na.svg" alt="Namibia flag" data-size="line"> | Namibia | NAM | 3 153 246 | 1 500 000 | 205 566 | **1 705 566** |
| <img src="../.gitbook/assets/flags/nr.svg" alt="Nauru flag" data-size="line"> | Nauru | NRU | 12 101 | 1 500 000 | 12 735 | **1 512 735** |
| <img src="../.gitbook/assets/flags/np.svg" alt="Nepal flag" data-size="line"> | Nepal | NPL | 29 629 410 | 1 500 000 | 630 136 | **2 130 136** |
| <img src="../.gitbook/assets/flags/nl.svg" alt="Netherlands flag" data-size="line"> | Netherlands | NLD | 18 818 739 | 1 500 000 | 502 190 | **2 002 190** |
| <img src="../.gitbook/assets/flags/nz.svg" alt="New Zealand flag" data-size="line"> | New Zealand | NZL | 5 290 170 | 1 500 000 | 266 261 | **1 766 261** |
| <img src="../.gitbook/assets/flags/ni.svg" alt="Nicaragua flag" data-size="line"> | Nicaragua | NIC | 7 097 329 | 1 500 000 | 308 404 | **1 808 404** |
| <img src="../.gitbook/assets/flags/ne.svg" alt="Niger flag" data-size="line"> | Niger | NER | 28 814 878 | 1 500 000 | 621 415 | **2 121 415** |
| <img src="../.gitbook/assets/flags/ng.svg" alt="Nigeria flag" data-size="line"> | Nigeria | NGA | 242 431 832 | 1 500 000 | 1 802 470 | **3 302 470** |
| <img src="../.gitbook/assets/flags/mk.svg" alt="North Macedonia flag" data-size="line"> | North Macedonia | MKD | 1 804 063 | 1 500 000 | 155 489 | **1 655 489** |
| <img src="../.gitbook/assets/flags/no.svg" alt="Norway flag" data-size="line"> | Norway | NOR | 5 652 989 | 1 500 000 | 275 240 | **1 775 240** |
| <img src="../.gitbook/assets/flags/om.svg" alt="Oman flag" data-size="line"> | Oman | OMN | 5 671 458 | 1 500 000 | 275 690 | **1 775 690** |
| <img src="../.gitbook/assets/flags/pk.svg" alt="Pakistan flag" data-size="line"> | Pakistan | PAK | 259 299 791 | 1 500 000 | 1 864 122 | **3 364 122** |
| <img src="../.gitbook/assets/flags/pw.svg" alt="Palau flag" data-size="line"> | Palau | PLW | 17 614 | 1 500 000 | 15 364 | **1 515 364** |
| <img src="../.gitbook/assets/flags/pa.svg" alt="Panama flag" data-size="line"> | Panama | PAN | 4 625 718 | 1 500 000 | 248 979 | **1 748 979** |
| <img src="../.gitbook/assets/flags/pg.svg" alt="Papua New Guinea flag" data-size="line"> | Papua New Guinea | PNG | 10 947 848 | 1 500 000 | 383 034 | **1 883 034** |
| <img src="../.gitbook/assets/flags/py.svg" alt="Paraguay flag" data-size="line"> | Paraguay | PRY | 7 095 279 | 1 500 000 | 308 360 | **1 808 360** |
| <img src="../.gitbook/assets/flags/pe.svg" alt="Peru flag" data-size="line"> | Peru | PER | 34 922 148 | 1 500 000 | 684 106 | **2 184 106** |
| <img src="../.gitbook/assets/flags/ph.svg" alt="Philippines flag" data-size="line"> | Philippines | PHL | 117 724 471 | 1 500 000 | 1 256 049 | **2 756 049** |
| <img src="../.gitbook/assets/flags/pl.svg" alt="Poland flag" data-size="line"> | Poland | POL | 37 843 188 | 1 500 000 | 712 143 | **2 212 143** |
| <img src="../.gitbook/assets/flags/pt.svg" alt="Portugal flag" data-size="line"> | Portugal | PRT | 10 395 362 | 1 500 000 | 373 244 | **1 873 244** |
| <img src="../.gitbook/assets/flags/qa.svg" alt="Qatar flag" data-size="line"> | Qatar | QAT | 3 173 559 | 1 500 000 | 206 227 | **1 706 227** |
| <img src="../.gitbook/assets/flags/kr.svg" alt="Republic of Korea flag" data-size="line"> | Republic of Korea | KOR | 51 600 388 | 1 500 000 | 831 572 | **2 331 572** |
| <img src="../.gitbook/assets/flags/md.svg" alt="Republic of Moldova flag" data-size="line"> | Republic of Moldova | MDA | 2 961 253 | 1 500 000 | 199 210 | **1 699 210** |
| <img src="../.gitbook/assets/flags/ro.svg" alt="Romania flag" data-size="line"> | Romania | ROU | 18 800 605 | 1 500 000 | 501 948 | **2 001 948** |
| <img src="../.gitbook/assets/flags/ru.svg" alt="Russian Federation flag" data-size="line"> | Russian Federation | RUS | 143 394 458 | 1 500 000 | 1 386 243 | **2 886 243** |
| <img src="../.gitbook/assets/flags/rw.svg" alt="Rwanda flag" data-size="line"> | Rwanda | RWA | 14 889 693 | 1 500 000 | 446 700 | **1 946 700** |
| <img src="../.gitbook/assets/flags/kn.svg" alt="Saint Kitts and Nevis flag" data-size="line"> | Saint Kitts and Nevis | KNA | 46 992 | 1 500 000 | 25 095 | **1 525 095** |
| <img src="../.gitbook/assets/flags/lc.svg" alt="Saint Lucia flag" data-size="line"> | Saint Lucia | LCA | 180 488 | 1 500 000 | 49 181 | **1 549 181** |
| <img src="../.gitbook/assets/flags/vc.svg" alt="Saint Vincent and the Grenadines flag" data-size="line"> | Saint Vincent and the Grenadines | VCT | 99 245 | 1 500 000 | 36 469 | **1 536 469** |
| <img src="../.gitbook/assets/flags/ws.svg" alt="Samoa flag" data-size="line"> | Samoa | WSM | 220 528 | 1 500 000 | 54 363 | **1 554 363** |
| <img src="../.gitbook/assets/flags/sm.svg" alt="San Marino flag" data-size="line"> | San Marino | SMR | 33 605 | 1 500 000 | 21 221 | **1 521 221** |
| <img src="../.gitbook/assets/flags/st.svg" alt="Sao Tome and Principe flag" data-size="line"> | Sao Tome and Principe | STP | 244 994 | 1 500 000 | 57 299 | **1 557 299** |
| <img src="../.gitbook/assets/flags/sa.svg" alt="Saudi Arabia flag" data-size="line"> | Saudi Arabia | SAU | 35 165 787 | 1 500 000 | 686 489 | **2 186 489** |
| <img src="../.gitbook/assets/flags/sn.svg" alt="Senegal flag" data-size="line"> | Senegal | SEN | 19 366 548 | 1 500 000 | 509 447 | **2 009 447** |
| <img src="../.gitbook/assets/flags/rs.svg" alt="Serbia flag" data-size="line"> | Serbia | SRB | 8 308 956 | 1 500 000 | 333 692 | **1 833 692** |
| <img src="../.gitbook/assets/flags/sc.svg" alt="Seychelles flag" data-size="line"> | Seychelles | SYC | 134 959 | 1 500 000 | 42 528 | **1 542 528** |
| <img src="../.gitbook/assets/flags/sl.svg" alt="Sierra Leone flag" data-size="line"> | Sierra Leone | SLE | 8 996 745 | 1 500 000 | 347 229 | **1 847 229** |
| <img src="../.gitbook/assets/flags/sg.svg" alt="Singapore flag" data-size="line"> | Singapore | SGP | 5 905 748 | 1 500 000 | 281 326 | **1 781 326** |
| <img src="../.gitbook/assets/flags/sk.svg" alt="Slovakia flag" data-size="line"> | Slovakia | SVK | 5 451 342 | 1 500 000 | 270 287 | **1 770 287** |
| <img src="../.gitbook/assets/flags/si.svg" alt="Slovenia flag" data-size="line"> | Slovenia | SVN | 2 114 573 | 1 500 000 | 168 339 | **1 668 339** |
| <img src="../.gitbook/assets/flags/sb.svg" alt="Solomon Islands flag" data-size="line"> | Solomon Islands | SLB | 858 288 | 1 500 000 | 107 248 | **1 607 248** |
| <img src="../.gitbook/assets/flags/so.svg" alt="Somalia flag" data-size="line"> | Somalia | SOM | 20 305 907 | 1 500 000 | 521 656 | **2 021 656** |
| <img src="../.gitbook/assets/flags/za.svg" alt="South Africa flag" data-size="line"> | South Africa | ZAF | 65 453 084 | 1 500 000 | 936 566 | **2 436 566** |
| <img src="../.gitbook/assets/flags/ss.svg" alt="South Sudan flag" data-size="line"> | South Sudan | SSD | 12 436 037 | 1 500 000 | 408 239 | **1 908 239** |
| <img src="../.gitbook/assets/flags/es.svg" alt="Spain flag" data-size="line"> | Spain | ESP | 47 850 793 | 1 500 000 | 800 788 | **2 300 788** |
| <img src="../.gitbook/assets/flags/lk.svg" alt="Sri Lanka flag" data-size="line"> | Sri Lanka | LKA | 23 348 315 | 1 500 000 | 559 372 | **2 059 372** |
| <img src="../.gitbook/assets/flags/sd.svg" alt="Sudan flag" data-size="line"> | Sudan | SDN | 53 282 719 | 1 500 000 | 845 019 | **2 345 019** |
| <img src="../.gitbook/assets/flags/sr.svg" alt="Suriname flag" data-size="line"> | Suriname | SUR | 645 256 | 1 500 000 | 92 991 | **1 592 991** |
| <img src="../.gitbook/assets/flags/se.svg" alt="Sweden flag" data-size="line"> | Sweden | SWE | 10 701 047 | 1 500 000 | 378 692 | **1 878 692** |
| <img src="../.gitbook/assets/flags/ch.svg" alt="Switzerland flag" data-size="line"> | Switzerland | CHE | 9 007 798 | 1 500 000 | 347 442 | **1 847 442** |
| <img src="../.gitbook/assets/flags/sy.svg" alt="Syrian Arab Republic flag" data-size="line"> | Syrian Arab Republic | SYR | 26 472 497 | 1 500 000 | 595 622 | **2 095 622** |
| <img src="../.gitbook/assets/flags/tj.svg" alt="Tajikistan flag" data-size="line"> | Tajikistan | TJK | 10 978 599 | 1 500 000 | 383 572 | **1 883 572** |
| <img src="../.gitbook/assets/flags/th.svg" alt="Thailand flag" data-size="line"> | Thailand | THA | 71 559 614 | 1 500 000 | 979 281 | **2 479 281** |
| <img src="../.gitbook/assets/flags/tl.svg" alt="Timor-Leste flag" data-size="line"> | Timor-Leste | TLS | 1 436 923 | 1 500 000 | 138 768 | **1 638 768** |
| <img src="../.gitbook/assets/flags/tg.svg" alt="Togo flag" data-size="line"> | Togo | TGO | 9 930 918 | 1 500 000 | 364 811 | **1 864 811** |
| <img src="../.gitbook/assets/flags/to.svg" alt="Tonga flag" data-size="line"> | Tonga | TON | 103 291 | 1 500 000 | 37 205 | **1 537 205** |
| <img src="../.gitbook/assets/flags/tt.svg" alt="Trinidad and Tobago flag" data-size="line"> | Trinidad and Tobago | TTO | 1 513 268 | 1 500 000 | 142 407 | **1 642 407** |
| <img src="../.gitbook/assets/flags/tn.svg" alt="Tunisia flag" data-size="line"> | Tunisia | TUN | 12 415 138 | 1 500 000 | 407 895 | **1 907 895** |
| <img src="../.gitbook/assets/flags/tm.svg" alt="Turkmenistan flag" data-size="line"> | Turkmenistan | TKM | 7 736 632 | 1 500 000 | 321 995 | **1 821 995** |
| <img src="../.gitbook/assets/flags/tv.svg" alt="Tuvalu flag" data-size="line"> | Tuvalu | TUV | 9 362 | 1 500 000 | 11 201 | **1 511 201** |
| <img src="../.gitbook/assets/flags/tr.svg" alt="Türkiye flag" data-size="line"> | Türkiye | TUR | 87 926 082 | 1 500 000 | 1 085 505 | **2 585 505** |
| <img src="../.gitbook/assets/flags/ug.svg" alt="Uganda flag" data-size="line"> | Uganda | UGA | 52 761 469 | 1 500 000 | 840 875 | **2 340 875** |
| <img src="../.gitbook/assets/flags/ua.svg" alt="Ukraine flag" data-size="line"> | Ukraine | UKR | 39 535 849 | 1 500 000 | 727 895 | **2 227 895** |
| <img src="../.gitbook/assets/flags/ae.svg" alt="United Arab Emirates flag" data-size="line"> | United Arab Emirates | ARE | 11 574 682 | 1 500 000 | 393 847 | **1 893 847** |
| <img src="../.gitbook/assets/flags/gb.svg" alt="United Kingdom flag" data-size="line"> | United Kingdom | GBR | 70 481 661 | 1 500 000 | 971 877 | **2 471 877** |
| <img src="../.gitbook/assets/flags/tz.svg" alt="United Republic of Tanzania flag" data-size="line"> | United Republic of Tanzania | TZA | 72 563 780 | 1 500 000 | 986 128 | **2 486 128** |
| <img src="../.gitbook/assets/flags/us.svg" alt="United States of America flag" data-size="line"> | United States of America | USA | 352 600 000 | 1 500 000 | 2 173 773 | **3 673 773** |
| <img src="../.gitbook/assets/flags/uy.svg" alt="Uruguay flag" data-size="line"> | Uruguay | URY | 3 382 537 | 1 500 000 | 212 909 | **1 712 909** |
| <img src="../.gitbook/assets/flags/uz.svg" alt="Uzbekistan flag" data-size="line"> | Uzbekistan | UZB | 37 724 223 | 1 500 000 | 711 022 | **2 211 022** |
| <img src="../.gitbook/assets/flags/vu.svg" alt="Vanuatu flag" data-size="line"> | Vanuatu | VUT | 342 564 | 1 500 000 | 67 755 | **1 567 755** |
| <img src="../.gitbook/assets/flags/ve.svg" alt="Venezuela (Bolivarian Republic of) flag" data-size="line"> | Venezuela (Bolivarian Republic of) | VEN | 28 633 711 | 1 500 000 | 619 458 | **2 119 458** |
| <img src="../.gitbook/assets/flags/vn.svg" alt="Viet Nam flag" data-size="line"> | Viet Nam | VNM | 102 177 431 | 1 500 000 | 1 170 174 | **2 670 174** |
| <img src="../.gitbook/assets/flags/ye.svg" alt="Yemen flag" data-size="line"> | Yemen | YEM | 42 961 653 | 1 500 000 | 758 776 | **2 258 776** |
| <img src="../.gitbook/assets/flags/zm.svg" alt="Zambia flag" data-size="line"> | Zambia | ZMB | 22 521 915 | 1 500 000 | 549 384 | **2 049 384** |
| <img src="../.gitbook/assets/flags/zw.svg" alt="Zimbabwe flag" data-size="line"> | Zimbabwe | ZWE | 17 273 580 | 1 500 000 | 481 132 | **1 981 132** |

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

During eligible service, the protocol calculates the vested and claimable amounts at the current block:

$\displaystyle V_i(b) = A_i \times \frac{\min\left(E_i(b), B_{5y}\right)}{B_{5y}}$

$\displaystyle C_i(b) = V_i(b) - R_i(b)$

**Formula key**

- **i** — the activated Member-State position being calculated;
- **b** — the current blockchain block used for the calculation;
- **Aᵢ** — the position's fixed reference allocation;
- **Eᵢ(b)** — its eligible service completed by the current block;
- **B₅ᵧ** — the configured number of blocks representing five years of eligible service;
- **Vᵢ(b)** — the total amount vested by the current block;
- **Rᵢ(b)** — the vested amount already released;
- **Cᵢ(b)** — the amount currently available to claim.

In plain language, the first formula releases the fixed allocation progressively during five years of eligible service. The second subtracts amounts already released to determine what remains claimable.

The authorized institutional controller may claim the accrued amount at any time. An unclaimed amount remains recorded as claimable.

If the position no longer satisfies the applicable institutional, staking, availability or security conditions, future accrual pauses. Reactivation resumes the schedule without retroactive accrual for the suspended interval. An amount already vested cannot be removed arbitrarily.

The reserve is fixed at 386,000,000 XTC. This release does not create new supply.

## Institutional continuity

Each position remains attached to the relevant State. It is not attached permanently to a president, minister, administration, individual signatory or infrastructure provider.

Successive administrations of the same State may transfer the institutional governance and operating mandate to their authorized successors without replacing the State position, its history or its remaining allocation.

A mandate transition may update the responsible representatives, mandatary, operator and payment instructions. The former team loses its authority when its mandate expires or is revoked. The State position continues under the authorized successor.

Buying tokens from a State or former operator does not grant control of the State position.

## Ordinary validator rights

Sovereign allocation and ordinary validator rewards are separate.

An activated sovereign validator participates under the same ordinary staking, commission, delegation, fee-distribution and slashing rules as other eligible validators. The sovereign position receives its finite allocation over five years while also participating in ordinary network rewards.

After five years of eligible service have fully vested, no further sovereign allocation is created. The position may continue validating and receiving ordinary network rewards while it remains eligible.

## How an institutional review begins

A public authority or formally authorized representative may initiate a review through the [institutional contact pathway](../start/official-links.md).

The first contact creates a case reference only. Before any application is accepted, KCALB LTD independently verifies the public institution, official-domain contact, authority of the representative and operating mandate through separate official sources and a secure communication channel.

Personal email, social-media identity or submitted documentation alone never proves governmental authority. No credentials, private keys or confidential identity documents should be sent through social media.

No position activates automatically. Activation requires verified institutional authority, the five-million-XTC self-delegation, operational review and explicit on-chain admission.


## Validator-capacity governance

The target network capacity remains **258 validator positions**: 193 reserved
Member-State positions and 65 general validator positions.

An approved increase in the reserved category reduces the general category by
the same number of positions. An approved decrease increases the general
category by the same number. Changing the total capacity requires a separate
on-chain governance decision.

Registry changes require an objective change in United Nations membership and
an explicit governance proposal. No change may create tokens, rewrite vested
allocations or reduce accrued rights. A new allocation must identify an
available, unallocated funding source.

## Current boundary

The sovereign position registry, institutional succession controls and activation-based vesting mechanism are under development and are not deployed. No application, position or allocation is active at this stage.

## Methodological scope and legal neutrality

For reproducibility, the reserved registry follows the 193 United Nations Member States recorded at the reference date. Xitcoin applies that external membership list as an objective technical criterion and does not create a separate diplomatic classification.

A future membership change does not modify the registry automatically. It requires an on-chain governance proposal, objective supporting evidence and the capacity and funding controls defined by the protocol. The process cannot create supply, rewrite vested allocations or reduce accrued rights.

The complete allocation data and technical verification sources are maintained in the Xitcoin blockchain repository:

- `docs/sovereign-allocation-2026.md`;
- `docs/sovereign-validator-framework.md`;
- `networks/testnet/sovereign-allocation-index-2026.csv`;
- `networks/testnet/sovereign-allocation-index-2026.json`;
- `networks/testnet/territorial-consolidation-2026.csv`;
- `scripts/verify-sovereign-allocation-2026.py`.
