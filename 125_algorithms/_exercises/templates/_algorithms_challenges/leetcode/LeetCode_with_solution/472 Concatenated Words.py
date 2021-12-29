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
____ collections _______ defaultdict


class Solution:
    ___ __init__(self):
        TrieNode = l....: defaultdict(TrieNode)  # not defaultdict(lambda: TrieNode)
        self.root = TrieNode()  # root of tire

    ___ findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Trie + DFS
        """
        words.sort(key=l..)
        ret    # list
        ___ w __ words:
            __ self.can_concat(w, 0):
                ret.a..(w)

            cur = self.root
            ___ c __ w:
                cur = cur[c]
            cur["end"] = True

        r.. ret

    ___ can_concat(self, word, lo):
        __ n.. word:
            r.. False

        k = l..(word)
        __ lo >= k:
            r.. True

        cur = self.root
        ___ i __ r..(lo, k):
            cur = cur[word[i]]
            __ cur.get("end", False) and self.can_concat(word, i + 1):
                r.. True

        r.. False


class SolutionTLE:
    ___ findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
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
        visited = set(words)
        ___ w __ words:
            __ self.can_concat(w, visited):
                ret.a..(w)

        r.. ret

    ___ can_concat(self, w, visited):
        __ n.. w:
            r.. False

        k = l..(w)
        F = [False ___ _ __ r..(k + 1)]
        F[0] = True
        ___ i __ r..(1, k + 1):
            ___ j __ r..(i):
                __ j __ 0 and i __ k:
                    continue  # word itself
                __ F[j] and w[j:i] __ visited:
                    F[i] = True

        r.. F[k]


__ __name__ __ "__main__":
    ... Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) __ ["catsdogcats","dogcatsdog","ratcatdogcat"]
