
from collections import defaultdict


memo = defaultdict(int)


# finds the length of hailstone sequence
def hailstone(n, length):

    if n in memo:
        return memo[n]

    # add n to the total sum
    length += 1

    # base case - n=1
    if n == 1:
        # memo[n] = length
        return length

    # if even, divide by 2
    if n % 2 == 0:
        memo[n] = hailstone(int(n/2), length)
        return memo[n]

    # if odd, multiply by 3, add 1
    memo[n] = hailstone(3 * n + 1, length)
    return memo[n]


if __name__ == "__main__":
    # n = int(input())

    big = 0

    for i in range(1234567, 1000000, -1):
        hs = hailstone(i, 0)

        if hs > big:
            big = hs
            print(big)


    # print(hailstone(n, 0))
    # print(memo)
