---
description: Operations and monitoring in the official Xitcoin Guide.
icon: chart-line
---

# Operations and monitoring

Monitor block height, peer count, synchronization status, disk usage, memory, signing performance and service restarts.

## Minimum checks

* `catching_up` is false;
* block height continues increasing;
* peer connectivity is stable;
* the binary checksum matches the approved release;
* backups and recovery instructions are tested;
* alerts reach an independent channel.

Never restart all validators simultaneously. Coordinate upgrades to preserve consensus continuity.

## Explorer maintenance

Treat explorer databases and caches separately from validator state. The EVM
explorer's backend, frontend and Stats form one public service; the
[deployment record](https://github.com/xitcoin-org/explorer-evm-testnet/blob/d33eb171032137008299bf00b63db63efb4bdc2e/docs/DEPLOYMENT.md)
describes the accepted version and recovery boundaries.

After a public cutover, preserve newly acquired database and Redis state before
planning recovery. Do not restart an old writer or restore an earlier dump over
the active database. An old upgrade script must be adapted and qualified against
the current installation before reuse. Keep at least 5 GiB free and preserve
recovery volumes, dumps and image archives.
