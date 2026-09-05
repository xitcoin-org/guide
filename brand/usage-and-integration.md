# Usage and integration

## Correct use

Use the supplied artwork with its original proportions, orientation and
complete canvas. Name the project **Xitcoin** and use **XTC** as the public
asset symbol. Keep the artwork distinct from surrounding text and controls.

## Prohibited modifications in official presentation

Do not redraw, crop, stretch, rotate, recolor, outline or add shadows or
effects. Do not merge the symbol with another project's mark, introduce
network-specific variants or imply an unapproved partnership or endorsement.
These are presentation rules, not additional license restrictions.

## Wallets, explorers and token lists

1. Select a [canonical download](logo-system.md) accepted by the integration.
2. Verify file encoding, dimensions and any transparency requirement.
3. Record the source repository, full commit, path and SHA-256 hash. Pin the
   commit for reproducible releases; `main` downloads can change.
4. If the platform needs a local copy, document its source and review updates
   against that hash. Do not maintain an independently edited logo.
5. Preview at final size and provide descriptive alternative text.
6. Verify the network and full asset identifier through the Guide.

A logo or ticker is not proof of identity. Native XTC uses `axtc`; a token
representation must also be identified by its network and complete contract,
mint or IBC denomination. Use [Network integration](../developers/network-integration.md)
and [XTC on Cronos](../xtc/cronos.md) for the relevant metadata.

Do not list an operational bridge representation based on a logo alone.
[Destination submission remains disabled](../bridge/status-and-security.md).
