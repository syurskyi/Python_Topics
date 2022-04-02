'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ longestCommonPrefix  strs
        """
        :type strs: List[str]
        :rtype: str
        """
        __ n.. strs: r.. ''
        ind = 0
        w... T...
            same = T..
            ___ i, s __ e..(strs
                __ ind __ l..(s
                    same = F..
                    _____
                __ i __ 0:
                    c = s[ind]
                ____ c != s[ind]:
                    same = F..
                    _____
            __ n.. same:
                _____
            ind += 1
        r.. strs[0][:ind]
    
    ___ test
        testCases = [
             'a', 'b' ,
             'aa', 'aa' ,
        ]
        ___ strs __ testCases:
            print('\n'.j..([s..(row) ___ row __ strs]))
            result = longestCommonPrefix(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
