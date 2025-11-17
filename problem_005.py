# Smallest Multiple

# Find the smallest number divisible by all number between 1 and 20

import sympy as sp

factors = {2: 1}
for n in range(3, 21):
    # if number % n != 0:
    for p, n in sp.factorint(n).items():
        try:
            if factors[p] < n:
                factors[p] = n
        except KeyError:
            factors[p] = n

number = 1
for p, n in factors.items():
    number *= p**n

print(number)
