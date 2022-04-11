#!/usr/bin/python3
"""
Initially on a notepad only one character 'A' is present. You can perform two
operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy
is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the
minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.


Note:

The n will be in the range [1, 1000].
"""


c_ Solution:
    ___ minSteps  n: i..) __ i..:
        """
        Prime numger
        To get 12
        We need to copy 6 (* 2)
        To get 6
        We need to copy 2 (* 3)
        To get 2
        We need to copy 1 (* 2)
        """
        ret 0
        ___ i __ r..(2, n+1
            w.... n % i __ 0:
                ret += i
                n //= i

        r.. ret

    ___ minSteps_dp  n: i..) __ i..:
        """
        Let F[i][j] be the minimum number to reach i A's with j copies
        F[i][k] = min
          F[i-k][k] + 1
          F[i/2][i/2] + 2  if i/2 == k

        Better dp:
        F[i] = F[j] + j / i   # copy j / i times
        """
        F [[f__('inf') ___ _ __ r..(n+1)] ___ _ __ r..(n+1)]
        F[1][0] 0
        F[1][1] 1
        ___ i __ r..(2, n + 1
            ___ j __ r..(i+1
                F[i][j] m..(
                    F[i][j],
                    F[i-j][j] + 1,
                )
                __ i % 2 __ 0:
                    F[i][i//2] m..(
                        F[i][i//2],
                        F[i//2][j] + 2
                    )


        ret m..(F[n])
        r.. ret


__ _______ __ _______
    ... Solution().minSteps(7) __ 7
    ... Solution().minSteps(3) __ 3
    ... Solution().minSteps(4) __ 4
