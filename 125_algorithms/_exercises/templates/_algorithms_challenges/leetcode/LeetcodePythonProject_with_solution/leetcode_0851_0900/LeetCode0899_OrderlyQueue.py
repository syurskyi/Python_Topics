class Solution(object):
    ___ orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        __ K > 1:
            return ''.join(sorted(S))
        n = len(S)
        minIdx = 0
        for i in range(1, n):
            for i1 in range(n):
                __ S[(i+i1)%n] < S[(minIdx+i1)%n]:
                    minIdx = i
                    break
                elif S[(i+i1)%n] > S[(minIdx+i1)%n]:
                    break
        return S[minIdx:] + S[:minIdx]

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
        for s, k in testCases:
            res = self.orderlyQueue(s, k)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ == '__main__':
    Solution().test()
