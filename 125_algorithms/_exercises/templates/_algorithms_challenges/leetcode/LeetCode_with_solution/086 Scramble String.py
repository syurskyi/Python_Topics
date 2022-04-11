"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
__author__ 'Danyang'
c_ Solution:
    ___ isScramble  s1, s2
        """
        dfs
        partition and compare

        Compare two trees constructed from the two strings respectively. Two trees are scramble of the other iff A's
        left/right subtree is the scramble of B's left/right subtree or A's left/right subtree is the scramble of B's
        right/left subtree.

        .....|... vs. .....|... or
        ...|..... vs. .....|...

        :param s1:
        :param s2:
        :return: boolean
        """
        __ l..(s1)!=l..(s2
            r.. F..
        chars [0 ___ _ __ x..(26)]
        ___ char __ s1:
            chars[o..(char)-o..('a')] += 1
        ___ char __ s2:
            chars[o..(char)-o..('a')] -_ 1

        # if filter(lambda x: x!=0, chars):
        #     return False
        ___ val __ chars:
            __ val!=0:
                r.. F..

        __ l..(s1)__1:
            r.. T..


        ___ i __ x..(1, l..(s1:
            __ isScramble(s1[:i], s2[:i]) a.. isScramble(s1[i:], s2[i:]) o. \
                isScramble(s1[:i], s2[-i:]) a.. isScramble(s1[i:], s2[:l..(s2)-i]
                r.. T..

        r.. F..



__ _____ __ ____
    ... Solution().isScramble("abc", "bca")__True
