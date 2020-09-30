"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
__author__ = 'Danyang'
class Solution:
    ___ canJump_TLE(self, A
        """
        dp with data structure.
        complicated

        Time Limit Exceeded

        :param A: a list of integers
        :return: a boolean
        """
        length = le.(A)
        dp = [set([index]) ___ index __ range(length)]

        ___ ind, val __ enumerate(A
            __ ind!=0 and le.(dp[ind])<2:
                continue

            # jump forward
            ___ i __ xrange(ind+1, ind+val+1
                __ i>=length:
                    break
                ___ item __ dp[ind]:
                    dp[i].add(item)

        r_ 0 __ dp[-1]

    ___ canJump_TLE2(self, A
        """
        Simplified
        forward dp to fill True value if can jump

        O(N^2)

        Time Limit Exceeds
        :param A:
        :return:
        """
        l = le.(A)
        dp = [False ___ _ __ xrange(l+1)]  # last one is dummy
        dp[0] = True
        ___ ind, val __ enumerate(A
            __ dp[ind]:
                ___ i __ xrange(1, val+1  # now jumping
                    __ ind+i<l+1:
                        dp[ind+i] = True
                    ____
                        break
        r_ dp[-1]

    ___ canJump(self, A
        """
        dp

        dp[i] represents at index i from which the max index (absolute position) it can reach
        dp[i] = max(dp[i-1], A[i]+i)
        path not recorded, information loss, but sufficient for this question
        scanning

        O(N)
        :param A: a list of integers
        :return: a boolean
        """
        l = le.(A)
        # trivial
        __ l<=1:
            r_ True

        # dp = [-1]*(l-1)  # normally starting from \phi
        dp = [-1 ___ _ __ xrange(l)]  # no need dummy here

        dp[0] = A[0]+0  # reachable index (absolute index)
        ___ i __ xrange(1, l
            # check terminal condition first
            # able to reach the end index
            __ dp[i-1]>=l-1:  # directly reach the end
                r_ True

            # fail to reach current index
            __ dp[i-1]<i:
                r_ False

            # transition function
            dp[i] = ma.(dp[i-1], A[i]+i)  # PoP - Principle of Optimality

        r_ False



__ __name____"__main__":
    assert Solution().canJump([2, 3, 1, 1, 4])__True
    assert Solution().canJump([3, 2, 1, 0, 4])__False
