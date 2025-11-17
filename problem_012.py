# Highly Divisible Triangular Number

import numpy as np
import sympy as sp

count = 1
max_count = 0
triangular = 1

i = 1
while count <= 500:
    i += 1
    count = 2  # all numbers are divisible by 1 and itself
    triangular += i
    n = triangular
    factors = set()
    for p in range(1, n):
        while n % p == 0:
            n = n//p
            factors = factors.union({p * f for f in factors})
            factors = factors.union({p})
            count = len(factors)
            if p == 1:
                break
        if p > n:
            break
    if max_count < count:
        max_count = count
        print(f'{max_count} for {triangular}')
        # print(factors)
print()
print(triangular)
