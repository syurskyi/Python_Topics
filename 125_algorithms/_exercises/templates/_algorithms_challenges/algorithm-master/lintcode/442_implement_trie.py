class TrieNode:
    ___ __init__(self
        self.end_of = None
        self.children = {}


class Trie:
    ___ __init__(self
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    ___ insert(self, word
        __ word is None:
            r_

        node = self.root

        ___ c in word:
            __ c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    ___ search(self, word
        __ word is None:
            r_ False

        node = self.root

        ___ c in word:
            __ c not in node.children:
                r_ False

            node = node.children[c]

        r_ node.end_of __ word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    ___ startsWith(self, prefix
        __ prefix is None:
            r_ False

        node = self.root

        ___ c in prefix:
            __ c not in node.children:
                r_ False

            node = node.children[c]

        r_ True
