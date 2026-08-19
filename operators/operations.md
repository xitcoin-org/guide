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
