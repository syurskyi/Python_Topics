#!/usr/bin/python3
"""
Given a string and a string dictionary, find the longest string in the
dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the
smallest lexicographical order. If there is no possible result, return the empty
string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
from collections ______ defaultdict


class Solution:
    ___ findLongestWord(self, s, d
        """
        Compare subsequence: O(|S|) (two pointers)
        Then iterate d, check subsequence: O(|S||d|)

        Generalize two pointers to n pointers
        O(|S||d|)


        :type s: str
        :type d: List[str]
        :rtype: str
        """
        h = defaultdict(list)
        ___ d_idx, w __ enumerate(d
            w_idx = 0
            h[w[w_idx]].append((d_idx, w_idx))

        ret = ""
        ___ e __ s:
            lst = h.pop(e,   # list)
            ___ d_idx, w_idx __ lst:
                w = d[d_idx]
                w_idx += 1
                __ w_idx >= le.(w
                    # if le.(w) >= le.(ret) and w < ret:  # error
                    ret = min(ret, w, key=lambda x: (-le.(x), x))  # compare with primary and secondary key
                ____
                    h[w[w_idx]].append((d_idx, w_idx))

        r_ ret


__  -n __ "__main__":
    assert Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) __ "apple"
