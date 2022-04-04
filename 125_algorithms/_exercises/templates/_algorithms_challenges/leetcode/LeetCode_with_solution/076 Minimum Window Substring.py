"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
_______ ___

__author__ = 'Danyang'


c_ Solution(o..
    ___ minWindow  S, T
        """
        Algorithm:
        two pointers

        Aggressively enclose the chars until find all T, and then shrink the window as far as possible
        :param S: str
        :param T: str
        :return: str
        """
        min_win = [0, ___.maxint]  # [start, end)
        w_cnt = [0 ___ _ __ r..(256)]  # window
        t_cnt = [0 ___ _ __ r..(256)]  # 256 ascii, static
        ___ char __ T:
            t_cnt[o..(char)] += 1

        appeared_cnt = 0
        lo = 0
        ___ hi __ x..(1, l..(S)+1
            # expand
            val = S[hi-1]
            __ t_cnt[o..(val)] > 0:
                w_cnt[o..(val)] += 1

            __ t_cnt[o..(val)] > 0 a.. w_cnt[o..(val)] <= t_cnt[o..(val)]:
                appeared_cnt += 1  # cache, determine when to decrease appeared_cnt

            # shrink
            __ appeared_cnt __ l..(T  # until find all
                w.... w_cnt[o..(S[lo])] > t_cnt[o..(S[lo])] o. t_cnt[o..(S[lo])] __ 0:
                    __ w_cnt[o..(S[lo])] > 0: w_cnt[o..(S[lo])] -= 1
                    lo += 1

                __ min_win[1]-min_win[0] > hi-lo:
                    min_win[0], min_win[1] = lo, hi

        __ min_win[1] __ ___.maxint:
            r.. ""
        ____
            r.. S[min_win[0]:min_win[1]]


__ _______ __ _______
    ... Solution().minWindow("ADOBECODEBANC", "ABC") __ "BANC"