# Sums of Square Reciprocals

# There are several ways to express a 1/2 as a sum of squared the reciprocals of positive integers.
# Using integers between 1 and 45 there are three ways to do this:
# {2,3,4,5,7,12,15,20,28,35}
# {2,3,4,6,7,9,10,20,28,35,36,45}
# {2,3,4,6,7,9,12,15,28,30,35,36,45}
#
# Can you find how many ways there are with integers between 1 and 80?
#
# ===============================
# Runs in 5m30s: Found 154 ways
# ===============================
import math
import sys
import time

import sympy


def get_primes_below(n):
    if n <= 2:
        return []

    sieve = bytearray([1]) * n
    sieve[0] = sieve[1] = 0  # 0 e 1 non sono numeri primi

    for i in range(2, math.isqrt(n - 1) + 1):
        if sieve[i]:
            sieve[i*i: n: i] = bytearray([0]) * len(range(i*i, n, i))

    return [i for i, is_prime in enumerate(sieve) if is_prime]


# Iterator over subsets
def subsets(set_full, min_size=0, max_size=None):
    if max_size is None:
        max_size = len(set_full)
    n = len(set_full)
    # Binary bit as combinations
    for i in range(1 << n):
        subset = [set_full[j] for j in range(n) if (i & (1 << j))]
        if min_size <= len(subset) <= max_size:
            yield subset


# sys.set_int_max_str_digits(1000000)
N = 81
primes = get_primes_below(N)
ns = [n for n in range(2, N+1)]
n_sqs = [n**2 for n in ns]


# filter numbers
exclude = []
for p in primes[1:]:
    np = [n for n in ns if n % p == 0]
    print(f'{p}: {np}')
    if len(np) == 1:
        exclude += [p]
    if len(np) == 2 and sum([(n//p)**2 for n in np]) % p != 0:
        exclude += [p]
        # n_sqs = [n for n in n_sqs if n % p != 0]
    if len(np) > 2:
        for s in subsets(np, 2):
            if sum([(n//p)**2 for n in s]) % p**2 == 0:
                print(f' -> Found subset {s} for prime {p}')
                break
        else:
            exclude += [p]

print(f'Found {len(exclude)} primes to exclude:')
for i in range(len(exclude))[::10]:
    print(f'{exclude[i:i+10]}')

print(f'Original set size: {len(n_sqs)}')
n_sqs = [n for n in n_sqs if all(n % p != 0 for p in exclude)]
print(f'Filtered set size: {len(n_sqs)}')

# sys.exit(0)


# get LCM to transform the problem from
# 1/2 = 1/p1 + .... + 1/pn
# TO
# q/2 = q/p1 + ... + q/pn
#
# Notice that by construction with q = lcm(p1,...,pn)
# all terms are integers

q = sympy.ilcm(*n_sqs)
terms = [q//n for n in n_sqs]
target = q//2


# Find greatest common divider
count = 0
results = []


def tree_search(subset, idx=0):
    global results
    global count
    count += 1
    # print(subset, idx)

    if count % 1_000_000 == 0:
        print(f'{count:,}, {count/2**(N-1)*100:.2}%')
        # print(f"{count:,} | idx: {idx}", end="\r")
    # stop when idx is out of bounds
    # if len(subset) == 0:
    #    return False
    r = sum(subset) - target
    if r == 0:
        results += [[q//i for i in subset]]
        print(f' ==> {[int(math.sqrt(v)) for v in subset]}')
        # print(f" ==> {subset}")
        return True
    elif idx >= len(terms):
        return False
    else:
        v = terms[idx]
        set_a = subset
        set_b = subset + [v]

        add_max = sum(terms[idx+1:])

        if r <= 0 and r + add_max >= 0:
            tree_search(set_a, idx + 1)

        if r + v <= 0 and r + v + add_max >= 0:
            tree_search(set_b, idx + 1)


start_time = time.time()
tree_search([])
end_time = time.time()


print("="*80)
print(count, count/2**(N-1)*100)
print(f'Found {len(results)} ways for N={N}')
for r in results:
    print(
        f'{2*sum([q//i for i in r])//q}, {2*sum([q//i for i in r]) % q}: {[int(math.sqrt(v)) for v in r]}')

results = sorted(results)
# for s in results:
# n, d = reciprocal_sum2(s)
# print(f'{2*n//d}, {2*n % d}: {[int(math.sqrt(v)) for v in s]}')


print(f"Time taken: {end_time - start_time:.2f} seconds")
