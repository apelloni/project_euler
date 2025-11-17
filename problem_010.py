# Summation of Primes

# Find the sum of all the primes below two million.

# Since the task is to find the 10001st prime we cannot use libraries to
# directly list primes

import numpy as np


def is_prime(n, primes) -> bool:
    max_p = np.sqrt(n)
    for p in primes:
        if p > max_p:
            return True
        if n % p == 0:
            return False
    return True


prime_sum = 2
primes = [2]
i = 1
while True:
    n = 2*i+1
    if n > 2*10**6:
        break
    if is_prime(n, primes):
        primes += [n]
        prime_sum += n
    i += 1


print(prime_sum)
