c_ Solution:
    ___ fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        __ n.. A o. n.. B o. n.. C o. n.. D:
            r.. ans

        S    # dict

        ___ c __ C:
            ___ d __ D:
                key = - (c + d)
                S[key] = S.get(key, 0) + 1

        ___ a __ A:
            ___ b __ B:
                __ a + b __ S:
                    ans += S[a + b]

        r.. ans
