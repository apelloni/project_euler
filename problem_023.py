# Non-Abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# A number is called:
#   - deficient if the sum of its proper divisors is less than itslef
#   - abundant if this sum exceeds its own value

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def proper_divisors(n):
    divisors = set()
    n0 = n
    for p in range(1, n//2+1):
        while n % p == 0:
            n = n//p
            divisors = divisors.union({p * f for f in divisors})
            divisors = divisors.union({p})
            if p == 1:
                break
        if p > n:
            break
    return [d for d in divisors if d < n0]


# Find all abundant number smaller then 28124
abundant_numbers = []
# for n in range(1, 28124):
for n in range(1, 28124):
    if sum(proper_divisors(n)) > n:
        abundant_numbers += [n]

numbers = set(range(1, 28124))
# Find all numbers that cannot be expressed as a sum of abundant numbers
while len(abundant_numbers) > 1:
    n1 = abundant_numbers[0]
    abundant_numbers = [x for x in abundant_numbers if x + n1 <= 28123]
    numbers -= set([n1 + x for x in abundant_numbers])
    abundant_numbers = abundant_numbers[1:]

print(sum(numbers))
