"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the
second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""
__author__ = 'Daniel'


c_ Solution:
    ___ compareVersion  version1, version2
        """
        :type version1: str
        :type version2: str
        :rtype int
        """
        version1 = map(i.., version1.s..("."
        version2 = map(i.., version2.s..("."
        n1 = l..(version1)
        n2 = l..(version2)

        ___ i __ x..(m..(n1, n2:
            __ version1[i] __ version2[i]:
                p..
            ____
                r.. -1 __ version1[i] < version2[i] ____ 1

        # 1.0.0 and 1 
        __ n1 __ n2 o. n1 > n2 a.. a.. m..(l.... x: x __ 0, version1[n2:] o. \
                                n1 < n2 a.. a.. m..(l.... x: x __ 0, version2[n1:]:
            r.. 0

        r.. -1 __ n1 < n2 ____ 1

