#!/usr/bin/python3
"""
Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat",
"ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""
____ typing _______ List
____ c.. _______ defaultdict


c_ Solution:
    ___ - ):
        TrieNode = l....: defaultdict(TrieNode)  # not defaultdict(lambda: TrieNode)
        root = TrieNode()  # root of tire

    ___ findAllConcatenatedWordsInADict  words: List[s..]) __ List[s..]:
        """
        Trie + DFS
        """
        words.s..(key=l..)
        ret    # list
        ___ w __ words:
            __ can_concat(w, 0):
                ret.a..(w)

            cur = root
            ___ c __ w:
                cur = cur[c]
            cur["end"] = T..

        r.. ret

    ___ can_concat  word, lo):
        __ n.. word:
            r.. F..

        k = l..(word)
        __ lo >= k:
            r.. T..

        cur = root
        ___ i __ r..(lo, k):
            cur = cur[word[i]]
            __ cur.get("end", F..) a.. can_concat(word, i + 1):
                r.. T..

        r.. F..


c_ SolutionTLE:
    ___ findAllConcatenatedWordsInADict  words: List[s..]) __ List[s..]:
        """
        Trie check cannot be greedy: cat sdog vs cats dog

        Sort + Trie dfs
        What is the complexity?

        Word break DP
        for a specific word
        F[i] means word[:i] can be formed using shorter words

        complexity
        O(n) * O(k^2) * O(k)
        n words * get F * compare words

        Hard question is solving a collections of medium problems
        """
        ret    # list
        # words.sort()  # sorting is unnecessary
        visited = s..(words)
        ___ w __ words:
            __ can_concat(w, visited):
                ret.a..(w)

        r.. ret

    ___ can_concat  w, visited):
        __ n.. w:
            r.. F..

        k = l..(w)
        F = [F.. ___ _ __ r..(k + 1)]
        F[0] = T..
        ___ i __ r..(1, k + 1):
            ___ j __ r..(i):
                __ j __ 0 a.. i __ k:
                    _____  # word itself
                __ F[j] a.. w[j:i] __ visited:
                    F[i] = T..

        r.. F[k]


__ _______ __ _______
    ... Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) __ ["catsdogcats","dogcatsdog","ratcatdogcat"]
