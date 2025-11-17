# Multiples of 3 or 5Multiples of 3 or 5

# sum all number below 1000 that are multiple of 3 or 5

result = 0

i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        result += i
    i += 1

print(result)
