'''
Created on Sep 11, 2019

@author: tongq
'''
c_ Solution(object):
    ___ kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, b = A, B
        __ a __ b:
            r.. 0
        q = [a]
        hashset = set([a])
        res = 0
        w.... q:
            res += 1
            size = l..(q)
            ___ _ __ r..(size):
                s = q.pop(0)
                i = 0
                w.... s[i] __ b[i]:
                    i += 1
                ___ j __ r..(i+1, l..(s)):
                    __ s[j] __ b[j] o. s[i] != b[j]:
                        continue
                    tmp = swap(s, i, j)
                    __ tmp __ b:
                        r.. res
                    __ tmp n.. __ hashset:
                        hashset.add(tmp)
                        q.a..(tmp)
        r.. res
    
    ___ swap(self, s, i, j):
        l = l..(s)
        l[i], l[j] = l[j], l[i]
        r.. ''.j..(l)
    
    ___ test
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
        ___ a, b __ testCases:
            res = kSimilarity(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
