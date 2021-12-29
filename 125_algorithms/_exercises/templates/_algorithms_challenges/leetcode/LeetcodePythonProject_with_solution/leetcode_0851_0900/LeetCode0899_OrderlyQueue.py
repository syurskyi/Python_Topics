class Solution(object):
    ___ orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        __ K > 1:
            r.. ''.join(s..(S))
        n = l..(S)
        minIdx = 0
        ___ i __ r..(1, n):
            ___ i1 __ r..(n):
                __ S[(i+i1)%n] < S[(minIdx+i1)%n]:
                    minIdx = i
                    break
                ____ S[(i+i1)%n] > S[(minIdx+i1)%n]:
                    break
        r.. S[minIdx:] + S[:minIdx]

    ___ test(self):
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
            res = self.orderlyQueue(s, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
