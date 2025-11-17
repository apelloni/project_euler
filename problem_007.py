# 10 001st Prime

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


primes = [2]


i = 1
while True:
    n = 2*i+1
    if is_prime(n, primes):
        primes += [n]
    if len(primes) == 10001:
        break
    i += 1


print(primes[-1])
