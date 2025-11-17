# Largest Prime Factor


import sympy as sp

n = 600851475143
m = 1
max_p = sp.sqrt(n)
for p in sp.primerange(0, max_p):
    while n % p == 0:
        n = n//p
        m *= p
        max_p = sp.sqrt(n)
        print(p)
    if p > max_p:
        if n != 1:
            print(n)
        break
