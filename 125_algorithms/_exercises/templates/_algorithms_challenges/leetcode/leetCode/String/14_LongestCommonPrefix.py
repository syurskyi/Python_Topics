#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ longestCommonPrefix  strs
        """
        :type strs: List[str]
        :rtype: str
        """
        __ n.. strs:
            r_ ""
        common_prefix = strs[0]
        ___ string __ strs:
            min_len = m.. l..(string), l..(common_prefix))
            mark = 0        # Record the longest commen prefix index right now.
            ___ i __ r..(min_len
                mark = i
                __ string[i] __ common_prefix[i]:
                    i += 1
                    mark = i
                ____
                    __ i __ 0:
                        r_ ""
                    ______
            common_prefix = common_prefix[:mark]

        r_ common_prefix

"""
[]
["abcd", "abc", "ab","acdef"]
["abc", "abcd", "d"]
"""
