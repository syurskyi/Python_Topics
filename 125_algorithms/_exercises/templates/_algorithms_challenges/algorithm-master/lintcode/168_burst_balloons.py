c_ Solution:
    """
    @param: V: A list of integer
    @return: An integer, maximum coins
    """
    ___ maxCoins(self, V):
        __ n.. V:
            r.. 0

        """
        the value of last balloons is `1 * v * 1`
        """
        V = [1] + V + [1]

        n = l..(V)

        """
        `dp[i][j]` means the maximum value when
        all the balloons in [i+1, j-1] was bursted
        """
        dp = [[0] * n ___ _ __ r..(n)]
        # pi = [[0] * n for _ in range(n)]

        ___ i __ r..(n - 1 - 2, -1, -1):
            ___ j __ r..(i + 2, n):

                """
                leave last balloon `k` to burst
                `i + 1 <= k <= j - 1`
                """
                ___ k __ r..(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + V[i] * V[k] * V[j]
                    )
                    # if dp[i][j] == dp[i][k] + dp[k][j] + V[i] * V[k] * V[j]:
                    #     pi[i][j] = k

        # self.print_paths(0, n - 1, V, pi)

        r.. dp[0][n - 1]

    # def print_paths(self, i, j, V, pi):
    #     if i + 1 == j:
    #         return

    #     self.print_paths(i, pi[i][j], V, pi)
    #     self.print_paths(pi[i][j], j, V, pi)

    #     print("burst {vk}, get coins {vi} * {vk} * {vj} = {vsum}".format(
    #         vi=V[i],
    #         vk=V[pi[i][j]],
    #         vj=V[j],
    #         vsum=V[i] * V[pi[i][j]] * V[j]
    #     ))
