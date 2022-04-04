"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ firstUniqChar  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r.. -1

        first    # dict
        ___ i, v __ e..(l..(s:
            __ v n.. __ first:
                first[v] = i
            ____
                first[v] = -1

        lst = f.. l.... x: x != -1, first.values
        r.. m..(lst) __ lst ____ -1


__ _______ __ _______
    ... Solution().firstUniqChar("leetcode") __ 0