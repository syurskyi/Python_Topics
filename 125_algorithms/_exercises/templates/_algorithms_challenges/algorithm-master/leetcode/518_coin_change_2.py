c_ Solution:
    ___ change  amount, coins
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        """
        `dp[a]` means the ways to make up amount `a`
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # the ways to make up `0` is just only 1

        """
        iterate coin first, and then amount
        otherwise it will add the dup ways in
        re-count if `[1, 2]` and `[2, 1]`, but they are same
        """
        ___ c __ coins:
            ___ a __ r..(c, amount + 1
                # if a < c: continue
                dp[a] += dp[a - c]

        r.. dp[amount]
