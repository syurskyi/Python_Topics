class TrieNode:
    ___ __init__(self):
        self.end_of = None
        self.children = {}


class Trie:
    ___ __init__(self):
        self.root = TrieNode()

    ___ put(self, word):
        __ not isinstance(word, str):
            return

        node = self.root

        for c in word:
            __ c not in node.children:
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

        for word in words:
            trie.put(word)

        ans = []
        dp = [i for i in range(len(target) + 1)]

        self.dfs(trie.root, k, target, ans, dp)

        return ans

    ___ dfs(self, node, k, target, ans, pre):
        n = len(target)

        __ node.end_of is not None and pre[n] <= k:
            ans.append(node.end_of)

        dp = [0] * (n + 1)

        for c in node.children:
            dp[0] = pre[0] + 1

            for i in range(1, n + 1):
                __ target[i - 1] == c:
                    dp[i] = min(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1]
                    )
                else:
                    dp[i] = min(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1] + 1
                    )

            self.dfs(node.children[c], k, target, ans, dp)
