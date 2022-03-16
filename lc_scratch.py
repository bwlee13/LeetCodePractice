from collections import deque

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


# c, a = [1,2,5], 11
# print(coinChange(c, a))









"""
write a function that returns the max value after filling a knapsack with n gems. The knapsack can hold weight w, and the two inputs
are quantity q and prices p of the gems found. You can use partial gems in q and not have to take the entire q[i]
q = [5,5,4,7]
p = [3,2,3,1]

go through highest price for Greedy solution, subtract weight from w until until w == 0 or quant is gone
zip to matrix, sort reversed
while weight, decriment from quant with highest price and add price to value every time

"""

def max_val_knap(q, p, w):
    matrix = list(zip(p, q))
    matrix.sort(reverse=True)
    value = 0

    for price, quant in matrix:
        for gem in range(quant):
            if w>0:
                value += price
                w -= 1

    print(value)
    return value





q = [5,5,1,7]
p = [1,2,10,1]
w = 3
max_val_knap(q, p, w)





"""
provided with a temp record temperatureRecord(temp, time)
return maximum temp in last 24 hours
ex: input= [(24,0), (14,8), (21,16), (20,25)] output= [24, 24, 24, 21]
"""

def daily_max_temp(temp_record):
    queue = deque()
    res = []
    for i in range(len(temp_record)):
        while queue and queue[0][1] < (temp_record[i][1]-24):
            queue.popleft()
        while queue and queue[-1][0] < temp_record[i][0]:
            queue.pop()
        queue.append(temp_record[i])
        res.append(queue[0][0])
    return res

temps = [(24,0), (14,8), (21,16), (20,25)]
# print(daily_max_temp(temps))






"""
Write a function to detect calendar meeting conflicts between two evens
"""

start1 = 2
end1 = 4
start2 = 5
end2 = 7


def has_conflict(s1, e1, s2, e2):
    if s1 < s2 and e1 <= s2:
        return False
    elif s2 < s1 and e2 <= s1:
        return False
    else:
        return True


# print(has_conflict(start1, end1, start2, end2))


"""
Given a String, get the run length encoding of the string.
ex: input= "wwwwaaadexxxxxx" output = "w4a3d1e1x6"
"""

def run_len_encoding(s):
    out = ""
    i=0
    while i < len(s)-1:
        count = 1
        while i<len(s)-1 and s[i] == s[i+1]:

            count += 1
            i += 1

        out += s[i]
        out += str(count)
        i += 1
    return out

# print(run_len_encoding("wwwwaaadexxxxxxywww"))


