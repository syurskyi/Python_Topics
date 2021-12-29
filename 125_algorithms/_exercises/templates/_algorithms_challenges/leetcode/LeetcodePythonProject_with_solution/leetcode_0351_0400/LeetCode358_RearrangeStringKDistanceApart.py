'''
Created on Mar 23, 2017

@author: MT
'''

_______ heapq

class Solution(object):
    ___ rearrangeString(self, s, k):
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        heap    # list
        ___ c, freq __ hashmap.items():
            heapq.heappush(heap, [-freq, c])
        queue    # list
        res    # list
        w.... heap:
            freq, c = heapq.heappop(heap)
            res.a..(c)
            queue.a..([freq, c])
            __ l..(queue) < k:
                continue
            freq, c = queue.pop(0)
            freq = -freq-1
            __ freq > 0:
                heapq.heappush(heap, [-freq, c])
        r.. ''.join(res) __ l..(res) __ l..(s) ____ ''
    
    ___ test(self):
        testCases = [
            ('aabbcc', 3),
            ('aaabc', 3),
            ('aaadbbcc', 2),
        ]
        ___ s, k __ testCases:
            print('s: %s' % (s))
            print('k: %s' % (k))
            result = self.rearrangeString(s, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
