class StockSpanner(object

    ___ __init__(self
        self.prices =   # list
        self.dp =   # list
        self.idx = 0

    ___ next(self, price
        """
        :type price: int
        :rtype: int
        """
        __ self.idx __ 0 or self.prices[-1] > price:
            self.dp.append(1)
        ____
            i = self.idx -1
            w___ i >= 0 and price >= self.prices[i]:
                i -= self.dp[i]
            self.dp.append(self.idx-i)
        self.prices.append(price)
        self.idx += 1
        r_ self.dp[-1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

__  -n __ '__main__':
    stockSpanner = StockSpanner()
    # print(stockSpanner.next(100))
    # print(stockSpanner.next(80))
    # print(stockSpanner.next(60))
    # print(stockSpanner.next(70))
    # print(stockSpanner.next(60))
    # print(stockSpanner.next(75))
    # print(stockSpanner.next(85))

    print(stockSpanner.next(29))
    print(stockSpanner.next(91))
    print(stockSpanner.next(62))
    print(stockSpanner.next(76))
    print(stockSpanner.next(51))
