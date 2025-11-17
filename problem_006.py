# Sum Square Difference


n = 10

a = 0
b = 0
for i in range(100+1):
    a += i ** 2
    b += i
print(b**2-a)
