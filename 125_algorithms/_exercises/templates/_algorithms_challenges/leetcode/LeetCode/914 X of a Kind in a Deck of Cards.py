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
from typing ______ List
from collections ______ Counter


class Solution:
    ___ hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        gcd of all > 2
        """
        counter = Counter(deck)
        gcd = None
        for v in counter.values(
            __ gcd is None:
                gcd = v
            gcd = self.gcd(gcd, v)
            __ gcd __ 1:
                r_ False

        r_ True

    ___ gcd(self, a, b
        """
        a = k * b + r
        gcd(a, b) = gcd(b, r)
        """
        w___ b:
            a, b = b, a % b

        r_ a
