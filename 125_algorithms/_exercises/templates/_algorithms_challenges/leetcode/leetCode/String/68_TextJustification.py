#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ fullJustify  words, maxWidth
        """ Straightforward solution for the problem

        Refer to:
        https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines

        Once you determine that there are only k words that can fit on a given line,
        you know what the total length of those words is cur_letters.
        Then the rest are spaces, and there are L = (maxWidth - cur_letters) of spaces.

        The trick here is to use mod operation to manage the spaces.
        The "or 1" part is for dealing with the edge case len(cur) == 1.
        """
        ans, cur_words, cur_letters   # list, [], 0
        ___ w __ words:
            __ l..(cur_words) + cur_letters + l..(w) > maxWidth:
                pad_space_cnt = maxWidth - cur_letters
                ___ i __ r..(pad_space_cnt
                    cur_words[i % (l..(cur_words) - 1 or 1)] += ' '
                ans.a.. ''.join(cur_words))

                cur_words, cur_letters   # list, 0

            cur_words.a.. w)
            cur_letters += l..(w)

        r_ ans + [' '.join(cur_words).ljust(maxWidth)]

"""
["a"]
1
[""]
2
["This", "is", "an", "example", "of", "text", "justification."]
15
["This", "is", "an", "example", "of", "text", "justification."]
16
["This", "is", "an", "example", "of", "text", "justification."]
20
["What","must","be","shall","be."]
12
"""
