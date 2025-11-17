# Number Letter Counts


def number_to_word(n):
    if n <= 20:
        return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                'eighteen', 'nineteen', 'twenty'][n - 1]
    if n < 100:
        m = n//10
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                'ninety'][m - 2] + ('' if n % 10 == 0 else number_to_word(n % 10))
    if n < 1000:
        m = n//100
        return number_to_word(m) + 'hundred' + ('' if n % 100 == 0 else 'and' + number_to_word(n % 100))
    if n < 10000:
        m = n//1000
        return number_to_word(m) + 'thousand' + ('' if n % 1000 == 0 else number_to_word(n % 1000))


print(number_to_word(42))  # Example usage
print(number_to_word(542))  # Example usage

result = 0
for i in range(1, 1000+1):
    result += len(number_to_word(i))
print(result)
