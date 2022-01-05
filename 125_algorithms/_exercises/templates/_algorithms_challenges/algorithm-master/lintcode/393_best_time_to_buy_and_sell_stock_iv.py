c_ Solution:
    """
    @param: K: An integer
    @param: P: An integer array
    @return: Maximum profit
    """
    ___ maxProfit  K, P):
        __ n.. K o. n.. P:
            r.. 0

        n = l..(P)

        """
        if `K >= n`, this problem is just
        `./lintcode/150_best_time_to_buy_and_sell_stock_ii.py`
        so we dont need to use `dp`, since it lead to overflow
        """
        __ K >= n:
            profit = 0
            ___ i __ r..(1, n):
                __ P[i] > P[i - 1]:
                    profit += P[i] - P[i - 1]
            r.. profit

        """
        the main concept is in
        `./lintcode/151_best_time_to_buy_and_sell_stock_iii.py`
        """
        STAGE = 2 * K + 1
        dp = [[0] * STAGE ___ _ __ r..(2)]

        i = j = prev = curr = profit = 0
        ___ i __ r..(1, n):
            prev = curr
            curr = 1 - prev
            profit = P[i] - P[i - 1]
            ___ j __ r..(1, STAGE, 2):
                dp[curr][j] = m..(dp[prev][j] + profit, dp[prev][j - 1])
            ___ j __ r..(2, STAGE, 2):
                dp[curr][j] = m..(dp[prev][j], dp[prev][j - 1] + profit)

        r.. m..(dp[curr])
