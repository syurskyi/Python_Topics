#!/usr/bin/python3
"""
A query word matches a given pattern if we can insert lowercase letters to the
pattern word so that it equals the query. (We may insert each character at any
position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where
answer[i] is true if and only if queries[i] matches the pattern.

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:
1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
"""
____ t___ _______ List


c_ Solution:
    ___ camelMatch  queries: List[s..], pattern: s..) __ List[b..]:
        ret    # list
        ___ q __ queries:
            ret.a..(m..(q, pattern))
            
        r.. ret

    ___ m..  q, p
        i = 0
        j = 0
        w.... i < l..(q) a.. j < l..(p
            __ q[i] __ p[j]:
                i += 1
                j += 1
            ____ q[i].isl..
                i += 1
            ____:
                _____

        w.... i < l..(q) a.. q[i].isl..
            i += 1

        r.. i __ l..(q) a.. j __ l..(p)


__ _______ __ _______
    ... Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa") __ [T.., F.., T.., F.., F..]
