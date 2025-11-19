# Reciprocal Cycles


best_period = 0
best_d = 2
best_digits: str = ''

period_size = 0
digits = ''
reciprocal = 1
while reciprocal < 1000:
    reciprocal += 1
    a, b = 1, reciprocal  # Fraction a/b
    base_inv = 10  # inverse base

    digits = ""
    recuring = False
    period_size = 0
    history = []
    while True:
        if recuring:
            if period_size > best_period:
                best_period = period_size
                best_d = reciprocal
                best_digits = digits
            break
        if a == 0:
            break
        # print(a, b)
        d = (a*base_inv)//b
        a = a*base_inv - d*b
        b = b * base_inv
        while a % 10 == 0 and b % 10 == 0:
            a //= 10
            b //= 10
        base_inv *= 10
        # Check if repeated
        recuring_idx = 0
        for n, (d0, (a0, b0)) in enumerate(history):
            if d == d0 and a == a0 and b % b0 == 0 and b//b0 % 10 == 0:
                recuring_idx = n
                period_size = len(digits) - recuring_idx
                digits = digits[:recuring_idx] + \
                    '(' + digits[recuring_idx:] + ')'
                recuring = True
                break
        else:
            # keep track on the digits to identify loops
            history.append((d, (a, b)))
            digits += str(d)

print(f"1/{best_d}=0.{best_digits}, period size={best_period}")
