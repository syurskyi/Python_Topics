'''
Created on Mar 19, 2017

@author: MT
'''

______ heapq

class Solution(object
    ___ findItinerary_orig(self, tickets
        __ not tickets:
            r_ []
        hashmap = {}
        ___ t1, t2 in tickets:
            __ t1 not in hashmap:
                hashmap[t1] = []
            heapq.heappush(hashmap[t1], t2)
        result = []
        self.dfs(result, hashmap, 'JFK')
        r_ result
        
    ___ dfs(self, result, hashmap, elem
        w___ hashmap.get(elem
            self.dfs(result, hashmap, heapq.heappop(hashmap[elem]))
        result.insert(0, elem)
    
    ___ test(self
        testCases = [
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
        ]
        ___ tickets in testCases:
            print('tickets: %s' % tickets)
            result = self.findItinerary(tickets)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

