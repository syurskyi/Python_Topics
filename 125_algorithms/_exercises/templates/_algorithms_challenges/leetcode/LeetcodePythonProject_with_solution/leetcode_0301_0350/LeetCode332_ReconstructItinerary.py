'''
Created on Mar 19, 2017

@author: MT
'''

_______ heapq

class Solution(object):
    ___ findItinerary_orig(self, tickets):
        __ n.. tickets:
            r.. []
        hashmap = {}
        ___ t1, t2 __ tickets:
            __ t1 n.. __ hashmap:
                hashmap[t1]    # list
            heapq.heappush(hashmap[t1], t2)
        result    # list
        self.dfs(result, hashmap, 'JFK')
        r.. result
        
    ___ dfs(self, result, hashmap, elem):
        while hashmap.get(elem):
            self.dfs(result, hashmap, heapq.heappop(hashmap[elem]))
        result.insert(0, elem)
    
    ___ test(self):
        testCases = [
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
        ]
        ___ tickets __ testCases:
            print('tickets: %s' % tickets)
            result = self.findItinerary(tickets)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

