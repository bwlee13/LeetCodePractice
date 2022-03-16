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