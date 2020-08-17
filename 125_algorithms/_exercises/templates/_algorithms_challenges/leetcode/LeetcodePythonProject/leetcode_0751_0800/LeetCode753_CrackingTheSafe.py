'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object
    ___ crackSafe(self, n, k
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n
        arr = ['0']*n
        visited = set(['0'*n])
        self.dfs(arr, total, visited, n, k)
        r_ ''.join(arr)
    
    ___ dfs(self, arr, goal, visited, n, k
        __ le.(visited) __ goal: r_ True
        prevArr = arr[le.(arr)-n+1:]
        ___ i in range(k
            nextArr = prevArr+[str(i)]
            nextStr = ''.join(nextArr)
            __ nextStr not in visited:
                visited.add(nextStr)
                arr.append(str(i))
                __ self.dfs(arr, goal, visited, n, k
                    r_ True
                visited.remove(nextStr)
                arr.p..
        r_ False
    
    ___ test(self
        testCases = [
            [1, 2],
            [2, 2],
        ]
        ___ n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.crackSafe(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
