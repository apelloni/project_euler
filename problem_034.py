# Digit Factorials


# 145 is a curious number, as 1! + 4! + 5! = 145
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not

# have that 9! = 362880 so we don't need to look at anything with more than 7 digits

import numpy as np

# Generate Factorial values

fact = [int(np.prod(range(1, n+1))) for n in range(10)]

numbers = []
for n in range(10, 1_000_000):
    r = sum([fact[int(x)] for x in str(n)])
    if n == r:
        numbers.append(n)

print(sum(numbers))
