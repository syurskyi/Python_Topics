'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    ___ calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        valuesMap = {}
        graph = {}
        for e, v in zip(equations, values):
            valuesMap[(e[0], e[1])] = v
            valuesMap[(e[1], e[0])] = 1.0/v
            __ e[0] in graph:
                graph[e[0]].add(e[1])
            else:
                graph[e[0]] = set([e[1]])
            __ e[1] in graph:
                graph[e[1]].add(e[0])
            else:
                graph[e[1]] = set([e[0]])
        result = []
        for query in queries:
            __ query[0] not in graph:
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1.0)
            else:
                tmp = [-1.0]
                self.dfs(valuesMap, graph, query[0], query[1], 1.0, set(), tmp)
                result.append(tmp[0])
        return result
    
    ___ dfs(self, valuesMap, graph, start, target, curr, visited, result):
        visited.add(start)
        __ start == target:
            result[0] = curr
        __ start in graph:
            for nextNode in graph[start]:
                __ nextNode not in visited:
                    self.dfs(valuesMap, graph, nextNode, target, curr*valuesMap[(start, nextNode)], visited, result)
    
    ___ test(self):
        testCases = [
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ],
            ),
        ]
        for equations, values, queries in testCases:
            result = self.calcEquation(equations, values, queries)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()


