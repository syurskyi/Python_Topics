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
        ans    # list
        __ n.. words:
            r.. ans

        self.dfs(words, l..(words[0]), ans, [])

        r.. ans

    ___ dfs(self, words, n, ans, path):
        __ (l..(path) __ n and
            self.is_valid(path)):
            ans.a..(path[:])
            r..

        __ l..(path) >= n:
            r..

        ___ i __ r..(l..(words)):
            path.a..(words[i])
            self.dfs(words, n, ans, path)
            path.pop()

    ___ is_valid(self, path):
        __ n.. path o. l..(path) != l..(path[0]):
            r.. False

        ___ i __ r..(1, l..(path)):
            ___ j __ r..(i):
                __ path[i][j] != path[j][i]:
                    r.. False

        r.. True
