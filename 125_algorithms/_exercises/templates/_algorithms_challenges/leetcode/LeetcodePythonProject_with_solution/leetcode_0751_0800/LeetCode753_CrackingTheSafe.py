'''
Created on Mar 28, 2018

@author: tongq
'''
c_ Solution(o..
    ___ crackSafe  n, k
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n
        arr =  '0' *n
        visited = s..( '0'*n])
        dfs(arr, total, visited, n, k)
        r.. ''.j..(arr)
    
    ___ dfs  arr, goal, visited, n, k
        __ l..(visited) __ goal: r.. T..
        prevArr = arr[l..(arr)-n+1:]
        ___ i __ r..(k
            nextArr = prevArr+[s..(i)]
            nextStr = ''.j..(nextArr)
            __ nextStr n.. __ visited:
                visited.add(nextStr)
                arr.a..(s..(i
                __ dfs(arr, goal, visited, n, k
                    r.. T..
                visited.remove(nextStr)
                arr.p.. )
        r.. F..
    
    ___ test
        testCases = [
            [1, 2],
            [2, 2],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = crackSafe(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
