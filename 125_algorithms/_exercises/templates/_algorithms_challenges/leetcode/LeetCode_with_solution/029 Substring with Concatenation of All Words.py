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
c_ Solution:
    ___ findSubstring_TLE  S, L):
        """
        Time limit exceeded

        Algorithm
        1. brutal force scanning: O(n*(l*k))
        2. sliding window: O(n*k)
        n: len(S)
        l: len(L)
        k: len(L[0])

        :param S: String
        :param L: a list of string
        :return: a list of integer
        """
        __ n.. L:
            r..

        k = l..(L[0])
        l = l..(L)

        working_list = l..(L)
        result    # list
        window_t = -1  # [0, t)
        window    # list
        i = 0
        w.... i<=l..(S)-3:
            # test window
            __ l..(window)__l:
                result.a..(window_t-l*k)

            word = S[i:i+3]
            __ word __ working_list:
                window.a..(word)
                working_list.remove(word)
                window_t = i+3
                i += 3

            ____ word n.. __ L:
                __ window:
                    i = window_t-l..(window)*k+1  # going to original point plus 1
                ____:
                    i += 1

                window    # list
                window_t = -1
                working_list = l..(L)


            ____ word __ L a.. word n.. __ working_list:
                window = window[window.index(word)+1:]
                window.a..(word)
                # working_list.remove(word)
                window_t = i+3
                i += 3

        r.. result

    ___ findSubstring  S, L):
        """
        Algorithm
        1. brutal force scanning: O(n*(l*k)), rechecking
        2. sliding window: O(n*k)
        n: len(S)
        l: len(L)
        k: len(L[0])

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
        __ n.. L:
            r..

        k = l..(L[0])
        l = l..(L)

        Lmap    # dict  # map of L
        ___ item __ L:
            __ item __ Lmap:
                Lmap[item] += 1
            ____:
                Lmap[item] = 1

        Lmap_original = d..(Lmap)

        ret    # list
        win_e = -1  # [0, t), no need start_ptr
        working_win    # list
        i = 0
        w.... i<l..(S):
            # test window
            __ l..(working_win)__l:
                ret.a..(win_e-l*k)
                candidate = win_e-l*k+1
                __ S[candidate:candidate+k] __ Lmap:
                    win_e = -1
                    i = candidate
                    Lmap = d..(Lmap_original)
                    working_win    # list

            word = S[i:i+k]
            # case 1, match one in L
            __ word __ Lmap a.. Lmap[word]>0:
                working_win.a..(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

            # case 2, no match
            ____ word n.. __ Lmap:
                __ working_win:
                    i = win_e-l..(working_win)*k+1  # going to window start+1  # cannot jump
                ____:
                    i += 1

                working_win    # list
                win_e = -1
                Lmap = d..(Lmap_original)

            # case 3, mach one in L not used up
            ____ word __ Lmap a.. Lmap[word]__0:
                ___ j __ xrange(0, working_win.index(word)+1):  # kind of prefix suffix concepts
                    Lmap[working_win[j]] += 1  # restore
                working_win = working_win[working_win.index(word)+1:]
                working_win.a..(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

        __ l..(working_win)__l:  # when reaching the end, assert Solution().findSubstring("a", ["a"])==[0]
            ret.a..(win_e-l*k)

        r.. ret

__ _____ __ ____
    ... Solution().findSubstring("abababab", ["a","b","a"])__[0,2,4]
    ... Solution().findSubstring("a", ["a"])__[0]
    ... Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])__[13]
    ... Solution().findSubstring("barfoofoofoobarman", ["foo", "foo"])__[3, 6]
