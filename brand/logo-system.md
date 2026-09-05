# Logo system and downloads

The supplied symbol is the official project and XTC asset mark. No separate
wordmark, monochrome reverse mark or typography system is established by the
inspected source package.

## Preview the supplied artwork

{% tabs %}
{% tab title="Standard" %}
<figure><img src="../.gitbook/assets/brand/standard-on-white.svg" alt="Standard Xitcoin symbol on white" width="400"><figcaption><p>Standard PNG: transparent canvas, original orange artwork.</p></figcaption></figure>

Use the standard PNG exports for most wallet, explorer and token-list artwork.
{% endtab %}

{% tab title="White background · legacy" %}
<figure><img src="../.gitbook/assets/brand/legacy-white.svg" alt="Legacy Xitcoin orange symbol with its original opaque white background" width="400"><figcaption><p>The legacy “white” variant has a white background. It is not a white reverse mark.</p></figcaption></figure>

The original filenames end in `.png`, but the files contain JPEG bytes.
Confirm the receiving platform accepts the actual encoding before selecting one.
{% endtab %}
{% endtabs %}

## Canonical downloads

| File | Actual encoding / dimensions | Intended selection |
|---|---|---|
| [32 × 32 PNG](https://raw.githubusercontent.com/xitcoin-org/brand/8a3e841dbb1f78b0a15386bc1fbad411e3334241/assets/png/standard/xitcoin-symbol-32.png) | PNG · 32 × 32 | Small raster integrations, subject to a final-size preview |
| [200 × 200 PNG](https://raw.githubusercontent.com/xitcoin-org/brand/8a3e841dbb1f78b0a15386bc1fbad411e3334241/assets/png/standard/xitcoin-symbol-200.png) | PNG · 200 × 200 | Wallet and directory artwork |
| [500 × 500 PNG](https://raw.githubusercontent.com/xitcoin-org/brand/8a3e841dbb1f78b0a15386bc1fbad411e3334241/assets/png/standard/xitcoin-symbol-500.png) | PNG · 500 × 500 | Larger display integrations |
| [3000 × 3000 PNG](https://raw.githubusercontent.com/xitcoin-org/brand/8a3e841dbb1f78b0a15386bc1fbad411e3334241/assets/png/standard/xitcoin-symbol-3000.png) | PNG · 3000 × 3000 | High-resolution raster use |
| [Legacy SVG package](https://github.com/xitcoin-org/brand/tree/main/assets/svg) | SVG · 3000 × 3000 canvas; embedded 1000 × 1000 PNG | Compatibility only; contains embedded raster images |
| [Legacy white-background package](https://github.com/xitcoin-org/brand/tree/main/assets/png/white) | JPEG · 32, 200, 512 or 3000 square pixels | Inspect format and opaque background before use |

The SVG files use a 3000 × 3000 canvas around a 1000 × 1000 embedded PNG.
They are not path-based vectors and should not be advertised as infinitely
scalable source artwork.

The files named `white` show an orange symbol on a white background. Their
raster files contain JPEG bytes under `.png` filenames; the nominal 500-pixel
file is 512 × 512. Do not treat them as transparent monochrome marks.

These observations apply to the Brand source at
[`8a3e841`](https://github.com/xitcoin-org/brand/tree/8a3e841dbb1f78b0a15386bc1fbad411e3334241).
A true vector master or corrected export requires approved artwork and a
reviewed update. Existing files must not be silently redrawn.
