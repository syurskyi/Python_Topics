'''
Created on Sep 9, 2017

@author: MT
'''
c_ Solution(object):
    ___ leastInterval  tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        arr = [0]*26
        ___ t __ tasks:
            arr[o..(t)-o..('A')] += 1
        arr.s..()
        i = 25
        w.... i >= 0 a.. arr[i]__arr[-1]:
            i -= 1
        r.. m..(l..(tasks), (arr[-1]-1)*(n+1)+25-i)
    
    ___ leastInterval_own  tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        _______ heapq
        hashmap    # dict
        ___ task __ tasks:
            hashmap[task] = hashmap.get(task, 0)+1
        heap    # list
        ___ c, count __ hashmap.i..:
            heapq.heappush(heap, (-count, c))
        res = 0
        queue    # list
        w.... heap:
            count, c = heapq.heappop(heap)
            queue.a..((-count, c))
            __ l..(queue) > n:
                res += l..(queue)
                w.... queue:
                    count, c = queue.pop(0)
                    count -= 1
                    __ count > 0:
                        heapq.heappush(heap, (-count, c))
            __ n.. heap:
                count0 = l..(queue)
                w.... queue:
                    count, c = queue.pop(0)
                    count -= 1
                    __ count > 0:
                        heapq.heappush(heap, (-count, c))
                __ n.. heap:
                    res += count0
                ____:
                    res += n+1
        r.. res
    
    ___ test
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
        ___ tasks, n __ testCases:
            print('tasks: %s' % tasks)
            print('n: %s' % n)
            result = leastInterval(tasks, n)
            result2 = leastInterval_own(tasks, n)
            print('result: %s' % result)
            print('result2: %s' % result2)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
