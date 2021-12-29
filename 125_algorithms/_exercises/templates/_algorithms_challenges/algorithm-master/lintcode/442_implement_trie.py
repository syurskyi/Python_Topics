class TrieNode:
    ___ __init__(self):
        self.end_of = N..
        self.children = {}


class Trie:
    ___ __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    ___ insert(self, word):
        __ word __ N..
            r..

        node = self.root

        ___ c __ word:
            __ c n.. __ node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    ___ search(self, word):
        __ word __ N..
            r.. False

        node = self.root

        ___ c __ word:
            __ c n.. __ node.children:
                r.. False

            node = node.children[c]

        r.. node.end_of __ word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    ___ startsWith(self, prefix):
        __ prefix __ N..
            r.. False

        node = self.root

        ___ c __ prefix:
            __ c n.. __ node.children:
                r.. False

            node = node.children[c]

        r.. True
