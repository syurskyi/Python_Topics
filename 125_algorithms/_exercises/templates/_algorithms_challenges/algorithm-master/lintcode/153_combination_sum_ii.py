c_ Solution:
    """
    @param: A: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    ___ combinationSum2  A, target
        ans    # list
        __ n.. A:
            r.. ans

        A.s..()
        dfs(A, 0, target, ans, [])
        r.. ans

    ___ dfs  A, start, remaining, ans, p..
        __ remaining __ 0:
            ans.a..(p.. | )
            r..

        ___ i __ r..(start, l..(A:
            __ remaining < A[i]:
                r..

            # to prevent [1', 2, 5] and [1", 2, 5]
            # appear in result at same time
            __ i > start a.. A[i] __ A[i - 1]:
                _____

            p...a..(A[i])
            dfs(A, i + 1, remaining - A[i], ans, p..)
            p...p.. )
