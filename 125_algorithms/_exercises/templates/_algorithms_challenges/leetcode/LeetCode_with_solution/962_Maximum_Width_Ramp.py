c_ Solution o..
    # def maxWidthRamp(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     # TLE
    #     if not A or len(A) == 0:
    #         return 0
    #     for ans in range(len(A) - 1, 0, -1):
    #         for i in range(len(A)):
    #             if i + ans > len(A) - 1:
    #                 break
    #             if (A[i + ans] >= A[i]):
    #                 return ans
    #     return 0

    ___ maxWidthRamp  A
        ans = 0
        m = float('inf')
        # Sort index based on value
        ___ i __ s..(r.. l.. A)), key=A.-g
            ans = m..(ans, i - m)
            m = m.. m, i)
        r_ ans


    # def maxWidthRamp(self, A):
    #     N = len(A)
    #     ans = 0
    #     candidates = [(A[N - 1], N - 1)]
    #     # candidates: i's decreasing, by increasing value of A[i]
    #     for i in xrange(N - 2, -1, -1):
    #         # Find largest j in candidates with A[j] >= A[i]
    #         jx = bisect.bisect(candidates, (A[i],))
    #         if jx < len(candidates):
    #             ans = max(ans, candidates[jx][1] - i)
    #         else:
    #             candidates.append((A[i], i))
    #     return ans


__ ____ __ ____
    s  ?
    print s.maxWidthRamp([6, 0, 8, 2, 1, 5])
    print s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
