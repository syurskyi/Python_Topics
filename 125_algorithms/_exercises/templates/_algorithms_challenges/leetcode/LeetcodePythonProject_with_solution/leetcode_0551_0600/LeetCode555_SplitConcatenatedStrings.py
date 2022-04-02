'''
Created on Aug 24, 2017

@author: MT
'''

c_ Solution(o..
    ___ splitLoopedString  strs
        """
        :type strs: List[str]
        :rtype: str
        """
        res = N..
        arr = [m..(s, s[::-1]) ___ s __ strs]
        ___ i, s __ e..(arr
            ___ start __ (s, s[::-1]
                ___ j __ r..(l..(start)+1
                    __ n.. res:
                        res = start[j:] + ''.j..(arr[i+1:]+arr[:i]) + start[:j]
                    ____:
                        res = m..(res, start[j:] + ''.j..(arr[i+1:]+arr[:i]) + start[:j])
        r.. res
    
    ___ test
        testCases = [
             'abc', 'xyz' ,
        ]
        ___ strs __ testCases:
            print('strs: %s' % strs)
            result = splitLoopedString(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
