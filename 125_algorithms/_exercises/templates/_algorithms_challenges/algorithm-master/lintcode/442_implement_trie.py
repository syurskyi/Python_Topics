class TrieNode:
    ___ __init__(self):
        self.end_of = None
        self.children = {}


class Trie:
    ___ __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    ___ insert(self, word):
        __ word __ None:
            return

        node = self.root

        for c in word:
            __ c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    ___ search(self, word):
        __ word __ None:
            return False

        node = self.root

        for c in word:
            __ c not in node.children:
                return False

            node = node.children[c]

        return node.end_of == word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    ___ startsWith(self, prefix):
        __ prefix __ None:
            return False

        node = self.root

        for c in prefix:
            __ c not in node.children:
                return False

            node = node.children[c]

        return True
