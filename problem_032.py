# Pandigital Products

import itertools

# Note that
# 99 x 100 = 9900 uses a total of 9 digits
# So there is no need to go above 99 with the first number
product = set()

for a in range(1, 100):
    for b in range(100, 10000):
        p = a * b
        # Check digits
        d = str(a) + str(b) + str(p)
        if len(d) == 9 and set(d) == set("123456789"):
            product.add(p)
print(sum(sorted(product)))
