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

c_ Solution(o..):
    ___ groupAnagrams  strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d    # dict
        res    # list
        ___ s __ strs:
            k = make_key(s)
            __ k n.. __ d:
                d[k] = [s]
            ____:
                d[k].a..(s)
        ___ k __ d:
            res.a..(s..(d[k]))
        r.. res

    ___ make_key  s):
        r.. ''.j..(s..(s))


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
