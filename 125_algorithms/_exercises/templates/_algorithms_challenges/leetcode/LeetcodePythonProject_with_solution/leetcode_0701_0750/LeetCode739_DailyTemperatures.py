'''
Created on Mar 14, 2018

@author: tongq
'''
c_ Solution(o..
    ___ dailyTemperatures  temperatures
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack    # list
        res    # list
        ___ i __ r..(l..(temperatures)-1, -1, -1
            t = temperatures[i]
            w.... stack a.. temperatures[stack[-1]] <_ t:
                stack.p.. )
            __ n.. stack:
                res.insert(0, 0)
            ____
                res.insert(0, stack[-1]-i)
            stack.a..(i)
        r.. res
    
    ___ test
        testCases = [
            [73, 74, 75, 71, 69, 72, 76, 73],
        ]
        ___ temperatures __ testCases:
            print('temperatures: %s' % temperatures)
            result = dailyTemperatures(temperatures)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
