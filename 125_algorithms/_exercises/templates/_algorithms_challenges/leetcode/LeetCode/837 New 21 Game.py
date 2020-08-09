#!/usr/bin/python3
"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers w___ she has less than K points.
During each draw, she gains an integer number of points randomly from the range
[1, W], where W is an integer.  Each draw is independent and the outcomes have
equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the
probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct
answer.
The judging time limit has been reduced for this question.
"""


class Solution:
    ___ new21Game(self, N: int, K: int, W: int) -> float:
        """
        F[i]: probability of get points i
        F[i] = F[j] * (1 / W) for every i - j <= W
        => O(N*W)
        F[i] = sum(last W dp values) * (1 / W)
        To get cur_sum, where cur_sum = sum(last W dp values), we can maintain a
        sliding window with size at most K.
        => O(N)
        """
        __ K __ 0:
            r_ 1

        F = [0 ___ _ in range(N+1)]
        F[0] = 1
        cur_sum = F[0]
        ret = 0
        ___ i in range(1, N+1
            F[i] = cur_sum * (1/W)
            __ i >= K:
                ret += F[i]
                # stop
            ____
                cur_sum += F[i]
                
            __ i - W >= 0:
                cur_sum -= F[i - W]

        r_ ret

    ___ new21Game_error(self, N: int, K: int, W: int) -> float:
        """
        DP
        Let F[i] be the probability of reaching point i

        O(N^2)
        """
        F = [0 ___ _ in range(K+W+1)]
        F[0] = 1
        ___ i in range(1, K+W+1
            ___ j in range(W, 0, -1
                __ i - j >= K:
                    break
                __ i - j >= 0:
                    F[i] += F[i-j] * 1 / W

        ret = su.(F[1:N+1])  # error
        print(F, ret)
        r_ ret


__ __name__ __ "__main__":
    assert Solution().new21Game(6, 1, 10) __ 0.6
