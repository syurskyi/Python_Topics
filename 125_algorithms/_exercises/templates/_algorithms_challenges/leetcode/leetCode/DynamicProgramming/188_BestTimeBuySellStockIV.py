# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-23 14:17:12
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ maxProfit  k, prices
        __ n.. prices or k __ 0:
            r_ 0

        # There is no limit on transaction's times in fact.
        days_num = l..(prices)
        __ k / 2 > days_num:
            r_ self.quick_solve(prices)

        # dp[i][j] is the max profit for up to i transactions by days j.
        # 1 <= i <= K, 0 <= j < das_num.
        dp = [[0 ___ day __ r..(days_num)] ___ trans __ r..(k + 1)]
        ___ i __ r..(1, k + 1
            # tmpMax means the maximum profit if we've just buy i-th stock so far.
            tmp_max = -prices[0]
            ___ j __ r..(1, days_num
                dp[i][j] = m..(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = m..(tmp_max, dp[i - 1][j - 1] - prices[j])
        r_ dp[k][days_num - 1]

    # Get the max profits without the limit of transactions actually.
    ___ quick_solve  prices
        profits = 0
        ___ i __ r..(1, l..(prices)):
            price_diff = prices[i] - prices[i - 1]
            profits += price_diff __ price_diff > 0 else 0
        r_ profits

"""
1
[8,5,3]
2
[1,8,3,2,7,12,7,15,16,17]
4
[1,8,3,2,7,12,7,15,16,17]
"""
