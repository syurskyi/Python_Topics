'''
Created on Mar 4, 2017

@author: MT
'''

c_ Solution(o..):
    ___ alienOrder  words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph    # dict
        degree    # dict
        ___ word __ words:
            ___ c __ word:
                degree[c] = 0
        ___ i __ r..(1, l..(words)):
            currWord = words[i]
            prevWord = words[i-1]
            length = m..(l..(currWord), l..(prevWord))
            ___ j __ r..(length):
                c1, c2 = prevWord[j], currWord[j]
                __ c1 != c2:
                    __ c1 n.. __ graph:
                        graph[c1] = set()
                    __ c2 n.. __ graph[c1]:
                        degree[c2] += 1
                    graph[c1].add(c2)
                    _____
        queue    # list
        ___ c, cnt __ degree.i..:
            __ cnt __ 0:
                queue.a..(c)
        res = ''
        w.... queue:
            c = queue.pop(0)
            res += c
            ___ c0 __ graph.get(c, []):
                degree[c0] -= 1
                __ degree[c0] __ 0:
                    queue.a..(c0)
        r.. res __ l..(res) __ l..(degree) ____ ''
    
    ___ test
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
        ___ words __ testCases:
            print('words: %s' % (words))
            result = alienOrder(words)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__  __ '__main__':
    Solution().test()
