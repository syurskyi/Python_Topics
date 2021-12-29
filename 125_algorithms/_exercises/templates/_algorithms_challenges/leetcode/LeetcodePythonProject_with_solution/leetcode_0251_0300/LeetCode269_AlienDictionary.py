'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    ___ alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {}
        degree = {}
        for word in words:
            for c in word:
                degree[c] = 0
        for i in range(1, len(words)):
            currWord = words[i]
            prevWord = words[i-1]
            length = min(len(currWord), len(prevWord))
            for j in range(length):
                c1, c2 = prevWord[j], currWord[j]
                __ c1 != c2:
                    __ c1 not in graph:
                        graph[c1] = set()
                    __ c2 not in graph[c1]:
                        degree[c2] += 1
                    graph[c1].add(c2)
                    break
        queue = []
        for c, cnt in degree.items():
            __ cnt == 0:
                queue.append(c)
        res = ''
        while queue:
            c = queue.pop(0)
            res += c
            for c0 in graph.get(c, []):
                degree[c0] -= 1
                __ degree[c0] == 0:
                    queue.append(c0)
        return res __ len(res) == len(degree) else ''
    
    ___ test(self):
        testCases = [
            [
                "wrt",
                "wrf",
                "er",
                "ett",
                "rftt",
            ],
            [
                'z',
                'x',
            ],
            [
                'z',
                'x',
                'z',
            ],
            ["za","zb","ca","cb"],
            ["a","b","ca","cc"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.alienOrder(words)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__  == '__main__':
    Solution().test()
