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


class Solution(object
    ___ firstUniqChar(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s:
            r_ -1

        first = {}
        ___ i, v in enumerate(list(s)):
            __ v not in first:
                first[v] = i
            ____
                first[v] = -1

        lst = filter(lambda x: x != -1, first.values())
        r_ min(lst) __ lst else -1


__ __name__ __ "__main__":
    assert Solution().firstUniqChar("leetcode") __ 0