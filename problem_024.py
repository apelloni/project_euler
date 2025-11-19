# Lexicographic Permutations


# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9


factorial = [1 for _ in range(9)]
for n in range(1, 10):
    factorial[n-1:] = [x*n for x in factorial[n-1:]]


# We use 'factorial' as the basis to express 1 million
b = [0 for _ in range(10)]

number = 1_000_000
for n, v in enumerate(reversed(factorial)):
    while number > v:
        number -= v
        b[n] += 1

# This tells us the type of permutations we have at the millionth position
# b = [2, 6, 6, 2, 5, 1, 2, 1, 1, 0]
digits = list(range(10))

for bi in b:
    print(digits.pop(bi), end='')
print()
