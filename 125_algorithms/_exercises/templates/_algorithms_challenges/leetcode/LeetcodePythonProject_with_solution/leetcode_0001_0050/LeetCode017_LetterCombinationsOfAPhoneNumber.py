'''
Created on Jan 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ letterCombinations  d..
        """
        :type digits: str
        :rtype: List[str]
        """
        letMap {
            0: l..(),
            1: l..(),
            2: l..('abc'),
            3: l..('def'),
            4: l..('ghi'),
            5: l..('jkl'),
            6: l..('mno'),
            7: l..('pqrs'),
            8: l..('tuv'),
            9: l..('wxyz'),
        }
        l    # list
        ___ d __ d..:
            d i..(d)
            __ d n.. __ (0, 1
                l.a..(letMap[d])
        __ n.. l: r..    # list
        elem ''
        result    # list
        dfs(l, 0, elem, result)
        r.. result
    
    ___ dfs  l, ind, elem, result
        __ l..(elem) __ l..(l
            result.a..(s..(elem
            r.. result
        ___ c __ l[ind]:
            elem += c
            dfs(l, ind+1, elem, result)
            elem elem[:-1]
    
    ___ test
        testCases [
            '',
            '001',
            '2',
            '23',
            '239',
        ]
        
        ___ d.. __ testCases:
            print('digits: %s' % (d..
            result letterCombinations(d..)
            print('result: %s' % (result
            print('-+'*15+'-')

__ _____ __ _____
    Solution().test()