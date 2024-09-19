for f in archive/logseq*;
do
    printf "$f: "
    cat $f | zfs receive -F xsjopool/zzfs;
    printf "\n"
done