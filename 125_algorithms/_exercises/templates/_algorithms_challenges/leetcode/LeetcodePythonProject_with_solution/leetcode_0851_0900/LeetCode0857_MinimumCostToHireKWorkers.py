'''
Created on Sep 16, 2019

@author: tongq
'''
c_ Solution(o..
    ___ mincostToHireWorkers  quality, wage, K
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        _______ heapq
        k K
        workers s..([f__(w)/q, q] ___ w, q __ z..(wage, quality
        res f__('inf')
        qsum 0
        heap    # list
        ___ r, q, __ workers:
            heapq.heappush(heap, -q)
            qsum += q
            __ l..(heap) > k:
                qsum += heapq.heappop(heap)
            __ l..(heap) __ k:
                res m..(res, qsum*r)
        r.. res
    
    ___ test
        testCases [
            
        ]
        ___ quality, wage, k __ testCases:
            res mincostToHireWorkers(quality, wage, k)
            print('res: %s' % res)
            print('-='*30 + '-')

__ _____ __ _____
    Solution().test()
