c_ Solution(o..
    ___ orderlyQueue  S, K
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        __ K > 1:
            r.. ''.j..(s..(S
        n = l..(S)
        minIdx = 0
        ___ i __ r..(1, n
            ___ i1 __ r..(n
                __ S[(i+i1)%n] < S[(minIdx+i1)%n]:
                    minIdx = i
                    _____
                ____ S[(i+i1)%n] > S[(minIdx+i1)%n]:
                    _____
        r.. S[minIdx:] + S[:minIdx]

    ___ test
        testCases = [
            [
                "cba", 1,
            ],
            [
                "baaca", 3,
            ],
            [
                "gxzv", 4,
            ],
        ]
        ___ s, k __ testCases:
            res = orderlyQueue(s, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ _____ __ _____
    Solution().test()
