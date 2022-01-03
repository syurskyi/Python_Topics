c_ TrieNode:
    ___ - , val_ N..
        end_at = val
        children    # dict


c_ Trie:
    ___ - ):
        trie = TrieNode()

    ___ insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        __ n.. word:
            r..

        node = trie
        ___ char __ word:
            __ char n.. __ node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_at = word

    ___ s..(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        __ n.. word:
            r.. F..

        node = trie
        ___ char __ word:
            __ char n.. __ node.children:
                r.. F..
            node = node.children[char]
        r.. node.end_at __ word

    ___ startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        __ n.. prefix:
            r.. F..

        node = trie
        ___ char __ prefix:
            __ char n.. __ node.children:
                r.. F..
            node = node.children[char]
        r.. T..


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
