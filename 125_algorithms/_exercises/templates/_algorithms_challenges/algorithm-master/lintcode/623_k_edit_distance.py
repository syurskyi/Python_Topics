class TrieNode:
    ___ __init__(self):
        self.end_of = N..
        self.children = {}


class Trie:
    ___ __init__(self):
        self.root = TrieNode()

    ___ put(self, word):
        __ n.. isi..(word, str):
            r..

        node = self.root

        ___ c __ word:
            __ c n.. __ node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word


class Solution:
    ___ kDistance(self, words, target, k):
        """
        :type words: list[str]
        :type target: str
        :type k: int
        :rtype: list[str]
        """
        trie = Trie()

        ___ word __ words:
            trie.put(word)

        ans    # list
        dp = [i ___ i __ r..(l..(target) + 1)]

        self.dfs(trie.root, k, target, ans, dp)

        r.. ans

    ___ dfs(self, node, k, target, ans, pre):
        n = l..(target)

        __ node.end_of __ n.. N.. and pre[n] <= k:
            ans.a..(node.end_of)

        dp = [0] * (n + 1)

        ___ c __ node.children:
            dp[0] = pre[0] + 1

            ___ i __ r..(1, n + 1):
                __ target[i - 1] __ c:
                    dp[i] = m..(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1]
                    )
                ____:
                    dp[i] = m..(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1] + 1
                    )

            self.dfs(node.children[c], k, target, ans, dp)
