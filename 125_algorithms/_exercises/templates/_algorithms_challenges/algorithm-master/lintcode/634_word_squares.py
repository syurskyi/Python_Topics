"""
Trie + DFS
"""



"""
TLE: DFS
"""
class Solution:
    ___ wordSquares(self, words):
        """
        :type words: list[str]
        :rtype: list[list[str]]
        """
        ans = []
        __ not words:
            return ans

        self.dfs(words, len(words[0]), ans, [])

        return ans

    ___ dfs(self, words, n, ans, path):
        __ (len(path) == n and
            self.is_valid(path)):
            ans.append(path[:])
            return

        __ len(path) >= n:
            return

        for i in range(len(words)):
            path.append(words[i])
            self.dfs(words, n, ans, path)
            path.pop()

    ___ is_valid(self, path):
        __ not path or len(path) != len(path[0]):
            return False

        for i in range(1, len(path)):
            for j in range(i):
                __ path[i][j] != path[j][i]:
                    return False

        return True
