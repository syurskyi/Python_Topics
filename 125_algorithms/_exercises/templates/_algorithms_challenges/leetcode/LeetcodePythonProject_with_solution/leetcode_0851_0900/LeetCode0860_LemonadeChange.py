'''
Created on Sep 15, 2019

@author: tongq
'''
c_ Solution(o..
    ___ lemonadeChange  bills
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap {
            5:0,
            10:0,
            20:0,
        }
        ___ b __ bills:
            __ b __ 10:
                __ hashmap[5] >_ 1:
                    hashmap[5] -_ 1
                ____
                    r.. F..
            ____ b __ 20:
                val 20
                __ hashmap[10] >_ 1:
                    hashmap[10] -_ 1
                    val -_ 10
                __ val __ 10:
                    __ hashmap[5] >_ 1:
                        hashmap[5] -_ 1
                    ____
                        r.. F..
                ____
                    __ hashmap[5] >_ 3:
                        hashmap[5] -_ 3
                    ____
                        r.. F..
            hashmap[b] += 1
        r.. T..
    
    ___ test
        testCases [
#             [5,5,5,10,20],
            [5, 5, 10, 10, 20],
        ]
        ___ bills __ testCases:
            res lemonadeChange(bills)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
