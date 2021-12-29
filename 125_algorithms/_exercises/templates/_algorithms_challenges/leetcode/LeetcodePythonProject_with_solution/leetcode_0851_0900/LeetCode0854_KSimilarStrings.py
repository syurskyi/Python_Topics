'''
Created on Sep 11, 2019

@author: tongq
'''
class Solution(object):
    ___ kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, b = A, B
        __ a == b:
            return 0
        q = [a]
        hashset = set([a])
        res = 0
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                s = q.pop(0)
                i = 0
                while s[i] == b[i]:
                    i += 1
                for j in range(i+1, len(s)):
                    __ s[j] == b[j] or s[i] != b[j]:
                        continue
                    tmp = self.swap(s, i, j)
                    __ tmp == b:
                        return res
                    __ tmp not in hashset:
                        hashset.add(tmp)
                        q.append(tmp)
        return res
    
    ___ swap(self, s, i, j):
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)
    
    ___ test(self):
        testCases = [
            [
                'ab',
                'ba',
            ],
            [
                'abc',
                'bca',
            ],
            [
                'abac',
                'baca',
            ],
            [
                'aabc',
                'abca',
            ],
            [
                'abccab',
                'abccab',
            ],
        ]
        for a, b in testCases:
            res = self.kSimilarity(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
