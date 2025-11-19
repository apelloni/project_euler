# Champernowne's Constant


s = ''

dn = 0
extract = [10**i for i in range(7)]
target = extract.pop(0)
n = 1

result = 1
while True:
    s = f'{n}'
    dn += len(s)
    if dn >= target:
        idx = target-dn-1
        print(s[idx])
        result *= int(s[idx])
        try:
            target = extract.pop(0)
        except IndexError:
            break

    n += 1

print(result)
