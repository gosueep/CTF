from base64 import b64encode

def original(m):
    # input("Valentine: ")
    valentine = bytes(m, "utf-8")
    a = b64encode(valentine)                    # b64 forward
    b = b64encode(valentine[::-1])              # b64 reversed
    print(a)
    print(b)
    a = list(map(ord, list(str(a))))            # makes them all ascii values
    b = list(map(ord, list(str(b))))
    for j in range(len(a)):
        enc = a[j] + b[j]                       # add 1st half and 2nd half 
        enc = enc % 58                          # mod 58 ??
        enc += 65                               # back to alphanum
        enc = chr(enc)                          # conver to ascii
        print(enc, end='')
    print("")


# a[0] + b[-1]  ===  a[-1] + b[0]


msg = 'WU]Wipuk\cYAvtEXHsRlP_YlPs[UMtVmkcOjupFCVGU'     # 43 long
print(msg)
msg = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA'
msg = 'AAAABBBBCCCCDDDDEEEEFFFFGGGG'
# msg = 'valentine{AAAAAAAAAAAAAAAAA}'
print(len(msg))

#always 'WU....GU"??

for i in msg:
    d = ord(i)
    d -= 65
    # print(d + 58, end=' ')

    #d           # a[j] + b[j] % 58


print(ord(msg[0])-65, ord(msg[-1])-65)

print(msg)
original(msg)
original(''.join(reversed(msg)))


# while 