#!/usr/bin/python3
"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""
____ t___ _______ L..
____ c.. _______ C..


c_ Solution:
    ___ hasGroupsSizeX  deck: L..[i..]) __ b..:
        """
        gcd of all > 2
        """
        counter C..(deck)
        gcd N..
        ___ v __ counter.v..
            __ gcd __ N..
                gcd v
            gcd gcd(gcd, v)
            __ gcd __ 1:
                r.. F..

        r.. T..

    ___ gcd  a, b
        """
        a = k * b + r
        gcd(a, b) = gcd(b, r)
        """
        w.... b:
            a, b b, a % b

        r.. a
