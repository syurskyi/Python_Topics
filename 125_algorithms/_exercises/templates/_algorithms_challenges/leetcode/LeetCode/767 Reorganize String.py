#!/usr/bin/python3
"""
Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
from collections ______ defaultdict


class Solution:
    ___ reorganizeString(self, S: str) -> str:
        """
        piles by max char and circular append
        """
        counter = defaultdict(int)
        for c in S:
            counter[c] += 1

        lst = [
            (-n, n, c)
            for c, n in counter.items()
        ]
        lst.sort()
        piles = []
        _, n, c = lst[0]
        for i in range(n
            piles.append([c])

        cnt = 0
        for _, n, c in lst[1:]:
            for _ in range(n
                piles[cnt].append(c)
                cnt = (cnt + 1) % le.(piles)

        __ le.(piles) > 1 and le.(piles[-2]) __ 1:
            r_ ""

        r_ "".join(
            map(lambda x: "".join(x), piles)
        )


__ __name__ __ "__main__":
    assert Solution().reorganizeString("vvvlo") __ "vlvov"
    assert Solution().reorganizeString("aab") __ "aba"
    assert Solution().reorganizeString("aaab") __ ""
