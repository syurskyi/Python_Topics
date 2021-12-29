'''
Created on Aug 29, 2017

@author: MT
'''
class Solution(object):
    ___ nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        k = l..(n)
        candidates = [str(10**k0+d) ___ k0 __ (k-1, k) ___ d __ (-1, 1)]
        prefix = n[:int((k+1)/2)]
        p = int(prefix)
        ___ start __ map(str, (p-1, p, p+1)):
            candidates.a..(start+(start[:-1] __ k%2 ____ start)[::-1])
        ___ delta(x):
            r.. abs(int(n)-int(x))
        res = N..
        ___ cand __ candidates:
            __ cand != n and n.. cand.startswith('00'):
                __ res __ N.. o. delta(cand) < delta(res) o.\
                    delta(cand) __ delta(res) and int(cand) < int(res):
                    res = cand
        r.. res
    
    ___ test(self):
        testCases = [
            '123',
            '12122',
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.nearestPalindromic(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
