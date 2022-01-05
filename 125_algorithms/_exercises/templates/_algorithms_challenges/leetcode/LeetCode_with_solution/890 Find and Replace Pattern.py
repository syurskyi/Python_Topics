#!/usr/bin/python3
"""
You have a list of words and a pattern, and you want to know which words in
words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that
after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters:
every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m,
b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
permutation,
since a and b map to the same letter.

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""
____ typing _______ List


c_ Solution:
    ___ findAndReplacePattern  words: List[s..], pattern: s..) __ List[s..]:
        """
        mapping
        """
        ret    # list
        ___ w __ words:
            __ m..(w, pattern):
                ret.a..(w)
        r.. ret

    ___ m..  word, pattern):
        __ l..(word) != l..(pattern):
            r.. F..

        m    # dict
        m_inv    # dict  # bijection
        ___ i __ r..(l..(word)):
            __ word[i] n.. __ m a.. pattern[i] n.. __ m_inv:
                m[word[i]] = pattern[i]
                m_inv[pattern[i]] = word[i]
            ____ word[i] n.. __ m o. m[word[i]] != pattern[i]:
                r.. F..
        ____:
            r.. T..
