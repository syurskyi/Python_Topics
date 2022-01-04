'''
Created on Apr 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        valuesMap    # dict
        graph    # dict
        ___ e, v __ z..(equations, values):
            valuesMap[(e[0], e[1])] = v
            valuesMap[(e[1], e[0])] = 1.0/v
            __ e[0] __ graph:
                graph[e[0]].add(e[1])
            ____:
                graph[e[0]] = set([e[1]])
            __ e[1] __ graph:
                graph[e[1]].add(e[0])
            ____:
                graph[e[1]] = set([e[0]])
        result    # list
        ___ query __ queries:
            __ query[0] n.. __ graph:
                result.a..(-1.0)
            ____ query[0] __ query[1]:
                result.a..(1.0)
            ____:
                tmp = [-1.0]
                dfs(valuesMap, graph, query[0], query[1], 1.0, set(), tmp)
                result.a..(tmp[0])
        r.. result
    
    ___ dfs(self, valuesMap, graph, start, target, curr, visited, result):
        visited.add(start)
        __ start __ target:
            result[0] = curr
        __ start __ graph:
            ___ nextNode __ graph[start]:
                __ nextNode n.. __ visited:
                    dfs(valuesMap, graph, nextNode, target, curr*valuesMap[(start, nextNode)], visited, result)
    
    ___ test
        testCases = [
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ],
            ),
        ]
        ___ equations, values, queries __ testCases:
            result = calcEquation(equations, values, queries)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


