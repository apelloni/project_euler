# Number Spiral Diagonals


N = 1001


sum = 1
n = 1
while n < N:
    n += 2
    for i in range(4):
        # print(n**2 - i*(n-1))
        sum += n**2 - i*(n-1)

print(sum)
