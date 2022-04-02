"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ longestCommonPrefix  strs
        __ n.. strs: r.. ""
        l = m.. m..(l.., strs))
        i = 0
        w.... i < l:
            char = strs[0][i]
            ___ s __ strs:
                __ s[i] != char:
                    r.. strs[0][:i]

            i += 1

        r.. strs[0][:i]

    ___ longestCommonPrefixComplex  strs
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
        min_len = m..(l..(s__) ___ s__ __ strs)
        ___ i __ r..(min_len
            char = strs[0][i]

            j = 0
            w.... j < n:
                ___
                    __ strs[j][i] != char: _____
                    j += 1
                ______ I..
                    _____

            __ j __ n:
                str_builder += char
            ____:
                _____

        r.. str_builder


__ _______ __ _______
    strs = ["abc", "abcd"]
    print Solution().longestCommonPrefix(strs)