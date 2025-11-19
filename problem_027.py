# Quadratic Primes

# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.


import sympy as sp
from sympy.ntheory import prime


def prime_formula(a, b):
    assert sp.isprime(abs(b)), "b must be prime"
    n = 0
    while sp.isprime(abs(n**2+a*n+b)):
        n += 1
    return n


max_n = 0
best_pair = (0, 0)
for a in range(-1000+1, 1000):
    for b in sp.primerange(-1000, 1000+1):
        n = prime_formula(a, b)
        if n > max_n:
            max_n = n
            best_pair = (a, b)


print(
    f'The coefficients are a={best_pair[0]}, b={best_pair[1]} generates {max_n} consecutive primes')
print(best_pair[0]*best_pair[1])
