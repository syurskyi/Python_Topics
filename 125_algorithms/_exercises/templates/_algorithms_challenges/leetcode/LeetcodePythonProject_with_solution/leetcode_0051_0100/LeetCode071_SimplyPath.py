'''
Created on Jan 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ simplifyPath  p..
        """
        :type path: str
        :rtype: str
        """
        __ n.. p..: r.. p..
        result ''
        __ p...e.. '/' p.. p..[:-1]
        __ p...s.. '/' p.. p..[1:]
        l p...s..('/')
        cont 0
        ___ i __ r..(l..(l)-1, -1, -1
            __ l[i] __ '.' o. l[i] __ '':
                _____
            __ l[i] __ '..':
                cont += 1
                _____
            __ cont > 0:
                cont -_ 1
            ____
                result '/' + l[i] + result
        __ result __ '':
            result '/'
        r.. result
    
    ___ test
        testCases [
            '/home/',
            '/a/./b/../../c/',
        ]
        ___ p.. __ testCases:
            print('path: %s' % p..)
            result simplifyPath(p..)
            print('result: %s' % result)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()