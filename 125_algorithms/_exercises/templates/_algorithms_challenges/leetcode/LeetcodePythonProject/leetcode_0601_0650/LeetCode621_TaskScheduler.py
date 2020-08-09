'''
Created on Sep 9, 2017

@author: MT
'''
class Solution(object
    ___ leastInterval(self, tasks, n
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        arr = [0]*26
        for t in tasks:
            arr[ord(t)-ord('A')] += 1
        arr.sort()
        i = 25
        w___ i >= 0 and arr[i]__arr[-1]:
            i -= 1
        r_ max(le.(tasks), (arr[-1]-1)*(n+1)+25-i)
    
    ___ leastInterval_own(self, tasks, n
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ______ heapq
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0)+1
        heap = []
        for c, count in hashmap.items(
            heapq.heappush(heap, (-count, c))
        res = 0
        queue = []
        w___ heap:
            count, c = heapq.heappop(heap)
            queue.append((-count, c))
            __ le.(queue) > n:
                res += le.(queue)
                w___ queue:
                    count, c = queue.pop(0)
                    count -= 1
                    __ count > 0:
                        heapq.heappush(heap, (-count, c))
            __ not heap:
                count0 = le.(queue)
                w___ queue:
                    count, c = queue.pop(0)
                    count -= 1
                    __ count > 0:
                        heapq.heappush(heap, (-count, c))
                __ not heap:
                    res += count0
                ____
                    res += n+1
        r_ res
    
    ___ test(self
        testCases = [
            [
                ['A', 'A', 'A', 'B', 'B', 'B'],
                2,
            ],
            [
                ['A','A','A','A','A','A','B','C','D','E','F','G'],
                2,
            ],
        ]
        for tasks, n in testCases:
            print('tasks: %s' % tasks)
            print('n: %s' % n)
            result = self.leastInterval(tasks, n)
            result2 = self.leastInterval_own(tasks, n)
            print('result: %s' % result)
            print('result2: %s' % result2)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
