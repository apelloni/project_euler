# Largest Palindrome Product

# Find the largest palindrome made from the product of two 3-digit numbers.


max_palindrome = 0

for d1 in range(100, 1000):
    for d2 in range(d1, 1000):
        n = d1 * d2
        if n == int(str(n)[::-1]) and n > max_palindrome:
            max_palindrome = n

print(max_palindrome)
