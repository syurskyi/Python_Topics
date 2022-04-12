'''
Created on Mar 30, 2018

@author: tongq
'''
# Definition for an interval.
c_ Interval(o..
    ___ - , s=0, e=0
        start s
        end e

c_ Solution(o..
    ___ employeeFreeTime  schedule
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        _______ h__
        heap    # list
        ___ arr __ schedule:
            ___ inter __ arr:
                h__.heappush(heap, [inter.start, inter.end])
        temp h__.heappop(heap)
        res    # list
        w.... heap:
            __ temp[1] < heap 0 0 :
                res.a..(Interval(temp[1], heap 0 0 
                temp h__.heappop(heap)
            ____
                __ temp[1] < heap[0][1]:
                    temp heap[0]
                h__.heappop(heap) 
        r.. res
    
    ___ test
        testCases [
            [
                [[1,2],[5,6]],
                [[1,3]],[[4,10]],
            ],
            [
                [[1,3],[6,7]],[[2,4]],
                [[2,5],[9,12]],
            ],
        ]
        ___ schedule __ testCases:
            print('schedule: %s' % schedule)
            arr    # list
            ___ arr0 __ schedule:
                arr.a..([Interval(inter[0], inter[1]) ___ inter __ arr0])
            schedule arr
            result employeeFreeTime(schedule)
            res [[inter.start, inter.end] ___ inter __ result]
            print('result: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
