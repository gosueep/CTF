# https://sagecell.sagemath.org/

from base64 import b64encode, b64decode
from random import choice
from sage.all import GF

b64_alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\\="

msg = 'V4m\\GDMHaDM3WKy6tACXaEuXumQgtJufGEyXTAtIuDm5GEHS'

field = list(GF(2**6))


def generate_secret_key(n):
  key = 1
  for _ in range(n):
    key *= choice(field)
    key += choice(field)
  return key


def encrypt(message, secret_key):
  message = b64encode(message)
  encrypted = ""
  mod_key = 6 * secret_key**6 + 3 * secret_key**4 + 7 * secret_key**3 + 15
  for char in message:
    t1 = b64_alpha.index(chr(char))
    t2 = field[t1] * mod_key
    t3 = b64_alpha[field.index(t2)]
    encrypted += t3
  return encrypted


key = generate_secret_key(10)
print(encrypt(b'[redacted]', key))

field_nums = [x.integer_representation() for x in field]
mod_key = 6 * key**6 + 3 * key**4 + 7 * key**3 + 15
print(field)
print(field_nums)

for k in field[1:]:

    tk = t = 6 * k**6 + 3 * k**4 + 7 * k**3 + 15

    dec = ""
    for c in msg:
        d3 = b64_alpha.index(c)
        d3 = field[d3]
        d2 = field.index(d3 / tk)
        d1 = b64_alpha[d2]

        dec += d1

    try:
        decoded = b64decode(dec)
#         print(str(decoded))
        if 'valentine{' in str(decoded):
            print(decoded)
    except Exception:
        a = 5  