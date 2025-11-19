# Double-base Palindromes


total = 0
for n in range(1, 1_000_000):
    if n % 10 == 0 or n % 2 == 0:
        continue
    # check palindrome b10 and b2
    a = str(n)
    b = f'{n:b}'
    if str(a) == str(a)[::-1] and str(b) == str(b)[::-1]:
        total += n
print(total)
