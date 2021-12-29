'''
Created on Mar 23, 2017

@author: MT
'''

import heapq

class Solution(object):
    ___ rearrangeString(self, s, k):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        heap = []
        for c, freq in hashmap.items():
            heapq.heappush(heap, [-freq, c])
        queue = []
        res = []
        while heap:
            freq, c = heapq.heappop(heap)
            res.append(c)
            queue.append([freq, c])
            __ len(queue) < k:
                continue
            freq, c = queue.pop(0)
            freq = -freq-1
            __ freq > 0:
                heapq.heappush(heap, [-freq, c])
        return ''.join(res) __ len(res) == len(s) else ''
    
    ___ test(self):
        testCases = [
            ('aabbcc', 3),
            ('aaabc', 3),
            ('aaadbbcc', 2),
        ]
        for s, k in testCases:
            print('s: %s' % (s))
            print('k: %s' % (k))
            result = self.rearrangeString(s, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
