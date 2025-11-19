# 1_000-digit Fibonacci Number


def fibonacci():
    a, b = 1, 1
    idx = 1
    while True:
        idx += 1
        a, b = b, a + b
        yield idx, a


for idx, f in fibonacci():
    if len(str(f)) >= 1_000:
        print(idx)
        break
