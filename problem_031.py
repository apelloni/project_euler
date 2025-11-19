# Coin Sums

import sys

currency = [1, 2, 5, 10, 20, 50, 100, 200]
max_coins = [200//d for d in currency]
target = 200


def coin_dispenser():
    yield [200, 0, 0, 0, 0, 0, 0]
    coins = [0 for _ in range(len(currency))]
    while coins[-1] != 1:
        i = 1

        # Find first to incement
        while coins[i] == max_coins[i]:
            i += 1
        # increase and reset previous entries
        coins[i] += 1
        coins[:i] = [0 for _ in range(i)]

        # If we are already at the limit we can simply increase move to the
        # next increment of the last update coin
        coins[0] = 0
        while sum([ci*vi for ci, vi in zip(coins, currency)]) > target:
            while coins[i] == max_coins[i]:
                i += 1
            coins[i] += 1
            coins[:i] = [0 for _ in range(i)]
        # Top up with 1 cents
        coins[0] = target - sum([ci*vi for ci, vi in zip(coins, currency)])

        yield coins


target = 200
count = 0
for n, x in enumerate(coin_dispenser()):
    if target == sum([xi*ci for xi, ci in zip(x, currency)]):
        count += 1

print(count)  # 73682
