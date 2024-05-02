# AutoCrypt

Prompt:
`We've intercepted this message that was encrypted using some kind of simple autokey cipher where the ciphertext is used as the subsequent encryption key. We don't have the initial encryption key but we know that the initial encryption key is only 1 byte, so it should be easily breakable. Can you help us crack the code?`

Given:
- ciphertext: `d2badfff99f594f3d3bac9e9baf1a885c491c58aa791a991a8`
- 

### Strategy

Brute Force??

d2badfff99f594f3d3bac9e9baf1a885c491c58aa791a991a8 (50 chars) -> 25 chars ASCII

d2 ba df ff 99 f5 94 f3 d3 ba c9 e9 ba f1 a8 85 c4 91 c5 8a a7 91 a9 91 a8


1b w/ ptext -> C1

C1's 1st byte w/ p2 -> C2

## Autokey

Key: primer + ptext (for padding)

ptext:  AAAAAAAAAA..... (25 chars)
key:    1b + 24 chars of ptext

ctext:  CCCCCCCCC...... (25 chars)



ctext: 
k1 p1 p2 p3 p4 ... p24
p1 p2 p3 p4 p5 ... p25  +

c1 c2 c3 c4 c5 ... c25  =

