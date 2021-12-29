"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'Danyang'


class Solution(object):
    ___ longestCommonPrefix(self, strs):
        __ n.. strs: r.. ""
        l = m..(map(l.., strs))
        i = 0
        while i < l:
            char = strs[0][i]
            ___ s __ strs:
                __ s[i] != char:
                    r.. strs[0][:i]

            i += 1

        r.. strs[0][:i]

    ___ longestCommonPrefixComplex(self, strs):
        """
        O(k*n)
        :param strs: a list of string
        :return: string, prefix
        """
        # checking, otherwise: ValueError: min() arg is an empty sequence
        __ n.. strs:
            r.. ""

        n = l..(strs)

        str_builder = ""
        min_len = m..(l..(string) ___ string __ strs)
        ___ i __ r..(min_len):
            char = strs[0][i]

            j = 0
            while j < n:
                try:
                    __ strs[j][i] != char: break
                    j += 1
                except IndexError:
                    break

            __ j __ n:
                str_builder += char
            ____:
                break

        r.. str_builder


__ __name__ __ "__main__":
    strs = ["abc", "abcd"]
    print Solution().longestCommonPrefix(strs)