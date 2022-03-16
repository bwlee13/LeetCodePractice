
""" Coin change problem : DP bottom up. Given coins of denominations,
sum up to target amount with fewest posisble coins"""

""" ex1: coins = [1,2,5] , amount = 11, output: 3
    ex2: coins = [2], amount = 3 , output: -1 (cant)"""


def coinChange(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for amnt in range(1, amount+1):
        for coin in coins:
            if amnt - coin >= 0:
                dp[amnt] = min(dp[amnt], 1 + dp[amnt-coin])

    return dp[amount] if dp[amount] != amount+1 else -1


c, a = [1,2,5], 11
print(coinChange(c, a))
