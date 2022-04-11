c_ Solution:
    ___ largestDivisibleSubset  A
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans    # list
        __ n.. A:
            r.. ans

        n l..(A)
        __ n __ 1:
            r.. A

        A.s..()

        """
        this problem similar with LIS

        `dp[i]` means the maximum size of subset end at `i`
        note that there is size, so init with `1`

        `pi[i]` records the previous num in ans, and allow to backtrack
        to find all num in ans

        `pe` means path end, to record the LDS end
        """
        dp [1] * n
        pi [0] * n
        pe max_size 0

        ___ i __ r..(n
            ___ j __ r..(i
                """
                backtracking

                `A[i]` is larger than `A[j]`,
                so check `A[i] % A[j]` if its zero
                """
                __ A[i] % A[j] __ 0 a.. dp[j] + 1 > dp[i]:
                    dp[i] dp[j] + 1
                    pi[i] j

                __ dp[i] > max_size:
                    max_size dp[i]
                    pe i

        ans [0] * max_size
        ___ i __ r..(max_size - 1, -1, -1
            ans[i] A[pe]
            pe pi[pe]

        r.. ans
