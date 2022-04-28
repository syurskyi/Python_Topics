c_ Solution o..

    ___ -(self):
        memo = []
        memo.append(0)
        memo.append(1)

    ___ fib  N):
        """
        DP with memo
        :type N: int
        :rtype: int
        """
        __ N < l.. memo):
            r_ memo[N]
        ___ i __ r.. l.. memo), N + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        r_ memo[N]

    # def fib(self, N):
    #     """
    #     Recursively, O(n)
    #     :type N: int
    #     :rtype: int
    #     """
    #     if N == 0:
    #         return 0
    #     if N == 1:
    #         return 1
    #     return self.fib(N - 1) + self.fib(N - 2)
