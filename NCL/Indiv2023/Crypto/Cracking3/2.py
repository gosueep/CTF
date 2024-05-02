from hashlib import md5

hashes = """
406b29cfbe9939e2514ff0a23f0f4236
902448f411c86949be776a73b0d8004c
9bb579775f2eaf77207457154e995aaa
"""
hashes = set([p for p in hashes.split()])


prefix = 'SKY-PASS-'


output = open('2.out', 'w')

# 0000-9999
# 10000-100000
for i in range(10000, 20000):
    suffix = str(i)[1:]
    pword = prefix + suffix

    hash = md5(bytes(pword, 'utf-8')).hexdigest()
    if hash in hashes:
        print(pword, hash)
        output.write(f'{pword}, {hash}\n')

    # exit(1)

