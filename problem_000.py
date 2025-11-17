# Sum of the first 305'000 perfect squares (only the odds)
result = 0
for i in range(629000//2):
    result += (2*i+1)**2

print(result)
