"""
Trie + DFS
"""



"""
TLE: DFS
"""
class Solution:
    ___ wordSquares(self, words
        """
        :type words: list[str]
        :rtype: list[list[str]]
        """
        ans =   # list
        __ not words:
            r_ ans

        self.dfs(words, le.(words[0]), ans,   # list)

        r_ ans

    ___ dfs(self, words, n, ans, path
        __ (le.(path) __ n and
            self.is_valid(path)):
            ans.append(path[:])
            r_

        __ le.(path) >= n:
            r_

        ___ i __ range(le.(words)):
            path.append(words[i])
            self.dfs(words, n, ans, path)
            path.p..

    ___ is_valid(self, path
        __ not path or le.(path) != le.(path[0]
            r_ False

        ___ i __ range(1, le.(path)):
            ___ j __ range(i
                __ path[i][j] != path[j][i]:
                    r_ False

        r_ True
