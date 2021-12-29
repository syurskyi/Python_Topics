"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    ___ reverseWords(self, s):
        """
        in-place without allocating extra space

        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, l..(s))
        i = 0
        while i < l..(s):
            j = i+1
            while j < l..(s) and s[j] != " ":
                j += 1

            self.reverse(s, i, j)
            i = j+1

    ___ reverse(self, s, start, end):
        i = start
        j = end
        while i < j-1:
            s[i], s[j-1] = s[j-1], s[i]
            i += 1
            j -= 1

__ __name__ __ "__main__":
    lst = l..("the sky is blue")
    Solution().reverseWords(lst)
    ... "".join(lst) __ "blue is sky the"