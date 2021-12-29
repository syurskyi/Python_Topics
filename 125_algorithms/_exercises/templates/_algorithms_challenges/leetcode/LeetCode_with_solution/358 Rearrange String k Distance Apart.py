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
____ collections _______ defaultdict
_______ heapq

__author__ = 'Daniel'


class Val(object):
    ___ __init__(self, cnt, val):
        self.cnt = cnt
        self.val = val

    ___ __cmp__(self, other):
        __ self.cnt __ other.cnt:
            r.. cmp(self.val, other.val)

        r.. -cmp(self.cnt, other.cnt)


class Solution(object):
    ___ rearrangeString(self, s, k):
        """
        Greedy, largest first, fill k first
        O(lg(26) n)
        :type s: str
        :type k: int
        :rtype: str
        """
        __ n.. s o. k __ 0: r.. s

        d = defaultdict(int)
        ___ c __ s:
            d[c] += 1

        h    # list
        ___ char, cnt __ d.items():
            heapq.heappush(h, Val(cnt, char))

        ret    # list
        w.... h:
            cur    # list
            ___ _ __ xrange(k):
                __ n.. h:
                    r.. "".join(ret) __ l..(ret) __ l..(s) ____ ""

                e = heapq.heappop(h)
                ret.a..(e.val)
                e.cnt -= 1
                __ e.cnt > 0:
                    cur.a..(e)

            ___ e __ cur:
                heapq.heappush(h, e)

        r.. "".join(ret)


__ __name__ __ "__main__":
    ... Solution().rearrangeString("aabbccdd", 4) __ "abcdabcd"
