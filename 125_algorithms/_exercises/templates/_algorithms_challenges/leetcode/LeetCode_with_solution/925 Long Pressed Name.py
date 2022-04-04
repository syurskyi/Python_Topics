#!/usr/bin/python3
"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a
character c, the key might get long pressed, and the character will be typed 1
or more times.

You examine the typed characters of the keyboard.  Return True if it is possible
that it was your friends name, with some characters (possibly none) being long
pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


c_ Solution:
    ___ isLongPressedName  name: s.., typed: s..) __ b..:
        """
        two pointers
        """
        m, n = l..(name), l..(typed)
        i, j = 0, 0
        w.... i < m a.. j < n:
            __ name[i] __ typed[j]:
                i += 1
                j += 1
            ____ j - 1 >= 0 a.. typed[j-1] __ typed[j]:
                j += 1
            ____
                r.. F..

        # tail
        w.... j - 1 >= 0 a.. j < n a.. typed[j-1] __ typed[j]:
            j += 1

        r.. i __ m a.. j __ n
