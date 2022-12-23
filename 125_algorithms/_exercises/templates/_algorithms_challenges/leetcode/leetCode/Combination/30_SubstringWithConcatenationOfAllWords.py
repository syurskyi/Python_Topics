#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-12 18:57:50


c.. Solution o..
    """ Easy to think, but is very slow.

    Use an unordered_map<string, int> counts to record the expected times of each word and
    another unordered_map<string, int> seen to record the times we have seen
    """

    ___ findSubstring  s, words
        __ n.. s or n.. words:
            r_ []

        word_cnt _ # dict
        ___ w __ words:
            word_cnt[w] = word_cnt.get(w, 0) + 1

        s_len, word_l = l..(s), l..(words[0])
        concatenation_l = l..(words) * word_l
        ans   # list
        ___ i __ r..(s_len - concatenation_l + 1
            candidate_map _ # dict
            j = 0
            _____ j < l..(words
                w = s[i + j * word_l: i + (j + 1) * word_l]
                __ w n.. __ word_cnt:
                    ______
                candidate_map[w] = candidate_map.get(w, 0) + 1
                __ candidate_map.get(w, 0) > word_cnt[w]:
                    ______
                j += 1

            __ j __ l..(words
                ans.a.. i)

        r_ ans


c.. Solution_2 o..
    """ Use hashmap and two point.

    Travel all the words combinations to maintain a slicing window.
    There are wl(word len) times travel, each time n/wl words:
    mostly 2 times travel for each word:
        one left side of the window, the other right side of the window
    So, time complexity O(wl * 2 * N/wl) = O(2N)
    Refer to:
    https://discuss.leetcode.com/topic/6617/an-o-n-solution-with-detailed-explanation
    """
    ___ findSubstring  s, words
        __ n.. s or n.. words:
            r_ []

        word_cnt _ # dict
        ___ w __ words:
            word_cnt[w] = word_cnt.get(w, 0) + 1

        s_len, w_len, cnt = l..(s), l..(words[0]), l..(words)
        i = 0
        ans   # list
        _____ i < w_len:
            left, count = i, 0
            candidate_cnt _ # dict
            ___ j __ r..(i, s_len, w_len
                cur_str = s[j: j + w_len]
                __ cur_str __ word_cnt:
                    candidate_cnt[cur_str] = candidate_cnt.get(cur_str, 0) + 1
                    count += 1
                    __ candidate_cnt[cur_str] <= word_cnt[cur_str]:
                        pass
                    ____
                        # A more word, advance the window left side possiablly
                        _____ candidate_cnt[cur_str] > word_cnt[cur_str]:
                            left_str = s[left: left + w_len]
                            candidate_cnt[left_str] -= 1
                            left += w_len
                            count -= 1

                    # come to a result
                    __ count __ cnt:
                        ans.a.. left)
                        candidate_cnt[s[left:left + w_len]] -= 1
                        count -= 1
                        left += w_len
                # not a valid word, clear the window.
                ____
                    candidate_cnt _ # dict
                    left = j + w_len
                    count = 0
            i += 1
        r_ ans


c.. Solution_Fail o..
    """ Pythonic way, easy to think, but Time Limit Exceeded.

    Use two hash-map.
    """
    ___ findSubstring  s, words
        __ n.. s or n.. words:
            r_ []
        import collections
        word_cnt = collections.Counter(words)
        s_len, word_l = l..(s), l..(words[0])
        concatenation_l = l..(words) * word_l
        ans   # list
        ___ i __ r..(s_len - concatenation_l + 1
            candidate_str = s[i:i + concatenation_l]
            split_str = [candidate_str[j:j + word_l]
                         ___ j __ r..(0, concatenation_l, word_l)]
            candidate_cnt = collections.Counter(split_str)
            __ n.. (word_cnt - candidate_cnt
                ans.a.. i)
        r_ ans

"""
""
[]
"barfoothefoobarman"
["foo", "bar"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
"""
