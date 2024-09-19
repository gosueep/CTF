
## using file

archive/logseq73122534017757-i:  ZFS snapshot (little-endian machine), version 17, type: ZFS, destination GUID: 5C 7D 6A 3A 35 4C 1C FFFFFF87, source GUID: FFFFFFF8 3B 73 06 FFFFFFC5 78 2D FFFFFF93, name: 'xsjopool/zzfs@logseq73122534017757'

IMPORTANT
- ZFS snapshots
- name: `xsjopool/zzfs`

## restoring
using a usb, wiped it and made it a zfs filesystem
created xsjopool

ran on each file
`cat $f | zfs receive -F xsjopool/zzfs;`


## results

didn't know the order so I just kept running my script over and over

useful

gosueep@nokron:~/forge/CTF/CBC/2024/task2/archive (main)$ zfs list


`find /xsjopool -type f -exec sha256sum {} \; | cut -d " " -f 1 | sort | uniq > hashes.txt`


