'''
Created on Aug 29, 2017

@author: MT
'''
class Solution(object
    ___ nearestPalindromic(self, n
        """
        :type n: str
        :rtype: str
        """
        k = le.(n)
        candidates = [str(10**k0+d) ___ k0 in (k-1, k) ___ d in (-1, 1)]
        prefix = n[:int((k+1)/2)]
        p = int(prefix)
        ___ start in map(str, (p-1, p, p+1)):
            candidates.append(start+(start[:-1] __ k%2 else start)[::-1])
        ___ delta(x
            r_ abs(int(n)-int(x))
        res = None
        ___ cand in candidates:
            __ cand != n and not cand.startswith('00'
                __ res pa__ None or delta(cand) < delta(res) or\
                    delta(cand) __ delta(res) and int(cand) < int(res
                    res = cand
        r_ res
    
    ___ test(self
        testCases = [
            '123',
            '12122',
        ]
        ___ n in testCases:
            print('n: %s' % n)
            result = self.nearestPalindromic(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
