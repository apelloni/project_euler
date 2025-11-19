# Amicable Numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair

import numpy as np
import sympy as sp


def proper_divisors(n):
    divisors = set()
    n0 = n
    for p in range(1, n//2+1):
        while n % p == 0:
            n = n//p
            divisors = divisors.union({p * f for f in divisors})
            divisors = divisors.union({p})
            if p == 1:
                break
        if p > n:
            break
    return [d for d in divisors if d < n0]


def d(n):
    return sum(proper_divisors(n))


print(proper_divisors(220))
print(proper_divisors(2))
print(proper_divisors(4))

# print(factors)
amicable = []
for n in range(3, 10000+1):
    if n in amicable:
        continue
    if d(d(n)) == n and n != d(n):
        amicable += [n, d(n)]

print(sum(amicable))
