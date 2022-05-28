'''
Created on Mar 4, 2017

@author: MT
'''

c_ Solution(o..
    ___ generatePalindromes  s
        """
        :type s: str
        :rtype: List[str]
        """
        __ n.. s: r.. F..
        hashmap    # dict
        ___ c __ s:
            hashmap[c] hashmap.g.. c, 0)+1
        odd 0
        oddVal ''
        ___ key, value __ hashmap.i..
            __ value%2 !_ 0:
                oddVal key
                odd += 1
        __ l..(s)%2 __ 0:
            __ odd !_ 0:
                r..    # list
        ____
            __ odd >_ 2:
                r..    # list
        result    # list
        helper(oddVal, l..(s), hashmap, result)
        r.. ?
    
    ___ helper  s0, length, hashmap, result
        __ l..(s0) >_ length:
            result.a..(s0)
            r..
        ___ c, val __ hashmap.i..
            __ val >_ 2:
                hashmap[c] -_ 2
                helper(c+s0+c, length, hashmap, result)
                hashmap[c] += 2
    
    ___ test
        testCases [
            'aaabb',
            'abc',
            'aab',
        ]
        ___ s __ testCases:
            print('s: %s' % (s
            result generatePalindromes(s)
            print('result: %s' % (result
            print('-='*20+'-')
            

__ _____ __ _____
    Solution().test()
