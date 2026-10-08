# Sums of Square Reciprocals

# There are several ways to express a 1/2 as a sum of squared the reciprocals of positive integers.
# Using integers between 1 and 45 there are three ways to do this:
# {2,3,4,5,7,12,15,20,28,35}
# {2,3,4,6,7,9,10,20,28,35,36,45}
# {2,3,4,6,7,9,12,15,28,30,35,36,45}
#
# Can you find how many ways there are with integers between 1 and 80?
import math
import sys
import time

import sympy

# import mpmath


# sys.set_int_max_str_digits(1000000)

N = 80
n_sqs = [n**2 for n in range(2, N+1)]
# n_sqs = [4, 9, 16, 25, 49, 144, 225, 400, 784, 1225]
# n_sqs = [4, 9, 16, 25, 36, 49, 64, 81, 100, 144, 196, 225,
#         256, 324, 400, 441, 576, 625, 729, 784, 900, 1024, 1225]
# remove from n_sqs all the number with prime factors larger than 7
for idx in range(len(n_sqs)-1, -1, -1):
    factors = sympy.factorint(n_sqs[idx])
    if any(p > 7 for p in factors.keys()):
        n_sqs.pop(idx)
print(f'List of squares ({len(n_sqs)}): {n_sqs}')

# Find greatest common divider


def reciprocal_sum2(number_sqs, den=1, num=0):
    den = 1
    for n in number_sqs:
        den *= n
    num = 0
    for n in number_sqs:
        num += (den//n)
    return [num, den]


# print(reciprocal_sum2([3, 6]))
#
# print(reciprocal_sum2(n_sqs))

count = 0
results = []


def tree_search(subset, cache, idx=0):
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
    n, d = reciprocal_sum2(subset)
    if 2*n == d:
        results += [[i for i in subset]]
        print(f' ==> {[int(math.sqrt(v)) for v in subset]}')
        # print(f" ==> {subset}")
        return True
    elif idx >= len(n_sqs):
        return False
    else:
        v = n_sqs[idx]
        set_a = subset
        set_b = subset + [v]

        # num/den - 1/v
        # num/(den' * v) - 1/v = (num -  den' * 1)/ ( den' * v )
        # n_c = num - den/v
        # d_c = den
        # print(cache["den"] % v)
        n_c = (cache["num"] - cache["den"]//v)//v
        d_c = cache["den"]//v

        # Create new cache for the next level of recursion
        cache_a = {"num": n_c, "den": d_c}
        cache_b = {"num": n_c, "den": d_c}
        # print((n_c, d_c), (reciprocal_sum2(n_sqs[idx+1:])))

        n_a, d_a = n, d
        n_b, d_b = n*v+d, d*v
        # n_c, d_c = reciprocal_sum2(n_sqs[idx+1:])

        n_a_max, d_a_max = n_a*d_c+n_c*d_a, d_a*d_c
        if 2*n_a <= d_a and 2*n_a_max >= d_a_max:
            tree_search(set_a, cache_a, idx + 1)

        n_b_max, d_b_max = n_b*d_c+n_c*d_b, d_b*d_c
        if 2*n_b <= d_b and 2*n_b_max >= d_b_max:
            tree_search(set_b, cache_b, idx + 1)


start_time = time.time()
n, d = reciprocal_sum2(n_sqs)
cache = {"num": n, "den": d}
tree_search([], cache)
end_time = time.time()


print("="*80)
print(count, count/2**(N-1)*100)
print(results)
print(f'Found {len(results)} ways for N={N}')

results = sorted(results)
for s in results:
    n, d = reciprocal_sum2(s)
    print(f'{2*n//d}, {2*n % d}: {[int(math.sqrt(v)) for v in s]}')


print(f"Time taken: {end_time - start_time:.2f} seconds")
