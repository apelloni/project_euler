# Truncatable Primes


import sympy as sp

count = 0


total = 0
p = 7
while count < 11:
    p = sp.nextprime(p)
    s = str(p)
    for i in range(1, len(s)):
        if not (sp.isprime(int(s[:i])) and sp.isprime(int(s[i:]))):
            break
    else:
        count += 1
        total += p


print(total)
