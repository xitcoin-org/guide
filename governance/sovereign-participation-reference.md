---
description: Methodology, allocation reference and participation requirements for institutional validator positions.
icon: globe
---

# Sovereign Participation Reference 2026

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

Before rounding to integer XTC, the reference quantity for position $i$ is:

$A_i = 386{,}000{,}000 \left( \frac{0.75}{193} + 0.25 \frac{\sqrt{P_i}}{\sum_{j=1}^{193}\sqrt{P_j}} \right)$

Here, $P_i$ is the consolidated population reference for 1 July 2026.

The square-root function recognizes population differences while limiting concentration: four times the population produces twice the demographic weight, rather than four times the weight.

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

## Complete Xitcoin Sovereign Reference Index 2026

The first column displays locally hosted reference flags for navigation. They are non-authoritative and do not affect identity, eligibility or quantity. United Nations M49 and ISO identifiers remain canonical.

| Flag | Member State | ISO3 | Population | Equal | Demographic | Total allocation |
|---|---|---:|---:|---:|---:|---:|
| <img src="../.gitbook/assets/flags/af.svg" alt="Afghanistan flag" width="40"> | Afghanistan | AFG | 45 047 069 | 1 500 000&nbsp;XTC | 776 974&nbsp;XTC | **2 276 974&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/al.svg" alt="Albania flag" width="40"> | Albania | ALB | 2 751 025 | 1 500 000&nbsp;XTC | 192 008&nbsp;XTC | **1 692 008&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/dz.svg" alt="Algeria flag" width="40"> | Algeria | DZA | 48 028 334 | 1 500 000&nbsp;XTC | 802 272&nbsp;XTC | **2 302 272&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ad.svg" alt="Andorra flag" width="40"> | Andorra | AND | 83 753 | 1 500 000&nbsp;XTC | 33 502&nbsp;XTC | **1 533 502&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ao.svg" alt="Angola flag" width="40"> | Angola | AGO | 40 215 179 | 1 500 000&nbsp;XTC | 734 122&nbsp;XTC | **2 234 122&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ag.svg" alt="Antigua and Barbuda flag" width="40"> | Antigua and Barbuda | ATG | 94 626 | 1 500 000&nbsp;XTC | 35 611&nbsp;XTC | **1 535 611&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ar.svg" alt="Argentina flag" width="40"> | Argentina | ARG | 46 003 734 | 1 500 000&nbsp;XTC | 785 181&nbsp;XTC | **2 285 181&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/am.svg" alt="Armenia flag" width="40"> | Armenia | ARM | 2 930 915 | 1 500 000&nbsp;XTC | 198 187&nbsp;XTC | **1 698 187&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/au.svg" alt="Australia flag" width="40"> | Australia | AUS | 27 227 096 | 1 500 000&nbsp;XTC | 604 051&nbsp;XTC | **2 104 051&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/at.svg" alt="Austria flag" width="40"> | Austria | AUT | 9 107 266 | 1 500 000&nbsp;XTC | 349 355&nbsp;XTC | **1 849 355&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/az.svg" alt="Azerbaijan flag" width="40"> | Azerbaijan | AZE | 10 454 855 | 1 500 000&nbsp;XTC | 374 311&nbsp;XTC | **1 874 311&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bs.svg" alt="Bahamas flag" width="40"> | Bahamas | BHS | 404 628 | 1 500 000&nbsp;XTC | 73 638&nbsp;XTC | **1 573 638&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bh.svg" alt="Bahrain flag" width="40"> | Bahrain | BHR | 1 675 572 | 1 500 000&nbsp;XTC | 149 849&nbsp;XTC | **1 649 849&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bd.svg" alt="Bangladesh flag" width="40"> | Bangladesh | BGD | 177 818 044 | 1 500 000&nbsp;XTC | 1 543 693&nbsp;XTC | **3 043 693&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bb.svg" alt="Barbados flag" width="40"> | Barbados | BRB | 282 724 | 1 500 000&nbsp;XTC | 61 554&nbsp;XTC | **1 561 554&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/by.svg" alt="Belarus flag" width="40"> | Belarus | BLR | 8 937 018 | 1 500 000&nbsp;XTC | 346 074&nbsp;XTC | **1 846 074&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/be.svg" alt="Belgium flag" width="40"> | Belgium | BEL | 11 774 642 | 1 500 000&nbsp;XTC | 397 235&nbsp;XTC | **1 897 235&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bz.svg" alt="Belize flag" width="40"> | Belize | BLZ | 428 644 | 1 500 000&nbsp;XTC | 75 792&nbsp;XTC | **1 575 792&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bj.svg" alt="Benin flag" width="40"> | Benin | BEN | 15 170 419 | 1 500 000&nbsp;XTC | 450 891&nbsp;XTC | **1 950 891&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bt.svg" alt="Bhutan flag" width="40"> | Bhutan | BTN | 802 214 | 1 500 000&nbsp;XTC | 103 686&nbsp;XTC | **1 603 686&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bo.svg" alt="Bolivia (Plurinational State of) flag" width="40"> | Bolivia (Plurinational State of) | BOL | 12 749 291 | 1 500 000&nbsp;XTC | 413 348&nbsp;XTC | **1 913 348&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ba.svg" alt="Bosnia and Herzegovina flag" width="40"> | Bosnia and Herzegovina | BIH | 3 114 242 | 1 500 000&nbsp;XTC | 204 291&nbsp;XTC | **1 704 291&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bw.svg" alt="Botswana flag" width="40"> | Botswana | BWA | 2 603 388 | 1 500 000&nbsp;XTC | 186 785&nbsp;XTC | **1 686 785&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/br.svg" alt="Brazil flag" width="40"> | Brazil | BRA | 213 562 666 | 1 500 000&nbsp;XTC | 1 691 749&nbsp;XTC | **3 191 749&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bn.svg" alt="Brunei Darussalam flag" width="40"> | Brunei Darussalam | BRN | 469 775 | 1 500 000&nbsp;XTC | 79 345&nbsp;XTC | **1 579 345&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bg.svg" alt="Bulgaria flag" width="40"> | Bulgaria | BGR | 6 667 659 | 1 500 000&nbsp;XTC | 298 923&nbsp;XTC | **1 798 923&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bf.svg" alt="Burkina Faso flag" width="40"> | Burkina Faso | BFA | 24 601 700 | 1 500 000&nbsp;XTC | 574 190&nbsp;XTC | **2 074 190&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/bi.svg" alt="Burundi flag" width="40"> | Burundi | BDI | 14 729 157 | 1 500 000&nbsp;XTC | 444 285&nbsp;XTC | **1 944 285&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cv.svg" alt="Cabo Verde flag" width="40"> | Cabo Verde | CPV | 529 630 | 1 500 000&nbsp;XTC | 84 248&nbsp;XTC | **1 584 248&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kh.svg" alt="Cambodia flag" width="40"> | Cambodia | KHM | 18 051 219 | 1 500 000&nbsp;XTC | 491 843&nbsp;XTC | **1 991 843&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cm.svg" alt="Cameroon flag" width="40"> | Cameroon | CMR | 30 640 817 | 1 500 000&nbsp;XTC | 640 801&nbsp;XTC | **2 140 801&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ca.svg" alt="Canada flag" width="40"> | Canada | CAN | 40 467 728 | 1 500 000&nbsp;XTC | 736 423&nbsp;XTC | **2 236 423&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cf.svg" alt="Central African Republic flag" width="40"> | Central African Republic | CAF | 5 698 984 | 1 500 000&nbsp;XTC | 276 358&nbsp;XTC | **1 776 358&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/td.svg" alt="Chad flag" width="40"> | Chad | TCD | 21 560 380 | 1 500 000&nbsp;XTC | 537 528&nbsp;XTC | **2 037 528&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cl.svg" alt="Chile flag" width="40"> | Chile | CHL | 19 945 850 | 1 500 000&nbsp;XTC | 517 011&nbsp;XTC | **2 017 011&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cn.svg" alt="China flag" width="40"> | China | CHN | 1 444 027 171 | 1 500 000&nbsp;XTC | 4 399 069&nbsp;XTC | **5 899 069&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/co.svg" alt="Colombia flag" width="40"> | Colombia | COL | 53 936 226 | 1 500 000&nbsp;XTC | 850 185&nbsp;XTC | **2 350 185&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/km.svg" alt="Comoros flag" width="40"> | Comoros | COM | 899 010 | 1 500 000&nbsp;XTC | 109 763&nbsp;XTC | **1 609 763&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cg.svg" alt="Congo flag" width="40"> | Congo | COG | 6 637 785 | 1 500 000&nbsp;XTC | 298 253&nbsp;XTC | **1 798 253&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cr.svg" alt="Costa Rica flag" width="40"> | Costa Rica | CRI | 5 174 789 | 1 500 000&nbsp;XTC | 263 342&nbsp;XTC | **1 763 342&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/hr.svg" alt="Croatia flag" width="40"> | Croatia | HRV | 3 822 345 | 1 500 000&nbsp;XTC | 226 328&nbsp;XTC | **1 726 328&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cu.svg" alt="Cuba flag" width="40"> | Cuba | CUB | 10 892 659 | 1 500 000&nbsp;XTC | 382 067&nbsp;XTC | **1 882 067&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cy.svg" alt="Cyprus flag" width="40"> | Cyprus | CYP | 1 382 334 | 1 500 000&nbsp;XTC | 136 107&nbsp;XTC | **1 636 107&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cz.svg" alt="Czechia flag" width="40"> | Czechia | CZE | 10 527 781 | 1 500 000&nbsp;XTC | 375 614&nbsp;XTC | **1 875 614&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ci.svg" alt="Côte d'Ivoire flag" width="40"> | Côte d'Ivoire | CIV | 33 494 346 | 1 500 000&nbsp;XTC | 669 975&nbsp;XTC | **2 169 975&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kp.svg" alt="Dem. People's Republic of Korea flag" width="40"> | Dem. People's Republic of Korea | PRK | 26 633 691 | 1 500 000&nbsp;XTC | 597 432&nbsp;XTC | **2 097 432&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/cd.svg" alt="Democratic Republic of the Congo flag" width="40"> | Democratic Republic of the Congo | COD | 116 452 162 | 1 500 000&nbsp;XTC | 1 249 243&nbsp;XTC | **2 749 243&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/dk.svg" alt="Denmark flag" width="40"> | Denmark | DNK | 6 135 675 | 1 500 000&nbsp;XTC | 286 751&nbsp;XTC | **1 786 751&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/dj.svg" alt="Djibouti flag" width="40"> | Djibouti | DJI | 1 199 459 | 1 500 000&nbsp;XTC | 126 784&nbsp;XTC | **1 626 784&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/dm.svg" alt="Dominica flag" width="40"> | Dominica | DMA | 65 511 | 1 500 000&nbsp;XTC | 29 630&nbsp;XTC | **1 529 630&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/do.svg" alt="Dominican Republic flag" width="40"> | Dominican Republic | DOM | 11 609 500 | 1 500 000&nbsp;XTC | 394 439&nbsp;XTC | **1 894 439&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ec.svg" alt="Ecuador flag" width="40"> | Ecuador | ECU | 18 444 506 | 1 500 000&nbsp;XTC | 497 172&nbsp;XTC | **1 997 172&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/eg.svg" alt="Egypt flag" width="40"> | Egypt | EGY | 120 101 175 | 1 500 000&nbsp;XTC | 1 268 664&nbsp;XTC | **2 768 664&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sv.svg" alt="El Salvador flag" width="40"> | El Salvador | SLV | 6 391 253 | 1 500 000&nbsp;XTC | 292 662&nbsp;XTC | **1 792 662&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gq.svg" alt="Equatorial Guinea flag" width="40"> | Equatorial Guinea | GNQ | 1 984 468 | 1 500 000&nbsp;XTC | 163 078&nbsp;XTC | **1 663 078&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/er.svg" alt="Eritrea flag" width="40"> | Eritrea | ERI | 3 682 669 | 1 500 000&nbsp;XTC | 222 154&nbsp;XTC | **1 722 154&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ee.svg" alt="Estonia flag" width="40"> | Estonia | EST | 1 331 062 | 1 500 000&nbsp;XTC | 133 559&nbsp;XTC | **1 633 559&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sz.svg" alt="Eswatini flag" width="40"> | Eswatini | SWZ | 1 269 859 | 1 500 000&nbsp;XTC | 130 452&nbsp;XTC | **1 630 452&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/et.svg" alt="Ethiopia flag" width="40"> | Ethiopia | ETH | 138 902 185 | 1 500 000&nbsp;XTC | 1 364 356&nbsp;XTC | **2 864 356&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/fj.svg" alt="Fiji flag" width="40"> | Fiji | FJI | 937 282 | 1 500 000&nbsp;XTC | 112 075&nbsp;XTC | **1 612 075&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/fi.svg" alt="Finland flag" width="40"> | Finland | FIN | 5 621 739 | 1 500 000&nbsp;XTC | 274 479&nbsp;XTC | **1 774 479&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/fr.svg" alt="France flag" width="40"> | France | FRA | 69 642 313 | 1 500 000&nbsp;XTC | 966 073&nbsp;XTC | **2 466 073&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ga.svg" alt="Gabon flag" width="40"> | Gabon | GAB | 2 647 399 | 1 500 000&nbsp;XTC | 188 357&nbsp;XTC | **1 688 357&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gm.svg" alt="Gambia flag" width="40"> | Gambia | GMB | 2 884 079 | 1 500 000&nbsp;XTC | 196 597&nbsp;XTC | **1 696 597&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ge.svg" alt="Georgia flag" width="40"> | Georgia | GEO | 3 804 642 | 1 500 000&nbsp;XTC | 225 803&nbsp;XTC | **1 725 803&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/de.svg" alt="Germany flag" width="40"> | Germany | DEU | 83 644 258 | 1 500 000&nbsp;XTC | 1 058 745&nbsp;XTC | **2 558 745&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gh.svg" alt="Ghana flag" width="40"> | Ghana | GHA | 35 697 557 | 1 500 000&nbsp;XTC | 691 660&nbsp;XTC | **2 191 660&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gr.svg" alt="Greece flag" width="40"> | Greece | GRC | 9 897 115 | 1 500 000&nbsp;XTC | 364 190&nbsp;XTC | **1 864 190&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gd.svg" alt="Grenada flag" width="40"> | Grenada | GRD | 117 362 | 1 500 000&nbsp;XTC | 39 659&nbsp;XTC | **1 539 659&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gt.svg" alt="Guatemala flag" width="40"> | Guatemala | GTM | 18 967 978 | 1 500 000&nbsp;XTC | 504 178&nbsp;XTC | **2 004 178&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gn.svg" alt="Guinea flag" width="40"> | Guinea | GIN | 15 441 993 | 1 500 000&nbsp;XTC | 454 909&nbsp;XTC | **1 954 909&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gw.svg" alt="Guinea-Bissau flag" width="40"> | Guinea-Bissau | GNB | 2 297 808 | 1 500 000&nbsp;XTC | 175 481&nbsp;XTC | **1 675 481&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gy.svg" alt="Guyana flag" width="40"> | Guyana | GUY | 840 890 | 1 500 000&nbsp;XTC | 106 156&nbsp;XTC | **1 606 156&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ht.svg" alt="Haiti flag" width="40"> | Haiti | HTI | 12 037 506 | 1 500 000&nbsp;XTC | 401 644&nbsp;XTC | **1 901 644&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/hn.svg" alt="Honduras flag" width="40"> | Honduras | HND | 11 184 760 | 1 500 000&nbsp;XTC | 387 156&nbsp;XTC | **1 887 156&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/hu.svg" alt="Hungary flag" width="40"> | Hungary | HUN | 9 585 818 | 1 500 000&nbsp;XTC | 358 416&nbsp;XTC | **1 858 416&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/is.svg" alt="Iceland flag" width="40"> | Iceland | ISL | 402 329 | 1 500 000&nbsp;XTC | 73 428&nbsp;XTC | **1 573 428&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/in.svg" alt="India flag" width="40"> | India | IND | 1 476 625 576 | 1 500 000&nbsp;XTC | 4 448 446&nbsp;XTC | **5 948 446&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/id.svg" alt="Indonesia flag" width="40"> | Indonesia | IDN | 287 886 782 | 1 500 000&nbsp;XTC | 1 964 192&nbsp;XTC | **3 464 192&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ir.svg" alt="Iran (Islamic Republic of) flag" width="40"> | Iran (Islamic Republic of) | IRN | 93 168 497 | 1 500 000&nbsp;XTC | 1 117 397&nbsp;XTC | **2 617 397&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/iq.svg" alt="Iraq flag" width="40"> | Iraq | IRQ | 48 007 437 | 1 500 000&nbsp;XTC | 802 098&nbsp;XTC | **2 302 098&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ie.svg" alt="Ireland flag" width="40"> | Ireland | IRL | 5 356 950 | 1 500 000&nbsp;XTC | 267 937&nbsp;XTC | **1 767 937&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/il.svg" alt="Israel flag" width="40"> | Israel | ISR | 9 647 689 | 1 500 000&nbsp;XTC | 359 571&nbsp;XTC | **1 859 571&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/it.svg" alt="Italy flag" width="40"> | Italy | ITA | 58 926 166 | 1 500 000&nbsp;XTC | 888 643&nbsp;XTC | **2 388 643&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/jm.svg" alt="Jamaica flag" width="40"> | Jamaica | JAM | 2 833 403 | 1 500 000&nbsp;XTC | 194 862&nbsp;XTC | **1 694 862&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/jp.svg" alt="Japan flag" width="40"> | Japan | JPN | 122 427 731 | 1 500 000&nbsp;XTC | 1 280 894&nbsp;XTC | **2 780 894&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/jo.svg" alt="Jordan flag" width="40"> | Jordan | JOR | 11 589 532 | 1 500 000&nbsp;XTC | 394 100&nbsp;XTC | **1 894 100&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kz.svg" alt="Kazakhstan flag" width="40"> | Kazakhstan | KAZ | 21 083 626 | 1 500 000&nbsp;XTC | 531 552&nbsp;XTC | **2 031 552&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ke.svg" alt="Kenya flag" width="40"> | Kenya | KEN | 58 636 412 | 1 500 000&nbsp;XTC | 886 455&nbsp;XTC | **2 386 455&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ki.svg" alt="Kiribati flag" width="40"> | Kiribati | KIR | 138 445 | 1 500 000&nbsp;XTC | 43 074&nbsp;XTC | **1 543 074&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kw.svg" alt="Kuwait flag" width="40"> | Kuwait | KWT | 5 102 773 | 1 500 000&nbsp;XTC | 261 503&nbsp;XTC | **1 761 503&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kg.svg" alt="Kyrgyzstan flag" width="40"> | Kyrgyzstan | KGZ | 7 400 465 | 1 500 000&nbsp;XTC | 314 922&nbsp;XTC | **1 814 922&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/la.svg" alt="Lao People's Democratic Republic flag" width="40"> | Lao People's Democratic Republic | LAO | 7 974 017 | 1 500 000&nbsp;XTC | 326 898&nbsp;XTC | **1 826 898&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lv.svg" alt="Latvia flag" width="40"> | Latvia | LVA | 1 835 935 | 1 500 000&nbsp;XTC | 156 856&nbsp;XTC | **1 656 856&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lb.svg" alt="Lebanon flag" width="40"> | Lebanon | LBN | 5 897 467 | 1 500 000&nbsp;XTC | 281 129&nbsp;XTC | **1 781 129&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ls.svg" alt="Lesotho flag" width="40"> | Lesotho | LSO | 2 389 336 | 1 500 000&nbsp;XTC | 178 942&nbsp;XTC | **1 678 942&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lr.svg" alt="Liberia flag" width="40"> | Liberia | LBR | 5 853 949 | 1 500 000&nbsp;XTC | 280 090&nbsp;XTC | **1 780 090&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ly.svg" alt="Libya flag" width="40"> | Libya | LBY | 7 539 851 | 1 500 000&nbsp;XTC | 317 874&nbsp;XTC | **1 817 874&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/li.svg" alt="Liechtenstein flag" width="40"> | Liechtenstein | LIE | 40 368 | 1 500 000&nbsp;XTC | 23 259&nbsp;XTC | **1 523 259&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lt.svg" alt="Lithuania flag" width="40"> | Lithuania | LTU | 2 797 338 | 1 500 000&nbsp;XTC | 193 618&nbsp;XTC | **1 693 618&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lu.svg" alt="Luxembourg flag" width="40"> | Luxembourg | LUX | 687 448 | 1 500 000&nbsp;XTC | 95 983&nbsp;XTC | **1 595 983&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mg.svg" alt="Madagascar flag" width="40"> | Madagascar | MDG | 33 522 052 | 1 500 000&nbsp;XTC | 670 252&nbsp;XTC | **2 170 252&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mw.svg" alt="Malawi flag" width="40"> | Malawi | MWI | 22 785 535 | 1 500 000&nbsp;XTC | 552 590&nbsp;XTC | **2 052 590&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/my.svg" alt="Malaysia flag" width="40"> | Malaysia | MYS | 36 385 115 | 1 500 000&nbsp;XTC | 698 289&nbsp;XTC | **2 198 289&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mv.svg" alt="Maldives flag" width="40"> | Maldives | MDV | 531 517 | 1 500 000&nbsp;XTC | 84 398&nbsp;XTC | **1 584 398&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ml.svg" alt="Mali flag" width="40"> | Mali | MLI | 25 932 275 | 1 500 000&nbsp;XTC | 589 513&nbsp;XTC | **2 089 513&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mt.svg" alt="Malta flag" width="40"> | Malta | MLT | 549 011 | 1 500 000&nbsp;XTC | 85 776&nbsp;XTC | **1 585 776&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mh.svg" alt="Marshall Islands flag" width="40"> | Marshall Islands | MHL | 35 075 | 1 500 000&nbsp;XTC | 21 681&nbsp;XTC | **1 521 681&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mr.svg" alt="Mauritania flag" width="40"> | Mauritania | MRT | 5 461 319 | 1 500 000&nbsp;XTC | 270 534&nbsp;XTC | **1 770 534&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mu.svg" alt="Mauritius flag" width="40"> | Mauritius | MUS | 1 265 059 | 1 500 000&nbsp;XTC | 130 205&nbsp;XTC | **1 630 205&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mx.svg" alt="Mexico flag" width="40"> | Mexico | MEX | 132 997 658 | 1 500 000&nbsp;XTC | 1 335 043&nbsp;XTC | **2 835 043&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/fm.svg" alt="Micronesia (Fed. States of) flag" width="40"> | Micronesia (Fed. States of) | FSM | 114 183 | 1 500 000&nbsp;XTC | 39 118&nbsp;XTC | **1 539 118&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mc.svg" alt="Monaco flag" width="40"> | Monaco | MCO | 38 087 | 1 500 000&nbsp;XTC | 22 592&nbsp;XTC | **1 522 592&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mn.svg" alt="Mongolia flag" width="40"> | Mongolia | MNG | 3 556 798 | 1 500 000&nbsp;XTC | 218 325&nbsp;XTC | **1 718 325&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/me.svg" alt="Montenegro flag" width="40"> | Montenegro | MNE | 626 233 | 1 500 000&nbsp;XTC | 91 610&nbsp;XTC | **1 591 610&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ma.svg" alt="Morocco flag" width="40"> | Morocco | MAR | 38 762 441 | 1 500 000&nbsp;XTC | 720 740&nbsp;XTC | **2 220 740&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mz.svg" alt="Mozambique flag" width="40"> | Mozambique | MOZ | 36 639 851 | 1 500 000&nbsp;XTC | 700 729&nbsp;XTC | **2 200 729&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mm.svg" alt="Myanmar flag" width="40"> | Myanmar | MMR | 55 184 819 | 1 500 000&nbsp;XTC | 859 969&nbsp;XTC | **2 359 969&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/na.svg" alt="Namibia flag" width="40"> | Namibia | NAM | 3 153 246 | 1 500 000&nbsp;XTC | 205 566&nbsp;XTC | **1 705 566&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/nr.svg" alt="Nauru flag" width="40"> | Nauru | NRU | 12 101 | 1 500 000&nbsp;XTC | 12 735&nbsp;XTC | **1 512 735&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/np.svg" alt="Nepal flag" width="40"> | Nepal | NPL | 29 629 410 | 1 500 000&nbsp;XTC | 630 136&nbsp;XTC | **2 130 136&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/nl.svg" alt="Netherlands flag" width="40"> | Netherlands | NLD | 18 818 739 | 1 500 000&nbsp;XTC | 502 190&nbsp;XTC | **2 002 190&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/nz.svg" alt="New Zealand flag" width="40"> | New Zealand | NZL | 5 290 170 | 1 500 000&nbsp;XTC | 266 261&nbsp;XTC | **1 766 261&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ni.svg" alt="Nicaragua flag" width="40"> | Nicaragua | NIC | 7 097 329 | 1 500 000&nbsp;XTC | 308 404&nbsp;XTC | **1 808 404&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ne.svg" alt="Niger flag" width="40"> | Niger | NER | 28 814 878 | 1 500 000&nbsp;XTC | 621 415&nbsp;XTC | **2 121 415&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ng.svg" alt="Nigeria flag" width="40"> | Nigeria | NGA | 242 431 832 | 1 500 000&nbsp;XTC | 1 802 470&nbsp;XTC | **3 302 470&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/mk.svg" alt="North Macedonia flag" width="40"> | North Macedonia | MKD | 1 804 063 | 1 500 000&nbsp;XTC | 155 489&nbsp;XTC | **1 655 489&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/no.svg" alt="Norway flag" width="40"> | Norway | NOR | 5 652 989 | 1 500 000&nbsp;XTC | 275 240&nbsp;XTC | **1 775 240&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/om.svg" alt="Oman flag" width="40"> | Oman | OMN | 5 671 458 | 1 500 000&nbsp;XTC | 275 690&nbsp;XTC | **1 775 690&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pk.svg" alt="Pakistan flag" width="40"> | Pakistan | PAK | 259 299 791 | 1 500 000&nbsp;XTC | 1 864 122&nbsp;XTC | **3 364 122&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pw.svg" alt="Palau flag" width="40"> | Palau | PLW | 17 614 | 1 500 000&nbsp;XTC | 15 364&nbsp;XTC | **1 515 364&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pa.svg" alt="Panama flag" width="40"> | Panama | PAN | 4 625 718 | 1 500 000&nbsp;XTC | 248 979&nbsp;XTC | **1 748 979&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pg.svg" alt="Papua New Guinea flag" width="40"> | Papua New Guinea | PNG | 10 947 848 | 1 500 000&nbsp;XTC | 383 034&nbsp;XTC | **1 883 034&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/py.svg" alt="Paraguay flag" width="40"> | Paraguay | PRY | 7 095 279 | 1 500 000&nbsp;XTC | 308 360&nbsp;XTC | **1 808 360&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pe.svg" alt="Peru flag" width="40"> | Peru | PER | 34 922 148 | 1 500 000&nbsp;XTC | 684 106&nbsp;XTC | **2 184 106&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ph.svg" alt="Philippines flag" width="40"> | Philippines | PHL | 117 724 471 | 1 500 000&nbsp;XTC | 1 256 049&nbsp;XTC | **2 756 049&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pl.svg" alt="Poland flag" width="40"> | Poland | POL | 37 843 188 | 1 500 000&nbsp;XTC | 712 143&nbsp;XTC | **2 212 143&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/pt.svg" alt="Portugal flag" width="40"> | Portugal | PRT | 10 395 362 | 1 500 000&nbsp;XTC | 373 244&nbsp;XTC | **1 873 244&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/qa.svg" alt="Qatar flag" width="40"> | Qatar | QAT | 3 173 559 | 1 500 000&nbsp;XTC | 206 227&nbsp;XTC | **1 706 227&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kr.svg" alt="Republic of Korea flag" width="40"> | Republic of Korea | KOR | 51 600 388 | 1 500 000&nbsp;XTC | 831 572&nbsp;XTC | **2 331 572&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/md.svg" alt="Republic of Moldova flag" width="40"> | Republic of Moldova | MDA | 2 961 253 | 1 500 000&nbsp;XTC | 199 210&nbsp;XTC | **1 699 210&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ro.svg" alt="Romania flag" width="40"> | Romania | ROU | 18 800 605 | 1 500 000&nbsp;XTC | 501 948&nbsp;XTC | **2 001 948&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ru.svg" alt="Russian Federation flag" width="40"> | Russian Federation | RUS | 143 394 458 | 1 500 000&nbsp;XTC | 1 386 243&nbsp;XTC | **2 886 243&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/rw.svg" alt="Rwanda flag" width="40"> | Rwanda | RWA | 14 889 693 | 1 500 000&nbsp;XTC | 446 700&nbsp;XTC | **1 946 700&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/kn.svg" alt="Saint Kitts and Nevis flag" width="40"> | Saint Kitts and Nevis | KNA | 46 992 | 1 500 000&nbsp;XTC | 25 095&nbsp;XTC | **1 525 095&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lc.svg" alt="Saint Lucia flag" width="40"> | Saint Lucia | LCA | 180 488 | 1 500 000&nbsp;XTC | 49 181&nbsp;XTC | **1 549 181&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/vc.svg" alt="Saint Vincent and the Grenadines flag" width="40"> | Saint Vincent and the Grenadines | VCT | 99 245 | 1 500 000&nbsp;XTC | 36 469&nbsp;XTC | **1 536 469&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ws.svg" alt="Samoa flag" width="40"> | Samoa | WSM | 220 528 | 1 500 000&nbsp;XTC | 54 363&nbsp;XTC | **1 554 363&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sm.svg" alt="San Marino flag" width="40"> | San Marino | SMR | 33 605 | 1 500 000&nbsp;XTC | 21 221&nbsp;XTC | **1 521 221&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/st.svg" alt="Sao Tome and Principe flag" width="40"> | Sao Tome and Principe | STP | 244 994 | 1 500 000&nbsp;XTC | 57 299&nbsp;XTC | **1 557 299&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sa.svg" alt="Saudi Arabia flag" width="40"> | Saudi Arabia | SAU | 35 165 787 | 1 500 000&nbsp;XTC | 686 489&nbsp;XTC | **2 186 489&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sn.svg" alt="Senegal flag" width="40"> | Senegal | SEN | 19 366 548 | 1 500 000&nbsp;XTC | 509 447&nbsp;XTC | **2 009 447&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/rs.svg" alt="Serbia flag" width="40"> | Serbia | SRB | 8 308 956 | 1 500 000&nbsp;XTC | 333 692&nbsp;XTC | **1 833 692&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sc.svg" alt="Seychelles flag" width="40"> | Seychelles | SYC | 134 959 | 1 500 000&nbsp;XTC | 42 528&nbsp;XTC | **1 542 528&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sl.svg" alt="Sierra Leone flag" width="40"> | Sierra Leone | SLE | 8 996 745 | 1 500 000&nbsp;XTC | 347 229&nbsp;XTC | **1 847 229&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sg.svg" alt="Singapore flag" width="40"> | Singapore | SGP | 5 905 748 | 1 500 000&nbsp;XTC | 281 326&nbsp;XTC | **1 781 326&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sk.svg" alt="Slovakia flag" width="40"> | Slovakia | SVK | 5 451 342 | 1 500 000&nbsp;XTC | 270 287&nbsp;XTC | **1 770 287&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/si.svg" alt="Slovenia flag" width="40"> | Slovenia | SVN | 2 114 573 | 1 500 000&nbsp;XTC | 168 339&nbsp;XTC | **1 668 339&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sb.svg" alt="Solomon Islands flag" width="40"> | Solomon Islands | SLB | 858 288 | 1 500 000&nbsp;XTC | 107 248&nbsp;XTC | **1 607 248&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/so.svg" alt="Somalia flag" width="40"> | Somalia | SOM | 20 305 907 | 1 500 000&nbsp;XTC | 521 656&nbsp;XTC | **2 021 656&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/za.svg" alt="South Africa flag" width="40"> | South Africa | ZAF | 65 453 084 | 1 500 000&nbsp;XTC | 936 566&nbsp;XTC | **2 436 566&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ss.svg" alt="South Sudan flag" width="40"> | South Sudan | SSD | 12 436 037 | 1 500 000&nbsp;XTC | 408 239&nbsp;XTC | **1 908 239&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/es.svg" alt="Spain flag" width="40"> | Spain | ESP | 47 850 793 | 1 500 000&nbsp;XTC | 800 788&nbsp;XTC | **2 300 788&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/lk.svg" alt="Sri Lanka flag" width="40"> | Sri Lanka | LKA | 23 348 315 | 1 500 000&nbsp;XTC | 559 372&nbsp;XTC | **2 059 372&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sd.svg" alt="Sudan flag" width="40"> | Sudan | SDN | 53 282 719 | 1 500 000&nbsp;XTC | 845 019&nbsp;XTC | **2 345 019&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sr.svg" alt="Suriname flag" width="40"> | Suriname | SUR | 645 256 | 1 500 000&nbsp;XTC | 92 991&nbsp;XTC | **1 592 991&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/se.svg" alt="Sweden flag" width="40"> | Sweden | SWE | 10 701 047 | 1 500 000&nbsp;XTC | 378 692&nbsp;XTC | **1 878 692&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ch.svg" alt="Switzerland flag" width="40"> | Switzerland | CHE | 9 007 798 | 1 500 000&nbsp;XTC | 347 442&nbsp;XTC | **1 847 442&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/sy.svg" alt="Syrian Arab Republic flag" width="40"> | Syrian Arab Republic | SYR | 26 472 497 | 1 500 000&nbsp;XTC | 595 622&nbsp;XTC | **2 095 622&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tj.svg" alt="Tajikistan flag" width="40"> | Tajikistan | TJK | 10 978 599 | 1 500 000&nbsp;XTC | 383 572&nbsp;XTC | **1 883 572&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/th.svg" alt="Thailand flag" width="40"> | Thailand | THA | 71 559 614 | 1 500 000&nbsp;XTC | 979 281&nbsp;XTC | **2 479 281&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tl.svg" alt="Timor-Leste flag" width="40"> | Timor-Leste | TLS | 1 436 923 | 1 500 000&nbsp;XTC | 138 768&nbsp;XTC | **1 638 768&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tg.svg" alt="Togo flag" width="40"> | Togo | TGO | 9 930 918 | 1 500 000&nbsp;XTC | 364 811&nbsp;XTC | **1 864 811&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/to.svg" alt="Tonga flag" width="40"> | Tonga | TON | 103 291 | 1 500 000&nbsp;XTC | 37 205&nbsp;XTC | **1 537 205&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tt.svg" alt="Trinidad and Tobago flag" width="40"> | Trinidad and Tobago | TTO | 1 513 268 | 1 500 000&nbsp;XTC | 142 407&nbsp;XTC | **1 642 407&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tn.svg" alt="Tunisia flag" width="40"> | Tunisia | TUN | 12 415 138 | 1 500 000&nbsp;XTC | 407 895&nbsp;XTC | **1 907 895&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tm.svg" alt="Turkmenistan flag" width="40"> | Turkmenistan | TKM | 7 736 632 | 1 500 000&nbsp;XTC | 321 995&nbsp;XTC | **1 821 995&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tv.svg" alt="Tuvalu flag" width="40"> | Tuvalu | TUV | 9 362 | 1 500 000&nbsp;XTC | 11 201&nbsp;XTC | **1 511 201&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tr.svg" alt="Türkiye flag" width="40"> | Türkiye | TUR | 87 926 082 | 1 500 000&nbsp;XTC | 1 085 505&nbsp;XTC | **2 585 505&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ug.svg" alt="Uganda flag" width="40"> | Uganda | UGA | 52 761 469 | 1 500 000&nbsp;XTC | 840 875&nbsp;XTC | **2 340 875&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ua.svg" alt="Ukraine flag" width="40"> | Ukraine | UKR | 39 535 849 | 1 500 000&nbsp;XTC | 727 895&nbsp;XTC | **2 227 895&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ae.svg" alt="United Arab Emirates flag" width="40"> | United Arab Emirates | ARE | 11 574 682 | 1 500 000&nbsp;XTC | 393 847&nbsp;XTC | **1 893 847&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/gb.svg" alt="United Kingdom flag" width="40"> | United Kingdom | GBR | 70 481 661 | 1 500 000&nbsp;XTC | 971 877&nbsp;XTC | **2 471 877&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/tz.svg" alt="United Republic of Tanzania flag" width="40"> | United Republic of Tanzania | TZA | 72 563 780 | 1 500 000&nbsp;XTC | 986 128&nbsp;XTC | **2 486 128&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/us.svg" alt="United States of America flag" width="40"> | United States of America | USA | 352 600 000 | 1 500 000&nbsp;XTC | 2 173 773&nbsp;XTC | **3 673 773&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/uy.svg" alt="Uruguay flag" width="40"> | Uruguay | URY | 3 382 537 | 1 500 000&nbsp;XTC | 212 909&nbsp;XTC | **1 712 909&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/uz.svg" alt="Uzbekistan flag" width="40"> | Uzbekistan | UZB | 37 724 223 | 1 500 000&nbsp;XTC | 711 022&nbsp;XTC | **2 211 022&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/vu.svg" alt="Vanuatu flag" width="40"> | Vanuatu | VUT | 342 564 | 1 500 000&nbsp;XTC | 67 755&nbsp;XTC | **1 567 755&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ve.svg" alt="Venezuela (Bolivarian Republic of) flag" width="40"> | Venezuela (Bolivarian Republic of) | VEN | 28 633 711 | 1 500 000&nbsp;XTC | 619 458&nbsp;XTC | **2 119 458&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/vn.svg" alt="Viet Nam flag" width="40"> | Viet Nam | VNM | 102 177 431 | 1 500 000&nbsp;XTC | 1 170 174&nbsp;XTC | **2 670 174&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/ye.svg" alt="Yemen flag" width="40"> | Yemen | YEM | 42 961 653 | 1 500 000&nbsp;XTC | 758 776&nbsp;XTC | **2 258 776&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/zm.svg" alt="Zambia flag" width="40"> | Zambia | ZMB | 22 521 915 | 1 500 000&nbsp;XTC | 549 384&nbsp;XTC | **2 049 384&nbsp;XTC** |
| <img src="../.gitbook/assets/flags/zw.svg" alt="Zimbabwe flag" width="40"> | Zimbabwe | ZWE | 17 273 580 | 1 500 000&nbsp;XTC | 481 132&nbsp;XTC | **1 981 132&nbsp;XTC** |

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

The allocation accrues linearly through deterministic on-chain accounting during eligible service. For position $i$ at block $b$:

$V_i(b) = A_i \times \frac{\min\left(E_i(b), B_{5y}\right)}{B_{5y}}$

$C_i(b) = V_i(b) - R_i(b)$

Where $A_i$ is the fixed reference allocation, $E_i(b)$ is eligible service measured in blocks, $B_{5y}$ is the configured five-year service duration in blocks, $V_i(b)$ is vested allocation, $R_i(b)$ is allocation already released and $C_i(b)$ is claimable allocation.

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

The first contact creates a case reference only. Before any application is accepted, Xitcoin independently verifies the public institution, official-domain contact, authority of the representative and operating mandate through separate official sources and a secure communication channel.

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
