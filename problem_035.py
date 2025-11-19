# Circular Primes

# The number, 197, is called a circular prime because all rotations of the digits:
#   197, 971, and 719,
# are themselves primes


import sympy as sp

circular_primes = set()
for p in sp.primerange(1_000_000):
    s = str(p)
    circular = True
    for i in range(len(s)):
        q = int(s[i:]+s[:i])
        circular = circular and (sp.isprime(q))

    if circular:
        circular_primes.add(p)

print(len(circular_primes))
