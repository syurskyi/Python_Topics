c_ TrieNode o..
    # https://leetcode.com/articles/implement-trie-prefix-tree/#trie-node-structure
    ___ - ____:
        """
        Initialize your data structure here.
        """
        links = [N..] * 26
        isEnd = F..

    ___ containsKey  ch):
        r_ links[o.. ch) - o.. 'a')] != N..

    ___ get  ch):
        r_ links[o.. ch) - o.. 'a')]

    ___ put  ch, node):
        links[o.. ch) - o.. 'a')] = node

    ___ setEnd ____:
        isEnd = T..


c_ Trie o..
    ___ - ____:
        root = TrieNode()

    ___ insert  word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = root
        ___ i __ r.. l.. word)):
            ch = word[i]
            __ node.containsKey(ch) is F..:
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    ___ searchPrefix  word):
        node = root
        ___ i __ r.. l.. word)):
            ch = word[i]
            __ node.containsKey(ch):
                node = node.get(ch)
            ____
                r_ N..
        r_ node


    ___ search  word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = searchPrefix(word)
        r_ node is not N.. and node.isEnd


    ___ startsWith  prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = searchPrefix(prefix)
        r_ node is not N..


        # Your Trie object will be instantiated and called as such:
        # trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")