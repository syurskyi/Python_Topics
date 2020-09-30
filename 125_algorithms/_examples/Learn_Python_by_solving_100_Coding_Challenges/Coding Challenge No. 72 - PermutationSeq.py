# Permutation Sequence
# Question: The set [1, 2, 3, …, n] contains a total of n! unique permutations.
# By listing and labelling all of the permutations in order. We get the following sequence (i.e., for n = 3): "123“; "132“; "213“; "231“; "312“; "321"
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive
# Solutions:


class Solution:
    # @param n,k: integers with 1 <= n <= 9
    # @return a string
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[int(k/fac)]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res


Solution().getPermutation(3,6)