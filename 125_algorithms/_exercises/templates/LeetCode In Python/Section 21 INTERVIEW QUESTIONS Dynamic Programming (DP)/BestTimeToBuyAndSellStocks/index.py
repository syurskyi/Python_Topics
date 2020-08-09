c_ Solution:
    ___ maxProfit(, prices: L.. in.)  in.:
        buyPrice _ float("inf")
        profit _ 0

        ___ i, price __ enumerate(prices
            __(buyPrice > price
                buyPrice _ price
            ____
                profit _ ma.(profit, price-buyPrice)

        r_ profit
