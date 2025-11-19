# Digit Fifth Powers

sum = 0
for n in range(10, 9**6):
    x = 0
    for d in str(n):
        x += int(d)**5
    if n == x:
        sum += n

print(sum)
