'''
Created on Feb 28, 2017

@author: MT
'''

c_ Solution(o..
    ___ findStrobogrammatic  n
        """
        :type n: int
        :rtype: List[str]
        """
        pairs =  '00', '11', '69', '96', '88'
        res    # list
        helper(0, n-1, ['']*n, res)
        r.. res
    
    ___ helper  l, r, curr, res
        __ l > r:
            res.a..(''.j..(curr
            r..
        ___ p __ pairs:
            curr[l] = p[0]
            curr[r] = p[1]
            __ l __ r a.. p[0] != p[1]:
                _____
            ____ l __ 0 a.. l != r a.. p[0] __ '0':
                _____
            helper(l+1, r-1, curr, res)
    
    ___ findStrobogrammatic_short  n
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate =  '11', '69', '88', '96', '00'
        oddMidCandidate =  '0', '1', '8'
        __ n __ 1:
            r.. oddMidCandidate
        __ n __ 2:
            r.. evenMidCandidate[:-1]
        __ n % 2 != 0:
            pre, midCandidate = findStrobogrammatic(n-1), oddMidCandidate
        ____:
            pre, midCandidate = findStrobogrammatic(n-2), evenMidCandidate
        premid = i..((n-1)/2)
        result    # list
        ___ c __ midCandidate:
            ___ p __ pre:
                result.a..(p[:premid]+c+p[premid:])
        r.. result
    
    ___ test
        testCases = [
            4,
        ]
        ___ n __ testCases:
            print('n: %s' % (n
            result = findStrobogrammatic(n)
            print('result: %s' % (result
            print('-='*20+'-')
 
__ _____ __ _____
    Solution().test()
