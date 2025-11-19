# Distinct Powers

numbers = set()

for a in range(2, 101):
    numbers = numbers | {a**b for b in range(2, 101)}

print(len(numbers))
