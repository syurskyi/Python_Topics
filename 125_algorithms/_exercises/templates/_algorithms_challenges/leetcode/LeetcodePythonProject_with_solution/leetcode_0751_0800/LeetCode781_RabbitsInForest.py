'''
Created on Apr 9, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numRabbits  answers
        """
        :type answers: List[int]
        :rtype: int
        """
        res 0
        hashmap    # dict
        ___ ans __ answers:
            hashmap[ans] hashmap.g.. ans, 0)+1
        ___ n, count __ hashmap.i..
            group count//(n+1)
            __ count%(n+1) !_ 0:
                res += (group+1)*(n+1)
            ____
                res += group*(n+1)
        r.. res
    
    ___ test
        testCases [
            [1, 1, 1, 1],
            [1, 1, 2],
            [10, 10, 10],
               # list,
        ]
        ___ answers __ testCases:
            print('answers: %s' % answers)
            result numRabbits(answers)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
