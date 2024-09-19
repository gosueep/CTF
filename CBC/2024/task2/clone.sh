for f in $(zfs list -r | grep logseq | awk '{ print $1}');
do
    printf "$f"
    sudo zfs clone $f "xsjopool/$(echo $f | cut -d "@" -f 2)"
    printf "\n"
done