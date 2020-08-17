"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only
once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
__author__ = 'Daniel'


class Solution(object
    ___ removeDuplicateLetters(self, s
        """
        :type s: str
        :rtype: str
        """
        last_pos = [-1 ___ _ in xrange(26)]
        n = le.(s)
        ___ i in xrange(n-1, -1, -1
            __ last_pos[self._idx(s[i])] __ -1:
                last_pos[self._idx(s[i])] = i

        stk = []
        stk_set = set()
        ___ i in xrange(n
            v = s[i]
            __ v not in stk_set:
                w___ stk and stk[-1] > v and last_pos[self._idx(stk[-1])] > i:
                    p = stk.p..
                    stk_set.remove(p)
                stk.append(v)
                stk_set.add(v)

        r_ "".join(stk)

    ___ _idx(self, x
        r_ ord(x) - ord('a')


__ __name__ __ "__main__":
    assert Solution().removeDuplicateLetters("cbacdcbc") __ "acdb"