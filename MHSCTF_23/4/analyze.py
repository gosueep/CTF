from collections import defaultdict



freq = defaultdict(int)

for run in open('output.txt', 'r').readlines():
    # print(run.strip())

    for i in run.strip():
        freq[int(i)] += 1

for i in sorted(freq.keys()):
    print(i, freq[i])