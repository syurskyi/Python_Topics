"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'Danyang'


c_ Solution:
    ___ maxProfit  prices
        """
        Algorithm: dp
        1-D dp.
        Given an i, split the whole array into TWO parts:
        [0... i] and [i+1... n-1], it generates two max value based on i, max_profit[0... i] and max_profit[i+1... n-1]

        global_max_profit = max(max_profit[0... i] + max_profit[i+1... n-1]), for all i.

        :param prices: list of integers
        :return: integer
        """
        __ l..(prices) <_ 1:
            r.. 0

        # O(n) using dp
        forward = [0 ___ _ __ x..(l..(prices]  # forward[i] for 0..i
        lowest_buy_price = prices[0]
        ___ i __ x..(1, l..(prices:
            # if i==0:
            # forward[i] = 0
            # else:
            forward[i] = m..(forward[i-1], prices[i]-lowest_buy_price)

            lowest_buy_price = m..(prices[i], lowest_buy_price)

        backward = [0 ___ _ __ x..(l..(prices]  # backward[i] for i..len-1
        highest_sell_price = prices[-1]
        ___ i __ x..(l..(prices)-2, -1, -1
            # if i==len(prices)-1:
            # backward[i] = 0
            # else:
            backward[i] = m..(backward[i+1], highest_sell_price-prices[i])

            highest_sell_price = m..(prices[i], highest_sell_price)

        max_profit = 0
        ___ i __ x..(l..(prices:
            max_profit = m..(max_profit, forward[i]+backward[i])
        r.. max_profit

    ___ maxProfit_error  prices
        """
        2 transactions
        you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

        :param prices: list of integers
        :return: integer
        """

        __ l..(prices) <_ 1:
            r.. 0

        delta_prices    # list
        ___ i __ x..(1, l..(prices:
            delta_prices.a..(prices[i]-prices[i-1])

        # O(n)
        max_profits = [0, 0]

        max_sub_array = 0
        current_sub_array = 0
        ___ j __ x..(l..(delta_prices:
            __ current_sub_array+delta_prices[j] >_ 0:
                current_sub_array += delta_prices[j]
                max_sub_array = m..(max_sub_array, current_sub_array)
            ____
                # keep two 2
                __ max_sub_array > max_profits[0]:
                    max_profits[1] = max_profits[0]
                    max_profits[0] = max_sub_array
                ____ max_sub_array > max_profits[1]:
                    max_profits[1] = max_sub_array
                max_sub_array = 0
                current_sub_array = 0

        r.. s..(max_profits)
