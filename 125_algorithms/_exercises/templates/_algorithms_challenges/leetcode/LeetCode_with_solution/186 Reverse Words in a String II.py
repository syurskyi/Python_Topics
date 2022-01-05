"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ reverseWords  s):
        """
        in-place without allocating extra space

        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        reverse(s, 0, l..(s))
        i = 0
        w.... i < l..(s):
            j = i+1
            w.... j < l..(s) a.. s[j] != " ":
                j += 1

            reverse(s, i, j)
            i = j+1

    ___ reverse  s, start, end):
        i = start
        j = end
        w.... i < j-1:
            s[i], s[j-1] = s[j-1], s[i]
            i += 1
            j -= 1

__ _______ __ _______
    lst = l..("the sky is blue")
    Solution().reverseWords(lst)
    ... "".j..(lst) __ "blue is sky the"