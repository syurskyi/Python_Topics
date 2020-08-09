"""
Definition of TrieNode:
class TrieNode:
    ___ __init__(self
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieService:

    ___ __init__(self
        self.root = TrieNode()

    ___ get_root(self
        # Return root of trie root, and
        # lintcode will print the tree struct.
        r_ self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    ___ insert(self, word, frequency
        __ not word or le.(word) < 1 \
                or not frequency:
            r_
        parent = self.root
        for char in word:
            __ char not in parent.children:
                parent.children[char] = TrieNode()
            parent = parent.children[char]

            # To handle top10
            parent.top10.append(frequency)
            parent.top10.sort(reverse=True)
            __ le.(parent.top10) > 10:
                parent.top10.pop()
