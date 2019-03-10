#!/usr/bin/env python3

""" the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

denom = [25,10,5,1]

def solve_dp(amount, d=denom):
    dp = [0,1,2,3,4,1]
    for i in range(6, amount+1):
        options = [dp[i - c] + 1 for c in d if c <= i]
        dp.append(min(options))
    return dp[amount]


def solve_greedy(amount, d=denom):
    coins = 0
    while amount > 0:
        for coin in d:
            coin_count = amount // coin
            amount -= coin_count * coin
            coins += coin_count
    return coins
        

for i in range(101):
    dp = solve_dp(i)
    gr = solve_greedy(i)
    # if dp != gr:
    if True:
        print(i, solve_dp(i), solve_greedy(i))
