# Digit Cancelling Fractions


# Find greatest common divider
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


# Generate all fractions with two digits numerator and denominators with
# value less then 1

den = 1
num = 1
for n in range(10, 100):
    for d in range(n+1, 100):
        s_n = str(n)
        s_d = str(d)
        common = (set(s_n) & set(s_d)) - {'0'}
        if len(common) != 0:
            r1 = n/d
            r2 = 0
            for c in common:
                a = int(s_n.replace(c, '', 1))
                b = int(s_d.replace(c, '', 1))
                if b != 0:
                    r2 = a/b

            if r1 == r2:
                den *= d
                num *= n


print(f'{num}/{den} = ', end='')
f = gcd(num, den)
print(f'{num//f}/{den//f}')
