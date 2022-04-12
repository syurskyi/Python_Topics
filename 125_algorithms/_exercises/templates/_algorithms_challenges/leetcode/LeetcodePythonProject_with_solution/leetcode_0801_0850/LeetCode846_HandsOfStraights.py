'''
Created on Mar 26, 2019

@author: tongq
'''
c_ Solution(o..
    ___ isNStraightHand  hand, W
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        w W
        __ l..(hand) % w !_ 0:
            r.. F..
        hashmap    # dict
        ___ num __ hand:
            hashmap[num] hashmap[num]+1 __ num __ hashmap ____ 1
        w.... hashmap:
            minVal m..(hashmap)
            ___ i __ r..(w
                __ minVal + i n.. __ hashmap:
                    r.. F..
                hashmap[minVal+i] -_ 1
                __ hashmap[minVal+i] __ 0:
                    del hashmap[minVal+i]
        r.. l..(hashmap) __ 0
    
    ___ test
        testCases [
            [
                [1,2,3,6,2,3,4,7,8],
                3,
            ],
            [
                [1,2,3,4,5],
                4,
            ],
        ]
        ___ hand, w __ testCases:
            result isNStraightHand(hand, w)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
