"""
DFS
"""
class Solution:
    """
    @param: A: A set of numbers
    @return: A list of lists
    """
    ___ subsets(self, A
        __ not A:
            r_ [[]]

        ans = []
        self.dfs(sorted(A), 0, ans, [])
        r_ ans

    ___ dfs(self, A, start, ans, subset
        ans.append(subset[:])

        __ start >= le.(A
            r_

        for i in range(start, le.(A)):
            self.dfs(A, i + 1, ans, subset + [A[i]])


"""
Bit Manipulation
"""
class Solution:
    """
    @param: A: A set of numbers
    @return: A list of lists
    """
    ___ subsets(self, A
        __ not A:
            r_ [[]]

        ans = []
        n = le.(A)

        A.sort()

        for i in range(1 << n
            subset = []
            for j in range(n
                """
                check `j`th digit in `bin(i)`

                example:
                i == 011
                j == 0 => 1 << 0 == 001 => 011 & 001 == 1
                j == 1 => 1 << 1 == 010 => 011 & 010 == 1
                j == 2 => 1 << 2 == 100 => 011 & 100 == 0
                """
                __ i & (1 << j
                    subset.append(A[j])

            ans.append(subset)

        r_ ans
