#!/usr/bin/python3
"""
Consider the string s to be the infinite wraparound string of
"abcdefghijklmnopqrstuvwxyz", so s will look like this:
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty
substrings of p are present in s. In particular, your input is the string p and
you need to output the number of different non-empty substrings of p in the
string s.

Note: p consists of only lowercase English letters and the size of p might be
over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string
"zab" in the string s.
"""


c_ Solution:
    ___ findSubstringInWraproundString  p
        """
        wrap around: +1 (delta=1)
        "zab": 3 + 2 + 1
        "zabc": 4 + 3 + 2 + 1
        To de-dpulicate, change the way of counting - count backward at the
        ending char.
        "zabc":
            "z": "z" : 1
            "a": "a", "za": 2
            "zab": "b", "ab", "zab": 3
            "zabc": "c", ...: 4

        p.s. possible to count forward but tedious 
        :type p: str
        :rtype: int
        """
        counter = {
            c: 1
            ___ c __ p
        }
        l = 1
        ___ i __ r..(1, l..(p)):
            __ (o..(p[i]) - o..(p[i-1])) % 26 __ 1:  # (0 - 25) % 26 == 1
                l += 1
            ____:
                l = 1
            counter[p[i]] = m..(counter[p[i]], l)

        r.. s..(counter.values

    ___ findSubstringInWraproundString_error  p
        """
        wrap around: +1 (delta=1)
        "zab": 3 + 2 + 1
        "zabc": 4 + 3 + 2 + 1
        :type p: str
        :rtype: int
        """
        __ n.. p:
            r.. 0

        ret = s..()
        i = 0
        w.... i < l..(p
            cur = [p[i]]
            j = i + 1
            w.... j < l..(p) a.. (o..(p[j]) - o..(cur[-1]) __ 1 o. p[j] __ "a" a.. cur[-1] __ "z"
                cur.a..(p[j])
                j += 1
            ret.add("".j..(cur))
            i = j

        r.. s.. m..(l.... x: (l..(x) + 1) * l..(x) // 2, ret))


__ _______ __ _______
    ... Solution().findSubstringInWraproundString("a") __ 1
    ... Solution().findSubstringInWraproundString("cac") __ 2
    ... Solution().findSubstringInWraproundString("zab") __ 6
    ... Solution().findSubstringInWraproundString("zaba") __ 6
