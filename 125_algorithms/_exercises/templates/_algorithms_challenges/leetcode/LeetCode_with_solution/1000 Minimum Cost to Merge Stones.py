#!/usr/bin/python3
"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i]
stones.

A move consists of merging exactly K consecutive piles into one pile, and the
cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is
impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't
merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""
____ t___ _______ L..
____ f.. _______ l..


c_ Solution:
    ___ mergeStones  stones: L..[i..], K: i..) __ i..
        """
        Mergeable? K -> 1. Reduction size (K - 1)
        N - (K - 1) * m = 1
        mergeable: (N - 1) % (K - 1) = 0

        K consecutive
        every piles involves at least once
        Non-consecutive: priority queue merge the least first
        But here it is consecutive, need to search, cannot gready

        * Merge the piles cost the same as merge individual ones.

        Attemp 1:
        F[i] = cost to merge A[:i] into 1
        F[i] = F[i-3] + A[i-1] + A[i-2] + A[i-3] ??

        Attemp 2:
        F[i][j] = cost of merge A[i:j] into 1
        F[i][j] = F[i][k] + F[k][j] ??

        Answer:
        F[i][j][m] = cost of merge A[i:j] into m piles
        F[i][j][1] = F[i][j][k] + sum(stones[i:j])  # merge 
        F[i][j][m] = min F[i][mid][1] + F[mid][j][m-1]  # add

        initial:
        F[i][i+1][1] = 0
        F[i][i+1][m] = inf

        since the mid goes through the middle in the i, j.
        Use memoization rather than dp
        """
        N l..(stones)
        sums [0]
        ___ s __ stones:
            sums.a..(sums[-1] + s)

        ??(N..)
        ___ F(i, j, m
            __ i >_ j o. m < 1
                r.. f__("inf")

            n j - i
            __ (n - m) % (K - 1) !_ 0:
                r.. f__("inf")

            __ j __ i + 1:
                __ m __ 1:
                    r.. 0
                r.. f__("inf")

            __ m __ 1:
                r.. F(i, j, K) + sums[j] - sums[i]

            ret m..(
                F(i, mid, 1) + F(mid, j, m - 1)
                ___ mid __ r..(i + 1, j, K - 1)
            )
            r.. ret

        ret F(0, N, 1)
        r.. ret __ ret !_ f__("inf") ____ -1


__ _______ __ _______
    ... Solution().mergeStones([3,5,1,2,6], 3) __ 25
