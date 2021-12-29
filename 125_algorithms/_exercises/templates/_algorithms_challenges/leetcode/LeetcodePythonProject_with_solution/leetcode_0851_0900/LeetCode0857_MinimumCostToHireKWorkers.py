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
        import heapq
        k = K
        workers = sorted([float(w)/q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q, in workers:
            heapq.heappush(heap, -q)
            qsum += q
            __ len(heap) > k:
                qsum += heapq.heappop(heap)
            __ len(heap) == k:
                res = min(res, qsum*r)
        return res
    
    ___ test(self):
        testCases = [
            
        ]
        for quality, wage, k in testCases:
            res = self.mincostToHireWorkers(quality, wage, k)
            print('res: %s' % res)
            print('-='*30 + '-')

__ __name__ == '__main__':
    Solution().test()
