# Integer Right Triangles


import numpy as np


def pitagora_triplets(p):
    # p: it the perimeter
    for a in range(1, p//2):
        b = (p**2 - 2*a*p)/(2*(p-a))
        if not b.is_integer() or b < a:
            continue
        c = np.sqrt(a**2+b**2)
        if c.is_integer() and b < c:
            yield (a, int(b), int(c))


p_max = 0
c_max = 0
for p in range(1_001):
    count = 0
    for t in pitagora_triplets(p):
        count += 1
        # print(f' - {t}')
    if c_max < count:
        c_max = count
        p_max = p

print(f'Perimeter with maximum right triangles: {p_max} ({c_max} triangles)')
