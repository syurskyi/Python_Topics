#!/usr/bin/python3
"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the
given list, so that the concatenation of the two words, i.e. words[i] + words[j]
is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""
____ typing _______ List
____ c.. _______ d..


c_ TrieNode:
    ___ -
        pali_prefix_idxes    # list  # suffix ends, prefix pali
        word_idx = N..
        children = d..(TrieNode)


c_ Solution:
    ___ palindromePairs  words: List[s..]) __ List[List[i..]]:
        """
        Brute force, i, j and then check palindrom
        O(N^2 * L)

        Reverse the str, and then check O(N * L). Does it work actually?
        Check: map str -> idx

        |---s1---|---s2--|     |---s1---|-s2-|    |-s1-|---s2---|
        Need to check whether part of the str is palindrome.
        Part of str -> Trie.
        How to check part of the str. Useful

        Better way of checking palindrome? Infamouse Manacher

        word_i   | word_j
        abc pppp | cba
             abc | pppp cba

        If palindrome suffix in work_i, we only need to check the "abc" against word_j
        Similarly for palindrome prefix in word_j

        Construct Trie for word_j reversely, since word_j is being checked
        """
        root = TrieNode()
        ___ idx, w __ e..(words
            cur = root
            ___ i __ r..(l..(w) - 1, -1, -1
                #  cur.children[w[i]]  # error, pre-advancing the trie is unable to handle empty str
                __ is_palindrome(w, 0, i + 1
                    cur.pali_prefix_idxes.a..(idx)

                cur = cur.children[w[i]]

            cur.pali_prefix_idxes.a..(idx)  # empty str is palindrome
            cur.word_idx = idx  # word ends

        ret    # list
        ___ idx, w __ e..(words
            cur = root
            ___ i __ r..(l..(w)):
                # cur.children.get(w[i], None)  # error, pre-advancing the trie is unable to handle empty str
                __ is_palindrome(w, i, l..(w)) a.. cur.word_idx __ n.. N.. a.. cur.word_idx != idx:
                    ret.a..([idx, cur.word_idx])

                cur = cur.children.g.. w[i], N..)
                __ cur __ N..
                    _____
            ____:
                ___ idx_j __ cur.pali_prefix_idxes:
                    __ idx != idx_j:
                        ret.a..([idx, idx_j])

        r.. ret

    ___ is_palindrome  w, lo, hi
        i = lo
        j = hi - 1
        w.... i < j:
            __ w[i] != w[j]:
                r.. F..
            i += 1
            j -= 1
        r.. T..


__ _______ __ _______
    ... Solution().palindromePairs(["a", ""]) __ [[0,1],[1,0]]
    ... Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]) __ [[0,1],[1,0],[2,4],[3,2]]
