# Combinations
# Question: Given two integers n and k, return all possible combinations of k numbers out of 1 … n.
# For example,
# If n = 4 and k = 2, a solution is:
# [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]
# Solutions:


class Solution:
    def combine(self,n, k):
        def dfs(start, valuelist):
            if self.count == k: ret.append(valuelist); return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        ret = []; self.count = 0
        dfs(1, [])
        return ret

Solution().combine(4,2)