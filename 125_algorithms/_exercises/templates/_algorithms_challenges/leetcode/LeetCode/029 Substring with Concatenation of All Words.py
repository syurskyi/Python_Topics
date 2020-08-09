"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
__author__ = 'Danyang'
class Solution:
    ___ findSubstring_TLE(self, S, L
        """
        Time limit exceeded

        Algorithm
        1. brutal force scanning: O(n*(l*k))
        2. sliding window: O(n*k)
        n: le.(S)
        l: le.(L)
        k: le.(L[0])

        :param S: String
        :param L: a list of string
        :return: a list of integer
        """
        __ not L:
            r_

        k = le.(L[0])
        l = le.(L)

        working_list = list(L)
        result = []
        window_t = -1  # [0, t)
        window = []
        i = 0
        w___ i<=le.(S)-3:
            # test window
            __ le.(window)__l:
                result.append(window_t-l*k)

            word = S[i:i+3]
            __ word in working_list:
                window.append(word)
                working_list.remove(word)
                window_t = i+3
                i += 3

            ____ word not in L:
                __ window:
                    i = window_t-le.(window)*k+1  # going to original point plus 1
                ____
                    i += 1

                window = []
                window_t = -1
                working_list = list(L)


            ____ word in L and word not in working_list:
                window = window[window.index(word)+1:]
                window.append(word)
                # working_list.remove(word)
                window_t = i+3
                i += 3

        r_ result

    ___ findSubstring(self, S, L
        """
        Algorithm
        1. brutal force scanning: O(n*(l*k)), rechecking
        2. sliding window: O(n*k)
        n: le.(S)
        l: le.(L)
        k: le.(L[0])

        S = a1a3a2a1a3a4a5
        L = a1a2a3

        [a1a3a2]a1a3a4a5
        a1[a3a2a1]a3a4a5
        a1a3[a2a1a3]a4a5

        Notice:
        1. notice "aaaaaaaa" ["aa", "aa", "aa"]; sometimes cannot jump the whole word

        :param S: String
        :param L: a list of string
        :return: a list of integer
        """
        __ not L:
            r_

        k = le.(L[0])
        l = le.(L)

        Lmap = {}  # map of L
        ___ item in L:
            __ item in Lmap:
                Lmap[item] += 1
            ____
                Lmap[item] = 1

        Lmap_original = dict(Lmap)

        ret = []
        win_e = -1  # [0, t), no need start_ptr
        working_win = []
        i = 0
        w___ i<le.(S
            # test window
            __ le.(working_win)__l:
                ret.append(win_e-l*k)
                candidate = win_e-l*k+1
                __ S[candidate:candidate+k] in Lmap:
                    win_e = -1
                    i = candidate
                    Lmap = dict(Lmap_original)
                    working_win = []

            word = S[i:i+k]
            # case 1, match one in L
            __ word in Lmap and Lmap[word]>0:
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

            # case 2, no match
            ____ word not in Lmap:
                __ working_win:
                    i = win_e-le.(working_win)*k+1  # going to window start+1  # cannot jump
                ____
                    i += 1

                working_win = []
                win_e = -1
                Lmap = dict(Lmap_original)

            # case 3, mach one in L not used up
            ____ word in Lmap and Lmap[word]__0:
                ___ j in xrange(0, working_win.index(word)+1  # kind of prefix suffix concepts
                    Lmap[working_win[j]] += 1  # restore
                working_win = working_win[working_win.index(word)+1:]
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

        __ le.(working_win)__l:  # when reaching the end, assert Solution().findSubstring("a", ["a"])==[0]
            ret.append(win_e-l*k)

        r_ ret

__ __name____"__main__":
    assert Solution().findSubstring("abababab", ["a","b","a"])__[0,2,4]
    assert Solution().findSubstring("a", ["a"])__[0]
    assert Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])__[13]
    assert Solution().findSubstring("barfoofoofoobarman", ["foo", "foo"])__[3, 6]
