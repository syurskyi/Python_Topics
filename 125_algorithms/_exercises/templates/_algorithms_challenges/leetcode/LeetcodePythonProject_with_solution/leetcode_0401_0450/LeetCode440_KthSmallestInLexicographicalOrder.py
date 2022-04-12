'''
Created on Apr 17, 2017

@author: MT
'''

c_ Solution(o..
    ___ findKthNumber  n, k
        curr 1
        k -_ 1
        w.... k > 0
            steps calSteps(n, curr, curr+1)
            __ steps <_ k:
                curr += 1
                k -_ steps
            ____
                curr *= 10
                k -_ 1
        r.. curr
    
    ___ calSteps  n, n1, n2
        steps 0
        w.... n1 <_ n:
            steps += m..(n+1, n2)-n1
            n1 *= 10
            n2 *= 10
        r.. steps
    
    ___ test
        testCases [
            [
                13,
                2,
            ],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result findKthNumber(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
