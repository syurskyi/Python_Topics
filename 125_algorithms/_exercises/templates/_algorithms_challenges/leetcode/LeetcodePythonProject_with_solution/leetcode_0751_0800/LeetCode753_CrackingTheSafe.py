'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object):
    ___ crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n
        arr = ['0']*n
        visited = set(['0'*n])
        self.dfs(arr, total, visited, n, k)
        r.. ''.join(arr)
    
    ___ dfs(self, arr, goal, visited, n, k):
        __ l..(visited) __ goal: r.. True
        prevArr = arr[l..(arr)-n+1:]
        ___ i __ r..(k):
            nextArr = prevArr+[str(i)]
            nextStr = ''.join(nextArr)
            __ nextStr n.. __ visited:
                visited.add(nextStr)
                arr.a..(str(i))
                __ self.dfs(arr, goal, visited, n, k):
                    r.. True
                visited.remove(nextStr)
                arr.pop()
        r.. False
    
    ___ test(self):
        testCases = [
            [1, 2],
            [2, 2],
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.crackSafe(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
