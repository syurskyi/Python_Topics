"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
______ ma__

__author__ = 'Danyang'


class Solution(object
    ___ numTrees_math(self, n
        """
        number of unique binary search tree
        Catalan Number

        C_n = {2n\choose n} - {2n\choose n+1}
        Proof: http://en.wikipedia.org/wiki/Catalan_number#Second_proof
        :param n: integer
        :return: integer
        """
        r_ ma__.factorial(2*n)/(ma__.factorial(n)*ma__.factorial(n))-ma__.factorial(2*n)/(
            ma__.factorial(n+1)*ma__.factorial(n-1))

    ___ numTrees(self, n
        """
        number of unique binary search tree
        dp

        dp[i] means # BST constructed from [1...i]

        dp[3] = dp[0]*dp[2]  # 1 as pivot
               +dp[1]*dp[1]  # 2 is pivot
               +dp[2]*dp[0]  # 3 as pivot

        follow the 2nd proof of Catalan number.
        Proof: http://en.wikipedia.org/wiki/Catalan_number#First_proof
        :param n: integer
        :return: integer
        """
        __ n < 2:
            r_ n

        dp = [0 ___ _ __ xrange(n+1)]
        dp[0] = 1
        ___ i __ xrange(1, n+1
            ___ j __ xrange(i
                dp[i] += dp[j]*dp[i-j-1]
        r_ dp[-1]


__  -n __ "__main__":
    assert Solution().numTrees(100) __ Solution().numTrees_math(100)