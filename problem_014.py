# Longest Collatz Sequence

#       / n/2 , if n even
#  n ->|
#       \ 3n+1, if n odd

class Collatz:
    _cache = {1: 1}

    @staticmethod
    def collatz_length(n, size=0):
        try:
            return size+Collatz._cache[n]
        except KeyError:
            if n % 2 == 0:
                collatz_len = Collatz.collatz_length(n//2, size+1)
                Collatz._cache[n] = collatz_len-size
            else:
                collatz_len = Collatz.collatz_length(3*n+1, size+1)
                Collatz._cache[n] = collatz_len-size
            return collatz_len


max_size = 0
for n in range(1, 10**6):
    collatz_len = Collatz.collatz_length(n)
    # print(f"{n} -> {collatz_len} ")
    if max_size < collatz_len:
        max_size = collatz_len
        print(f'New max size {max_size} for n={n}')
