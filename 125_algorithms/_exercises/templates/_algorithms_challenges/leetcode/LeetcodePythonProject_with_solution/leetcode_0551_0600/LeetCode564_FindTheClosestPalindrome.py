'''
Created on Aug 29, 2017

@author: MT
'''
c_ Solution(o..
    ___ nearestPalindromic  n
        """
        :type n: str
        :rtype: str
        """
        k = l..(n)
        candidates = [s..(10**k0+d) ___ k0 __ (k-1, k) ___ d __ (-1, 1)]
        prefix = n[:i..((k+1)/2)]
        p = i..(prefix)
        ___ start __ map(s.., (p-1, p, p+1:
            candidates.a..(start+(start[:-1] __ k%2 ____ start)[::-1])
        ___ delta(x
            r.. abs(i..(n)-i..(x
        res = N..
        ___ cand __ candidates:
            __ cand != n a.. n.. cand.startswith('00'
                __ res __ N.. o. delta(cand) < delta(res) o.\
                    delta(cand) __ delta(res) a.. i..(cand) < i..(res
                    res = cand
        r.. res
    
    ___ test
        testCases = [
            '123',
            '12122',
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = nearestPalindromic(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
