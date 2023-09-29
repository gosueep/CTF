# picoCTF{R0UND_N_R0UND_B6B25531}
def mod1():
    message = "202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397"
    result = ""
    for i in message.split():
        num = int(i) % 37
        result += mapChars(num)

    print(result)

# picoCTF{}
def mod2():
    message = "104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370"
    result = ""
    for i in message.split():
        num = int(i) % 41
        num = inverse(num)
        result += mapChars(num-1)

    print(result)

def mapChars(num):
    if num == 36:
        return "_"
    elif num >= 26:
        return str(num - 26)
    else:
        return chr(num % 37 + 65)


def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)


def euclid(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, y, x = euclid(b % a, a)
        return (g, x - (b // a) * y, y)

#inverse in mod 41
def inverse(a):
    g, x, y = euclid(a, 41)
    if g != 1:
        print("mod inverse doesn't exist")
    else:
        return euclid(a, 41)[1] % 41

def main():
    # mod1()
    mod2()

if __name__ == "__main__":
    main()