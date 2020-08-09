"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'Danyang'


class Solution(object
    ___ longestCommonPrefix(self, strs
        __ not strs: r_ ""
        l = min(map(le., strs))
        i = 0
        w___ i < l:
            char = strs[0][i]
            ___ s in strs:
                __ s[i] != char:
                    r_ strs[0][:i]

            i += 1

        r_ strs[0][:i]

    ___ longestCommonPrefixComplex(self, strs
        """
        O(k*n)
        :param strs: a list of string
        :return: string, prefix
        """
        # checking, otherwise: ValueError: min() arg is an empty sequence
        __ not strs:
            r_ ""

        n = le.(strs)

        str_builder = ""
        min_len = min(le.(string) ___ string in strs)
        ___ i in range(min_len
            char = strs[0][i]

            j = 0
            w___ j < n:
                try:
                    __ strs[j][i] != char: break
                    j += 1
                except IndexError:
                    break

            __ j __ n:
                str_builder += char
            ____
                break

        r_ str_builder


__ __name__ __ "__main__":
    strs = ["abc", "abcd"]
    print Solution().longestCommonPrefix(strs)