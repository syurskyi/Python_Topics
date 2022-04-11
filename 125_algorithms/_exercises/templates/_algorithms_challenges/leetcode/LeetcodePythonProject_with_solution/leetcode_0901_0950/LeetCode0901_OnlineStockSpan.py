c_ StockSpanner(o..

    ___ -
        prices    # list
        dp    # list
        idx 0

    ___ next  price
        """
        :type price: int
        :rtype: int
        """
        __ idx __ 0 o. prices[-1] > price:
            dp.a..(1)
        ____
            i idx -1
            w.... i >_ 0 a.. price >_ prices[i]:
                i -_ dp[i]
            dp.a..(idx-i)
        prices.a..(price)
        idx += 1
        r.. dp[-1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

__ _____ __ _____
    stockSpanner StockSpanner()
    # print(stockSpanner.next(100))
    # print(stockSpanner.next(80))
    # print(stockSpanner.next(60))
    # print(stockSpanner.next(70))
    # print(stockSpanner.next(60))
    # print(stockSpanner.next(75))
    # print(stockSpanner.next(85))

    print(stockSpanner.next(29
    print(stockSpanner.next(91
    print(stockSpanner.next(62
    print(stockSpanner.next(76
    print(stockSpanner.next(51
