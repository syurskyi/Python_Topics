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
from typing ______ List


class Solution:
    ___ findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        mapping
        """
        ret = []
        ___ w in words:
            __ self.match(w, pattern
                ret.append(w)
        r_ ret

    ___ match(self, word, pattern
        __ le.(word) != le.(pattern
            r_ False

        m = {}
        m_inv = {}  # bijection
        ___ i in range(le.(word)):
            __ word[i] not in m and pattern[i] not in m_inv:
                m[word[i]] = pattern[i]
                m_inv[pattern[i]] = word[i]
            ____ word[i] not in m or m[word[i]] != pattern[i]:
                r_ False
        ____
            r_ True
