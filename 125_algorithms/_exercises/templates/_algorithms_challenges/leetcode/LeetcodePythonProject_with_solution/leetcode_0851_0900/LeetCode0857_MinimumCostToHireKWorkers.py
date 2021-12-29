'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    ___ mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        _______ heapq
        k = K
        workers = s..([float(w)/q, q] ___ w, q __ zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap    # list
        ___ r, q, __ workers:
            heapq.heappush(heap, -q)
            qsum += q
            __ l..(heap) > k:
                qsum += heapq.heappop(heap)
            __ l..(heap) __ k:
                res = m..(res, qsum*r)
        r.. res
    
    ___ test(self):
        testCases = [
            
        ]
        ___ quality, wage, k __ testCases:
            res = self.mincostToHireWorkers(quality, wage, k)
            print('res: %s' % res)
            print('-='*30 + '-')

__ __name__ __ '__main__':
    Solution().test()
