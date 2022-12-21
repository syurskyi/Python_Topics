#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-26 19:18:40


c.. Solution o..
    ___ groupAnagrams  strs
        """Hash tables: use sorted(word) as key.

        Note that list is unhashable type, so we need to change sorted
        str to tuple, which is hashable type.
        """
        d _ # dict
        ___ w __ s..(strs
            key = tuple(s..(w))
            d[key] = d.get(key, []) + [w]
        r_ d.values()

"""
[""]
["aaa", "aaa", "aa", "bb"]
["a", "b", "c", "d"]
"""
