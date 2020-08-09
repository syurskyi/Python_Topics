"""
Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance
k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string
"".

Example 1:
str = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
str = "aaabc", k = 3

Answer: ""

It is not possible to rearrange the string.
Example 3:
str = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.

"""
from collections ______ defaultdict
______ heapq

__author__ = 'Daniel'


class Val(object
    ___ __init__(self, cnt, val
        self.cnt = cnt
        self.val = val

    ___ __cmp__(self, other
        __ self.cnt __ other.cnt:
            r_ cmp(self.val, other.val)

        r_ -cmp(self.cnt, other.cnt)


class Solution(object
    ___ rearrangeString(self, s, k
        """
        Greedy, largest first, fill k first
        O(lg(26) n)
        :type s: str
        :type k: int
        :rtype: str
        """
        __ not s or k __ 0: r_ s

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        h = []
        for char, cnt in d.items(
            heapq.heappush(h, Val(cnt, char))

        ret = []
        w___ h:
            cur = []
            for _ in xrange(k
                __ not h:
                    r_ "".join(ret) __ le.(ret) __ le.(s) else ""

                e = heapq.heappop(h)
                ret.append(e.val)
                e.cnt -= 1
                __ e.cnt > 0:
                    cur.append(e)

            for e in cur:
                heapq.heappush(h, e)

        r_ "".join(ret)


__ __name__ __ "__main__":
    assert Solution().rearrangeString("aabbccdd", 4) __ "abcdabcd"
