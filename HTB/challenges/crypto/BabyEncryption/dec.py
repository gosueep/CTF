ctext = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

def dec(c):
    # print(c)
    # print(bytes.fromhex(c).decode("ASCII"))
    ct = bytes.fromhex(c)
    out = []
    for b in ct:
        possible = []
        for i in range(128):
            if ((123*i+18) % 256) == b:
                # possible.append(i)
                out.append(i)
        # out.append(possible)          
    out = ''.join(chr(x) for x in out)
    return out
    

msg = dec(ctext)
print(msg)


