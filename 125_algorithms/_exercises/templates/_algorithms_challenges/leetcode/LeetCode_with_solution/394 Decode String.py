"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat
numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ decodeString  s
        """
        :type s: str
        :rtype: str
        """
        stk [
            [1, []]
        ]  # with default
        i 0
        w.... i < l..(s
            __ s[i].i..  # construct number from digit
                j i+1
                w.... s[j] !_ ' ': j += 1
                stk.a..([
                    i..(s[i:j]),    # list
                ])
                i j+1
            ____ s[i].isl..  # append alphabet
                stk[-1][1].a..(s[i])
                i += 1
            ____ s[i] __ ' ':  # pop
                cnt, p.. stk.p.. )
                p.. ''.j..(p..) * cnt
                stk[-1][1].a..(p..)
                i += 1

        r.. ''.j..(stk.p.. )[1])


c_ SolutionVerbose(o..
    ___ decodeString  s
        """
        :type s: str
        :rtype: str
        """
        stk    # list
        i 0
        ret    # list
        w.... i < l..(s
            __ s[i].i..  # construct number from digit
                j i+1
                w.... s[j] !_ ' ': j += 1
                stk.a..([
                    i..(s[i:j]),    # list
                ])
                i j+1
            ____ s[i].isl..  # append alphabet
                __ n.. stk:
                    ret.a..(s[i])
                ____
                    stk[-1][1].a..(s[i])
                i += 1
            ____ s[i] __ ' ':  # pop
                cnt, p.. stk.p.. )
                p.. ''.j..(p..) * cnt
                __ n.. stk:
                   ret.a..(p..)
                ____
                    stk[-1][1].a..(p..)

                i += 1

        r.. ''.j..(ret)


c_ SolutionError(o..
    ___ decodeString  s
        """
        :type s: str
        :rtype: str
        """
        stk    # list
        i 0
        ret    # list
        w.... i < l..(s
            __ s[i].i..
                j i + 1
                w.... s[j] !_ ' ': j += 1
                prev stk[-1] __ stk ____ 1
                stk.a..(prev * i..(s[i:j]
                i j + 1
            ____ s[i].isl..
                repeat stk[-1] __ stk ____ 1
                ___ _ __ x..(repeat ret.a..(s[i])
                i += 1
            ____ s[i] __ ' ':
                stk.p.. )
                i += 1

        r.. ''.j..(ret)


__ _______ __ _______
    ... Solution().decodeString('2[abc]3[cd]ef') __ 'abcabccdcdcdef'




