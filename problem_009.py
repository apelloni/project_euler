# Special Pythagorean Triplet


# Find a^2+b^2=c^2 with a+b+c=1000

for i in range(1, 1000):
    for j in range(i, 1000):
        k = 1000-i-j
        if k < j:
            continue

        if i**2+j**2-k**2 == 0:
            print(i*j*k)
