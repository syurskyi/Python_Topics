c_ Solution o..
    ___ minimumTotal  triangle
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        __ triangle is N.. or l.. triangle) __ 0:
            r_ 0
        ls = l.. triangle)
        dp = [0] * ls
        dp[0] = triangle[0][0]
        ___ i __ r.. 1, ls
            # note that dp should be updated in reversed order
            dp[i] = dp[i - 1] + triangle[i][i]
            ___ j __ reversed(r.. 1, i)):
                dp[j] = m.. dp[j - 1] + triangle[i][j], dp[j] + triangle[i][j])
            dp[0] = dp[0] + triangle[i][0]
        r_ m.. dp)
