#!/usr/bin/python3
"""
We are stacking blocks to form a pyramid. Each block has a color which is a one
letter string.

We are allowed to place any color block C on top of two adjacent blocks of
colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also
start with a list of allowed triples allowed. Each allowed triple is represented
as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.
Similarly, we can place E on top of C and D, then A on top of G and E.


Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.


Note:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
'F', 'G'}.
"""
_______ i..
____ t___ _______ L..
____ c.. _______ d..


c_ Solution:
    ___ pyramidTransition  bottom: s.., allowed: L..s.. __ b..
        """
        Need search, since multiple placements are possible
        The order of allowed matters
        """
        T d..(s..)  # transition matrix
        ___ a, b, c __ allowed:
            T[a, b].add(c)

        r.. dfs(T, bottom)

    ___ dfs  T, level) __ b..
        __ l..(level) __ 1:
            r.. T..

        # for nxt_level in self.gen_nxt_level(T, level, 0):
        ___ nxt_level __ i...product(
            *[T[a, b] ___ a, b __ z..(level, level[1:])]

            __ dfs(T, nxt_level
                r.. T..

        r.. F..

    ___ gen_nxt_level  T, level, lo
        """
        equiv to itertools.product - nested for-loops in a generator expression
        Cartesian product
        """
        __ lo + 1 >_ l..(level
            y.. ""
            r..

        ___ head __ T[level[lo], level[lo + 1]]:
            ___ tail __ gen_nxt_level(T, level, lo + 1
                y.. head + tail


    ___ dfs_deep  T, level, lo, nxt_level) __ b..
        __ lo + 1 __ l..(level
            r.. T..

        ___ nxt __ T[level[lo], level[lo + 1]]:
            nxt_level.a..(nxt)
            __ dfs(T, level, lo + 1, nxt_level
                # Too deep - check till top
                __ dfs(T, nxt_level, 0,    # list
                    r.. T..
            nxt_level.p.. )

        r.. F..


__ _______ __ _______
    ... Solution().pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) __ T..
    ... Solution().pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) __ F..
