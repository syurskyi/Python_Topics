'''
Created on Mar 19, 2017

@author: MT
'''

import heapq

class Solution(object):
    ___ findItinerary_orig(self, tickets):
        __ not tickets:
            return []
        hashmap = {}
        for t1, t2 in tickets:
            __ t1 not in hashmap:
                hashmap[t1] = []
            heapq.heappush(hashmap[t1], t2)
        result = []
        self.dfs(result, hashmap, 'JFK')
        return result
        
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
        for tickets in testCases:
            print('tickets: %s' % tickets)
            result = self.findItinerary(tickets)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()

