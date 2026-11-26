import math

n = int(input())
arr = list(map(int, input().split()))


def lcm(i):
    if i == 0:
        return arr[0]
    prev = lcm(i - 1)
    return prev * arr[i] // math.gcd(prev, arr[i])


print(lcm(n - 1))