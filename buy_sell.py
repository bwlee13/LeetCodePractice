"""
You operate a marketplace for buying & selling used textbooks For a given textbook eg“TheoryofCryptography”
there are people who want to buy this textbook and people who want to sell

OfferstoBUY: [$100, $100, $99, $99, $97, $90]

OfferstoSELL:[$109, $110, $110, $114, $115$, 119]

A match occurs when two people agree on a price. Some new offers do not match, These offers should be added to the active set of offers.

For example, Tim offers to SELL at $150 This will not match anyone is willing to buy at that price so we save the offer

OfferstoSELL:: [$109, $110, $110, $114, $115, $119, $150]

When matching we want to give the customer the “best price”

Example matches: If Jane offers to BUY at $120

she will match and buy a book for $109 (the lowest offer)
"""

import heapq


class BuySell:
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell

    def buy_sell_offer(self, price, is_sell = True):
        if is_sell:
            heapq.heappush(self.sell, price)
        else:
            heapq.heappush(self.buy, price)

        if self.buy and self.sell:
            if self.buy[-1] >= self.sell[0]:
                buy_val, sell_val = self.buy.pop(), heapq.heappop(self.sell)

                return [buy_val, sell_val]

        return -1


buyy = [100, 100, 99, 99, 97, 90]
selly = [109, 110, 120, 110, 114, 115]
heapq.heapify(buyy)
heapq.heapify(selly)

t = BuySell(buyy, selly)
vals = t.buy_sell_offer(150, is_sell=False)
print(vals)
print(t.buy, t.sell)


# FOLLOW UP QUESTION, TURN TO TUPLE WITH EXPIRE - TIME FACTOR

class BuySellTime:
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell

    def isValid(self, order):
        time = 2
        return order[1] > time

    def buy_sell_offer(self, price, is_sell = True):
        if is_sell:
            heapq.heappush(self.sell, price)
        else:
            heapq.heappush(self.buy, price)

        if self.buy and self.sell:
            if self.buy[-1][0] >= self.sell[0][0] and self.isValid(self.buy[-1]) and self.isValid(self.sell[0]):
                buy_val, sell_val = self.buy.pop(), heapq.heappop(self.sell)

                return [buy_val, sell_val]

        return -1


buy_t = [(100, 5), (100, 6), (99, 7), (99, 8), (97, 9), (90, 8)]
sell_t = [(109, 5), (110, 7), (120, 7), (110, 5), (114, 5), (115, 6)]
heapq.heapify(buy_t)
heapq.heapify(sell_t)

c = BuySellTime(buy_t, sell_t)
val = c.buy_sell_offer((150, 9), is_sell=False)
print(val)
print(c.buy, c.sell)




















