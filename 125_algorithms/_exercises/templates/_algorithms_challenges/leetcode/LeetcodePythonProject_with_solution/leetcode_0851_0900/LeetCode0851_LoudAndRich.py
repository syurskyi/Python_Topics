'''
Created on Sep 9, 2019

@author: tongq
'''
c_ Solution(o..
    ___ loudAndRich  richer, quiet
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = l..(quiet)
        richer2    # dict
        ___ i __ r..(n
            richer2[i]    # list
        ___ v __ richer:
            richer2[v[1]].a..(v[0])
        res = [-1 ___ i __ r..(n)]
        ___ i __ r..(n
            dfs(i, quiet, richer2, res)
        r.. res
    
    ___ dfs  i, quiet, richer2, res
        __ (res[i] >_ 0
            r.. res[i]
        res[i] = i
        ___ j __ richer2[i]:
            __ quiet[res[i]] > quiet[dfs(j, quiet, richer2, res)]:
                res[i] = res[j]
        r.. res[i]
    
    ___ test
        testCase = [
            [
                [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                [3,2,5,4,6,1,7,0],
            ],
        ]
        ___ richer, quiet __ testCase:
            res = loudAndRich(richer, quiet)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
