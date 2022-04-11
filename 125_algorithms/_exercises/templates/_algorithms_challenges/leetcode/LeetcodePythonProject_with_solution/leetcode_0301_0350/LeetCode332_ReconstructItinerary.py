'''
Created on Mar 19, 2017

@author: MT
'''

_______ heapq

c_ Solution(o..
    ___ findItinerary_orig  tickets
        __ n.. tickets:
            r.. []
        hashmap    # dict
        ___ t1, t2 __ tickets:
            __ t1 n.. __ hashmap:
                hashmap[t1]    # list
            heapq.heappush(hashmap[t1], t2)
        result    # list
        dfs(result, hashmap, 'JFK')
        r.. result
        
    ___ dfs  result, hashmap, elem
        w.... hashmap.g.. elem
            dfs(result, hashmap, heapq.heappop(hashmap[elem]
        result.insert(0, elem)
    
    ___ test
        testCases [
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
        ]
        ___ tickets __ testCases:
            print('tickets: %s' % tickets)
            result findItinerary(tickets)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

