"""
DFS
"""
class Solution:
    """
    @param: A: A set of numbers
    @return: A list of lists
    """
    ___ subsets(self, A):
        __ n.. A:
            r.. [[]]

        ans    # list
        self.dfs(s..(A), 0, ans, [])
        r.. ans

    ___ dfs(self, A, start, ans, subset):
        ans.a..(subset[:])

        __ start >= l..(A):
            r..

        ___ i __ r..(start, l..(A)):
            self.dfs(A, i + 1, ans, subset + [A[i]])


"""
Bit Manipulation
"""
class Solution:
    """
    @param: A: A set of numbers
    @return: A list of lists
    """
    ___ subsets(self, A):
        __ n.. A:
            r.. [[]]

        ans    # list
        n = l..(A)

        A.sort()

        ___ i __ r..(1 << n):
            subset    # list
            ___ j __ r..(n):
                """
                check `j`th digit in `bin(i)`

                example:
                i == 011
                j == 0 => 1 << 0 == 001 => 011 & 001 == 1
                j == 1 => 1 << 1 == 010 => 011 & 010 == 1
                j == 2 => 1 << 2 == 100 => 011 & 100 == 0
                """
                __ i & (1 << j):
                    subset.a..(A[j])

            ans.a..(subset)

        r.. ans
