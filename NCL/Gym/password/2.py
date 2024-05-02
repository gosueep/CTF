from hashlib import md5

hashes = """
71b816fe0b7b763d889ecc227eab400a
674291170dffcf620bda2a604a6820ea
06f03267f31077d2c4b5c728472070ae
d866f4b3b34b598375149fb7661113ab
d9053951a8d1c15254b46ec9fc974a6b
"""
hashes = set([p for p in hashes.split()])


prefix = 'SKY-HQNT-'


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

