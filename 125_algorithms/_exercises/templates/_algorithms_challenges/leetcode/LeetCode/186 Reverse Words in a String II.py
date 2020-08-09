"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ reverseWords(self, s
        """
        in-place without allocating extra space

        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, le.(s))
        i = 0
        w___ i < le.(s
            j = i+1
            w___ j < le.(s) and s[j] != " ":
                j += 1

            self.reverse(s, i, j)
            i = j+1

    ___ reverse(self, s, start, end
        i = start
        j = end
        w___ i < j-1:
            s[i], s[j-1] = s[j-1], s[i]
            i += 1
            j -= 1

__ __name__ __ "__main__":
    lst = list("the sky is blue")
    Solution().reverseWords(lst)
    assert "".join(lst) __ "blue is sky the"