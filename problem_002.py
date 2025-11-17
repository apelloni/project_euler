# Even Fibonacci Numbers

# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued term


from mpmath import mp

# First two fibonacci numbers
f1 = 1
f2 = 2

# Fibonacci number counter
n = 2

result = 2
while True:
    fn = 2*f1+3*f2
    f1 = f1+2*f2
    f2 = fn
    if fn < 4*10**6:
        result += fn
    else:
        break

print(result)
