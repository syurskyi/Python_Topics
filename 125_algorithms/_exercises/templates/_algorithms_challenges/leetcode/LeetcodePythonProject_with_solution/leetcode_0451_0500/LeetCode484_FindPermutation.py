'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    ___ findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = l..(s)
        res = l..(r..(1, n+2))
        i = 0
        w.... i < n:
            __ s[i] __ 'D':
                prev = i
                w.... i+1 < n a.. s[i+1]__'D':
                    i += 1
                self.reverse(res, prev, i+1)
            i += 1
        r.. res
    
    ___ reverse(self, res, l, r):
        w.... l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
    
    ___ test(self):
        testCases = [
            'I',
            'DI',
            'DDDI',
            'DIDDI',
            'DD',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.findPermutation(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
