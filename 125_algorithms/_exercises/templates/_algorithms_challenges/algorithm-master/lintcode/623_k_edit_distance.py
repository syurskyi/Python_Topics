c_ TrieNode:
    ___ - ):
        end_of = N..
        children    # dict


c_ Trie:
    ___ - ):
        root = TrieNode()

    ___ put  word):
        __ n.. isi..(word, s..):
            r..

        node = root

        ___ c __ word:
            __ c n.. __ node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word


c_ Solution:
    ___ kDistance  words, target, k):
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

        dfs(trie.root, k, target, ans, dp)

        r.. ans

    ___ dfs  node, k, target, ans, pre):
        n = l..(target)

        __ node.end_of __ n.. N.. a.. pre[n] <= k:
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

            dfs(node.children[c], k, target, ans, dp)
