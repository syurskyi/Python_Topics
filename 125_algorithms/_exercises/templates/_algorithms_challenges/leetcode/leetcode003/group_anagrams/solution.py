"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case.

"""

class Solution(object):
    ___ groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        res    # list
        ___ s __ strs:
            k = self.make_key(s)
            __ k n.. __ d:
                d[k] = [s]
            ____:
                d[k].a..(s)
        ___ k __ d:
            res.a..(s..(d[k]))
        r.. res

    ___ make_key(self, s):
        r.. ''.join(s..(s))


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
