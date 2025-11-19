# Pandigital Multiples

# Find the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1.

max = 0
n = 1
while n < 10:
    n += 1
    i = 10**((9//n)+1)
    while i > 0:
        i -= 1
        q = int(''.join([str(j*i) for j in range(1, n+1)]))
        s = str(q)
        if q < max or len(s) != 9:
            continue
        if len(set(s)) == 9 and not ('0' in s):
            if max < q:
                print(f'{i} (1 .. {n}) = {q} <- NEW MAX')
                max = q
            break

print(max)
